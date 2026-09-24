#!/usr/bin/env bash
# Runs every quickstart against tools/mockapi (a local stand-in that answers the contract's own 200
# examples) and asserts what each one SENT: key header, limit=5, Idempotency-Key, dry_run=true.
# Then runs each once with a malformed key and asserts it exits 1 on the contract's 401 envelope.
# Called by `make -C examples smoke` (which sets ROOT, COMPOSER_IMAGE, DOTNET_IMAGE, PYTHON_VERSION).
set -euo pipefail

# Containers run as the calling user (root-owned files would break the next checkout on a persistent
# self-hosted runner) with every tool's home in the container's /tmp.
docker_user=(--user "$(id -u):$(id -g)" -e HOME=/tmp -e COMPOSER_HOME=/tmp/composer -e DOTNET_CLI_HOME=/tmp
  -e NUGET_PACKAGES=/tmp/nuget -e DOTNET_CLI_TELEMETRY_OPTOUT=1 -e DOTNET_NOLOGO=1)

# Scratch space inside the (git-ignored) build/ dir: per-checkout, so per-runner, and mountable into
# containers everywhere (Docker Desktop does not share every host temp dir).
mkdir -p "$ROOT/build"
tmp="$(mktemp -d "$ROOT/build/smoke.XXXXXX")"
mock_ctr="dona-api-smoke-$$"
cleanup() {
  if [[ -n "${mock_pid:-}" ]]; then kill "$mock_pid" 2>/dev/null || true; wait "$mock_pid" 2>/dev/null || true; fi
  docker rm -f "$mock_ctr" >/dev/null 2>&1 || true
  rm -rf "$tmp"
}
trap cleanup EXIT

key="dona_sk_live_EXAMPLE_not_a_real_key"   # the mock accepts any `Bearer dona_…`
bad="not-a-dona-key"

# ── host mock: typescript · python · go ───────────────────────────────────────────────────────────
(cd "$ROOT/tools" && go build -o "$tmp/mockapi" ./mockapi)
"$tmp/mockapi" -spec "$ROOT/spec/openapi.yaml" -log "$tmp/host.jsonl" -addr 127.0.0.1:0 -addr-file "$tmp/host.addr" \
  2>"$tmp/host.log" &
mock_pid=$!
for _ in $(seq 50); do [[ -s "$tmp/host.addr" ]] && break; sleep 0.1; done
[[ -s "$tmp/host.addr" ]] || { cat "$tmp/host.log"; echo "smoke: host mock did not start" >&2; exit 1; }
host_url="http://$(cat "$tmp/host.addr")/seller-api/v1"

run() { # run <lang> <key> <command...> — prints output, returns the example's exit code
  local lang="$1" k="$2"; shift 2
  echo "── $lang (key: ${k:0:12}…)"
  set +e
  DONA_API_KEY="$k" DONA_API_BASE_URL="$url" "$@" >"$tmp/$lang.out" 2>"$tmp/$lang.err"
  local rc=$?
  set -e
  sed 's/^/   /' "$tmp/$lang.out" "$tmp/$lang.err"
  return $rc
}
expect_ok() { run "$@" || { echo "smoke: $1 quickstart failed" >&2; exit 1; }; }
expect_rejected() { # the malformed key must end in exit 1 with the 401 code printed
  local rc=0
  run "$1-badkey" "$bad" "${@:2}" || rc=$?
  if [[ $rc -ne 1 ]] || ! grep -q api_key_malformed "$tmp/$1-badkey.err"; then
    echo "smoke: $1 did not surface the 401 envelope (exit $rc)" >&2
    exit 1
  fi
}

url="$host_url"
ts=(node "$ROOT/examples/typescript/src/quickstart.ts")
py=(uv run --isolated --no-project --python "$PYTHON_VERSION" --with "$ROOT/sdks/python" python "$ROOT/examples/python/quickstart.py")
(cd "$ROOT/examples/go" && go build -o "$tmp/go-quickstart" ./cmd/quickstart)
gobin=("$tmp/go-quickstart")
expect_ok typescript "$key" "${ts[@]}";  expect_rejected typescript "${ts[@]}"
expect_ok python "$key" "${py[@]}";      expect_rejected python "${py[@]}"
expect_ok go "$key" "${gobin[@]}";       expect_rejected go "${gobin[@]}"

# ── container mock: php · csharp share its network namespace, so 127.0.0.1 is the mock ─────────────
arch="$(docker version --format '{{.Server.Arch}}')"
(cd "$ROOT/tools" && CGO_ENABLED=0 GOOS=linux GOARCH="$arch" go build -o "$tmp/mockapi-linux" ./mockapi)
chmod -R a+rwX "$tmp"
docker run -d --name "$mock_ctr" "${docker_user[@]}" -v "$tmp:/smoke" -v "$ROOT/spec:/spec:ro" --entrypoint /smoke/mockapi-linux \
  "$COMPOSER_IMAGE" -spec /spec/openapi.yaml -log /smoke/docker.jsonl -addr 127.0.0.1:8080 -addr-file /smoke/docker.addr >/dev/null
for _ in $(seq 50); do [[ -s "$tmp/docker.addr" ]] && break; sleep 0.1; done
[[ -s "$tmp/docker.addr" ]] || { docker logs "$mock_ctr"; echo "smoke: container mock did not start" >&2; exit 1; }

url="http://127.0.0.1:8080/seller-api/v1"
in_ctr() { docker run --rm --network "container:$mock_ctr" "${docker_user[@]}" -e DONA_API_KEY -e DONA_API_BASE_URL -v "$ROOT:/work" "$@"; }
php=(in_ctr -w /work/examples/php --entrypoint php "$COMPOSER_IMAGE" quickstart.php)
docker run --rm "${docker_user[@]}" -v "$ROOT:/work" -v "$tmp:/smoke" -w /work/examples/csharp "$DOTNET_IMAGE" \
  sh -ec 'dotnet build -c Release -o /smoke/cs -v quiet -nologo >/smoke/cs-build.log 2>&1 || { cat /smoke/cs-build.log; exit 1; }'
cs=(in_ctr -v "$tmp:/smoke" "$DOTNET_IMAGE" dotnet /smoke/cs/DonaExamples.dll quickstart)
expect_ok php "$key" "${php[@]}";        expect_rejected php "${php[@]}"
expect_ok csharp "$key" "${cs[@]}";      expect_rejected csharp "${cs[@]}"

# ── what did they send? ───────────────────────────────────────────────────────────────────────────
cat "$tmp/host.jsonl" "$tmp/docker.jsonl" >"$tmp/all.jsonl"
uv run --isolated --no-project --python "$PYTHON_VERSION" python "$ROOT/examples/smoke_assert.py" "$tmp/all.jsonl"

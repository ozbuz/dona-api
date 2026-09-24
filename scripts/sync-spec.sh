#!/usr/bin/env bash
# Copy the Dona API contract into spec/ and record its fingerprints.
#
# The contract's ONE source of truth is OZB/architecture/DB/seller-api/contract/openapi.yaml (the OZB
# workspace). It changes there first; ozb-backend carries only a minified JSON generated from it
# (docs/openapi/seller-api.json + .sha256, via its scripts/openapi-sync.sh) and serves that at
# GET https://api.dona.im/seller-api/v1/openapi.json. This repository copies the SAME YAML and proves,
# in CI, that it is the one the backend serves: tools/openapi2json is a verbatim copy of the backend's
# converter, so YAML → minified JSON here gives the backend's bytes, and its sha256 must equal the
# backend's checked-in seller-api.json.sha256.
#
# Writes:
#   spec/openapi.yaml          byte-identical copy of the contract
#   spec/openapi.yaml.sha256   `<sha256>  openapi.yaml`
#   spec/seller-api.json.sha256  the backend's checked-in sha, copied verbatim from
#                              `git -C $OZB_BACKEND show origin/main:docs/openapi/seller-api.json.sha256`
#                              — the value CI holds our conversion to
#
# usage: scripts/sync-spec.sh            then `make generate` and commit spec/ + sdks/ together
# env:   OZB_HOME (default ~/GitHub/OZB) · OZB_BACKEND (default ~/GitHub/ozbuz/ozb-backend)
set -euo pipefail
# sha256sum (Linux, recent macOS) or shasum -a 256 (older macOS) — same output and -c format.
sha256() { if command -v sha256sum >/dev/null; then sha256sum "$@"; else shasum -a 256 "$@"; fi; }

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
src="${OZB_HOME:-$HOME/GitHub/OZB}/architecture/DB/seller-api/contract/openapi.yaml"
backend="${OZB_BACKEND:-$HOME/GitHub/ozbuz/ozb-backend}"

[[ -f "$src" ]] || { echo "sync-spec: contract not found: $src (set OZB_HOME)" >&2; exit 1; }

cp "$src" "$repo/spec/openapi.yaml"
chmod 0644 "$repo/spec/openapi.yaml"
(cd "$repo/spec" && sha256 openapi.yaml >openapi.yaml.sha256)

ours="$(cd "$repo/tools" && go run ./openapi2json <"$repo/spec/openapi.yaml" | sha256 | cut -d' ' -f1)"

if [[ -d "$backend/.git" ]]; then
  git -C "$backend" fetch -q origin main
  if theirs_line="$(git -C "$backend" show origin/main:docs/openapi/seller-api.json.sha256 2>/dev/null)"; then
    printf '%s\n' "$theirs_line" >"$repo/spec/seller-api.json.sha256"
    theirs="${theirs_line%% *}"
    if [[ "$ours" != "$theirs" ]]; then
      echo "sync-spec: ⚠ the contract's JSON sha ${ours:0:12}… ≠ ozb-backend origin/main ${theirs:0:12}…" >&2
      echo "  the backend has not run scripts/openapi-sync.sh for this contract yet (or runs an older one)." >&2
      echo "  CI will FAIL until they agree — sync the backend first (backend first, then clients)." >&2
      exit 1
    fi
  else
    echo "sync-spec: ozb-backend origin/main has no docs/openapi/seller-api.json.sha256" >&2
    exit 1
  fi
else
  echo "sync-spec: no ozb-backend clone at $backend (set OZB_BACKEND) — cannot record its sha" >&2
  exit 1
fi

echo "sync-spec: spec/openapi.yaml $(cut -c1-12 "$repo/spec/openapi.yaml.sha256")…  json ${ours:0:12}… = backend origin/main"

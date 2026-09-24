# shellcheck shell=bash
# Shared by the openapi-generator languages (php, csharp). Sourced, not executed.
#
# openapi_generator <generator> <spec> <out-dir> <additional-properties>
# Runs the pinned openapi-generator image (versions.env OPENAPI_GENERATOR_IMAGE) as the calling user,
# with the repository mounted at /work. No tests, no git_push.sh, no CI stubs — only the library.
openapi_generator() {
  local gen="$1" spec="$2" out="$3" props="$4" root
  root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
  spec="$(cd "$(dirname "$spec")" && pwd)/$(basename "$spec")"
  rm -rf "$out"
  mkdir -p "$out"
  out="$(cd "$out" && pwd)"
  case "$spec" in "$root"/*) ;; *) echo "openapi_generator: spec must live inside the repo" >&2; return 1 ;; esac
  case "$out" in "$root"/*) ;; *) echo "openapi_generator: out must live inside the repo" >&2; return 1 ;; esac
  cat >"$out/.openapi-generator-ignore" <<'IGN'
git_push.sh
.travis.yml
.gitlab-ci.yml
appveyor.yml
.github/**
test/**
IGN
  # Per-language extras (space-separated globs), e.g. the csharp test-project stub.
  local -a extra=()
  read -ra extra <<<"${OPENAPI_GENERATOR_EXTRA_IGNORE:-}"   # read, not a bare $VAR: no glob expansion
  ((${#extra[@]})) && printf '%s\n' "${extra[@]}" >>"$out/.openapi-generator-ignore"
  docker run --rm --user "$(id -u):$(id -g)" -v "$root:/work" -w /work "$OPENAPI_GENERATOR_IMAGE" generate \
    --generator-name "$gen" \
    --input-spec "/work/${spec#"$root"/}" \
    --output "/work/${out#"$root"/}" \
    --additional-properties "$props" \
    --git-host github.com --git-user-id ozbuz --git-repo-id dona-api \
    --release-note "Generated from spec/openapi.yaml - see https://github.com/ozbuz/dona-api" \
    --global-property apiTests=false,modelTests=false \
    --skip-validate-spec \
    >/dev/null
}

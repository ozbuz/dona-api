#!/usr/bin/env bash
# CI gate: spec/ is the synced contract, and it is the one the backend serves.
#   1. spec/openapi.yaml matches spec/openapi.yaml.sha256        (nobody edited the copy by hand)
#   2. openapi2json(spec/openapi.yaml) == spec/seller-api.json.sha256  (= ozb-backend's checked-in sha at sync)
#   3. drift: that sha == the backend's CURRENT one — read from ozb-backend origin/main when a token or
#      a clone can reach it, else from the public GET https://api.dona.im/seller-api/v1/openapi.json
#      (the server embeds that JSON byte for byte). Skipped only with SPEC_DRIFT=off.
set -euo pipefail
# sha256sum (Linux, recent macOS) or shasum -a 256 (older macOS) — same output and -c format.
sha256() { if command -v sha256sum >/dev/null; then sha256sum "$@"; else shasum -a 256 "$@"; fi; }

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo/spec"

sha256 -c openapi.yaml.sha256 >/dev/null || {
  echo "check-spec: spec/openapi.yaml differs from its recorded sha — it was edited by hand. The contract" >&2
  echo "  changes in OZB/architecture/DB/seller-api/contract/ first; then scripts/sync-spec.sh." >&2
  exit 1
}

ours="$(cd "$repo/tools" && go run ./openapi2json <"$repo/spec/openapi.yaml" | sha256 | cut -d' ' -f1)"
recorded="$(cut -d' ' -f1 seller-api.json.sha256)"
if [[ "$ours" != "$recorded" ]]; then
  echo "check-spec: openapi2json(spec/openapi.yaml) = ${ours:0:12}…, ozb-backend's recorded sha = ${recorded:0:12}… — re-run scripts/sync-spec.sh" >&2
  exit 1
fi
echo "check-spec: spec/openapi.yaml → JSON ${ours:0:12}… = ozb-backend seller-api.json.sha256 (recorded)"

[[ "${SPEC_DRIFT:-on}" == "off" ]] && { echo "check-spec: drift check skipped (SPEC_DRIFT=off)"; exit 0; }

current="" source=""
if [[ -n "${BACKEND_READ_TOKEN:-}" ]]; then
  current="$(GH_TOKEN="$BACKEND_READ_TOKEN" gh api -H 'Accept: application/vnd.github.raw' \
    'repos/ozbuz/ozb-backend/contents/docs/openapi/seller-api.json.sha256?ref=main' | cut -d' ' -f1)"
  source="ozb-backend main (API)"
elif [[ -d "${OZB_BACKEND:-$HOME/GitHub/ozbuz/ozb-backend}/.git" ]]; then
  b="${OZB_BACKEND:-$HOME/GitHub/ozbuz/ozb-backend}"
  git -C "$b" fetch -q origin main
  current="$(git -C "$b" show origin/main:docs/openapi/seller-api.json.sha256 | cut -d' ' -f1)"
  source="ozb-backend origin/main (clone)"
else
  current="$(curl -fsS --max-time 20 https://api.dona.im/seller-api/v1/openapi.json | sha256 | cut -d' ' -f1)"
  source="https://api.dona.im/seller-api/v1/openapi.json (served)"
fi
if [[ "$current" != "$ours" ]]; then
  echo "check-spec: DRIFT — $source is ${current:0:12}…, this repo's spec ${ours:0:12}…" >&2
  echo "  the contract moved; run scripts/sync-spec.sh + make generate and commit spec/ + sdks/." >&2
  exit 1
fi
echo "check-spec: no drift — $source = ${current:0:12}…"

#!/usr/bin/env bash
# Python SDK: openapi-python-client (httpx + attrs, sync + asyncio). Output: sdks/python/.
# Usage: generators/python/generate.sh <client-view.yaml> <out-dir> <sdk-version>
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=../versions.env
source "$here/../versions.env"
spec="$1" out="$2" version="$3"

cfg="$(mktemp)"
trap 'rm -f "$cfg"' EXIT
sed -e "s/@SDK_VERSION@/${version}/" -e "s/@RUFF_VERSION@/${RUFF_VERSION}/g" "$here/config.yaml.in" >"$cfg"

rm -rf "$out"
uvx --python "$PYTHON_VERSION" --from "openapi-python-client==${OPENAPI_PYTHON_CLIENT_VERSION}" \
  openapi-python-client generate --path "$spec" --config "$cfg" --meta uv --output-path "$out" >/dev/null
rm -rf "$out/.ruff_cache"
cp "$here/../SDK_README.md" "$out/SDK.md"
cp "$here/../../LICENSE" "$out/LICENSE"

# openapi-python-client's uv template has no license field of its own (PEP 639 — the pinned uv_build
# backend supports both `license` and `license-files`, proved by a local `uv build`). Insert
# deterministically right after `readme = ` so a generator upgrade that removes the anchor fails
# loudly instead of silently dropping the license from the built wheel/sdist.
anchor='readme = "README.md"'
grep -qF "$anchor" "$out/pyproject.toml" || { echo "python generate: pyproject.toml no longer has '$anchor' — re-check where to insert the license field" >&2; exit 1; }
sed -i.bak "s/^readme = \"README.md\"\$/readme = \"README.md\"\nlicense = \"Apache-2.0\"\nlicense-files = [\"LICENSE\"]/" "$out/pyproject.toml"
rm -f "$out/pyproject.toml.bak"
grep -qF 'license = "Apache-2.0"' "$out/pyproject.toml"

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

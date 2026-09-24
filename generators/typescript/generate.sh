#!/usr/bin/env bash
# TypeScript SDK: openapi-typescript (types) + openapi-fetch (runtime). Output: sdks/typescript/.
# Usage (from the Makefile): generators/typescript/generate.sh <client-view.yaml> <out-dir> <sdk-version>
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=../versions.env
source "$here/../versions.env"
spec="$1" out="$2" version="$3"

rm -rf "$out"
mkdir -p "$out/src"
npx --yes "openapi-typescript@${OPENAPI_TYPESCRIPT_VERSION}" "$spec" -o "$out/src/schema.ts" >/dev/null
# The banner openapi-typescript writes is fine; add ours so a reader knows not to edit.
{ printf '// GENERATED from spec/openapi.yaml by openapi-typescript %s — do not edit; run `make generate`.\n' \
    "$OPENAPI_TYPESCRIPT_VERSION"; cat "$out/src/schema.ts"; } >"$out/src/schema.ts.tmp"
mv "$out/src/schema.ts.tmp" "$out/src/schema.ts"

cp "$here/template/src/index.ts" "$out/src/index.ts"
cp "$here/template/tsconfig.json" "$out/tsconfig.json"
sed -e "s/@SDK_VERSION@/${version}/" \
    -e "s/@OPENAPI_FETCH_VERSION@/${OPENAPI_FETCH_VERSION}/" \
    -e "s/@TYPESCRIPT_VERSION@/${TYPESCRIPT_VERSION}/" \
    "$here/template/package.json" >"$out/package.json"
cp "$here/../SDK_README.md" "$out/README.md"

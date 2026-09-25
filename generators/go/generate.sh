#!/usr/bin/env bash
# Go SDK: oapi-codegen (models + client, net/http). Output: sdks/go/ (module github.com/ozbuz/dona-api/sdks/go).
# Usage: generators/go/generate.sh <client-view.yaml> <out-dir> <sdk-version>
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=../versions.env
source "$here/../versions.env"
spec="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")" out="$2"

rm -rf "$out"
mkdir -p "$out"
out="$(cd "$out" && pwd)"
sed -e "s/@GO_VERSION@/${GO_VERSION}/" -e "s/@OAPI_CODEGEN_RUNTIME_VERSION@/${OAPI_CODEGEN_RUNTIME_VERSION}/" \
  "$here/template/go.mod" >"$out/go.mod"
cp "$here/template/client.go" "$out/client.go"
(cd "$out" && go run "github.com/oapi-codegen/oapi-codegen/v2/cmd/oapi-codegen@${OAPI_CODEGEN_VERSION}" \
  -config "$here/oapi-codegen.yaml" "$spec")
(cd "$out" && go mod tidy)
cp "$here/../SDK_README.md" "$out/README.md"
cp "$here/../../LICENSE" "$out/LICENSE"

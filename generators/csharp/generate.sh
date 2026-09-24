#!/usr/bin/env bash
# C# SDK: openapi-generator `csharp` (library generichost, System.Text.Json, net10.0). Output: sdks/csharp/ (NuGet `Dona.Api`).
# Usage: generators/csharp/generate.sh <client-view.yaml> <out-dir> <sdk-version>
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=../versions.env
source "$here/../versions.env"
# shellcheck source=../lib.sh
source "$here/../lib.sh"
spec="$1" out="$2" version="$3"
# No commas: openapi-generator splits --additional-properties on them.
DESCRIPTION="Dona API client (C#) — generated from the OpenAPI contract. Do not edit: regenerate."
# packageGuid is FIXED: left unset the generator mints a random one per run and the output never compares clean.
# The empty test-project stub and the copy of the spec under api/ are not part of the library.
export OPENAPI_GENERATOR_EXTRA_IGNORE="src/Dona.Api.Test/** api/**"
openapi_generator csharp "$spec" "$out" \
  "library=generichost,packageName=Dona.Api,packageVersion=${version},targetFramework=net10.0,nullableReferenceTypes=true,useDateTimeOffset=true,packageCompany=Dona,packageAuthors=Dona,packageTitle=Dona API,sourceFolder=src,equatable=false,validatable=false,packageDescription=${DESCRIPTION},packageCopyright=Dona,packageGuid={6B1D0A5E-3C2F-4E8B-9D7A-D0A0A91C5D01}"
cp "$here/../SDK_README.md" "$out/SDK.md"

#!/usr/bin/env bash
# PHP SDK: openapi-generator `php` (Guzzle 7, PSR-4 `Dona\Api\`). Output: sdks/php/ (composer `ozbuz/dona-api` — openapi-generator derives it from --git-user-id/--git-repo-id).
# Usage: generators/php/generate.sh <client-view.yaml> <out-dir> <sdk-version>
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=../versions.env
source "$here/../versions.env"
# shellcheck source=../lib.sh
source "$here/../lib.sh"
spec="$1" out="$2" version="$3"
openapi_generator php "$spec" "$out" \
  "invokerPackage=Dona\\Api,packageName=dona-api,artifactVersion=${version},licenseName=proprietary,developerOrganization=Dona,developerOrganizationUrl=https://dona.uz,artifactUrl=https://github.com/ozbuz/dona-api"
# ⛔ Booleans in the QUERY must go out as `true`/`false`. The generator's runtime default is `1`/`0`,
# and `?dry_run=1` is not the contract's boolean — a server that reads it as "not a dry run" would
# perform a REAL write the caller believed was a rehearsal. Flip the default in the generated
# Configuration; fail loudly if a generator upgrade moved the line (never ship the unsafe default).
cfg="$out/lib/Configuration.php"
unsafe='protected $booleanFormatForQueryString = self::BOOLEAN_FORMAT_INT;'
grep -qF "$unsafe" "$cfg" || { echo "php generate: Configuration.php no longer has the boolean-format line — re-check dry_run serialisation" >&2; exit 1; }
sed -i.bak "s/self::BOOLEAN_FORMAT_INT;/self::BOOLEAN_FORMAT_STRING; \/\/ Dona: query booleans are true\/false (generators\/php\/generate.sh)/" "$cfg"
rm -f "$cfg.bak"
grep -qF 'protected $booleanFormatForQueryString = self::BOOLEAN_FORMAT_STRING;' "$cfg"
cp "$here/../SDK_README.md" "$out/SDK.md"

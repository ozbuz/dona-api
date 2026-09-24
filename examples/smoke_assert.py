"""Asserts the mock's request log (one JSON line per request) from examples/smoke.sh.

For every language, with the real-shaped key: GET /me, GET /products with limit=5, and POST /stock with
a non-empty Idempotency-Key and dry_run=true — all answered 200. With the malformed key: exactly one
request, answered 401 (the example must stop at the first error).
"""

import json
import sys
from collections import defaultdict

LANGS = ["typescript", "python", "go", "php", "csharp"]
rows = [json.loads(line) for line in open(sys.argv[1], encoding="utf-8") if line.strip()]
by_lang: dict[str, list[dict]] = defaultdict(list)
for r in rows:
    by_lang[r.get("integration", "").removeprefix("dona-api-examples/")].append(r)

problems = []
for lang in LANGS:
    reqs = by_lang.get(lang, [])
    ok = [r for r in reqs if r["authorized"]]
    rejected = [r for r in reqs if not r["authorized"]]
    calls = {(r["method"], r["path"].removeprefix("/seller-api/v1")): r for r in ok}
    me, products, stock = calls.get(("GET", "/me")), calls.get(("GET", "/products")), calls.get(("POST", "/stock"))
    if not me or me["status"] != 200:
        problems.append(f"{lang}: GET /me missing or not 200")
    if not products or products["status"] != 200 or "limit=5" not in products["query"].split("&"):
        problems.append(f"{lang}: GET /products?limit=5 missing, not 200, or limit≠5 ({products and products['query']})")
    if not stock or stock["status"] != 200:
        problems.append(f"{lang}: POST /stock missing or not 200")
    elif not stock["idempotency_key"] or not stock["dry_run"]:
        problems.append(f"{lang}: POST /stock without Idempotency-Key or dry_run=true")
    if len(ok) != 3:
        problems.append(f"{lang}: expected 3 authorised requests, saw {len(ok)}")
    if len(rejected) != 1 or rejected[0]["status"] != 401:
        problems.append(f"{lang}: malformed key should produce exactly one 401, saw {[r['status'] for r in rejected]}")

stray = set(by_lang) - set(LANGS)
if stray:
    problems.append(f"requests without a known X-Dona-Integration: {sorted(stray)}")
if problems:
    print("smoke: FAILED\n  " + "\n  ".join(problems), file=sys.stderr)
    sys.exit(1)
print(f"smoke: ok — {len(LANGS)} languages × (3 calls + 1 rejected key), {len(rows)} requests")

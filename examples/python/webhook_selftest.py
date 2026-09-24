"""Runs the shared vectors (examples/testdata/webhook-vectors.json) through verify_webhook."""

import json
import pathlib
import sys

from webhook import WebhookVerificationError, verify_webhook

vectors = json.loads((pathlib.Path(__file__).parent.parent / "testdata" / "webhook-vectors.json").read_text("utf-8"))
failed = 0
for c in vectors["cases"]:
    headers = {"webhook-id": c["id"], "webhook-timestamp": str(c["timestamp"]), "webhook-signature": c["signature"]}
    try:
        verify_webhook(c["secret"], headers, c["body"], now=c["now"])
        valid = True
    except WebhookVerificationError:
        valid = False
    if valid != c["valid"]:
        failed += 1
        print(f"FAIL {c['name']}: got valid={valid}, want {c['valid']}", file=sys.stderr)
print(f"python webhook: {len(vectors['cases']) - failed}/{len(vectors['cases'])} vectors")
sys.exit(1 if failed else 0)

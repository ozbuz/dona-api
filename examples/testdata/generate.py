"""Writes webhook-vectors.json — the cases EVERY language's webhook verifier must agree on.

Run: python3 examples/testdata/generate.py   (stdlib only; the output is committed)

Signing is Standard Webhooks (https://www.standardwebhooks.com), as the contract states:
  webhook-signature = space-delimited "v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + "." + ts + "." + rawBody)>"
  reject when |now - webhook-timestamp| > 300 s.
Case 1 is the reference vector published by the Standard Webhooks project, so a verifier that passes
it interoperates with every other implementation, not only with ours.
"""
import base64
import hashlib
import hmac
import json
import pathlib

TOLERANCE = 300


def sign(secret: str, msg_id: str, ts: int, body: str) -> str:
    key = base64.b64decode(secret.removeprefix("whsec_"))
    mac = hmac.new(key, f"{msg_id}.{ts}.".encode() + body.encode("utf-8"), hashlib.sha256).digest()
    return "v1," + base64.b64encode(mac).decode()


REF_SECRET = "whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw"
DONA_SECRET = "whsec_MfKQ9r2ysWbG2xZt8k1r5sFh3Dq0Vv7L"  # the contract's own example secret
OTHER_SECRET = "whsec_2b9Lr8QpXw4Tn6Yc1Hs0Kd5Fa3Gm7Ze9"
EVT_ID = "01997b31-2c4d-7e5f-8a9b-0c1d2e3f4a5b"
TS = 1758704700
BODY = json.dumps(
    {"id": EVT_ID, "type": "order.created", "occurred_at": "2026-09-24T14:05:00+05:00",
     "data": {"order_id": "01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b", "status": "paid"}},
    separators=(",", ":"), ensure_ascii=False)
BODY_UTF8 = json.dumps({"id": EVT_ID, "type": "product.published", "data": {"title": {"uz": "Oʻyinchoq ayiq", "ru": "Плюшевый мишка"}}},
                       separators=(",", ":"), ensure_ascii=False)

good = sign(DONA_SECRET, EVT_ID, TS, BODY)
wrong = sign(OTHER_SECRET, EVT_ID, TS, BODY)

cases = [
    dict(name="standard-webhooks reference vector", secret=REF_SECRET, id="msg_p5jXN8AQM9LWM0D4loKWxJek",
         timestamp=1614265330, body='{"test": 2432232314}', signature="v1,g0hM9SsE+OTPJTGt/tmIKtSyZlE3uFJELVlNIOLJ1OE=",
         now=1614265330, valid=True),
    dict(name="dona event", secret=DONA_SECRET, id=EVT_ID, timestamp=TS, body=BODY, signature=good, now=TS + 5, valid=True),
    dict(name="rotation: old secret listed first, new second", secret=DONA_SECRET, id=EVT_ID, timestamp=TS, body=BODY,
         signature=f"{wrong} {good}", now=TS, valid=True),
    dict(name="utf-8 body signed as raw bytes", secret=DONA_SECRET, id=EVT_ID, timestamp=TS, body=BODY_UTF8,
         signature=sign(DONA_SECRET, EVT_ID, TS, BODY_UTF8), now=TS, valid=True),
    dict(name="exactly at the 300 s tolerance", secret=DONA_SECRET, id=EVT_ID, timestamp=TS, body=BODY,
         signature=good, now=TS + TOLERANCE, valid=True),
    dict(name="tampered body", secret=DONA_SECRET, id=EVT_ID, timestamp=TS, body=BODY.replace("paid", "cancelled"),
         signature=good, now=TS, valid=False),
    dict(name="signed with another secret", secret=DONA_SECRET, id=EVT_ID, timestamp=TS, body=BODY,
         signature=wrong, now=TS, valid=False),
    dict(name="different webhook-id", secret=DONA_SECRET, id="01997b31-2c4d-7e5f-8a9b-000000000000", timestamp=TS,
         body=BODY, signature=good, now=TS, valid=False),
    dict(name="timestamp too old (301 s)", secret=DONA_SECRET, id=EVT_ID, timestamp=TS, body=BODY, signature=good,
         now=TS + TOLERANCE + 1, valid=False),
    dict(name="timestamp in the future (301 s)", secret=DONA_SECRET, id=EVT_ID, timestamp=TS, body=BODY, signature=good,
         now=TS - TOLERANCE - 1, valid=False),
    dict(name="unknown signature version only", secret=DONA_SECRET, id=EVT_ID, timestamp=TS, body=BODY,
         signature="v1a," + good.split(",", 1)[1], now=TS, valid=False),
    dict(name="empty signature header", secret=DONA_SECRET, id=EVT_ID, timestamp=TS, body=BODY, signature="", now=TS,
         valid=False),
]

out = pathlib.Path(__file__).with_name("webhook-vectors.json")
out.write_text(json.dumps({"tolerance_seconds": TOLERANCE, "cases": cases}, indent=2, ensure_ascii=False) + "\n",
               encoding="utf-8")
print(f"wrote {out.name}: {len(cases)} cases")

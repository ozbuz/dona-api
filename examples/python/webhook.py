"""Dona webhook signature verification (Standard Webhooks) — stdlib only.

Headers on every delivery: webhook-id · webhook-timestamp · webhook-signature.
  signature = space-delimited "v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id.ts.raw_body)>"
  (two entries for 24 h after a secret rotation — accept if ANY matches)

⚠ Verify the RAW request bytes (Flask: request.get_data(), Django: request.body, FastAPI:
  await request.body()). Re-serialised JSON never matches. Then dedupe on webhook-id for 24 h.

    try:
        verify_webhook(os.environ["DONA_WEBHOOK_SECRET"], request.headers, request.get_data())
    except WebhookVerificationError:
        return "", 401
    return "", 204          # acknowledge fast; process asynchronously
"""

import base64
import hashlib
import hmac
import time
from collections.abc import Mapping

TOLERANCE_SECONDS = 300


class WebhookVerificationError(Exception):
    pass


def _header(headers: Mapping[str, str], name: str) -> str:
    for k, v in headers.items():
        if k.lower() == name:
            return v
    return ""


def verify_webhook(secret: str, headers: Mapping[str, str], raw_body: bytes | str, now: int | None = None) -> None:
    """Raises WebhookVerificationError unless the delivery is authentic and fresh."""
    msg_id = _header(headers, "webhook-id")
    ts = _header(headers, "webhook-timestamp")
    signatures = _header(headers, "webhook-signature")
    if not (msg_id and ts and signatures):
        raise WebhookVerificationError("missing webhook-* headers")
    try:
        timestamp = int(ts)
    except ValueError as e:
        raise WebhookVerificationError("bad webhook-timestamp") from e
    now = int(time.time()) if now is None else now
    if abs(now - timestamp) > TOLERANCE_SECONDS:
        raise WebhookVerificationError("timestamp outside tolerance")

    key = base64.b64decode(secret.removeprefix("whsec_"))
    body = raw_body.encode("utf-8") if isinstance(raw_body, str) else raw_body
    expected = hmac.new(key, f"{msg_id}.{ts}.".encode() + body, hashlib.sha256).digest()
    for entry in signatures.split(" "):
        version, _, sig = entry.partition(",")
        if version != "v1" or not sig:
            continue
        try:
            got = base64.b64decode(sig, validate=True)
        except ValueError:
            continue
        if hmac.compare_digest(got, expected):
            return
    raise WebhookVerificationError("no matching signature")

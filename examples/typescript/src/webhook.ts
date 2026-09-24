// Dona webhook signature verification (Standard Webhooks) — Node, no dependencies.
//
// Headers on every delivery: webhook-id · webhook-timestamp · webhook-signature.
//   signature = space-delimited "v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id.ts.rawBody)>"
//   (two entries for 24 h after a secret rotation — accept if ANY matches)
//
// ⚠ Verify the RAW request bytes. Parsing the JSON and re-serialising it changes the bytes and the
//   signature will never match. Then dedupe on webhook-id (it is the event id) for 24 h.
//
//   http.createServer(async (req, res) => {
//     const body = Buffer.concat(await Array.fromAsync(req));
//     try { verifyWebhook(process.env.DONA_WEBHOOK_SECRET!, req.headers, body); }
//     catch { res.writeHead(401).end(); return; }
//     res.writeHead(204).end();          // acknowledge fast; process asynchronously
//   });
import { createHmac, timingSafeEqual } from "node:crypto";

export const TOLERANCE_SECONDS = 300;

export class WebhookVerificationError extends Error {}

type HeaderBag = Record<string, string | string[] | undefined> | Headers;

function header(h: HeaderBag, name: string): string {
  const v = h instanceof Headers ? h.get(name) : h[name] ?? h[name.toLowerCase()];
  return (Array.isArray(v) ? v[0] : v) ?? "";
}

/** Throws WebhookVerificationError unless the delivery is authentic and fresh. */
export function verifyWebhook(
  secret: string,
  headers: HeaderBag,
  rawBody: Uint8Array | string,
  nowSeconds: number = Math.floor(Date.now() / 1000),
): void {
  const id = header(headers, "webhook-id");
  const ts = header(headers, "webhook-timestamp");
  const signatures = header(headers, "webhook-signature");
  if (!id || !ts || !signatures) throw new WebhookVerificationError("missing webhook-* headers");

  const timestamp = Number(ts);
  if (!Number.isInteger(timestamp)) throw new WebhookVerificationError("bad webhook-timestamp");
  if (Math.abs(nowSeconds - timestamp) > TOLERANCE_SECONDS) throw new WebhookVerificationError("timestamp outside tolerance");

  const key = Buffer.from(secret.startsWith("whsec_") ? secret.slice(6) : secret, "base64");
  const body = typeof rawBody === "string" ? Buffer.from(rawBody, "utf8") : Buffer.from(rawBody);
  const expected = createHmac("sha256", key).update(`${id}.${ts}.`).update(body).digest();

  for (const entry of signatures.split(" ")) {
    const [version, sig] = entry.split(",", 2);
    if (version !== "v1" || !sig) continue;
    const got = Buffer.from(sig, "base64");
    if (got.length === expected.length && timingSafeEqual(got, expected)) return;
  }
  throw new WebhookVerificationError("no matching signature");
}

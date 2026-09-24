// Runs the shared vectors (examples/testdata/webhook-vectors.json) through verifyWebhook.
import { readFileSync } from "node:fs";
import { verifyWebhook } from "./webhook.ts";

interface Vector { name: string; secret: string; id: string; timestamp: number; body: string; signature: string; now: number; valid: boolean }
const { cases } = JSON.parse(readFileSync(new URL("../../testdata/webhook-vectors.json", import.meta.url), "utf8")) as { cases: Vector[] };

let failed = 0;
for (const c of cases) {
  let valid = true;
  try {
    verifyWebhook(c.secret, { "webhook-id": c.id, "webhook-timestamp": String(c.timestamp), "webhook-signature": c.signature }, c.body, c.now);
  } catch {
    valid = false;
  }
  if (valid !== c.valid) {
    failed++;
    console.error(`FAIL ${c.name}: got valid=${valid}, want ${c.valid}`);
  }
}
console.log(`typescript webhook: ${cases.length - failed}/${cases.length} vectors`);
process.exit(failed ? 1 : 0);

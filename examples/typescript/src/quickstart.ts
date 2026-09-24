// Dona API quickstart — the portal's "Boshlash" steps 2–4, in TypeScript.
//
//   DONA_API_KEY=dona_sk_live_… npm run quickstart
//
// 1. GET /me                  who the key is: shop, tier, limits
// 2. GET /products?limit=5    the first page of the catalogue
// 3. POST /stock?dry_run=true re-sends the first product's CURRENT stock as a rehearsal: validated,
//                             guarded and rolled back — nothing is written, whatever the answer.
//
// Optional: DONA_API_BASE_URL (defaults to production, the only environment).
import { randomUUID } from "node:crypto";
import { createDonaClient, DONA_API_BASE_URL, isHeldForReview, rateLimit, type DonaError } from "@dona/api";

const apiKey = process.env.DONA_API_KEY;
if (!apiKey) {
  console.error("Set DONA_API_KEY (dona_sk_live_…) — the shop owner mints it in Sozlamalar › API.");
  process.exit(2);
}

const dona = createDonaClient({
  apiKey,
  baseUrl: process.env.DONA_API_BASE_URL ?? DONA_API_BASE_URL,
  integration: "dona-api-examples/typescript",
});

function fail(step: string, response: Response, error: DonaError | undefined): never {
  // Branch on `error` (a stable code), never on `message` (localised text).
  console.error(`${step} → HTTP ${response.status} ${error?.error ?? ""}: ${error?.message ?? ""} (request ${error?.request_id ?? "?"})`);
  const rl = rateLimit(response);
  if (rl.retryAfter) console.error(`  retry after ${rl.retryAfter}s (${rl.reason ?? "rate limited"})`);
  process.exit(1);
}

// 1 ─ who am I
const me = await dona.GET("/me");
if (!me.data) fail("GET /me", me.response, me.error);
const { shop, tier, writes_enabled } = me.data;
console.log(`shop: ${shop.name} (${shop.status}) · tier ${tier} · writes_enabled ${writes_enabled}`);
const rl = rateLimit(me.response);
console.log(`rate limit: ${rl.remaining ?? "?"}/${rl.limit ?? "?"} left · policy ${rl.policy ?? "?"}`);

// 2 ─ first five products
const products = await dona.GET("/products", { params: { query: { limit: 5 } } });
if (!products.data) fail("GET /products", products.response, products.error);
for (const p of products.data.items) {
  console.log(`  ${p.id}  ${p.seller_sku ?? "-"}  stock ${p.stock}  ${p.title.uz ?? p.title.ru ?? ""}`);
}

// 3 ─ rehearse a stock write
const first = products.data.items[0];
if (!first) {
  console.log("no products yet — skipping the POST /stock rehearsal");
  process.exit(0);
}
const variant = first.variants?.[0];
const line = variant
  ? { product_id: first.id, variant_id: variant.id, quantity: variant.stock }
  : { product_id: first.id, quantity: first.stock };

const stock = await dona.POST("/stock", {
  params: {
    query: { dry_run: true },
    // One key per logical write. Re-send the SAME key on a retry: the answer is replayed for 24 h.
    header: { "Idempotency-Key": randomUUID() },
  },
  body: { items: [line] },
});
if (stock.response.status === 202 && isHeldForReview(stock.data)) {
  console.log(`POST /stock held for review: rule ${stock.data.rule} · approval ${stock.data.approval_id} — nothing was written`);
} else if (stock.data && "summary" in stock.data) {
  const s = stock.data.summary;
  console.log(`POST /stock dry_run=${stock.data.dry_run}: ok ${s.ok} · error ${s.error} · held ${s.held}`);
} else {
  fail("POST /stock", stock.response, stock.error);
}

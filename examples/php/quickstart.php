<?php
// Dona API quickstart — the portal's "Boshlash" steps 2–4, in PHP.
//
//   composer install && DONA_API_KEY=dona_sk_live_… php quickstart.php
//
// 1. GET /me                   who the key is: shop, tier, limits
// 2. GET /products?limit=5     the first page of the catalogue
// 3. POST /stock?dry_run=true  re-sends the first product's CURRENT stock as a rehearsal: validated,
//                              guarded and rolled back — nothing is written, whatever the answer.
//
// Optional: DONA_API_BASE_URL (defaults to production, the only environment).
declare(strict_types=1);

require __DIR__ . '/vendor/autoload.php';

use Dona\Api\Api\AccountApi;
use Dona\Api\Api\CatalogApi;
use Dona\Api\Api\StockPricesApi;
use Dona\Api\ApiException;
use Dona\Api\Configuration;
use Dona\Api\Model\BulkResult;
use Dona\Api\Model\Error;
use Dona\Api\Model\HeldForReview;
use Dona\Api\Model\StockLine;
use Dona\Api\Model\StockRequest;
use GuzzleHttp\Client;

const INTEGRATION = 'dona-api-examples/php';

$apiKey = getenv('DONA_API_KEY') ?: '';
if ($apiKey === '') {
    fwrite(STDERR, "Set DONA_API_KEY (dona_sk_live_…) — the shop owner mints it in Sozlamalar › API.\n");
    exit(2);
}

$config = Configuration::getDefaultConfiguration()->setAccessToken($apiKey); // Authorization: Bearer <key>
if ($base = getenv('DONA_API_BASE_URL')) {
    $config->setHost($base);
}
$http = new Client(['timeout' => 30]);

/** Prints the error envelope. Branch on `error` (a stable code), never on `message` (localised). */
function fail(string $step, ApiException $e): never
{
    $err = $e->getResponseObject();
    $code = $err instanceof Error ? $err->getError() : '';
    $msg = $err instanceof Error ? $err->getMessage() : $e->getMessage();
    fwrite(STDERR, sprintf("%s → HTTP %d %s: %s\n", $step, $e->getCode(), $code, $msg));
    $retry = array_change_key_case($e->getResponseHeaders() ?? [], CASE_LOWER)['retry-after'][0] ?? null;
    if ($retry !== null) {
        fwrite(STDERR, "  retry after {$retry}s\n");
    }
    exit(1);
}

// 1 ─ who am I
try {
    [$me, , $headers] = (new AccountApi($http, $config))->getMeWithHttpInfo('uz', INTEGRATION);
    $headers = array_change_key_case($headers, CASE_LOWER); // header names are case-insensitive; PHP keys are not
} catch (ApiException $e) {
    fail('GET /me', $e);
}
printf("shop: %s (%s) · tier %s · writes_enabled %s\n", $me->getShop()->getName(), $me->getShop()->getStatus(),
    $me->getTier(), var_export($me->getWritesEnabled(), true));
printf("rate limit: %s/%s left · policy %s\n", $headers['x-ratelimit-remaining'][0] ?? '?',
    $headers['x-ratelimit-limit'][0] ?? '?', $headers['ratelimit-policy'][0] ?? '?');

// 2 ─ first five products
try {
    $page = (new CatalogApi($http, $config))->listProducts(limit: 5, x_dona_integration: INTEGRATION);
} catch (ApiException $e) {
    fail('GET /products', $e);
}
foreach ($page->getItems() as $p) {
    $title = $p->getTitle()->getUz() ?? $p->getTitle()->getRu() ?? '';
    printf("  %s  %s  stock %d  %s\n", $p->getId(), $p->getSellerSku() ?? '-', $p->getStock(), $title);
}

// 3 ─ rehearse a stock write
$first = $page->getItems()[0] ?? null;
if ($first === null) {
    echo "no products yet — skipping the POST /stock rehearsal\n";
    exit(0);
}
$variant = $first->getVariants()[0] ?? null;
$line = $variant !== null
    ? new StockLine(['product_id' => $first->getId(), 'variant_id' => $variant->getId(), 'quantity' => $variant->getStock()])
    : new StockLine(['product_id' => $first->getId(), 'quantity' => $first->getStock()]);

try {
    $result = (new StockPricesApi($http, $config))->setStock(
        // One key per logical write. Re-send the SAME key on a retry: the answer is replayed for 24 h.
        idempotency_key: bin2hex(random_bytes(16)),
        stock_request: new StockRequest(['items' => [$line]]),
        dry_run: true,
        x_dona_integration: INTEGRATION,
    );
} catch (ApiException $e) {
    fail('POST /stock', $e);
}
if ($result instanceof HeldForReview) {
    printf("POST /stock held for review: rule %s · approval %s — nothing was written\n", $result->getRule(), $result->getApprovalId());
} elseif ($result instanceof BulkResult) {
    $s = $result->getSummary();
    printf("POST /stock dry_run=%s: ok %d · error %d · held %d\n", var_export($result->getDryRun(), true), $s->getOk(), $s->getError(), $s->getHeld());
}

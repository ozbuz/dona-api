# Dona\Api\StockPricesApi



All URIs are relative to https://api.dona.im/seller-api/v1, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**listStock()**](StockPricesApi.md#listStock) | **GET** /stock | Stock, SKU-level |
| [**setPrices()**](StockPricesApi.md#setPrices) | **POST** /prices | Set absolute prices (≤ 1 000 lines) |
| [**setStock()**](StockPricesApi.md#setStock) | **POST** /stock | Set absolute stock (≤ 1 000 lines) |


## `listStock()`

```php
listStock($cursor, $page, $limit, $updated_since, $seller_sku, $if_none_match, $accept_language, $dona_seller, $x_dona_integration): \Dona\Api\Model\StockLineViewPage
```

Stock, SKU-level

One row per product without variants, one per variant otherwise. `cursor` or 0-based `page` (slower).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\StockPricesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$cursor = 'cursor_example'; // string | Opaque keyset cursor from `next_cursor`.
$page = 56; // int | 0-based page alias (Uzum parity) — slower than `cursor`, ≤ 1 000 pages; mutually exclusive with `cursor`.
$limit = 50; // int | Page size, default 50, max 100 (clamped, with `Dona-API-Warn`). `limit > 50` costs `1 + ceil(limit/50)`.
$updated_since = 2026-09-24T09:00:00+05:00; // string | ISO 8601 with offset, or epoch milliseconds. The visible high-water mark is capped at `now() − 10 s` so a slow transaction is never skipped.
$seller_sku = 'seller_sku_example'; // string | Exact.
$if_none_match = 'if_none_match_example'; // string | An `ETag` from a previous identical request ⇒ `304` with rate headers (cost 0.5).
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$dona_seller = 'dona_seller_example'; // string | Vendor-app install keys only (`dona_it_live_…`, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"required\"}]`; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no `urn:uuid:`, no padding) ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"invalid\"}]`; naming any other shop — even one that installed the same app ⇒ `404 not_found` (never 403; nothing is read). Ignored on a seller key (`dona_sk_`).
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->listStock($cursor, $page, $limit, $updated_since, $seller_sku, $if_none_match, $accept_language, $dona_seller, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling StockPricesApi->listStock: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cursor** | **string**| Opaque keyset cursor from &#x60;next_cursor&#x60;. | [optional] |
| **page** | **int**| 0-based page alias (Uzum parity) — slower than &#x60;cursor&#x60;, ≤ 1 000 pages; mutually exclusive with &#x60;cursor&#x60;. | [optional] |
| **limit** | **int**| Page size, default 50, max 100 (clamped, with &#x60;Dona-API-Warn&#x60;). &#x60;limit &gt; 50&#x60; costs &#x60;1 + ceil(limit/50)&#x60;. | [optional] [default to 50] |
| **updated_since** | **string**| ISO 8601 with offset, or epoch milliseconds. The visible high-water mark is capped at &#x60;now() − 10 s&#x60; so a slow transaction is never skipped. | [optional] |
| **seller_sku** | **string**| Exact. | [optional] |
| **if_none_match** | **string**| An &#x60;ETag&#x60; from a previous identical request ⇒ &#x60;304&#x60; with rate headers (cost 0.5). | [optional] |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **dona_seller** | **string**| Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

[**\Dona\Api\Model\StockLineViewPage**](../Model/StockLineViewPage.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `setPrices()`

```php
setPrices($idempotency_key, $price_request, $atomic, $dona_dry_run, $dry_run, $accept_language, $dona_seller, $x_dona_integration): \Dona\Api\Model\BulkResult
```

Set absolute prices (≤ 1 000 lines)

As `POST /stock`. Price < `catalog.price_floor_uzs` (1 000) or > 100× drop vs current/last-sold ⇒ `held`; `compare_at_uzs` must exceed `price_uzs`. Kill switch: `writes_enabled`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\StockPricesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$idempotency_key = sync-2026-09-24T09:05; // string | 1–255 chars. Scope = this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ `400 invalid_body` with `details[{field:\"Idempotency-Key\",code:\"required\"}]`.
$price_request = new \Dona\Api\Model\PriceRequest(); // \Dona\Api\Model\PriceRequest
$atomic = True; // bool | All-or-nothing.
$dona_dry_run = 'dona_dry_run_example'; // string | `true` ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as `?dry_run=true`. Only the literal `true` / `false`; any other value ⇒ `400 invalid_body` + `details[{field:\"Dona-Dry-Run\", code:\"invalid\"}]` (C51).
$dry_run = 'dry_run_example'; // string | Alias of the `Dona-Dry-Run` header. Only the literal strings `true` / `false` — `1`, `0`, `TRUE`, `yes`, an empty value ⇒ `400 invalid_body` + `details[{field:\"dry_run\", code:\"invalid\"}]` (C51). A string enum, not a boolean, so no SDK generator serialises it as `1`/`0`.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$dona_seller = 'dona_seller_example'; // string | Vendor-app install keys only (`dona_it_live_…`, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"required\"}]`; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no `urn:uuid:`, no padding) ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"invalid\"}]`; naming any other shop — even one that installed the same app ⇒ `404 not_found` (never 403; nothing is read). Ignored on a seller key (`dona_sk_`).
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->setPrices($idempotency_key, $price_request, $atomic, $dona_dry_run, $dry_run, $accept_language, $dona_seller, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling StockPricesApi->setPrices: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **idempotency_key** | **string**| 1–255 chars. Scope &#x3D; this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ &#x60;400 invalid_body&#x60; with &#x60;details[{field:\&quot;Idempotency-Key\&quot;,code:\&quot;required\&quot;}]&#x60;. | |
| **price_request** | [**\Dona\Api\Model\PriceRequest**](../Model/PriceRequest.md)|  | |
| **atomic** | **bool**| All-or-nothing. | [optional] |
| **dona_dry_run** | **string**| &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. Only the literal &#x60;true&#x60; / &#x60;false&#x60;; any other value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Dry-Run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). | [optional] |
| **dry_run** | **string**| Alias of the &#x60;Dona-Dry-Run&#x60; header. Only the literal strings &#x60;true&#x60; / &#x60;false&#x60; — &#x60;1&#x60;, &#x60;0&#x60;, &#x60;TRUE&#x60;, &#x60;yes&#x60;, an empty value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;dry_run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). A string enum, not a boolean, so no SDK generator serialises it as &#x60;1&#x60;/&#x60;0&#x60;. | [optional] |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **dona_seller** | **string**| Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

[**\Dona\Api\Model\BulkResult**](../Model/BulkResult.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `setStock()`

```php
setStock($idempotency_key, $stock_request, $atomic, $dona_dry_run, $dry_run, $accept_language, $dona_seller, $x_dona_integration): \Dona\Api\Model\BulkResult
```

Set absolute stock (≤ 1 000 lines)

Synchronous, through `catalog.ApplyGuardedStockPrice`. `200` with per-line results — the request is refused whole only for shape/budget (400/413/422). `?atomic=true` = all-or-nothing (any held line ⇒ `202` for the batch). |Δ| > 10× and > 1 000, or zeroing > 50 % of lines ⇒ `held`. One object ≤ 1 write / 10 s ⇒ line `error: object_cooldown`. Kill switch: `writes_enabled`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\StockPricesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$idempotency_key = sync-2026-09-24T09:05; // string | 1–255 chars. Scope = this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ `400 invalid_body` with `details[{field:\"Idempotency-Key\",code:\"required\"}]`.
$stock_request = new \Dona\Api\Model\StockRequest(); // \Dona\Api\Model\StockRequest
$atomic = True; // bool | All-or-nothing (Yandex default).
$dona_dry_run = 'dona_dry_run_example'; // string | `true` ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as `?dry_run=true`. Only the literal `true` / `false`; any other value ⇒ `400 invalid_body` + `details[{field:\"Dona-Dry-Run\", code:\"invalid\"}]` (C51).
$dry_run = 'dry_run_example'; // string | Alias of the `Dona-Dry-Run` header. Only the literal strings `true` / `false` — `1`, `0`, `TRUE`, `yes`, an empty value ⇒ `400 invalid_body` + `details[{field:\"dry_run\", code:\"invalid\"}]` (C51). A string enum, not a boolean, so no SDK generator serialises it as `1`/`0`.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$dona_seller = 'dona_seller_example'; // string | Vendor-app install keys only (`dona_it_live_…`, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"required\"}]`; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no `urn:uuid:`, no padding) ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"invalid\"}]`; naming any other shop — even one that installed the same app ⇒ `404 not_found` (never 403; nothing is read). Ignored on a seller key (`dona_sk_`).
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->setStock($idempotency_key, $stock_request, $atomic, $dona_dry_run, $dry_run, $accept_language, $dona_seller, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling StockPricesApi->setStock: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **idempotency_key** | **string**| 1–255 chars. Scope &#x3D; this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ &#x60;400 invalid_body&#x60; with &#x60;details[{field:\&quot;Idempotency-Key\&quot;,code:\&quot;required\&quot;}]&#x60;. | |
| **stock_request** | [**\Dona\Api\Model\StockRequest**](../Model/StockRequest.md)|  | |
| **atomic** | **bool**| All-or-nothing (Yandex default). | [optional] |
| **dona_dry_run** | **string**| &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. Only the literal &#x60;true&#x60; / &#x60;false&#x60;; any other value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Dry-Run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). | [optional] |
| **dry_run** | **string**| Alias of the &#x60;Dona-Dry-Run&#x60; header. Only the literal strings &#x60;true&#x60; / &#x60;false&#x60; — &#x60;1&#x60;, &#x60;0&#x60;, &#x60;TRUE&#x60;, &#x60;yes&#x60;, an empty value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;dry_run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). A string enum, not a boolean, so no SDK generator serialises it as &#x60;1&#x60;/&#x60;0&#x60;. | [optional] |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **dona_seller** | **string**| Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

[**\Dona\Api\Model\BulkResult**](../Model/BulkResult.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

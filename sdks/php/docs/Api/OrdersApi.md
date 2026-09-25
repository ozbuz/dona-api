# Dona\Api\OrdersApi

The &#x60;orders:read&#x60; projection has no buyer PII; &#x60;orders:pii&#x60; (ADVANCED, &#x60;sk&#x60;) adds it.

All URIs are relative to https://api.dona.im/seller-api/v1, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**acceptOrder()**](OrdersApi.md#acceptOrder) | **POST** /orders/{id}/accept | Accept |
| [**addOrderNote()**](OrdersApi.md#addOrderNote) | **POST** /orders/{id}/notes | Add a seller note |
| [**batchOrderLabels()**](OrdersApi.md#batchOrderLabels) | **POST** /orders/labels | Labels for ≤ 100 orders (one PDF) |
| [**cancelOrder()**](OrdersApi.md#cancelOrder) | **POST** /orders/{id}/cancel | Cancel (after acceptance) — money-reversing |
| [**declineOrder()**](OrdersApi.md#declineOrder) | **POST** /orders/{id}/decline | Decline (before acceptance) — money-reversing |
| [**getOrder()**](OrdersApi.md#getOrder) | **GET** /orders/{id} | Get an order (PII only with orders:pii) |
| [**getOrderInvoice()**](OrdersApi.md#getOrderInvoice) | **GET** /orders/{id}/invoice.pdf | Invoice (PDF, contains PII) |
| [**getOrderLabel()**](OrdersApi.md#getOrderLabel) | **GET** /orders/{id}/label.pdf | Shipping label (PDF, contains PII) |
| [**getOrderTimeline()**](OrdersApi.md#getOrderTimeline) | **GET** /orders/{id}/timeline | Order timeline |
| [**handoverOrder()**](OrdersApi.md#handoverOrder) | **POST** /orders/{id}/handover | Hand over to the courier |
| [**listOrders()**](OrdersApi.md#listOrders) | **GET** /orders | List orders (no buyer PII) |
| [**markOrderReady()**](OrdersApi.md#markOrderReady) | **POST** /orders/{id}/ready | Mark ready to ship |
| [**shipOrder()**](OrdersApi.md#shipOrder) | **POST** /orders/{id}/ship | Ship |


## `acceptOrder()`

```php
acceptOrder($id, $idempotency_key, $dona_dry_run, $dry_run, $accept_language, $dona_seller, $x_dona_integration): \Dona\Api\Model\OrderTransition
```

Accept

The `intake.go` accept body, extracted. Needs a pickup address. 409: `order_not_acceptable`, `no_pickup_address`. Kill switch: `writes_enabled`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\OrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Resource id (UUIDv7). A foreign or missing id is always `404 not_found`.
$idempotency_key = sync-2026-09-24T09:05; // string | 1–255 chars. Scope = this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ `400 invalid_body` with `details[{field:\"Idempotency-Key\",code:\"required\"}]`.
$dona_dry_run = 'dona_dry_run_example'; // string | `true` ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as `?dry_run=true`. Only the literal `true` / `false`; any other value ⇒ `400 invalid_body` + `details[{field:\"Dona-Dry-Run\", code:\"invalid\"}]` (C51).
$dry_run = 'dry_run_example'; // string | Alias of the `Dona-Dry-Run` header. Only the literal strings `true` / `false` — `1`, `0`, `TRUE`, `yes`, an empty value ⇒ `400 invalid_body` + `details[{field:\"dry_run\", code:\"invalid\"}]` (C51). A string enum, not a boolean, so no SDK generator serialises it as `1`/`0`.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$dona_seller = 'dona_seller_example'; // string | Vendor-app install keys only (`dona_it_live_…`, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"required\"}]`; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no `urn:uuid:`, no padding) ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"invalid\"}]`; naming any other shop — even one that installed the same app ⇒ `404 not_found` (never 403; nothing is read). Ignored on a seller key (`dona_sk_`).
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->acceptOrder($id, $idempotency_key, $dona_dry_run, $dry_run, $accept_language, $dona_seller, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrdersApi->acceptOrder: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. | |
| **idempotency_key** | **string**| 1–255 chars. Scope &#x3D; this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ &#x60;400 invalid_body&#x60; with &#x60;details[{field:\&quot;Idempotency-Key\&quot;,code:\&quot;required\&quot;}]&#x60;. | |
| **dona_dry_run** | **string**| &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. Only the literal &#x60;true&#x60; / &#x60;false&#x60;; any other value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Dry-Run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). | [optional] |
| **dry_run** | **string**| Alias of the &#x60;Dona-Dry-Run&#x60; header. Only the literal strings &#x60;true&#x60; / &#x60;false&#x60; — &#x60;1&#x60;, &#x60;0&#x60;, &#x60;TRUE&#x60;, &#x60;yes&#x60;, an empty value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;dry_run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). A string enum, not a boolean, so no SDK generator serialises it as &#x60;1&#x60;/&#x60;0&#x60;. | [optional] |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **dona_seller** | **string**| Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

[**\Dona\Api\Model\OrderTransition**](../Model/OrderTransition.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `addOrderNote()`

```php
addOrderNote($id, $idempotency_key, $note_request, $dona_dry_run, $dry_run, $accept_language, $dona_seller, $x_dona_integration): \Dona\Api\Model\NoteCreated
```

Add a seller note

Appends to `order_notes`. Kill switch: `writes_enabled`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\OrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Resource id (UUIDv7). A foreign or missing id is always `404 not_found`.
$idempotency_key = sync-2026-09-24T09:05; // string | 1–255 chars. Scope = this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ `400 invalid_body` with `details[{field:\"Idempotency-Key\",code:\"required\"}]`.
$note_request = new \Dona\Api\Model\NoteRequest(); // \Dona\Api\Model\NoteRequest
$dona_dry_run = 'dona_dry_run_example'; // string | `true` ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as `?dry_run=true`. Only the literal `true` / `false`; any other value ⇒ `400 invalid_body` + `details[{field:\"Dona-Dry-Run\", code:\"invalid\"}]` (C51).
$dry_run = 'dry_run_example'; // string | Alias of the `Dona-Dry-Run` header. Only the literal strings `true` / `false` — `1`, `0`, `TRUE`, `yes`, an empty value ⇒ `400 invalid_body` + `details[{field:\"dry_run\", code:\"invalid\"}]` (C51). A string enum, not a boolean, so no SDK generator serialises it as `1`/`0`.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$dona_seller = 'dona_seller_example'; // string | Vendor-app install keys only (`dona_it_live_…`, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"required\"}]`; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no `urn:uuid:`, no padding) ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"invalid\"}]`; naming any other shop — even one that installed the same app ⇒ `404 not_found` (never 403; nothing is read). Ignored on a seller key (`dona_sk_`).
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->addOrderNote($id, $idempotency_key, $note_request, $dona_dry_run, $dry_run, $accept_language, $dona_seller, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrdersApi->addOrderNote: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. | |
| **idempotency_key** | **string**| 1–255 chars. Scope &#x3D; this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ &#x60;400 invalid_body&#x60; with &#x60;details[{field:\&quot;Idempotency-Key\&quot;,code:\&quot;required\&quot;}]&#x60;. | |
| **note_request** | [**\Dona\Api\Model\NoteRequest**](../Model/NoteRequest.md)|  | |
| **dona_dry_run** | **string**| &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. Only the literal &#x60;true&#x60; / &#x60;false&#x60;; any other value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Dry-Run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). | [optional] |
| **dry_run** | **string**| Alias of the &#x60;Dona-Dry-Run&#x60; header. Only the literal strings &#x60;true&#x60; / &#x60;false&#x60; — &#x60;1&#x60;, &#x60;0&#x60;, &#x60;TRUE&#x60;, &#x60;yes&#x60;, an empty value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;dry_run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). A string enum, not a boolean, so no SDK generator serialises it as &#x60;1&#x60;/&#x60;0&#x60;. | [optional] |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **dona_seller** | **string**| Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

[**\Dona\Api\Model\NoteCreated**](../Model/NoteCreated.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `batchOrderLabels()`

```php
batchOrderLabels($labels_request, $accept_language, $dona_seller, $x_dona_integration): string
```

Labels for ≤ 100 orders (one PDF)

A read with a body — no `Idempotency-Key`. Any foreign/missing id ⇒ `404 not_found` for the whole call. Doors and 409s as `label.pdf` (C53); `no_tracking_number` names every offending order. Cost 10 on the key-rate bucket (C54), charged only once the batch holds a drawing slot (`429 api_busy` as `label.pdf`).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\OrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$labels_request = new \Dona\Api\Model\LabelsRequest(); // \Dona\Api\Model\LabelsRequest
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$dona_seller = 'dona_seller_example'; // string | Vendor-app install keys only (`dona_it_live_…`, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"required\"}]`; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no `urn:uuid:`, no padding) ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"invalid\"}]`; naming any other shop — even one that installed the same app ⇒ `404 not_found` (never 403; nothing is read). Ignored on a seller key (`dona_sk_`).
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->batchOrderLabels($labels_request, $accept_language, $dona_seller, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrdersApi->batchOrderLabels: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **labels_request** | [**\Dona\Api\Model\LabelsRequest**](../Model/LabelsRequest.md)|  | |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **dona_seller** | **string**| Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

**string**

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/pdf`, `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `cancelOrder()`

```php
cancelOrder($id, $idempotency_key, $decline_request, $dona_dry_run, $dry_run, $accept_language, $dona_seller, $x_dona_integration): \Dona\Api\Model\OrderTransition
```

Cancel (after acceptance) — money-reversing

An ACCEPTED order: the portal seller-cancel's own statements (`order.SellerCancelOrderTx`) — same reasons (C15) and money effects as `decline`. The reason is stored in the order's `cancel_reason` (with the comment), NOT in `decline_reason_code`, which stays `null` (C52); the `cancelled`/`seller` timeline row, the card refund and the buyer notice run after the commit. 409 `order_not_cancellable` — a delivered or cancelled order, or one NOT YET ACCEPTED (`details[{field:\"status\", code:\"not_accepted\"}]`: decline it) — and `order_has_active_return`. Kill switch: `writes_enabled`. `503 role_unavailable` from a SERVER_ROLE=seller-api server, as `decline`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\OrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Resource id (UUIDv7). A foreign or missing id is always `404 not_found`.
$idempotency_key = sync-2026-09-24T09:05; // string | 1–255 chars. Scope = this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ `400 invalid_body` with `details[{field:\"Idempotency-Key\",code:\"required\"}]`.
$decline_request = new \Dona\Api\Model\DeclineRequest(); // \Dona\Api\Model\DeclineRequest
$dona_dry_run = 'dona_dry_run_example'; // string | `true` ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as `?dry_run=true`. Only the literal `true` / `false`; any other value ⇒ `400 invalid_body` + `details[{field:\"Dona-Dry-Run\", code:\"invalid\"}]` (C51).
$dry_run = 'dry_run_example'; // string | Alias of the `Dona-Dry-Run` header. Only the literal strings `true` / `false` — `1`, `0`, `TRUE`, `yes`, an empty value ⇒ `400 invalid_body` + `details[{field:\"dry_run\", code:\"invalid\"}]` (C51). A string enum, not a boolean, so no SDK generator serialises it as `1`/`0`.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$dona_seller = 'dona_seller_example'; // string | Vendor-app install keys only (`dona_it_live_…`, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"required\"}]`; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no `urn:uuid:`, no padding) ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"invalid\"}]`; naming any other shop — even one that installed the same app ⇒ `404 not_found` (never 403; nothing is read). Ignored on a seller key (`dona_sk_`).
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->cancelOrder($id, $idempotency_key, $decline_request, $dona_dry_run, $dry_run, $accept_language, $dona_seller, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrdersApi->cancelOrder: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. | |
| **idempotency_key** | **string**| 1–255 chars. Scope &#x3D; this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ &#x60;400 invalid_body&#x60; with &#x60;details[{field:\&quot;Idempotency-Key\&quot;,code:\&quot;required\&quot;}]&#x60;. | |
| **decline_request** | [**\Dona\Api\Model\DeclineRequest**](../Model/DeclineRequest.md)|  | |
| **dona_dry_run** | **string**| &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. Only the literal &#x60;true&#x60; / &#x60;false&#x60;; any other value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Dry-Run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). | [optional] |
| **dry_run** | **string**| Alias of the &#x60;Dona-Dry-Run&#x60; header. Only the literal strings &#x60;true&#x60; / &#x60;false&#x60; — &#x60;1&#x60;, &#x60;0&#x60;, &#x60;TRUE&#x60;, &#x60;yes&#x60;, an empty value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;dry_run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). A string enum, not a boolean, so no SDK generator serialises it as &#x60;1&#x60;/&#x60;0&#x60;. | [optional] |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **dona_seller** | **string**| Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

[**\Dona\Api\Model\OrderTransition**](../Model/OrderTransition.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `declineOrder()`

```php
declineOrder($id, $idempotency_key, $decline_request, $dona_dry_run, $dry_run, $accept_language, $dona_seller, $x_dona_integration): \Dona\Api\Model\OrderTransition
```

Decline (before acceptance) — money-reversing

An order NOT YET ACCEPTED. The portal decline's own body (`order.DeclineOrderInTx`) on the marketplace pool, in the write pipeline (stamped transaction, wallet-cutover fence): restock, the buyer's kiwi/vouchers/delivery money back, the `declined`/`seller` timeline row; the card refund at the provider and the buyer notice run after the commit (never on a dry run). The reason is stored in `decline_reason_code`. ADVANCED, derived on THIS request (a documents-waived or downgraded shop is `403 tier_required`). 400 `invalid_decline_reason` (`details[comment: required]` for `other` without words); 409 `order_not_acceptable` (an accepted or closed order — the portal names it `order_not_decidable`; cancel an accepted one), `order_has_active_return`. Another shop's order ⇒ `404`. Kill switch: `writes_enabled`. Served by the marketplace process only: a SERVER_ROLE=seller-api server answers `503 role_unavailable` (after the key, scope and tier; before the dry-run flag, the switch, the body and the idempotency claim — nothing changes; D3).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\OrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Resource id (UUIDv7). A foreign or missing id is always `404 not_found`.
$idempotency_key = sync-2026-09-24T09:05; // string | 1–255 chars. Scope = this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ `400 invalid_body` with `details[{field:\"Idempotency-Key\",code:\"required\"}]`.
$decline_request = new \Dona\Api\Model\DeclineRequest(); // \Dona\Api\Model\DeclineRequest
$dona_dry_run = 'dona_dry_run_example'; // string | `true` ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as `?dry_run=true`. Only the literal `true` / `false`; any other value ⇒ `400 invalid_body` + `details[{field:\"Dona-Dry-Run\", code:\"invalid\"}]` (C51).
$dry_run = 'dry_run_example'; // string | Alias of the `Dona-Dry-Run` header. Only the literal strings `true` / `false` — `1`, `0`, `TRUE`, `yes`, an empty value ⇒ `400 invalid_body` + `details[{field:\"dry_run\", code:\"invalid\"}]` (C51). A string enum, not a boolean, so no SDK generator serialises it as `1`/`0`.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$dona_seller = 'dona_seller_example'; // string | Vendor-app install keys only (`dona_it_live_…`, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"required\"}]`; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no `urn:uuid:`, no padding) ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"invalid\"}]`; naming any other shop — even one that installed the same app ⇒ `404 not_found` (never 403; nothing is read). Ignored on a seller key (`dona_sk_`).
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->declineOrder($id, $idempotency_key, $decline_request, $dona_dry_run, $dry_run, $accept_language, $dona_seller, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrdersApi->declineOrder: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. | |
| **idempotency_key** | **string**| 1–255 chars. Scope &#x3D; this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ &#x60;400 invalid_body&#x60; with &#x60;details[{field:\&quot;Idempotency-Key\&quot;,code:\&quot;required\&quot;}]&#x60;. | |
| **decline_request** | [**\Dona\Api\Model\DeclineRequest**](../Model/DeclineRequest.md)|  | |
| **dona_dry_run** | **string**| &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. Only the literal &#x60;true&#x60; / &#x60;false&#x60;; any other value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Dry-Run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). | [optional] |
| **dry_run** | **string**| Alias of the &#x60;Dona-Dry-Run&#x60; header. Only the literal strings &#x60;true&#x60; / &#x60;false&#x60; — &#x60;1&#x60;, &#x60;0&#x60;, &#x60;TRUE&#x60;, &#x60;yes&#x60;, an empty value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;dry_run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). A string enum, not a boolean, so no SDK generator serialises it as &#x60;1&#x60;/&#x60;0&#x60;. | [optional] |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **dona_seller** | **string**| Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

[**\Dona\Api\Model\OrderTransition**](../Model/OrderTransition.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getOrder()`

```php
getOrder($id, $accept_language, $dona_seller, $x_dona_integration): \Dona\Api\Model\GetOrder200Response
```

Get an order (PII only with orders:pii)

`orders:read` ⇒ `Order`. A key that ALSO holds `orders:pii` (ADVANCED, `sk` only, S4) gets `OrderWithPii` (adds `recipient`) and the call is logged `pii=true`. When the `orders:pii` door would refuse this request (the shop is not ADVANCED now, or the key's recipient is third-party — D7) the ORDER is still answered, without `recipient`, and `Dona-API-Warn: recipient withheld: <tier_required|pii_third_party_pending_counsel|…>` says why (C59).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\OrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Resource id (UUIDv7). A foreign or missing id is always `404 not_found`.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$dona_seller = 'dona_seller_example'; // string | Vendor-app install keys only (`dona_it_live_…`, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"required\"}]`; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no `urn:uuid:`, no padding) ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"invalid\"}]`; naming any other shop — even one that installed the same app ⇒ `404 not_found` (never 403; nothing is read). Ignored on a seller key (`dona_sk_`).
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->getOrder($id, $accept_language, $dona_seller, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrdersApi->getOrder: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. | |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **dona_seller** | **string**| Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

[**\Dona\Api\Model\GetOrder200Response**](../Model/GetOrder200Response.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getOrderInvoice()`

```php
getOrderInvoice($id, $accept_language, $dona_seller, $x_dona_integration): string
```

Invoice (PDF, contains PII)

The invoice for one order, drawn as a PDF from the SAME figures as the portal's invoice page (one loader). Doors, 409s and the `429 api_busy` bound as `label.pdf` (C53, C54). ⚠ PII set WIDER than the label's: like the portal's invoice it prints the PURCHASER's account name and phone (the buyer who is invoiced) — on a gift order that is not the recipient the label and the `recipient` block name (Form A Q12 states both).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\OrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Resource id (UUIDv7). A foreign or missing id is always `404 not_found`.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$dona_seller = 'dona_seller_example'; // string | Vendor-app install keys only (`dona_it_live_…`, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"required\"}]`; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no `urn:uuid:`, no padding) ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"invalid\"}]`; naming any other shop — even one that installed the same app ⇒ `404 not_found` (never 403; nothing is read). Ignored on a seller key (`dona_sk_`).
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->getOrderInvoice($id, $accept_language, $dona_seller, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrdersApi->getOrderInvoice: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. | |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **dona_seller** | **string**| Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

**string**

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/pdf`, `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getOrderLabel()`

```php
getOrderLabel($id, $accept_language, $dona_seller, $x_dona_integration): string
```

Shipping label (PDF, contains PII)

The portal's sticker for one order: prints the buyer's name, phone and address. `sk` keys only (`orders:pii` on any other kind ⇒ `403 insufficient_scope` + `details[scope_not_allowed_for_kind]`); ADVANCED now (`403 tier_required`); a key minted for a THIRD-PARTY recipient ⇒ `403 tier_required` + `details[pii_recipient: pii_third_party_pending_counsel]` (D7). Logged `pii=true` (always journaled, never sampled); never stored by the API. Normal key-rate bucket (C54). 409 `no_tracking_number` (+ `orders`: the order codes without a carrier number yet — print later), `no_items_selected`, `all_items_delayed` (nothing left to put in the parcel) (C53). A server draws at most 2 documents at once: past that `429 api_busy` (`Dona-Rate-Limited-Reason: global`, `Retry-After: 2`) before any read, and a batch is not charged.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\OrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Resource id (UUIDv7). A foreign or missing id is always `404 not_found`.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$dona_seller = 'dona_seller_example'; // string | Vendor-app install keys only (`dona_it_live_…`, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"required\"}]`; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no `urn:uuid:`, no padding) ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"invalid\"}]`; naming any other shop — even one that installed the same app ⇒ `404 not_found` (never 403; nothing is read). Ignored on a seller key (`dona_sk_`).
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->getOrderLabel($id, $accept_language, $dona_seller, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrdersApi->getOrderLabel: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. | |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **dona_seller** | **string**| Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

**string**

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/pdf`, `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getOrderTimeline()`

```php
getOrderTimeline($id, $accept_language, $dona_seller, $x_dona_integration): \Dona\Api\Model\OrderTimeline
```

Order timeline

`order_events` in order.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\OrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Resource id (UUIDv7). A foreign or missing id is always `404 not_found`.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$dona_seller = 'dona_seller_example'; // string | Vendor-app install keys only (`dona_it_live_…`, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"required\"}]`; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no `urn:uuid:`, no padding) ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"invalid\"}]`; naming any other shop — even one that installed the same app ⇒ `404 not_found` (never 403; nothing is read). Ignored on a seller key (`dona_sk_`).
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->getOrderTimeline($id, $accept_language, $dona_seller, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrdersApi->getOrderTimeline: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. | |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **dona_seller** | **string**| Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

[**\Dona\Api\Model\OrderTimeline**](../Model/OrderTimeline.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `handoverOrder()`

```php
handoverOrder($id, $idempotency_key, $dona_dry_run, $dry_run, $accept_language, $dona_seller, $x_dona_integration): \Dona\Api\Model\OrderTransition
```

Hand over to the courier

`sellerMayTransitionSQL` rules. 409: `order_not_shippable`. Kill switch: `writes_enabled`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\OrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Resource id (UUIDv7). A foreign or missing id is always `404 not_found`.
$idempotency_key = sync-2026-09-24T09:05; // string | 1–255 chars. Scope = this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ `400 invalid_body` with `details[{field:\"Idempotency-Key\",code:\"required\"}]`.
$dona_dry_run = 'dona_dry_run_example'; // string | `true` ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as `?dry_run=true`. Only the literal `true` / `false`; any other value ⇒ `400 invalid_body` + `details[{field:\"Dona-Dry-Run\", code:\"invalid\"}]` (C51).
$dry_run = 'dry_run_example'; // string | Alias of the `Dona-Dry-Run` header. Only the literal strings `true` / `false` — `1`, `0`, `TRUE`, `yes`, an empty value ⇒ `400 invalid_body` + `details[{field:\"dry_run\", code:\"invalid\"}]` (C51). A string enum, not a boolean, so no SDK generator serialises it as `1`/`0`.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$dona_seller = 'dona_seller_example'; // string | Vendor-app install keys only (`dona_it_live_…`, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"required\"}]`; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no `urn:uuid:`, no padding) ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"invalid\"}]`; naming any other shop — even one that installed the same app ⇒ `404 not_found` (never 403; nothing is read). Ignored on a seller key (`dona_sk_`).
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->handoverOrder($id, $idempotency_key, $dona_dry_run, $dry_run, $accept_language, $dona_seller, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrdersApi->handoverOrder: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. | |
| **idempotency_key** | **string**| 1–255 chars. Scope &#x3D; this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ &#x60;400 invalid_body&#x60; with &#x60;details[{field:\&quot;Idempotency-Key\&quot;,code:\&quot;required\&quot;}]&#x60;. | |
| **dona_dry_run** | **string**| &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. Only the literal &#x60;true&#x60; / &#x60;false&#x60;; any other value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Dry-Run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). | [optional] |
| **dry_run** | **string**| Alias of the &#x60;Dona-Dry-Run&#x60; header. Only the literal strings &#x60;true&#x60; / &#x60;false&#x60; — &#x60;1&#x60;, &#x60;0&#x60;, &#x60;TRUE&#x60;, &#x60;yes&#x60;, an empty value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;dry_run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). A string enum, not a boolean, so no SDK generator serialises it as &#x60;1&#x60;/&#x60;0&#x60;. | [optional] |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **dona_seller** | **string**| Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

[**\Dona\Api\Model\OrderTransition**](../Model/OrderTransition.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listOrders()`

```php
listOrders($cursor, $page, $limit, $updated_since, $status, $scheme, $from, $to, $accept_language, $dona_seller, $x_dona_integration): \Dona\Api\Model\OrderPage
```

List orders (no buyer PII)

The `orders:read` projection. `status` takes the portal buckets (`all`, `pending`, `paid`, `ready_to_ship`, `to_ship`, `shipped`, `delivered`, `cancelled`, `return_refund`). `from`/`to` span ≤ 90 d, `to` exclusive.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\OrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$cursor = 'cursor_example'; // string | Opaque keyset cursor from `next_cursor`.
$page = 56; // int | 0-based page alias (Uzum parity) — slower than `cursor`, ≤ 1 000 pages; mutually exclusive with `cursor`.
$limit = 50; // int | Page size, default 50, max 100 (clamped, with `Dona-API-Warn`). `limit > 50` costs `1 + ceil(limit/50)`.
$updated_since = 2026-09-24T09:00:00+05:00; // string | ISO 8601 with offset, or epoch milliseconds. The visible high-water mark is capped at `now() − 10 s` so a slow transaction is never skipped.
$status = 'status_example'; // string | Portal bucket.
$scheme = 'scheme_example'; // string | Derived fulfilment scheme.
$from = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | created_at ≥ from.
$to = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | created_at < to.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$dona_seller = 'dona_seller_example'; // string | Vendor-app install keys only (`dona_it_live_…`, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"required\"}]`; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no `urn:uuid:`, no padding) ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"invalid\"}]`; naming any other shop — even one that installed the same app ⇒ `404 not_found` (never 403; nothing is read). Ignored on a seller key (`dona_sk_`).
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->listOrders($cursor, $page, $limit, $updated_since, $status, $scheme, $from, $to, $accept_language, $dona_seller, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrdersApi->listOrders: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cursor** | **string**| Opaque keyset cursor from &#x60;next_cursor&#x60;. | [optional] |
| **page** | **int**| 0-based page alias (Uzum parity) — slower than &#x60;cursor&#x60;, ≤ 1 000 pages; mutually exclusive with &#x60;cursor&#x60;. | [optional] |
| **limit** | **int**| Page size, default 50, max 100 (clamped, with &#x60;Dona-API-Warn&#x60;). &#x60;limit &gt; 50&#x60; costs &#x60;1 + ceil(limit/50)&#x60;. | [optional] [default to 50] |
| **updated_since** | **string**| ISO 8601 with offset, or epoch milliseconds. The visible high-water mark is capped at &#x60;now() − 10 s&#x60; so a slow transaction is never skipped. | [optional] |
| **status** | **string**| Portal bucket. | [optional] |
| **scheme** | **string**| Derived fulfilment scheme. | [optional] |
| **from** | **\DateTime**| created_at ≥ from. | [optional] |
| **to** | **\DateTime**| created_at &lt; to. | [optional] |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **dona_seller** | **string**| Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

[**\Dona\Api\Model\OrderPage**](../Model/OrderPage.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `markOrderReady()`

```php
markOrderReady($id, $idempotency_key, $dona_dry_run, $dry_run, $accept_language, $dona_seller, $x_dona_integration): \Dona\Api\Model\OrderTransition
```

Mark ready to ship

Sets `ready_to_ship`. 409: `order_not_shippable`. Kill switch: `writes_enabled`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\OrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Resource id (UUIDv7). A foreign or missing id is always `404 not_found`.
$idempotency_key = sync-2026-09-24T09:05; // string | 1–255 chars. Scope = this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ `400 invalid_body` with `details[{field:\"Idempotency-Key\",code:\"required\"}]`.
$dona_dry_run = 'dona_dry_run_example'; // string | `true` ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as `?dry_run=true`. Only the literal `true` / `false`; any other value ⇒ `400 invalid_body` + `details[{field:\"Dona-Dry-Run\", code:\"invalid\"}]` (C51).
$dry_run = 'dry_run_example'; // string | Alias of the `Dona-Dry-Run` header. Only the literal strings `true` / `false` — `1`, `0`, `TRUE`, `yes`, an empty value ⇒ `400 invalid_body` + `details[{field:\"dry_run\", code:\"invalid\"}]` (C51). A string enum, not a boolean, so no SDK generator serialises it as `1`/`0`.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$dona_seller = 'dona_seller_example'; // string | Vendor-app install keys only (`dona_it_live_…`, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"required\"}]`; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no `urn:uuid:`, no padding) ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"invalid\"}]`; naming any other shop — even one that installed the same app ⇒ `404 not_found` (never 403; nothing is read). Ignored on a seller key (`dona_sk_`).
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->markOrderReady($id, $idempotency_key, $dona_dry_run, $dry_run, $accept_language, $dona_seller, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrdersApi->markOrderReady: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. | |
| **idempotency_key** | **string**| 1–255 chars. Scope &#x3D; this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ &#x60;400 invalid_body&#x60; with &#x60;details[{field:\&quot;Idempotency-Key\&quot;,code:\&quot;required\&quot;}]&#x60;. | |
| **dona_dry_run** | **string**| &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. Only the literal &#x60;true&#x60; / &#x60;false&#x60;; any other value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Dry-Run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). | [optional] |
| **dry_run** | **string**| Alias of the &#x60;Dona-Dry-Run&#x60; header. Only the literal strings &#x60;true&#x60; / &#x60;false&#x60; — &#x60;1&#x60;, &#x60;0&#x60;, &#x60;TRUE&#x60;, &#x60;yes&#x60;, an empty value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;dry_run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). A string enum, not a boolean, so no SDK generator serialises it as &#x60;1&#x60;/&#x60;0&#x60;. | [optional] |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **dona_seller** | **string**| Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

[**\Dona\Api\Model\OrderTransition**](../Model/OrderTransition.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `shipOrder()`

```php
shipOrder($id, $idempotency_key, $dona_dry_run, $dry_run, $accept_language, $dona_seller, $x_dona_integration): \Dona\Api\Model\OrderTransition
```

Ship

409: `order_not_shippable`, `order_awaiting_courier`. Kill switch: `writes_enabled`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\OrdersApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Resource id (UUIDv7). A foreign or missing id is always `404 not_found`.
$idempotency_key = sync-2026-09-24T09:05; // string | 1–255 chars. Scope = this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ `400 invalid_body` with `details[{field:\"Idempotency-Key\",code:\"required\"}]`.
$dona_dry_run = 'dona_dry_run_example'; // string | `true` ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as `?dry_run=true`. Only the literal `true` / `false`; any other value ⇒ `400 invalid_body` + `details[{field:\"Dona-Dry-Run\", code:\"invalid\"}]` (C51).
$dry_run = 'dry_run_example'; // string | Alias of the `Dona-Dry-Run` header. Only the literal strings `true` / `false` — `1`, `0`, `TRUE`, `yes`, an empty value ⇒ `400 invalid_body` + `details[{field:\"dry_run\", code:\"invalid\"}]` (C51). A string enum, not a boolean, so no SDK generator serialises it as `1`/`0`.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$dona_seller = 'dona_seller_example'; // string | Vendor-app install keys only (`dona_it_live_…`, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"required\"}]`; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no `urn:uuid:`, no padding) ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"invalid\"}]`; naming any other shop — even one that installed the same app ⇒ `404 not_found` (never 403; nothing is read). Ignored on a seller key (`dona_sk_`).
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->shipOrder($id, $idempotency_key, $dona_dry_run, $dry_run, $accept_language, $dona_seller, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OrdersApi->shipOrder: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. | |
| **idempotency_key** | **string**| 1–255 chars. Scope &#x3D; this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ &#x60;400 invalid_body&#x60; with &#x60;details[{field:\&quot;Idempotency-Key\&quot;,code:\&quot;required\&quot;}]&#x60;. | |
| **dona_dry_run** | **string**| &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. Only the literal &#x60;true&#x60; / &#x60;false&#x60;; any other value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Dry-Run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). | [optional] |
| **dry_run** | **string**| Alias of the &#x60;Dona-Dry-Run&#x60; header. Only the literal strings &#x60;true&#x60; / &#x60;false&#x60; — &#x60;1&#x60;, &#x60;0&#x60;, &#x60;TRUE&#x60;, &#x60;yes&#x60;, an empty value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;dry_run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). A string enum, not a boolean, so no SDK generator serialises it as &#x60;1&#x60;/&#x60;0&#x60;. | [optional] |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **dona_seller** | **string**| Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

[**\Dona\Api\Model\OrderTransition**](../Model/OrderTransition.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

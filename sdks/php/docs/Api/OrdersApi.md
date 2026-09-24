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
acceptOrder($id, $idempotency_key, $dona_dry_run, $dry_run, $accept_language, $x_dona_integration): \Dona\Api\Model\OrderTransition
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
$dona_dry_run = 'dona_dry_run_example'; // string | `true` ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as `?dry_run=true`.
$dry_run = True; // bool | Alias of the `Dona-Dry-Run` header.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->acceptOrder($id, $idempotency_key, $dona_dry_run, $dry_run, $accept_language, $x_dona_integration);
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
| **dona_dry_run** | **string**| &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. | [optional] |
| **dry_run** | **bool**| Alias of the &#x60;Dona-Dry-Run&#x60; header. | [optional] |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
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
addOrderNote($id, $idempotency_key, $note_request, $dona_dry_run, $dry_run, $accept_language, $x_dona_integration): \Dona\Api\Model\NoteCreated
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
$dona_dry_run = 'dona_dry_run_example'; // string | `true` ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as `?dry_run=true`.
$dry_run = True; // bool | Alias of the `Dona-Dry-Run` header.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->addOrderNote($id, $idempotency_key, $note_request, $dona_dry_run, $dry_run, $accept_language, $x_dona_integration);
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
| **dona_dry_run** | **string**| &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. | [optional] |
| **dry_run** | **bool**| Alias of the &#x60;Dona-Dry-Run&#x60; header. | [optional] |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
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
batchOrderLabels($labels_request, $accept_language, $x_dona_integration): string
```

Labels for ≤ 100 orders (one PDF)

A read with a body — no `Idempotency-Key`. Any foreign/missing id ⇒ `404 not_found` for the whole call. ≤ 30/min.

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
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->batchOrderLabels($labels_request, $accept_language, $x_dona_integration);
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
cancelOrder($id, $idempotency_key, $decline_request, $dona_dry_run, $dry_run, $accept_language, $x_dona_integration): \Dona\Api\Model\OrderTransition
```

Cancel (after acceptance) — money-reversing

Same reasons and effects as `decline`, for an accepted order. 409 `order_not_cancellable` (existing estate code). Kill switch: `writes_enabled`.

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
$dona_dry_run = 'dona_dry_run_example'; // string | `true` ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as `?dry_run=true`.
$dry_run = True; // bool | Alias of the `Dona-Dry-Run` header.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->cancelOrder($id, $idempotency_key, $decline_request, $dona_dry_run, $dry_run, $accept_language, $x_dona_integration);
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
| **dona_dry_run** | **string**| &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. | [optional] |
| **dry_run** | **bool**| Alias of the &#x60;Dona-Dry-Run&#x60; header. | [optional] |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
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
declineOrder($id, $idempotency_key, $decline_request, $dona_dry_run, $dry_run, $accept_language, $x_dona_integration): \Dona\Api\Model\OrderTransition
```

Decline (before acceptance) — money-reversing

`declineOrderTx` on the marketplace pool. ADVANCED: a documents-waived shop is `403 tier_required`. 400 `invalid_decline_reason`; 409 `order_not_acceptable`. Kill switch: `writes_enabled`.

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
$dona_dry_run = 'dona_dry_run_example'; // string | `true` ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as `?dry_run=true`.
$dry_run = True; // bool | Alias of the `Dona-Dry-Run` header.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->declineOrder($id, $idempotency_key, $decline_request, $dona_dry_run, $dry_run, $accept_language, $x_dona_integration);
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
| **dona_dry_run** | **string**| &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. | [optional] |
| **dry_run** | **bool**| Alias of the &#x60;Dona-Dry-Run&#x60; header. | [optional] |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
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
getOrder($id, $accept_language, $x_dona_integration): \Dona\Api\Model\GetOrder200Response
```

Get an order (PII only with orders:pii)

`orders:read` ⇒ `Order`. A key that ALSO holds `orders:pii` (ADVANCED, `sk` only, S4) gets `OrderWithPii` (adds `recipient`) and the call is logged `pii=true`.

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
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->getOrder($id, $accept_language, $x_dona_integration);
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
getOrderInvoice($id, $accept_language, $x_dona_integration): string
```

Invoice (PDF, contains PII)

As the label. ≤ 30/min.

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
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->getOrderInvoice($id, $accept_language, $x_dona_integration);
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
getOrderLabel($id, $accept_language, $x_dona_integration): string
```

Shipping label (PDF, contains PII)

Prints buyer name/phone/address. `sk` keys only; logged `pii=true`; never stored by the API. ≤ 30/min.

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
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->getOrderLabel($id, $accept_language, $x_dona_integration);
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
getOrderTimeline($id, $accept_language, $x_dona_integration): \Dona\Api\Model\OrderTimeline
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
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->getOrderTimeline($id, $accept_language, $x_dona_integration);
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
handoverOrder($id, $idempotency_key, $dona_dry_run, $dry_run, $accept_language, $x_dona_integration): \Dona\Api\Model\OrderTransition
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
$dona_dry_run = 'dona_dry_run_example'; // string | `true` ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as `?dry_run=true`.
$dry_run = True; // bool | Alias of the `Dona-Dry-Run` header.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->handoverOrder($id, $idempotency_key, $dona_dry_run, $dry_run, $accept_language, $x_dona_integration);
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
| **dona_dry_run** | **string**| &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. | [optional] |
| **dry_run** | **bool**| Alias of the &#x60;Dona-Dry-Run&#x60; header. | [optional] |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
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
listOrders($cursor, $page, $limit, $updated_since, $status, $scheme, $from, $to, $accept_language, $x_dona_integration): \Dona\Api\Model\OrderPage
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
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->listOrders($cursor, $page, $limit, $updated_since, $status, $scheme, $from, $to, $accept_language, $x_dona_integration);
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
markOrderReady($id, $idempotency_key, $dona_dry_run, $dry_run, $accept_language, $x_dona_integration): \Dona\Api\Model\OrderTransition
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
$dona_dry_run = 'dona_dry_run_example'; // string | `true` ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as `?dry_run=true`.
$dry_run = True; // bool | Alias of the `Dona-Dry-Run` header.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->markOrderReady($id, $idempotency_key, $dona_dry_run, $dry_run, $accept_language, $x_dona_integration);
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
| **dona_dry_run** | **string**| &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. | [optional] |
| **dry_run** | **bool**| Alias of the &#x60;Dona-Dry-Run&#x60; header. | [optional] |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
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
shipOrder($id, $idempotency_key, $dona_dry_run, $dry_run, $accept_language, $x_dona_integration): \Dona\Api\Model\OrderTransition
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
$dona_dry_run = 'dona_dry_run_example'; // string | `true` ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as `?dry_run=true`.
$dry_run = True; // bool | Alias of the `Dona-Dry-Run` header.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->shipOrder($id, $idempotency_key, $dona_dry_run, $dry_run, $accept_language, $x_dona_integration);
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
| **dona_dry_run** | **string**| &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. | [optional] |
| **dry_run** | **bool**| Alias of the &#x60;Dona-Dry-Run&#x60; header. | [optional] |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
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

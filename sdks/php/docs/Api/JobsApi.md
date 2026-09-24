# Dona\Api\JobsApi

Async exports and product batches.

All URIs are relative to https://api.dona.im/seller-api/v1, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**exportOrders()**](JobsApi.md#exportOrders) | **POST** /exports/orders | Export orders (async, no PII) |
| [**exportProducts()**](JobsApi.md#exportProducts) | **POST** /exports/products | Export products (async) |
| [**getJob()**](JobsApi.md#getJob) | **GET** /jobs/{id} | Poll a job |


## `exportOrders()`

```php
exportOrders($idempotency_key, $export_request, $accept_language, $x_dona_integration): \Dona\Api\Model\JobAccepted
```

Export orders (async, no PII)

The `orders:read` projection only — an export never carries `recipient`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\JobsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$idempotency_key = sync-2026-09-24T09:05; // string | 1–255 chars. Scope = this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ `400 invalid_body` with `details[{field:\"Idempotency-Key\",code:\"required\"}]`.
$export_request = new \Dona\Api\Model\ExportRequest(); // \Dona\Api\Model\ExportRequest
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->exportOrders($idempotency_key, $export_request, $accept_language, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling JobsApi->exportOrders: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **idempotency_key** | **string**| 1–255 chars. Scope &#x3D; this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ &#x60;400 invalid_body&#x60; with &#x60;details[{field:\&quot;Idempotency-Key\&quot;,code:\&quot;required\&quot;}]&#x60;. | |
| **export_request** | [**\Dona\Api\Model\ExportRequest**](../Model/ExportRequest.md)|  | |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

[**\Dona\Api\Model\JobAccepted**](../Model/JobAccepted.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `exportProducts()`

```php
exportProducts($idempotency_key, $export_request, $accept_language, $x_dona_integration): \Dona\Api\Model\JobAccepted
```

Export products (async)

CSV or JSONL. ≤ 2 running jobs per key, ≤ 20/day per shop. Not gated by `writes_enabled`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\JobsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$idempotency_key = sync-2026-09-24T09:05; // string | 1–255 chars. Scope = this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ `400 invalid_body` with `details[{field:\"Idempotency-Key\",code:\"required\"}]`.
$export_request = new \Dona\Api\Model\ExportRequest(); // \Dona\Api\Model\ExportRequest
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->exportProducts($idempotency_key, $export_request, $accept_language, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling JobsApi->exportProducts: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **idempotency_key** | **string**| 1–255 chars. Scope &#x3D; this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ &#x60;400 invalid_body&#x60; with &#x60;details[{field:\&quot;Idempotency-Key\&quot;,code:\&quot;required\&quot;}]&#x60;. | |
| **export_request** | [**\Dona\Api\Model\ExportRequest**](../Model/ExportRequest.md)|  | |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

[**\Dona\Api\Model\JobAccepted**](../Model/JobAccepted.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getJob()`

```php
getJob($id, $accept_language, $x_dona_integration): \Dona\Api\Model\Job
```

Poll a job

Readable by any key of the shop that holds the scope the job's kind needs (`catalog:read` for `export_products`, `orders:read` for `export_orders`, `catalog:write` for `products_batch`); otherwise `404 not_found`. Poll ≥ 5 s (`Retry-After` is set while pending/running). After `expires_at` (7 d) ⇒ `404 not_found`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\JobsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Resource id (UUIDv7). A foreign or missing id is always `404 not_found`.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->getJob($id, $accept_language, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling JobsApi->getJob: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. | |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

[**\Dona\Api\Model\Job**](../Model/Job.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

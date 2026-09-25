# Dona\Api\ReturnsApi

Read-only in v1.

All URIs are relative to https://api.dona.im/seller-api/v1, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getReturn()**](ReturnsApi.md#getReturn) | **GET** /returns/{id} | Get a return |
| [**listReturns()**](ReturnsApi.md#listReturns) | **GET** /returns | List returns |


## `getReturn()`

```php
getReturn($id, $accept_language, $dona_seller, $x_dona_integration): \Dona\Api\Model\ModelReturn
```

Get a return

Includes the buyer's `reason_text` (detail only).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\ReturnsApi(
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
    $result = $apiInstance->getReturn($id, $accept_language, $dona_seller, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ReturnsApi->getReturn: ', $e->getMessage(), PHP_EOL;
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

[**\Dona\Api\Model\ModelReturn**](../Model/ModelReturn.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listReturns()`

```php
listReturns($cursor, $limit, $updated_since, $status, $accept_language, $dona_seller, $x_dona_integration): \Dona\Api\Model\ReturnPage
```

List returns

Read-only in v1 — approving a return is `orders.refund`, never issuable.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\ReturnsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$cursor = 'cursor_example'; // string | Opaque keyset cursor from `next_cursor`.
$limit = 50; // int | Page size, default 50, max 100 (clamped, with `Dona-API-Warn`). `limit > 50` costs `1 + ceil(limit/50)`.
$updated_since = 2026-09-24T09:00:00+05:00; // string | ISO 8601 with offset, or epoch milliseconds. The visible high-water mark is capped at `now() − 10 s` so a slow transaction is never skipped.
$status = 'status_example'; // string | Exact.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$dona_seller = 'dona_seller_example'; // string | Vendor-app install keys only (`dona_it_live_…`, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"required\"}]`; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no `urn:uuid:`, no padding) ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"invalid\"}]`; naming any other shop — even one that installed the same app ⇒ `404 not_found` (never 403; nothing is read). Ignored on a seller key (`dona_sk_`).
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->listReturns($cursor, $limit, $updated_since, $status, $accept_language, $dona_seller, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ReturnsApi->listReturns: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cursor** | **string**| Opaque keyset cursor from &#x60;next_cursor&#x60;. | [optional] |
| **limit** | **int**| Page size, default 50, max 100 (clamped, with &#x60;Dona-API-Warn&#x60;). &#x60;limit &gt; 50&#x60; costs &#x60;1 + ceil(limit/50)&#x60;. | [optional] [default to 50] |
| **updated_since** | **string**| ISO 8601 with offset, or epoch milliseconds. The visible high-water mark is capped at &#x60;now() − 10 s&#x60; so a slow transaction is never skipped. | [optional] |
| **status** | **string**| Exact. | [optional] |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **dona_seller** | **string**| Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

[**\Dona\Api\Model\ReturnPage**](../Model/ReturnPage.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

# Dona\Api\AttentionApi

The seller-keyed \&quot;errors, warnings, attention required\&quot; channel (&#x60;seller_attention_items&#x60;).

All URIs are relative to https://api.dona.im/seller-api/v1, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**ackAttention()**](AttentionApi.md#ackAttention) | **POST** /attention/{id}/ack | Acknowledge |
| [**getAttention()**](AttentionApi.md#getAttention) | **GET** /attention/{id} | One attention item |
| [**listAttention()**](AttentionApi.md#listAttention) | **GET** /attention | Errors, warnings, attention required |


## `ackAttention()`

```php
ackAttention($id, $accept_language, $x_dona_integration): \Dona\Api\Model\AttentionItem
```

Acknowledge

Idempotent by nature (no `Idempotency-Key`). Ack never clears a condition; only `ip_blocked` and `api_anomaly` resolve on ack (`resolved_reason=acked`). Counts against the writes/min bucket; not gated by `writes_enabled`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\AttentionApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Resource id (UUIDv7). A foreign or missing id is always `404 not_found`.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->ackAttention($id, $accept_language, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AttentionApi->ackAttention: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. | |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

[**\Dona\Api\Model\AttentionItem**](../Model/AttentionItem.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAttention()`

```php
getAttention($id, $accept_language, $x_dona_integration): \Dona\Api\Model\AttentionItem
```

One attention item

—

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\AttentionApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Resource id (UUIDv7). A foreign or missing id is always `404 not_found`.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->getAttention($id, $accept_language, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AttentionApi->getAttention: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. | |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

[**\Dona\Api\Model\AttentionItem**](../Model/AttentionItem.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listAttention()`

```php
listAttention($status, $kind, $severity, $action_required, $subject_type, $updated_since, $cursor, $limit, $if_none_match, $accept_language, $x_dona_integration): \Dona\Api\Model\AttentionPage
```

Errors, warnings, attention required

Sorted `action_required desc, severity desc, deadline_at nulls last, opened_at desc`. Array filters repeat the key (`kind=stock_out&kind=stock_low`).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\AttentionApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$status = 'open'; // string | Default `open`.
$kind = array('kind_example'); // string[] | Repeatable.
$severity = array('severity_example'); // string[] | Repeatable.
$action_required = True; // bool | Only items the seller can clear.
$subject_type = 'subject_type_example'; // string | e.g. `order`.
$updated_since = 2026-09-24T09:00:00+05:00; // string | ISO 8601 with offset, or epoch milliseconds. The visible high-water mark is capped at `now() − 10 s` so a slow transaction is never skipped.
$cursor = 'cursor_example'; // string | Opaque keyset cursor from `next_cursor`.
$limit = 50; // int | Page size, default 50, max 100 (clamped, with `Dona-API-Warn`). `limit > 50` costs `1 + ceil(limit/50)`.
$if_none_match = 'if_none_match_example'; // string | An `ETag` from a previous identical request ⇒ `304` with rate headers (cost 0.5).
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->listAttention($status, $kind, $severity, $action_required, $subject_type, $updated_since, $cursor, $limit, $if_none_match, $accept_language, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AttentionApi->listAttention: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **status** | **string**| Default &#x60;open&#x60;. | [optional] [default to &#39;open&#39;] |
| **kind** | [**string[]**](../Model/string.md)| Repeatable. | [optional] |
| **severity** | [**string[]**](../Model/string.md)| Repeatable. | [optional] |
| **action_required** | **bool**| Only items the seller can clear. | [optional] |
| **subject_type** | **string**| e.g. &#x60;order&#x60;. | [optional] |
| **updated_since** | **string**| ISO 8601 with offset, or epoch milliseconds. The visible high-water mark is capped at &#x60;now() − 10 s&#x60; so a slow transaction is never skipped. | [optional] |
| **cursor** | **string**| Opaque keyset cursor from &#x60;next_cursor&#x60;. | [optional] |
| **limit** | **int**| Page size, default 50, max 100 (clamped, with &#x60;Dona-API-Warn&#x60;). &#x60;limit &gt; 50&#x60; costs &#x60;1 + ceil(limit/50)&#x60;. | [optional] [default to 50] |
| **if_none_match** | **string**| An &#x60;ETag&#x60; from a previous identical request ⇒ &#x60;304&#x60; with rate headers (cost 0.5). | [optional] |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

[**\Dona\Api\Model\AttentionPage**](../Model/AttentionPage.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

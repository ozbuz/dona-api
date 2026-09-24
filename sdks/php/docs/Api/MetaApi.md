# Dona\Api\MetaApi

Public: ping, status, changelog, this spec, llms.txt.

All URIs are relative to https://api.dona.im/seller-api/v1, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getChangelog()**](MetaApi.md#getChangelog) | **GET** /changelog | Changelog (JSON, or RSS with Accept) |
| [**getLlmsTxt()**](MetaApi.md#getLlmsTxt) | **GET** /llms.txt | llms.txt index for AI agents |
| [**getOpenApi()**](MetaApi.md#getOpenApi) | **GET** /openapi.json | This document |
| [**getStatus()**](MetaApi.md#getStatus) | **GET** /status | Service status |
| [**ping()**](MetaApi.md#ping) | **GET** /ping | Liveness (key optional) |


## `getChangelog()`

```php
getChangelog($cursor, $limit, $accept_language): \Dona\Api\Model\ChangelogEntryPage
```

Changelog (JSON, or RSS with Accept)

Public. `Accept: application/rss+xml` returns RSS. Backed by `seller_api_changelog` (0465, S4) — an empty list until then.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\MetaApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$cursor = 'cursor_example'; // string | Opaque keyset cursor from `next_cursor`.
$limit = 50; // int | Page size, default 50, max 100 (clamped, with `Dona-API-Warn`). `limit > 50` costs `1 + ceil(limit/50)`.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.

try {
    $result = $apiInstance->getChangelog($cursor, $limit, $accept_language);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MetaApi->getChangelog: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cursor** | **string**| Opaque keyset cursor from &#x60;next_cursor&#x60;. | [optional] |
| **limit** | **int**| Page size, default 50, max 100 (clamped, with &#x60;Dona-API-Warn&#x60;). &#x60;limit &gt; 50&#x60; costs &#x60;1 + ceil(limit/50)&#x60;. | [optional] [default to 50] |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |

### Return type

[**\Dona\Api\Model\ChangelogEntryPage**](../Model/ChangelogEntryPage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/rss+xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getLlmsTxt()`

```php
getLlmsTxt($accept_language): string
```

llms.txt index for AI agents

Plain-text index of the docs + spec links (`llms-full.txt` beside it).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\MetaApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.

try {
    $result = $apiInstance->getLlmsTxt($accept_language);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MetaApi->getLlmsTxt: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |

### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/plain`, `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getOpenApi()`

```php
getOpenApi($accept_language): object
```

This document

OpenAPI 3.1, public, `Cache-Control: public, max-age=300`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\MetaApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.

try {
    $result = $apiInstance->getOpenApi($accept_language);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MetaApi->getOpenApi: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getStatus()`

```php
getStatus($accept_language): \Dona\Api\Model\Status
```

Service status

Public; edge-cacheable 60 s; linked from every 503's `doc_url`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\MetaApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.

try {
    $result = $apiInstance->getStatus($accept_language);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MetaApi->getStatus: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |

### Return type

[**\Dona\Api\Model\Status**](../Model/Status.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `ping()`

```php
ping($accept_language): \Dona\Api\Model\Ping
```

Liveness (key optional)

Public. Without `Authorization` it answers `authenticated:false`. With a key the key is fully verified — a bad key is `401`, never a silent `false`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\MetaApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.

try {
    $result = $apiInstance->ping($accept_language);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling MetaApi->ping: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |

### Return type

[**\Dona\Api\Model\Ping**](../Model/Ping.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

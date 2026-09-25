# Dona\Api\EventsApi

&#x60;/events&#x60; — the primary, pollable change feed.

All URIs are relative to https://api.dona.im/seller-api/v1, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**listEvents()**](EventsApi.md#listEvents) | **GET** /events | The change feed (primary channel) |


## `listEvents()`

```php
listEvents($cursor, $since, $types, $limit, $if_none_match, $accept_language, $dona_seller, $x_dona_integration): \Dona\Api\Model\EventPage
```

The change feed (primary channel)

Poll `?cursor=<last event id>`; omit it for the oldest retained event or pass `since`. Events are readable **30 days** from `occurred_at`. A cursor older than the window ⇒ `400 invalid_body` with `details[{field:\"cursor\",code:\"cursor_expired\"}]` and `meta.oldest_event_id`: full-reconcile via `updated_since`, then restart there. Ordered by `id` (near, not exact, `occurred_at` order). `limit` ≤ 200.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\EventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$cursor = 'cursor_example'; // string | Last event id seen.
$since = 'since_example'; // string | ISO 8601 or epoch-ms; ignored when `cursor` is set.
$types = array('types_example'); // string[] | Repeatable; exact names or prefixes (`order.*`).
$limit = 100; // int | Default 100, max 200.
$if_none_match = 'if_none_match_example'; // string | An `ETag` from a previous identical request ⇒ `304` with rate headers (cost 0.5).
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$dona_seller = 'dona_seller_example'; // string | Vendor-app install keys only (`dona_it_live_…`, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"required\"}]`; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no `urn:uuid:`, no padding) ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"invalid\"}]`; naming any other shop — even one that installed the same app ⇒ `404 not_found` (never 403; nothing is read). Ignored on a seller key (`dona_sk_`).
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->listEvents($cursor, $since, $types, $limit, $if_none_match, $accept_language, $dona_seller, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling EventsApi->listEvents: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cursor** | **string**| Last event id seen. | [optional] |
| **since** | **string**| ISO 8601 or epoch-ms; ignored when &#x60;cursor&#x60; is set. | [optional] |
| **types** | [**string[]**](../Model/string.md)| Repeatable; exact names or prefixes (&#x60;order.*&#x60;). | [optional] |
| **limit** | **int**| Default 100, max 200. | [optional] [default to 100] |
| **if_none_match** | **string**| An &#x60;ETag&#x60; from a previous identical request ⇒ &#x60;304&#x60; with rate headers (cost 0.5). | [optional] |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **dona_seller** | **string**| Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

[**\Dona\Api\Model\EventPage**](../Model/EventPage.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

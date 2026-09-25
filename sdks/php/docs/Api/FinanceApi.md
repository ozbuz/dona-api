# Dona\Api\FinanceApi

Balance and settlement lines (ADVANCED).

All URIs are relative to https://api.dona.im/seller-api/v1, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getBalance()**](FinanceApi.md#getBalance) | **GET** /finance/balance | Balance |
| [**listSettlements()**](FinanceApi.md#listSettlements) | **GET** /finance/settlements | Settlement lines |


## `getBalance()`

```php
getBalance($accept_language, $dona_seller, $x_dona_integration): \Dona\Api\Model\Balance
```

Balance

The wallet's answer for the key's shop, asked as the shop's CURRENT owner (the portal's own finance bridge), projected field by field. Never error-copied. No requisites, PAN or statement URLs. The wallet unreachable, erroring or not knowing the shop ⇒ `503 wallet_unavailable` (`Retry-After: 30`), never its body (C57). Served by the marketplace process only: a SERVER_ROLE=seller-api server answers `503 role_unavailable` before any read (D3).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\FinanceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$dona_seller = 'dona_seller_example'; // string | Vendor-app install keys only (`dona_it_live_…`, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"required\"}]`; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no `urn:uuid:`, no padding) ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"invalid\"}]`; naming any other shop — even one that installed the same app ⇒ `404 not_found` (never 403; nothing is read). Ignored on a seller key (`dona_sk_`).
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->getBalance($accept_language, $dona_seller, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FinanceApi->getBalance: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **dona_seller** | **string**| Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

[**\Dona\Api\Model\Balance**](../Model/Balance.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listSettlements()`

```php
listSettlements($cursor, $limit, $order_id, $from, $to, $accept_language, $dona_seller, $x_dona_integration): \Dona\Api\Model\SettlementPage
```

Settlement lines

The wallet statement's lines for the shop, newest first (asked as the shop's current owner). `memo` is the line's machine `kind` from the wallet's CLOSED vocabulary (`sale_income`, `escrow_hold`, `escrow_release`, `refund`, `return`, `adjustment`, `withdrawal`, `withdrawal_failed`, `fee`, `commission`, `hold_placed`, `hold_captured`, `hold_released`, `cod_collected`, `cod_remitted`, `transfer`) or `other` — never the wallet's free-text title (C57). A line whose `id` or `txn_id` is not a UUID, or a `next_cursor` that is not an opaque ≤ 512-character URL-safe token, refuses the whole page. `503 wallet_unavailable` / `role_unavailable` as `/finance/balance`.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\FinanceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$cursor = 'cursor_example'; // string | Opaque keyset cursor from `next_cursor`.
$limit = 50; // int | Page size, default 50, max 100 (clamped, with `Dona-API-Warn`). `limit > 50` costs `1 + ceil(limit/50)`.
$order_id = 'order_id_example'; // string | Exact.
$from = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Inclusive.
$to = new \DateTime('2013-10-20T19:20:30+01:00'); // \DateTime | Exclusive.
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$dona_seller = 'dona_seller_example'; // string | Vendor-app install keys only (`dona_it_live_…`, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"required\"}]`; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no `urn:uuid:`, no padding) ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"invalid\"}]`; naming any other shop — even one that installed the same app ⇒ `404 not_found` (never 403; nothing is read). Ignored on a seller key (`dona_sk_`).
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->listSettlements($cursor, $limit, $order_id, $from, $to, $accept_language, $dona_seller, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling FinanceApi->listSettlements: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cursor** | **string**| Opaque keyset cursor from &#x60;next_cursor&#x60;. | [optional] |
| **limit** | **int**| Page size, default 50, max 100 (clamped, with &#x60;Dona-API-Warn&#x60;). &#x60;limit &gt; 50&#x60; costs &#x60;1 + ceil(limit/50)&#x60;. | [optional] [default to 50] |
| **order_id** | **string**| Exact. | [optional] |
| **from** | **\DateTime**| Inclusive. | [optional] |
| **to** | **\DateTime**| Exclusive. | [optional] |
| **accept_language** | **string**| Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &#39;uz&#39;] |
| **dona_seller** | **string**| Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional] |
| **x_dona_integration** | **string**| &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional] |

### Return type

[**\Dona\Api\Model\SettlementPage**](../Model/SettlementPage.md)

### Authorization

[bearerKey](../../README.md#bearerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

# Dona\Api\WebhookEventsApi



All URIs are relative to https://api.dona.im/seller-api/v1, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**onAccountAgreementOwed()**](WebhookEventsApi.md#onAccountAgreementOwed) | **POST** /account.agreement_owed | &#x60;account.agreement_owed&#x60; |
| [**onAccountDocumentsDecided()**](WebhookEventsApi.md#onAccountDocumentsDecided) | **POST** /account.documents_decided | &#x60;account.documents_decided&#x60; |
| [**onAccountHealthChanged()**](WebhookEventsApi.md#onAccountHealthChanged) | **POST** /account.health_changed | &#x60;account.health_changed&#x60; |
| [**onAccountKycReopened()**](WebhookEventsApi.md#onAccountKycReopened) | **POST** /account.kyc_reopened | &#x60;account.kyc_reopened&#x60; |
| [**onAccountStatusChanged()**](WebhookEventsApi.md#onAccountStatusChanged) | **POST** /account.status_changed | &#x60;account.status_changed&#x60; |
| [**onAccountSuppressed()**](WebhookEventsApi.md#onAccountSuppressed) | **POST** /account.suppressed | &#x60;account.suppressed&#x60; |
| [**onAttentionOpened()**](WebhookEventsApi.md#onAttentionOpened) | **POST** /attention.opened | &#x60;attention.opened&#x60; |
| [**onAttentionResolved()**](WebhookEventsApi.md#onAttentionResolved) | **POST** /attention.resolved | &#x60;attention.resolved&#x60; |
| [**onKeyExpiring()**](WebhookEventsApi.md#onKeyExpiring) | **POST** /key.expiring | &#x60;key.expiring&#x60; |
| [**onKeySuspended()**](WebhookEventsApi.md#onKeySuspended) | **POST** /key.suspended | &#x60;key.suspended&#x60; |
| [**onKeyUnsuspended()**](WebhookEventsApi.md#onKeyUnsuspended) | **POST** /key.unsuspended | &#x60;key.unsuspended&#x60; |
| [**onLiveAccessChanged()**](WebhookEventsApi.md#onLiveAccessChanged) | **POST** /live.access_changed | &#x60;live.access_changed&#x60; |
| [**onLiveStrike()**](WebhookEventsApi.md#onLiveStrike) | **POST** /live.strike | &#x60;live.strike&#x60; |
| [**onOrderAcceptDueSoon()**](WebhookEventsApi.md#onOrderAcceptDueSoon) | **POST** /order.accept_due_soon | &#x60;order.accept_due_soon&#x60; |
| [**onOrderAccepted()**](WebhookEventsApi.md#onOrderAccepted) | **POST** /order.accepted | &#x60;order.accepted&#x60; |
| [**onOrderCancelled()**](WebhookEventsApi.md#onOrderCancelled) | **POST** /order.cancelled | &#x60;order.cancelled&#x60; |
| [**onOrderCreated()**](WebhookEventsApi.md#onOrderCreated) | **POST** /order.created | &#x60;order.created&#x60; |
| [**onOrderDeclined()**](WebhookEventsApi.md#onOrderDeclined) | **POST** /order.declined | &#x60;order.declined&#x60; |
| [**onOrderDelivered()**](WebhookEventsApi.md#onOrderDelivered) | **POST** /order.delivered | &#x60;order.delivered&#x60; |
| [**onOrderLineCancelled()**](WebhookEventsApi.md#onOrderLineCancelled) | **POST** /order.line_cancelled | &#x60;order.line_cancelled&#x60; |
| [**onOrderPaid()**](WebhookEventsApi.md#onOrderPaid) | **POST** /order.paid | &#x60;order.paid&#x60; |
| [**onOrderReady()**](WebhookEventsApi.md#onOrderReady) | **POST** /order.ready | &#x60;order.ready&#x60; |
| [**onOrderShipOverdue()**](WebhookEventsApi.md#onOrderShipOverdue) | **POST** /order.ship_overdue | &#x60;order.ship_overdue&#x60; |
| [**onOrderShipped()**](WebhookEventsApi.md#onOrderShipped) | **POST** /order.shipped | &#x60;order.shipped&#x60; |
| [**onPing()**](WebhookEventsApi.md#onPing) | **POST** /ping | &#x60;ping&#x60; |
| [**onProductDeleted()**](WebhookEventsApi.md#onProductDeleted) | **POST** /product.deleted | &#x60;product.deleted&#x60; |
| [**onProductDemoted()**](WebhookEventsApi.md#onProductDemoted) | **POST** /product.demoted | &#x60;product.demoted&#x60; |
| [**onProductHeld()**](WebhookEventsApi.md#onProductHeld) | **POST** /product.held | &#x60;product.held&#x60; |
| [**onProductPublished()**](WebhookEventsApi.md#onProductPublished) | **POST** /product.published | &#x60;product.published&#x60; |
| [**onProductRejected()**](WebhookEventsApi.md#onProductRejected) | **POST** /product.rejected | &#x60;product.rejected&#x60; |
| [**onProductViolation()**](WebhookEventsApi.md#onProductViolation) | **POST** /product.violation | &#x60;product.violation&#x60; |
| [**onReturnRequested()**](WebhookEventsApi.md#onReturnRequested) | **POST** /return.requested | &#x60;return.requested&#x60; |
| [**onReturnStatusChanged()**](WebhookEventsApi.md#onReturnStatusChanged) | **POST** /return.status_changed | &#x60;return.status_changed&#x60; |
| [**onStockLow()**](WebhookEventsApi.md#onStockLow) | **POST** /stock.low | &#x60;stock.low&#x60; |
| [**onStockOut()**](WebhookEventsApi.md#onStockOut) | **POST** /stock.out | &#x60;stock.out&#x60; |
| [**onWebhookDisabled()**](WebhookEventsApi.md#onWebhookDisabled) | **POST** /webhook.disabled | &#x60;webhook.disabled&#x60; |
| [**onWebhookFailing()**](WebhookEventsApi.md#onWebhookFailing) | **POST** /webhook.failing | &#x60;webhook.failing&#x60; |
| [**onWriteApproved()**](WebhookEventsApi.md#onWriteApproved) | **POST** /write.approved | &#x60;write.approved&#x60; |
| [**onWriteExpired()**](WebhookEventsApi.md#onWriteExpired) | **POST** /write.expired | &#x60;write.expired&#x60; |
| [**onWriteHeld()**](WebhookEventsApi.md#onWriteHeld) | **POST** /write.held | &#x60;write.held&#x60; |
| [**onWriteRejected()**](WebhookEventsApi.md#onWriteRejected) | **POST** /write.rejected | &#x60;write.rejected&#x60; |


## `onAccountAgreementOwed()`

```php
onAccountAgreementOwed($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_account_agreement_owed_request)
```

`account.agreement_owed`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_account_agreement_owed_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"account.agreement_owed","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"annex_version":"api-annex-2026-10","binds_at":"2026-10-24T00:00:00+05:00"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnAccountAgreementOwedRequest

try {
    $apiInstance->onAccountAgreementOwed($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_account_agreement_owed_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onAccountAgreementOwed: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_account_agreement_owed_request** | [**\Dona\Api\Model\OnAccountAgreementOwedRequest**](../Model/OnAccountAgreementOwedRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onAccountDocumentsDecided()`

```php
onAccountDocumentsDecided($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_account_documents_decided_request)
```

`account.documents_decided`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_account_documents_decided_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"account.documents_decided","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"documents_status":"approved","reason_code":null,"can_sell":true,"action_url":"/verification"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnAccountDocumentsDecidedRequest

try {
    $apiInstance->onAccountDocumentsDecided($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_account_documents_decided_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onAccountDocumentsDecided: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_account_documents_decided_request** | [**\Dona\Api\Model\OnAccountDocumentsDecidedRequest**](../Model/OnAccountDocumentsDecidedRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onAccountHealthChanged()`

```php
onAccountHealthChanged($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_account_health_changed_request)
```

`account.health_changed`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_account_health_changed_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"account.health_changed","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"health_label":"fair","reputation_score":71.2,"suppressed":false},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnAccountHealthChangedRequest

try {
    $apiInstance->onAccountHealthChanged($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_account_health_changed_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onAccountHealthChanged: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_account_health_changed_request** | [**\Dona\Api\Model\OnAccountHealthChangedRequest**](../Model/OnAccountHealthChangedRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onAccountKycReopened()`

```php
onAccountKycReopened($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_account_kyc_reopened_request)
```

`account.kyc_reopened`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_account_kyc_reopened_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"account.kyc_reopened","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"kyc_status":"reopened","reason_code":"passport_expired","can_sell":true,"action_url":"/verification"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnAccountKycReopenedRequest

try {
    $apiInstance->onAccountKycReopened($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_account_kyc_reopened_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onAccountKycReopened: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_account_kyc_reopened_request** | [**\Dona\Api\Model\OnAccountKycReopenedRequest**](../Model/OnAccountKycReopenedRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onAccountStatusChanged()`

```php
onAccountStatusChanged($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_account_status_changed_request)
```

`account.status_changed`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_account_status_changed_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"account.status_changed","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"status":"approved","reason_code":null,"can_sell":true,"action_url":"/account-health"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnAccountStatusChangedRequest

try {
    $apiInstance->onAccountStatusChanged($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_account_status_changed_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onAccountStatusChanged: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_account_status_changed_request** | [**\Dona\Api\Model\OnAccountStatusChangedRequest**](../Model/OnAccountStatusChangedRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onAccountSuppressed()`

```php
onAccountSuppressed($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_account_suppressed_request)
```

`account.suppressed`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_account_suppressed_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"account.suppressed","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"suppressed":true,"reason_code":"late_shipment_rate","can_sell":true,"action_url":"/account-health"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnAccountSuppressedRequest

try {
    $apiInstance->onAccountSuppressed($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_account_suppressed_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onAccountSuppressed: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_account_suppressed_request** | [**\Dona\Api\Model\OnAccountSuppressedRequest**](../Model/OnAccountSuppressedRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onAttentionOpened()`

```php
onAttentionOpened($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_attention_opened_request)
```

`attention.opened`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_attention_opened_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"attention.opened","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"attention_id":"01997b30-0a1b-7c2d-9e3f-4a5b6c7d8e9f","kind":"order_accept_due","severity":"high","action_required":true,"subject":{"type":"order","id":"01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"},"deadline_at":"2026-09-25T09:12:00+05:00"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnAttentionOpenedRequest

try {
    $apiInstance->onAttentionOpened($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_attention_opened_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onAttentionOpened: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_attention_opened_request** | [**\Dona\Api\Model\OnAttentionOpenedRequest**](../Model/OnAttentionOpenedRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onAttentionResolved()`

```php
onAttentionResolved($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_attention_opened_request)
```

`attention.resolved`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_attention_opened_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"attention.resolved","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"attention_id":"01997b30-0a1b-7c2d-9e3f-4a5b6c7d8e9f","kind":"order_accept_due","severity":"high","action_required":true,"subject":{"type":"order","id":"01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"},"deadline_at":"2026-09-25T09:12:00+05:00"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnAttentionOpenedRequest

try {
    $apiInstance->onAttentionResolved($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_attention_opened_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onAttentionResolved: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_attention_opened_request** | [**\Dona\Api\Model\OnAttentionOpenedRequest**](../Model/OnAttentionOpenedRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onKeyExpiring()`

```php
onKeyExpiring($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_key_expiring_request)
```

`key.expiring`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_key_expiring_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"key.expiring","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"key_id":"0199760c-2f4b-7a3e-9d21-5c8e4b1f0a37","prefix":"dona_sk_live_3fK","expires_at":"2026-10-24T00:00:00+05:00","suspended_until":null,"reason_code":null},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnKeyExpiringRequest

try {
    $apiInstance->onKeyExpiring($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_key_expiring_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onKeyExpiring: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_key_expiring_request** | [**\Dona\Api\Model\OnKeyExpiringRequest**](../Model/OnKeyExpiringRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onKeySuspended()`

```php
onKeySuspended($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_key_expiring_request)
```

`key.suspended`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_key_expiring_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"key.suspended","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"key_id":"0199760c-2f4b-7a3e-9d21-5c8e4b1f0a37","prefix":"dona_sk_live_3fK","expires_at":"2026-10-24T00:00:00+05:00","suspended_until":null,"reason_code":null},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnKeyExpiringRequest

try {
    $apiInstance->onKeySuspended($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_key_expiring_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onKeySuspended: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_key_expiring_request** | [**\Dona\Api\Model\OnKeyExpiringRequest**](../Model/OnKeyExpiringRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onKeyUnsuspended()`

```php
onKeyUnsuspended($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_key_expiring_request)
```

`key.unsuspended`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_key_expiring_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"key.unsuspended","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"key_id":"0199760c-2f4b-7a3e-9d21-5c8e4b1f0a37","prefix":"dona_sk_live_3fK","expires_at":"2026-10-24T00:00:00+05:00","suspended_until":null,"reason_code":null},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnKeyExpiringRequest

try {
    $apiInstance->onKeyUnsuspended($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_key_expiring_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onKeyUnsuspended: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_key_expiring_request** | [**\Dona\Api\Model\OnKeyExpiringRequest**](../Model/OnKeyExpiringRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onLiveAccessChanged()`

```php
onLiveAccessChanged($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_live_access_changed_request)
```

`live.access_changed`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_live_access_changed_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"live.access_changed","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"state":"banned","until":"2026-10-01T00:00:00+05:00"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnLiveAccessChangedRequest

try {
    $apiInstance->onLiveAccessChanged($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_live_access_changed_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onLiveAccessChanged: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_live_access_changed_request** | [**\Dona\Api\Model\OnLiveAccessChangedRequest**](../Model/OnLiveAccessChangedRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onLiveStrike()`

```php
onLiveStrike($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_live_strike_request)
```

`live.strike`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_live_strike_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"live.strike","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"strike_count":1,"expires_at":"2027-03-24T14:05:12+05:00"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnLiveStrikeRequest

try {
    $apiInstance->onLiveStrike($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_live_strike_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onLiveStrike: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_live_strike_request** | [**\Dona\Api\Model\OnLiveStrikeRequest**](../Model/OnLiveStrikeRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onOrderAcceptDueSoon()`

```php
onOrderAcceptDueSoon($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_order_accept_due_soon_request)
```

`order.accept_due_soon`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_order_accept_due_soon_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"order.accept_due_soon","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"order_id":"01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b","deadline_at":"2026-09-25T09:12:00+05:00","overdue_by_seconds":null},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnOrderAcceptDueSoonRequest

try {
    $apiInstance->onOrderAcceptDueSoon($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_order_accept_due_soon_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onOrderAcceptDueSoon: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_order_accept_due_soon_request** | [**\Dona\Api\Model\OnOrderAcceptDueSoonRequest**](../Model/OnOrderAcceptDueSoonRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onOrderAccepted()`

```php
onOrderAccepted($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_order_created_request)
```

`order.accepted`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_order_created_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"order.accepted","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"order_id":"01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b","status":"paid","payment_status":"paid","payment_method":"card","scheme":"own_fleet","total_uzs":259000,"accept_deadline":"2026-09-25T09:12:00+05:00","ship_by_deadline":null,"updated_at":"2026-09-24T09:12:31+05:00"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnOrderCreatedRequest

try {
    $apiInstance->onOrderAccepted($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_order_created_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onOrderAccepted: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_order_created_request** | [**\Dona\Api\Model\OnOrderCreatedRequest**](../Model/OnOrderCreatedRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onOrderCancelled()`

```php
onOrderCancelled($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_order_declined_request)
```

`order.cancelled`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_order_declined_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"order.cancelled","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"order_id":"01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b","status":"cancelled","payment_status":"paid","payment_method":"card","scheme":"own_fleet","total_uzs":259000,"accept_deadline":"2026-09-25T09:12:00+05:00","ship_by_deadline":null,"updated_at":"2026-09-24T09:12:31+05:00","cancelled_by":"seller","reason_code":"out_of_stock","comment_present":false},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnOrderDeclinedRequest

try {
    $apiInstance->onOrderCancelled($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_order_declined_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onOrderCancelled: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_order_declined_request** | [**\Dona\Api\Model\OnOrderDeclinedRequest**](../Model/OnOrderDeclinedRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onOrderCreated()`

```php
onOrderCreated($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_order_created_request)
```

`order.created`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_order_created_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"order.created","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"order_id":"01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b","status":"paid","payment_status":"paid","payment_method":"card","scheme":"own_fleet","total_uzs":259000,"accept_deadline":"2026-09-25T09:12:00+05:00","ship_by_deadline":null,"updated_at":"2026-09-24T09:12:31+05:00"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnOrderCreatedRequest

try {
    $apiInstance->onOrderCreated($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_order_created_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onOrderCreated: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_order_created_request** | [**\Dona\Api\Model\OnOrderCreatedRequest**](../Model/OnOrderCreatedRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onOrderDeclined()`

```php
onOrderDeclined($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_order_declined_request)
```

`order.declined`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_order_declined_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"order.declined","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"order_id":"01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b","status":"cancelled","payment_status":"paid","payment_method":"card","scheme":"own_fleet","total_uzs":259000,"accept_deadline":"2026-09-25T09:12:00+05:00","ship_by_deadline":null,"updated_at":"2026-09-24T09:12:31+05:00","cancelled_by":"seller","reason_code":"out_of_stock","comment_present":false},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnOrderDeclinedRequest

try {
    $apiInstance->onOrderDeclined($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_order_declined_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onOrderDeclined: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_order_declined_request** | [**\Dona\Api\Model\OnOrderDeclinedRequest**](../Model/OnOrderDeclinedRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onOrderDelivered()`

```php
onOrderDelivered($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_order_created_request)
```

`order.delivered`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_order_created_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"order.delivered","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"order_id":"01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b","status":"paid","payment_status":"paid","payment_method":"card","scheme":"own_fleet","total_uzs":259000,"accept_deadline":"2026-09-25T09:12:00+05:00","ship_by_deadline":null,"updated_at":"2026-09-24T09:12:31+05:00"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnOrderCreatedRequest

try {
    $apiInstance->onOrderDelivered($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_order_created_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onOrderDelivered: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_order_created_request** | [**\Dona\Api\Model\OnOrderCreatedRequest**](../Model/OnOrderCreatedRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onOrderLineCancelled()`

```php
onOrderLineCancelled($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_order_line_cancelled_request)
```

`order.line_cancelled`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_order_line_cancelled_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"order.line_cancelled","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"order_id":"01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b","order_item_id":"01997b2e-41c1-7a22-9b3c-4d5e6f7a8b9c","quantity":1,"reason_code":"out_of_stock"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnOrderLineCancelledRequest

try {
    $apiInstance->onOrderLineCancelled($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_order_line_cancelled_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onOrderLineCancelled: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_order_line_cancelled_request** | [**\Dona\Api\Model\OnOrderLineCancelledRequest**](../Model/OnOrderLineCancelledRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onOrderPaid()`

```php
onOrderPaid($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_order_created_request)
```

`order.paid`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_order_created_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"order.paid","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"order_id":"01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b","status":"paid","payment_status":"paid","payment_method":"card","scheme":"own_fleet","total_uzs":259000,"accept_deadline":"2026-09-25T09:12:00+05:00","ship_by_deadline":null,"updated_at":"2026-09-24T09:12:31+05:00"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnOrderCreatedRequest

try {
    $apiInstance->onOrderPaid($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_order_created_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onOrderPaid: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_order_created_request** | [**\Dona\Api\Model\OnOrderCreatedRequest**](../Model/OnOrderCreatedRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onOrderReady()`

```php
onOrderReady($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_order_created_request)
```

`order.ready`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_order_created_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"order.ready","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"order_id":"01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b","status":"paid","payment_status":"paid","payment_method":"card","scheme":"own_fleet","total_uzs":259000,"accept_deadline":"2026-09-25T09:12:00+05:00","ship_by_deadline":null,"updated_at":"2026-09-24T09:12:31+05:00"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnOrderCreatedRequest

try {
    $apiInstance->onOrderReady($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_order_created_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onOrderReady: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_order_created_request** | [**\Dona\Api\Model\OnOrderCreatedRequest**](../Model/OnOrderCreatedRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onOrderShipOverdue()`

```php
onOrderShipOverdue($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_order_accept_due_soon_request)
```

`order.ship_overdue`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_order_accept_due_soon_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"order.ship_overdue","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"order_id":"01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b","deadline_at":"2026-09-25T09:12:00+05:00","overdue_by_seconds":null},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnOrderAcceptDueSoonRequest

try {
    $apiInstance->onOrderShipOverdue($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_order_accept_due_soon_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onOrderShipOverdue: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_order_accept_due_soon_request** | [**\Dona\Api\Model\OnOrderAcceptDueSoonRequest**](../Model/OnOrderAcceptDueSoonRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onOrderShipped()`

```php
onOrderShipped($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_order_created_request)
```

`order.shipped`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_order_created_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"order.shipped","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"order_id":"01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b","status":"paid","payment_status":"paid","payment_method":"card","scheme":"own_fleet","total_uzs":259000,"accept_deadline":"2026-09-25T09:12:00+05:00","ship_by_deadline":null,"updated_at":"2026-09-24T09:12:31+05:00"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnOrderCreatedRequest

try {
    $apiInstance->onOrderShipped($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_order_created_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onOrderShipped: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_order_created_request** | [**\Dona\Api\Model\OnOrderCreatedRequest**](../Model/OnOrderCreatedRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onPing()`

```php
onPing($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_ping_request)
```

`ping`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_ping_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"ping","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"webhook_id":"01997b32-2c3d-7e4f-9a5b-6c7d8e9f0a1b"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnPingRequest

try {
    $apiInstance->onPing($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_ping_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onPing: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_ping_request** | [**\Dona\Api\Model\OnPingRequest**](../Model/OnPingRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onProductDeleted()`

```php
onProductDeleted($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_product_published_request)
```

`product.deleted`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_product_published_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"product.deleted","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"product_id":"0199612e-8a0b-7c4d-b1e2-3f4a5b6c7d8e","seller_sku":"A-200","status":"active","prev_status":"draft"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnProductPublishedRequest

try {
    $apiInstance->onProductDeleted($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_product_published_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onProductDeleted: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_product_published_request** | [**\Dona\Api\Model\OnProductPublishedRequest**](../Model/OnProductPublishedRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onProductDemoted()`

```php
onProductDemoted($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_product_published_request)
```

`product.demoted`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_product_published_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"product.demoted","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"product_id":"0199612e-8a0b-7c4d-b1e2-3f4a5b6c7d8e","seller_sku":"A-200","status":"active","prev_status":"draft"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnProductPublishedRequest

try {
    $apiInstance->onProductDemoted($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_product_published_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onProductDemoted: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_product_published_request** | [**\Dona\Api\Model\OnProductPublishedRequest**](../Model/OnProductPublishedRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onProductHeld()`

```php
onProductHeld($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_product_held_request)
```

`product.held`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_product_held_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"product.held","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"product_id":"0199612e-8a0b-7c4d-b1e2-3f4a5b6c7d8e","reason_code":"shop_not_activated","issue_id":null,"action_url":"/products/0199612e-8a0b-7c4d-b1e2-3f4a5b6c7d8e"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnProductHeldRequest

try {
    $apiInstance->onProductHeld($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_product_held_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onProductHeld: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_product_held_request** | [**\Dona\Api\Model\OnProductHeldRequest**](../Model/OnProductHeldRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onProductPublished()`

```php
onProductPublished($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_product_published_request)
```

`product.published`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_product_published_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"product.published","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"product_id":"0199612e-8a0b-7c4d-b1e2-3f4a5b6c7d8e","seller_sku":"A-200","status":"active","prev_status":"draft"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnProductPublishedRequest

try {
    $apiInstance->onProductPublished($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_product_published_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onProductPublished: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_product_published_request** | [**\Dona\Api\Model\OnProductPublishedRequest**](../Model/OnProductPublishedRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onProductRejected()`

```php
onProductRejected($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_product_held_request)
```

`product.rejected`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_product_held_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"product.rejected","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"product_id":"0199612e-8a0b-7c4d-b1e2-3f4a5b6c7d8e","reason_code":"shop_not_activated","issue_id":null,"action_url":"/products/0199612e-8a0b-7c4d-b1e2-3f4a5b6c7d8e"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnProductHeldRequest

try {
    $apiInstance->onProductRejected($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_product_held_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onProductRejected: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_product_held_request** | [**\Dona\Api\Model\OnProductHeldRequest**](../Model/OnProductHeldRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onProductViolation()`

```php
onProductViolation($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_product_held_request)
```

`product.violation`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_product_held_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"product.violation","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"product_id":"0199612e-8a0b-7c4d-b1e2-3f4a5b6c7d8e","reason_code":"shop_not_activated","issue_id":null,"action_url":"/products/0199612e-8a0b-7c4d-b1e2-3f4a5b6c7d8e"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnProductHeldRequest

try {
    $apiInstance->onProductViolation($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_product_held_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onProductViolation: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_product_held_request** | [**\Dona\Api\Model\OnProductHeldRequest**](../Model/OnProductHeldRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onReturnRequested()`

```php
onReturnRequested($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_return_requested_request)
```

`return.requested`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_return_requested_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"return.requested","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"return_id":"01997c10-5d2e-7f30-8c41-5a6b7c8d9e0f","order_id":"01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b","status":"requested","due_at":"2026-09-27T12:00:00+05:00"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnReturnRequestedRequest

try {
    $apiInstance->onReturnRequested($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_return_requested_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onReturnRequested: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_return_requested_request** | [**\Dona\Api\Model\OnReturnRequestedRequest**](../Model/OnReturnRequestedRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onReturnStatusChanged()`

```php
onReturnStatusChanged($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_return_requested_request)
```

`return.status_changed`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_return_requested_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"return.status_changed","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"return_id":"01997c10-5d2e-7f30-8c41-5a6b7c8d9e0f","order_id":"01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b","status":"requested","due_at":"2026-09-27T12:00:00+05:00"},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnReturnRequestedRequest

try {
    $apiInstance->onReturnStatusChanged($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_return_requested_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onReturnStatusChanged: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_return_requested_request** | [**\Dona\Api\Model\OnReturnRequestedRequest**](../Model/OnReturnRequestedRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onStockLow()`

```php
onStockLow($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_stock_low_request)
```

`stock.low`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_stock_low_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"stock.low","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"product_id":"0199612e-8a0b-7c4d-b1e2-3f4a5b6c7d8e","variant_id":"0199612e-8a0c-7d11-a0b2-9e8f7a6b5c4d","seller_sku":"A-200-R-M","stock":0},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnStockLowRequest

try {
    $apiInstance->onStockLow($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_stock_low_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onStockLow: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_stock_low_request** | [**\Dona\Api\Model\OnStockLowRequest**](../Model/OnStockLowRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onStockOut()`

```php
onStockOut($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_stock_low_request)
```

`stock.out`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_stock_low_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"stock.out","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"product_id":"0199612e-8a0b-7c4d-b1e2-3f4a5b6c7d8e","variant_id":"0199612e-8a0c-7d11-a0b2-9e8f7a6b5c4d","seller_sku":"A-200-R-M","stock":0},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnStockLowRequest

try {
    $apiInstance->onStockOut($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_stock_low_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onStockOut: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_stock_low_request** | [**\Dona\Api\Model\OnStockLowRequest**](../Model/OnStockLowRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onWebhookDisabled()`

```php
onWebhookDisabled($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_webhook_failing_request)
```

`webhook.disabled`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_webhook_failing_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"webhook.disabled","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"webhook_id":"01997b32-2c3d-7e4f-9a5b-6c7d8e9f0a1b","failing_since":"2026-09-22T09:00:00+05:00","attempts":9,"last_status":502},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnWebhookFailingRequest

try {
    $apiInstance->onWebhookDisabled($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_webhook_failing_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onWebhookDisabled: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_webhook_failing_request** | [**\Dona\Api\Model\OnWebhookFailingRequest**](../Model/OnWebhookFailingRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onWebhookFailing()`

```php
onWebhookFailing($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_webhook_failing_request)
```

`webhook.failing`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_webhook_failing_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"webhook.failing","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"webhook_id":"01997b32-2c3d-7e4f-9a5b-6c7d8e9f0a1b","failing_since":"2026-09-22T09:00:00+05:00","attempts":9,"last_status":502},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnWebhookFailingRequest

try {
    $apiInstance->onWebhookFailing($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_webhook_failing_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onWebhookFailing: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_webhook_failing_request** | [**\Dona\Api\Model\OnWebhookFailingRequest**](../Model/OnWebhookFailingRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onWriteApproved()`

```php
onWriteApproved($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_write_held_request)
```

`write.approved`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_write_held_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"write.approved","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"approval_id":"01997b31-1b2c-7d3e-8f4a-5b6c7d8e9f0a","kind":"price","subject_type":"product","subject_id":"0199612e-8a0b-7c4d-b1e2-3f4a5b6c7d8e","rule":"price_floor","decided_by_kind":null},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnWriteHeldRequest

try {
    $apiInstance->onWriteApproved($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_write_held_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onWriteApproved: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_write_held_request** | [**\Dona\Api\Model\OnWriteHeldRequest**](../Model/OnWriteHeldRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onWriteExpired()`

```php
onWriteExpired($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_write_held_request)
```

`write.expired`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_write_held_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"write.expired","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"approval_id":"01997b31-1b2c-7d3e-8f4a-5b6c7d8e9f0a","kind":"price","subject_type":"product","subject_id":"0199612e-8a0b-7c4d-b1e2-3f4a5b6c7d8e","rule":"price_floor","decided_by_kind":null},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnWriteHeldRequest

try {
    $apiInstance->onWriteExpired($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_write_held_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onWriteExpired: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_write_held_request** | [**\Dona\Api\Model\OnWriteHeldRequest**](../Model/OnWriteHeldRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onWriteHeld()`

```php
onWriteHeld($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_write_held_request)
```

`write.held`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_write_held_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"write.held","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"approval_id":"01997b31-1b2c-7d3e-8f4a-5b6c7d8e9f0a","kind":"price","subject_type":"product","subject_id":"0199612e-8a0b-7c4d-b1e2-3f4a5b6c7d8e","rule":"price_floor","decided_by_kind":null},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnWriteHeldRequest

try {
    $apiInstance->onWriteHeld($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_write_held_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onWriteHeld: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_write_held_request** | [**\Dona\Api\Model\OnWriteHeldRequest**](../Model/OnWriteHeldRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `onWriteRejected()`

```php
onWriteRejected($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_write_held_request)
```

`write.rejected`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new Dona\Api\Api\WebhookEventsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$webhook_id = 'webhook_id_example'; // string | = the event id. Your idempotency key — dedupe for 24 h.
$webhook_timestamp = 56; // int | Unix seconds. Reject if |now − ts| > 300 s. A redelivery carries a FRESH timestamp.
$webhook_signature = v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=; // string | Standard Webhooks: space-delimited `v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id + \".\" + ts + \".\" + rawBody)>`; two entries during a 24 h rotation.
$dona_request_id = 'dona_request_id_example'; // string | Correlates with the delivery log.
$on_write_held_request = {"id":"01997b2e-7f00-7123-8456-789abcdef012","type":"write.rejected","occurred_at":"2026-09-24T09:12:31+05:00","seller_id":"0198f3a2-6c1d-7b40-8e55-2a9c3d4e5f60","api_version":"v1","data":{"approval_id":"01997b31-1b2c-7d3e-8f4a-5b6c7d8e9f0a","kind":"price","subject_type":"product","subject_id":"0199612e-8a0b-7c4d-b1e2-3f4a5b6c7d8e","rule":"price_floor","decided_by_kind":null},"links":{"self":"/seller-api/v1/orders/01997b2e-41c0-7e6f-8a9b-0c1d2e3f4a5b"}}; // \Dona\Api\Model\OnWriteHeldRequest

try {
    $apiInstance->onWriteRejected($webhook_id, $webhook_timestamp, $webhook_signature, $dona_request_id, $on_write_held_request);
} catch (Exception $e) {
    echo 'Exception when calling WebhookEventsApi->onWriteRejected: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **webhook_id** | **string**| &#x3D; the event id. Your idempotency key — dedupe for 24 h. | |
| **webhook_timestamp** | **int**| Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. | |
| **webhook_signature** | **string**| Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. | |
| **dona_request_id** | **string**| Correlates with the delivery log. | |
| **on_write_held_request** | [**\Dona\Api\Model\OnWriteHeldRequest**](../Model/OnWriteHeldRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

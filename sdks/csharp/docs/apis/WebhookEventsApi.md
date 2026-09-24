# Dona.Api.Api.WebhookEventsApi

All URIs are relative to *https://api.dona.im/seller-api/v1*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**OnAccountAgreementOwed**](WebhookEventsApi.md#onaccountagreementowed) | **POST** /account.agreement_owed | &#x60;account.agreement_owed&#x60; |
| [**OnAccountDocumentsDecided**](WebhookEventsApi.md#onaccountdocumentsdecided) | **POST** /account.documents_decided | &#x60;account.documents_decided&#x60; |
| [**OnAccountHealthChanged**](WebhookEventsApi.md#onaccounthealthchanged) | **POST** /account.health_changed | &#x60;account.health_changed&#x60; |
| [**OnAccountKycReopened**](WebhookEventsApi.md#onaccountkycreopened) | **POST** /account.kyc_reopened | &#x60;account.kyc_reopened&#x60; |
| [**OnAccountStatusChanged**](WebhookEventsApi.md#onaccountstatuschanged) | **POST** /account.status_changed | &#x60;account.status_changed&#x60; |
| [**OnAccountSuppressed**](WebhookEventsApi.md#onaccountsuppressed) | **POST** /account.suppressed | &#x60;account.suppressed&#x60; |
| [**OnAttentionOpened**](WebhookEventsApi.md#onattentionopened) | **POST** /attention.opened | &#x60;attention.opened&#x60; |
| [**OnAttentionResolved**](WebhookEventsApi.md#onattentionresolved) | **POST** /attention.resolved | &#x60;attention.resolved&#x60; |
| [**OnKeyExpiring**](WebhookEventsApi.md#onkeyexpiring) | **POST** /key.expiring | &#x60;key.expiring&#x60; |
| [**OnKeySuspended**](WebhookEventsApi.md#onkeysuspended) | **POST** /key.suspended | &#x60;key.suspended&#x60; |
| [**OnKeyUnsuspended**](WebhookEventsApi.md#onkeyunsuspended) | **POST** /key.unsuspended | &#x60;key.unsuspended&#x60; |
| [**OnLiveAccessChanged**](WebhookEventsApi.md#onliveaccesschanged) | **POST** /live.access_changed | &#x60;live.access_changed&#x60; |
| [**OnLiveStrike**](WebhookEventsApi.md#onlivestrike) | **POST** /live.strike | &#x60;live.strike&#x60; |
| [**OnOrderAcceptDueSoon**](WebhookEventsApi.md#onorderacceptduesoon) | **POST** /order.accept_due_soon | &#x60;order.accept_due_soon&#x60; |
| [**OnOrderAccepted**](WebhookEventsApi.md#onorderaccepted) | **POST** /order.accepted | &#x60;order.accepted&#x60; |
| [**OnOrderCancelled**](WebhookEventsApi.md#onordercancelled) | **POST** /order.cancelled | &#x60;order.cancelled&#x60; |
| [**OnOrderCreated**](WebhookEventsApi.md#onordercreated) | **POST** /order.created | &#x60;order.created&#x60; |
| [**OnOrderDeclined**](WebhookEventsApi.md#onorderdeclined) | **POST** /order.declined | &#x60;order.declined&#x60; |
| [**OnOrderDelivered**](WebhookEventsApi.md#onorderdelivered) | **POST** /order.delivered | &#x60;order.delivered&#x60; |
| [**OnOrderLineCancelled**](WebhookEventsApi.md#onorderlinecancelled) | **POST** /order.line_cancelled | &#x60;order.line_cancelled&#x60; |
| [**OnOrderPaid**](WebhookEventsApi.md#onorderpaid) | **POST** /order.paid | &#x60;order.paid&#x60; |
| [**OnOrderReady**](WebhookEventsApi.md#onorderready) | **POST** /order.ready | &#x60;order.ready&#x60; |
| [**OnOrderShipOverdue**](WebhookEventsApi.md#onordershipoverdue) | **POST** /order.ship_overdue | &#x60;order.ship_overdue&#x60; |
| [**OnOrderShipped**](WebhookEventsApi.md#onordershipped) | **POST** /order.shipped | &#x60;order.shipped&#x60; |
| [**OnPing**](WebhookEventsApi.md#onping) | **POST** /ping | &#x60;ping&#x60; |
| [**OnProductDeleted**](WebhookEventsApi.md#onproductdeleted) | **POST** /product.deleted | &#x60;product.deleted&#x60; |
| [**OnProductDemoted**](WebhookEventsApi.md#onproductdemoted) | **POST** /product.demoted | &#x60;product.demoted&#x60; |
| [**OnProductHeld**](WebhookEventsApi.md#onproductheld) | **POST** /product.held | &#x60;product.held&#x60; |
| [**OnProductPublished**](WebhookEventsApi.md#onproductpublished) | **POST** /product.published | &#x60;product.published&#x60; |
| [**OnProductRejected**](WebhookEventsApi.md#onproductrejected) | **POST** /product.rejected | &#x60;product.rejected&#x60; |
| [**OnProductViolation**](WebhookEventsApi.md#onproductviolation) | **POST** /product.violation | &#x60;product.violation&#x60; |
| [**OnReturnRequested**](WebhookEventsApi.md#onreturnrequested) | **POST** /return.requested | &#x60;return.requested&#x60; |
| [**OnReturnStatusChanged**](WebhookEventsApi.md#onreturnstatuschanged) | **POST** /return.status_changed | &#x60;return.status_changed&#x60; |
| [**OnStockLow**](WebhookEventsApi.md#onstocklow) | **POST** /stock.low | &#x60;stock.low&#x60; |
| [**OnStockOut**](WebhookEventsApi.md#onstockout) | **POST** /stock.out | &#x60;stock.out&#x60; |
| [**OnWebhookDisabled**](WebhookEventsApi.md#onwebhookdisabled) | **POST** /webhook.disabled | &#x60;webhook.disabled&#x60; |
| [**OnWebhookFailing**](WebhookEventsApi.md#onwebhookfailing) | **POST** /webhook.failing | &#x60;webhook.failing&#x60; |
| [**OnWriteApproved**](WebhookEventsApi.md#onwriteapproved) | **POST** /write.approved | &#x60;write.approved&#x60; |
| [**OnWriteExpired**](WebhookEventsApi.md#onwriteexpired) | **POST** /write.expired | &#x60;write.expired&#x60; |
| [**OnWriteHeld**](WebhookEventsApi.md#onwriteheld) | **POST** /write.held | &#x60;write.held&#x60; |
| [**OnWriteRejected**](WebhookEventsApi.md#onwriterejected) | **POST** /write.rejected | &#x60;write.rejected&#x60; |

<a id="onaccountagreementowed"></a>
# **OnAccountAgreementOwed**
> void OnAccountAgreementOwed (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnAccountAgreementOwedRequest onAccountAgreementOwedRequest)

`account.agreement_owed`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onAccountAgreementOwedRequest** | [**OnAccountAgreementOwedRequest**](OnAccountAgreementOwedRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onaccountdocumentsdecided"></a>
# **OnAccountDocumentsDecided**
> void OnAccountDocumentsDecided (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnAccountDocumentsDecidedRequest onAccountDocumentsDecidedRequest)

`account.documents_decided`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onAccountDocumentsDecidedRequest** | [**OnAccountDocumentsDecidedRequest**](OnAccountDocumentsDecidedRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onaccounthealthchanged"></a>
# **OnAccountHealthChanged**
> void OnAccountHealthChanged (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnAccountHealthChangedRequest onAccountHealthChangedRequest)

`account.health_changed`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onAccountHealthChangedRequest** | [**OnAccountHealthChangedRequest**](OnAccountHealthChangedRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onaccountkycreopened"></a>
# **OnAccountKycReopened**
> void OnAccountKycReopened (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnAccountKycReopenedRequest onAccountKycReopenedRequest)

`account.kyc_reopened`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onAccountKycReopenedRequest** | [**OnAccountKycReopenedRequest**](OnAccountKycReopenedRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onaccountstatuschanged"></a>
# **OnAccountStatusChanged**
> void OnAccountStatusChanged (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnAccountStatusChangedRequest onAccountStatusChangedRequest)

`account.status_changed`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onAccountStatusChangedRequest** | [**OnAccountStatusChangedRequest**](OnAccountStatusChangedRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onaccountsuppressed"></a>
# **OnAccountSuppressed**
> void OnAccountSuppressed (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnAccountSuppressedRequest onAccountSuppressedRequest)

`account.suppressed`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onAccountSuppressedRequest** | [**OnAccountSuppressedRequest**](OnAccountSuppressedRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onattentionopened"></a>
# **OnAttentionOpened**
> void OnAttentionOpened (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnAttentionOpenedRequest onAttentionOpenedRequest)

`attention.opened`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onAttentionOpenedRequest** | [**OnAttentionOpenedRequest**](OnAttentionOpenedRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onattentionresolved"></a>
# **OnAttentionResolved**
> void OnAttentionResolved (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnAttentionOpenedRequest onAttentionOpenedRequest)

`attention.resolved`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onAttentionOpenedRequest** | [**OnAttentionOpenedRequest**](OnAttentionOpenedRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onkeyexpiring"></a>
# **OnKeyExpiring**
> void OnKeyExpiring (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnKeyExpiringRequest onKeyExpiringRequest)

`key.expiring`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onKeyExpiringRequest** | [**OnKeyExpiringRequest**](OnKeyExpiringRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onkeysuspended"></a>
# **OnKeySuspended**
> void OnKeySuspended (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnKeyExpiringRequest onKeyExpiringRequest)

`key.suspended`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onKeyExpiringRequest** | [**OnKeyExpiringRequest**](OnKeyExpiringRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onkeyunsuspended"></a>
# **OnKeyUnsuspended**
> void OnKeyUnsuspended (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnKeyExpiringRequest onKeyExpiringRequest)

`key.unsuspended`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onKeyExpiringRequest** | [**OnKeyExpiringRequest**](OnKeyExpiringRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onliveaccesschanged"></a>
# **OnLiveAccessChanged**
> void OnLiveAccessChanged (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnLiveAccessChangedRequest onLiveAccessChangedRequest)

`live.access_changed`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onLiveAccessChangedRequest** | [**OnLiveAccessChangedRequest**](OnLiveAccessChangedRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onlivestrike"></a>
# **OnLiveStrike**
> void OnLiveStrike (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnLiveStrikeRequest onLiveStrikeRequest)

`live.strike`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onLiveStrikeRequest** | [**OnLiveStrikeRequest**](OnLiveStrikeRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onorderacceptduesoon"></a>
# **OnOrderAcceptDueSoon**
> void OnOrderAcceptDueSoon (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnOrderAcceptDueSoonRequest onOrderAcceptDueSoonRequest)

`order.accept_due_soon`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onOrderAcceptDueSoonRequest** | [**OnOrderAcceptDueSoonRequest**](OnOrderAcceptDueSoonRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onorderaccepted"></a>
# **OnOrderAccepted**
> void OnOrderAccepted (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnOrderCreatedRequest onOrderCreatedRequest)

`order.accepted`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onOrderCreatedRequest** | [**OnOrderCreatedRequest**](OnOrderCreatedRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onordercancelled"></a>
# **OnOrderCancelled**
> void OnOrderCancelled (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnOrderDeclinedRequest onOrderDeclinedRequest)

`order.cancelled`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onOrderDeclinedRequest** | [**OnOrderDeclinedRequest**](OnOrderDeclinedRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onordercreated"></a>
# **OnOrderCreated**
> void OnOrderCreated (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnOrderCreatedRequest onOrderCreatedRequest)

`order.created`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onOrderCreatedRequest** | [**OnOrderCreatedRequest**](OnOrderCreatedRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onorderdeclined"></a>
# **OnOrderDeclined**
> void OnOrderDeclined (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnOrderDeclinedRequest onOrderDeclinedRequest)

`order.declined`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onOrderDeclinedRequest** | [**OnOrderDeclinedRequest**](OnOrderDeclinedRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onorderdelivered"></a>
# **OnOrderDelivered**
> void OnOrderDelivered (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnOrderCreatedRequest onOrderCreatedRequest)

`order.delivered`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onOrderCreatedRequest** | [**OnOrderCreatedRequest**](OnOrderCreatedRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onorderlinecancelled"></a>
# **OnOrderLineCancelled**
> void OnOrderLineCancelled (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnOrderLineCancelledRequest onOrderLineCancelledRequest)

`order.line_cancelled`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onOrderLineCancelledRequest** | [**OnOrderLineCancelledRequest**](OnOrderLineCancelledRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onorderpaid"></a>
# **OnOrderPaid**
> void OnOrderPaid (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnOrderCreatedRequest onOrderCreatedRequest)

`order.paid`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onOrderCreatedRequest** | [**OnOrderCreatedRequest**](OnOrderCreatedRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onorderready"></a>
# **OnOrderReady**
> void OnOrderReady (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnOrderCreatedRequest onOrderCreatedRequest)

`order.ready`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onOrderCreatedRequest** | [**OnOrderCreatedRequest**](OnOrderCreatedRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onordershipoverdue"></a>
# **OnOrderShipOverdue**
> void OnOrderShipOverdue (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnOrderAcceptDueSoonRequest onOrderAcceptDueSoonRequest)

`order.ship_overdue`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onOrderAcceptDueSoonRequest** | [**OnOrderAcceptDueSoonRequest**](OnOrderAcceptDueSoonRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onordershipped"></a>
# **OnOrderShipped**
> void OnOrderShipped (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnOrderCreatedRequest onOrderCreatedRequest)

`order.shipped`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onOrderCreatedRequest** | [**OnOrderCreatedRequest**](OnOrderCreatedRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onping"></a>
# **OnPing**
> void OnPing (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnPingRequest onPingRequest)

`ping`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onPingRequest** | [**OnPingRequest**](OnPingRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onproductdeleted"></a>
# **OnProductDeleted**
> void OnProductDeleted (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnProductPublishedRequest onProductPublishedRequest)

`product.deleted`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onProductPublishedRequest** | [**OnProductPublishedRequest**](OnProductPublishedRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onproductdemoted"></a>
# **OnProductDemoted**
> void OnProductDemoted (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnProductPublishedRequest onProductPublishedRequest)

`product.demoted`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onProductPublishedRequest** | [**OnProductPublishedRequest**](OnProductPublishedRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onproductheld"></a>
# **OnProductHeld**
> void OnProductHeld (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnProductHeldRequest onProductHeldRequest)

`product.held`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onProductHeldRequest** | [**OnProductHeldRequest**](OnProductHeldRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onproductpublished"></a>
# **OnProductPublished**
> void OnProductPublished (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnProductPublishedRequest onProductPublishedRequest)

`product.published`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onProductPublishedRequest** | [**OnProductPublishedRequest**](OnProductPublishedRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onproductrejected"></a>
# **OnProductRejected**
> void OnProductRejected (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnProductHeldRequest onProductHeldRequest)

`product.rejected`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onProductHeldRequest** | [**OnProductHeldRequest**](OnProductHeldRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onproductviolation"></a>
# **OnProductViolation**
> void OnProductViolation (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnProductHeldRequest onProductHeldRequest)

`product.violation`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onProductHeldRequest** | [**OnProductHeldRequest**](OnProductHeldRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onreturnrequested"></a>
# **OnReturnRequested**
> void OnReturnRequested (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnReturnRequestedRequest onReturnRequestedRequest)

`return.requested`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onReturnRequestedRequest** | [**OnReturnRequestedRequest**](OnReturnRequestedRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onreturnstatuschanged"></a>
# **OnReturnStatusChanged**
> void OnReturnStatusChanged (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnReturnRequestedRequest onReturnRequestedRequest)

`return.status_changed`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onReturnRequestedRequest** | [**OnReturnRequestedRequest**](OnReturnRequestedRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onstocklow"></a>
# **OnStockLow**
> void OnStockLow (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnStockLowRequest onStockLowRequest)

`stock.low`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onStockLowRequest** | [**OnStockLowRequest**](OnStockLowRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onstockout"></a>
# **OnStockOut**
> void OnStockOut (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnStockLowRequest onStockLowRequest)

`stock.out`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onStockLowRequest** | [**OnStockLowRequest**](OnStockLowRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onwebhookdisabled"></a>
# **OnWebhookDisabled**
> void OnWebhookDisabled (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnWebhookFailingRequest onWebhookFailingRequest)

`webhook.disabled`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onWebhookFailingRequest** | [**OnWebhookFailingRequest**](OnWebhookFailingRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onwebhookfailing"></a>
# **OnWebhookFailing**
> void OnWebhookFailing (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnWebhookFailingRequest onWebhookFailingRequest)

`webhook.failing`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onWebhookFailingRequest** | [**OnWebhookFailingRequest**](OnWebhookFailingRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onwriteapproved"></a>
# **OnWriteApproved**
> void OnWriteApproved (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnWriteHeldRequest onWriteHeldRequest)

`write.approved`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onWriteHeldRequest** | [**OnWriteHeldRequest**](OnWriteHeldRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onwriteexpired"></a>
# **OnWriteExpired**
> void OnWriteExpired (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnWriteHeldRequest onWriteHeldRequest)

`write.expired`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onWriteHeldRequest** | [**OnWriteHeldRequest**](OnWriteHeldRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onwriteheld"></a>
# **OnWriteHeld**
> void OnWriteHeld (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnWriteHeldRequest onWriteHeldRequest)

`write.held`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onWriteHeldRequest** | [**OnWriteHeldRequest**](OnWriteHeldRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="onwriterejected"></a>
# **OnWriteRejected**
> void OnWriteRejected (Guid webhookId, int webhookTimestamp, string webhookSignature, string donaRequestId, OnWriteHeldRequest onWriteHeldRequest)

`write.rejected`

One event per POST (≤ 20 KB), at-least-once, unordered. Reply 2xx within 10 s (ack first, process after); 3xx is a failure; `410 Gone` disables the endpoint. Retry ladder: immediate · 5 s · 5 m · 30 m · 2 h · 5 h · 10 h · 14 h · 20 h · 24 h (≈ 75 h, ±10 % jitter).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **webhookId** | **Guid** | &#x3D; the event id. Your idempotency key — dedupe for 24 h. |  |
| **webhookTimestamp** | **int** | Unix seconds. Reject if |now − ts| &gt; 300 s. A redelivery carries a FRESH timestamp. |  |
| **webhookSignature** | **string** | Standard Webhooks: space-delimited &#x60;v1,&lt;base64 HMAC-SHA256(base64decode(secret after whsec_), id + \&quot;.\&quot; + ts + \&quot;.\&quot; + rawBody)&gt;&#x60;; two entries during a 24 h rotation. |  |
| **donaRequestId** | **string** | Correlates with the delivery log. |  |
| **onWriteHeldRequest** | [**OnWriteHeldRequest**](OnWriteHeldRequest.md) |  |  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **410** | Endpoint gone — Dona disables it immediately. |  -  |
| **2XX** | Acknowledged; the body is ignored. |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)


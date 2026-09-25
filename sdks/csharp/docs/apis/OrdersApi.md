# Dona.Api.Api.OrdersApi

All URIs are relative to *https://api.dona.im/seller-api/v1*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**AcceptOrder**](OrdersApi.md#acceptorder) | **POST** /orders/{id}/accept | Accept |
| [**AddOrderNote**](OrdersApi.md#addordernote) | **POST** /orders/{id}/notes | Add a seller note |
| [**BatchOrderLabels**](OrdersApi.md#batchorderlabels) | **POST** /orders/labels | Labels for ≤ 100 orders (one PDF) |
| [**CancelOrder**](OrdersApi.md#cancelorder) | **POST** /orders/{id}/cancel | Cancel (after acceptance) — money-reversing |
| [**DeclineOrder**](OrdersApi.md#declineorder) | **POST** /orders/{id}/decline | Decline (before acceptance) — money-reversing |
| [**GetOrder**](OrdersApi.md#getorder) | **GET** /orders/{id} | Get an order (PII only with orders:pii) |
| [**GetOrderInvoice**](OrdersApi.md#getorderinvoice) | **GET** /orders/{id}/invoice.pdf | Invoice (PDF, contains PII) |
| [**GetOrderLabel**](OrdersApi.md#getorderlabel) | **GET** /orders/{id}/label.pdf | Shipping label (PDF, contains PII) |
| [**GetOrderTimeline**](OrdersApi.md#getordertimeline) | **GET** /orders/{id}/timeline | Order timeline |
| [**HandoverOrder**](OrdersApi.md#handoverorder) | **POST** /orders/{id}/handover | Hand over to the courier |
| [**ListOrders**](OrdersApi.md#listorders) | **GET** /orders | List orders (no buyer PII) |
| [**MarkOrderReady**](OrdersApi.md#markorderready) | **POST** /orders/{id}/ready | Mark ready to ship |
| [**ShipOrder**](OrdersApi.md#shiporder) | **POST** /orders/{id}/ship | Ship |

<a id="acceptorder"></a>
# **AcceptOrder**
> OrderTransition AcceptOrder (Guid id, string idempotencyKey, string donaDryRun = null, string dryRun = null, string acceptLanguage = null, Guid donaSeller = null, string xDonaIntegration = null)

Accept

The `intake.go` accept body, extracted. Needs a pickup address. 409: `order_not_acceptable`, `no_pickup_address`. Kill switch: `writes_enabled`.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** | Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. |  |
| **idempotencyKey** | **string** | 1–255 chars. Scope &#x3D; this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ &#x60;400 invalid_body&#x60; with &#x60;details[{field:\&quot;Idempotency-Key\&quot;,code:\&quot;required\&quot;}]&#x60;. |  |
| **donaDryRun** | **string** | &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. Only the literal &#x60;true&#x60; / &#x60;false&#x60;; any other value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Dry-Run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). | [optional]  |
| **dryRun** | **string** | Alias of the &#x60;Dona-Dry-Run&#x60; header. Only the literal strings &#x60;true&#x60; / &#x60;false&#x60; — &#x60;1&#x60;, &#x60;0&#x60;, &#x60;TRUE&#x60;, &#x60;yes&#x60;, an empty value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;dry_run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). A string enum, not a boolean, so no SDK generator serialises it as &#x60;1&#x60;/&#x60;0&#x60;. | [optional]  |
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |
| **donaSeller** | **Guid** | Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional]  |
| **xDonaIntegration** | **string** | &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional]  |

### Return type

[**OrderTransition**](OrderTransition.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Dona-Request-Id -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * X-Dona-Key-Expires -  <br>  * Dona-API-Warn -  <br>  * Deprecation -  <br>  * Sunset -  <br>  * Cache-Control -  <br>  |
| **400** | &#x60;invalid_body&#x60; — malformed JSON, a missing &#x60;Idempotency-Key&#x60;, validation (&#x60;details[]&#x60; carries field codes such as &#x60;ikpu_required&#x60;, &#x60;cursor_expired&#x60;), a &#x60;dry_run&#x60; / &#x60;Dona-Dry-Run&#x60; that is not the literal &#x60;true&#x60;/&#x60;false&#x60; (&#x60;details[{field, code:\&quot;invalid\&quot;}]&#x60;, C51), a vendor-app install key without &#x60;Dona-Seller&#x60; (&#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;, S6) or with a repeated / non-canonical one (&#x60;code:\&quot;invalid\&quot;&#x60;), or an op-specific 400 (&#x60;invalid_decline_reason&#x60;). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **401** | &#x60;api_key_malformed&#x60; (checksum fails — refused before any DB read) · &#x60;api_key_expired&#x60; (+&#x60;rotate_url&#x60;, no grace) · &#x60;api_key_revoked&#x60; (also a vendor-app key whose install was uninstalled — S6) · &#x60;key_kind_not_accepted&#x60; (an agent key &#x60;ak&#x60; on this tree) · &#x60;use_authorization_header&#x60; (&#x60;X-Api-Key&#x60; or a query-string key) · a seller/app/staff JWT on this tree. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **403** | &#x60;insufficient_scope&#x60; (+&#x60;required_scope&#x60;; also a scope in &#x60;disabled_scopes&#x60;) · &#x60;tier_required&#x60; (+&#x60;scope&#x60;; derived on every request; also a key minted for a third-party &#x60;orders:pii&#x60; recipient — &#x60;details[pii_recipient: pii_third_party_pending_counsel]&#x60;, D7, C59) · &#x60;key_suspended&#x60; (+&#x60;suspended_until&#x60;, &#x60;Retry-After&#x60;, &#x60;Dona-Rate-Limited-Reason: suspended&#x60;) · &#x60;api_blocked&#x60; · &#x60;ip_not_allowed&#x60; (judged on the trusted client IP only) · &#x60;seller_not_approved&#x60; (shop closed/blocked/suspended/restricted) · &#x60;not_a_seller&#x60; (never on this tree; the portal&#39;s owner doors) · &#x60;app_frozen&#x60; (S6: every key of a frozen vendor app, from the next request) · &#x60;agreement_required&#x60; (+&#x60;accept_url&#x60;: the shop owner has not accepted the CURRENT Annex 2 «API and automated access» — the version in force or, while none is, the earliest announced; accepted once in Settings › API, then every door admits the key again. Checked after the sanctions, before the scopes). |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |
| **404** | &#x60;not_found&#x60; — every missing OR foreign id (never 403: no existence oracle). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **409** | &#x60;idempotency_in_progress&#x60; (+&#x60;Retry-After: 2&#x60;) · &#x60;idempotency_mismatch&#x60; · &#x60;version_conflict&#x60; · &#x60;ai_review_open&#x60; (publish of a product whose Dona AI review case is open — the review decides its status) · order codes &#x60;order_not_acceptable&#x60;, &#x60;no_pickup_address&#x60;, &#x60;order_not_shippable&#x60;, &#x60;order_awaiting_courier&#x60;, &#x60;order_not_cancellable&#x60;, &#x60;order_has_active_return&#x60; · document codes &#x60;no_tracking_number&#x60; (+&#x60;orders&#x60;), &#x60;no_items_selected&#x60;, &#x60;all_items_delayed&#x60; (S4, C53) · a replay of a rejected held write. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Cache-Control -  <br>  |
| **429** | &#x60;rate_limited&#x60; (with &#x60;Dona-Rate-Limited-Reason: app-rate&#x60;: a vendor app&#39;s bucket, shared by all its installs — S6) · &#x60;write_rate_limited&#x60; · &#x60;concurrency_limited&#x60; · &#x60;seller_rate_limited&#x60; · &#x60;object_cooldown&#x60; · &#x60;api_busy&#x60;. Always a JSON body + &#x60;Retry-After&#x60; from the origin (an edge 429 from Cloudflare has NO body — treat it as &#x60;Retry-After: 60&#x60;). Costs 0 and never counts toward the breaker. &#x60;rate_limited&#x60; is also the pre-auth ADDRESS guard, answered before the key is read: an address over 1 200 requests a minute that were not admitted (no key, a public route, a malformed, unknown or refused key — admitted requests never count), or one tarpitted at 60/min for 15 min after ≥ 20 unknown keys in a minute. No key is ever suspended by traffic that did not prove it. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * Cache-Control -  <br>  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **503** | &#x60;auth_unavailable&#x60; (key lookup failed — fail closed) · &#x60;limits_unavailable&#x60; (limiter blind on a write/MCP call, or a kill switch is off: &#x60;enabled&#x60;, &#x60;writes_enabled&#x60;, &#x60;webhooks_enabled&#x60;; &#x60;Retry-After: 30&#x60;) · &#x60;attention_busy&#x60; (an acknowledgement that resolves an item could not take the attention writer lock within 2 s — nothing was written; retry after &#x60;Retry-After: 2&#x60;) · &#x60;wallet_unavailable&#x60; (&#x60;/finance/_*&#x60;: the wallet could not answer for the shop; &#x60;Retry-After: 30&#x60;; its body is never relayed or error-copied — S4, C57) · &#x60;role_unavailable&#x60; (+ &#x60;served_by: \&quot;marketplace\&quot;&#x60;: a SERVER_ROLE&#x3D;seller-api server does not serve decline / cancel or &#x60;/finance/_*&#x60;; answered before any read or write, nothing changed; no &#x60;Retry-After&#x60; — D3). Costs 0. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="addordernote"></a>
# **AddOrderNote**
> NoteCreated AddOrderNote (Guid id, string idempotencyKey, NoteRequest noteRequest, string donaDryRun = null, string dryRun = null, string acceptLanguage = null, Guid donaSeller = null, string xDonaIntegration = null)

Add a seller note

Appends to `order_notes`. Kill switch: `writes_enabled`.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** | Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. |  |
| **idempotencyKey** | **string** | 1–255 chars. Scope &#x3D; this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ &#x60;400 invalid_body&#x60; with &#x60;details[{field:\&quot;Idempotency-Key\&quot;,code:\&quot;required\&quot;}]&#x60;. |  |
| **noteRequest** | [**NoteRequest**](NoteRequest.md) |  |  |
| **donaDryRun** | **string** | &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. Only the literal &#x60;true&#x60; / &#x60;false&#x60;; any other value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Dry-Run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). | [optional]  |
| **dryRun** | **string** | Alias of the &#x60;Dona-Dry-Run&#x60; header. Only the literal strings &#x60;true&#x60; / &#x60;false&#x60; — &#x60;1&#x60;, &#x60;0&#x60;, &#x60;TRUE&#x60;, &#x60;yes&#x60;, an empty value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;dry_run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). A string enum, not a boolean, so no SDK generator serialises it as &#x60;1&#x60;/&#x60;0&#x60;. | [optional]  |
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |
| **donaSeller** | **Guid** | Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional]  |
| **xDonaIntegration** | **string** | &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional]  |

### Return type

[**NoteCreated**](NoteCreated.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  * Dona-Request-Id -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * X-Dona-Key-Expires -  <br>  * Dona-API-Warn -  <br>  * Deprecation -  <br>  * Sunset -  <br>  * Cache-Control -  <br>  |
| **400** | &#x60;invalid_body&#x60; — malformed JSON, a missing &#x60;Idempotency-Key&#x60;, validation (&#x60;details[]&#x60; carries field codes such as &#x60;ikpu_required&#x60;, &#x60;cursor_expired&#x60;), a &#x60;dry_run&#x60; / &#x60;Dona-Dry-Run&#x60; that is not the literal &#x60;true&#x60;/&#x60;false&#x60; (&#x60;details[{field, code:\&quot;invalid\&quot;}]&#x60;, C51), a vendor-app install key without &#x60;Dona-Seller&#x60; (&#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;, S6) or with a repeated / non-canonical one (&#x60;code:\&quot;invalid\&quot;&#x60;), or an op-specific 400 (&#x60;invalid_decline_reason&#x60;). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **401** | &#x60;api_key_malformed&#x60; (checksum fails — refused before any DB read) · &#x60;api_key_expired&#x60; (+&#x60;rotate_url&#x60;, no grace) · &#x60;api_key_revoked&#x60; (also a vendor-app key whose install was uninstalled — S6) · &#x60;key_kind_not_accepted&#x60; (an agent key &#x60;ak&#x60; on this tree) · &#x60;use_authorization_header&#x60; (&#x60;X-Api-Key&#x60; or a query-string key) · a seller/app/staff JWT on this tree. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **403** | &#x60;insufficient_scope&#x60; (+&#x60;required_scope&#x60;; also a scope in &#x60;disabled_scopes&#x60;) · &#x60;tier_required&#x60; (+&#x60;scope&#x60;; derived on every request; also a key minted for a third-party &#x60;orders:pii&#x60; recipient — &#x60;details[pii_recipient: pii_third_party_pending_counsel]&#x60;, D7, C59) · &#x60;key_suspended&#x60; (+&#x60;suspended_until&#x60;, &#x60;Retry-After&#x60;, &#x60;Dona-Rate-Limited-Reason: suspended&#x60;) · &#x60;api_blocked&#x60; · &#x60;ip_not_allowed&#x60; (judged on the trusted client IP only) · &#x60;seller_not_approved&#x60; (shop closed/blocked/suspended/restricted) · &#x60;not_a_seller&#x60; (never on this tree; the portal&#39;s owner doors) · &#x60;app_frozen&#x60; (S6: every key of a frozen vendor app, from the next request) · &#x60;agreement_required&#x60; (+&#x60;accept_url&#x60;: the shop owner has not accepted the CURRENT Annex 2 «API and automated access» — the version in force or, while none is, the earliest announced; accepted once in Settings › API, then every door admits the key again. Checked after the sanctions, before the scopes). |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |
| **404** | &#x60;not_found&#x60; — every missing OR foreign id (never 403: no existence oracle). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **409** | &#x60;idempotency_in_progress&#x60; (+&#x60;Retry-After: 2&#x60;) · &#x60;idempotency_mismatch&#x60; · &#x60;version_conflict&#x60; · &#x60;ai_review_open&#x60; (publish of a product whose Dona AI review case is open — the review decides its status) · order codes &#x60;order_not_acceptable&#x60;, &#x60;no_pickup_address&#x60;, &#x60;order_not_shippable&#x60;, &#x60;order_awaiting_courier&#x60;, &#x60;order_not_cancellable&#x60;, &#x60;order_has_active_return&#x60; · document codes &#x60;no_tracking_number&#x60; (+&#x60;orders&#x60;), &#x60;no_items_selected&#x60;, &#x60;all_items_delayed&#x60; (S4, C53) · a replay of a rejected held write. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Cache-Control -  <br>  |
| **429** | &#x60;rate_limited&#x60; (with &#x60;Dona-Rate-Limited-Reason: app-rate&#x60;: a vendor app&#39;s bucket, shared by all its installs — S6) · &#x60;write_rate_limited&#x60; · &#x60;concurrency_limited&#x60; · &#x60;seller_rate_limited&#x60; · &#x60;object_cooldown&#x60; · &#x60;api_busy&#x60;. Always a JSON body + &#x60;Retry-After&#x60; from the origin (an edge 429 from Cloudflare has NO body — treat it as &#x60;Retry-After: 60&#x60;). Costs 0 and never counts toward the breaker. &#x60;rate_limited&#x60; is also the pre-auth ADDRESS guard, answered before the key is read: an address over 1 200 requests a minute that were not admitted (no key, a public route, a malformed, unknown or refused key — admitted requests never count), or one tarpitted at 60/min for 15 min after ≥ 20 unknown keys in a minute. No key is ever suspended by traffic that did not prove it. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * Cache-Control -  <br>  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **503** | &#x60;auth_unavailable&#x60; (key lookup failed — fail closed) · &#x60;limits_unavailable&#x60; (limiter blind on a write/MCP call, or a kill switch is off: &#x60;enabled&#x60;, &#x60;writes_enabled&#x60;, &#x60;webhooks_enabled&#x60;; &#x60;Retry-After: 30&#x60;) · &#x60;attention_busy&#x60; (an acknowledgement that resolves an item could not take the attention writer lock within 2 s — nothing was written; retry after &#x60;Retry-After: 2&#x60;) · &#x60;wallet_unavailable&#x60; (&#x60;/finance/_*&#x60;: the wallet could not answer for the shop; &#x60;Retry-After: 30&#x60;; its body is never relayed or error-copied — S4, C57) · &#x60;role_unavailable&#x60; (+ &#x60;served_by: \&quot;marketplace\&quot;&#x60;: a SERVER_ROLE&#x3D;seller-api server does not serve decline / cancel or &#x60;/finance/_*&#x60;; answered before any read or write, nothing changed; no &#x60;Retry-After&#x60; — D3). Costs 0. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="batchorderlabels"></a>
# **BatchOrderLabels**
> string BatchOrderLabels (LabelsRequest labelsRequest, string acceptLanguage = null, Guid donaSeller = null, string xDonaIntegration = null)

Labels for ≤ 100 orders (one PDF)

A read with a body — no `Idempotency-Key`. Any foreign/missing id ⇒ `404 not_found` for the whole call. Doors and 409s as `label.pdf` (C53); `no_tracking_number` names every offending order. Cost 10 on the key-rate bucket (C54), charged only once the batch holds a drawing slot (`429 api_busy` as `label.pdf`).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **labelsRequest** | [**LabelsRequest**](LabelsRequest.md) |  |  |
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |
| **donaSeller** | **Guid** | Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional]  |
| **xDonaIntegration** | **string** | &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional]  |

### Return type

**string**

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/pdf, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Dona-Request-Id -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * X-Dona-Key-Expires -  <br>  * Dona-API-Warn -  <br>  * Deprecation -  <br>  * Sunset -  <br>  * Cache-Control -  <br>  |
| **400** | &#x60;invalid_body&#x60; — malformed JSON, a missing &#x60;Idempotency-Key&#x60;, validation (&#x60;details[]&#x60; carries field codes such as &#x60;ikpu_required&#x60;, &#x60;cursor_expired&#x60;), a &#x60;dry_run&#x60; / &#x60;Dona-Dry-Run&#x60; that is not the literal &#x60;true&#x60;/&#x60;false&#x60; (&#x60;details[{field, code:\&quot;invalid\&quot;}]&#x60;, C51), a vendor-app install key without &#x60;Dona-Seller&#x60; (&#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;, S6) or with a repeated / non-canonical one (&#x60;code:\&quot;invalid\&quot;&#x60;), or an op-specific 400 (&#x60;invalid_decline_reason&#x60;). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **401** | &#x60;api_key_malformed&#x60; (checksum fails — refused before any DB read) · &#x60;api_key_expired&#x60; (+&#x60;rotate_url&#x60;, no grace) · &#x60;api_key_revoked&#x60; (also a vendor-app key whose install was uninstalled — S6) · &#x60;key_kind_not_accepted&#x60; (an agent key &#x60;ak&#x60; on this tree) · &#x60;use_authorization_header&#x60; (&#x60;X-Api-Key&#x60; or a query-string key) · a seller/app/staff JWT on this tree. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **403** | &#x60;insufficient_scope&#x60; (+&#x60;required_scope&#x60;; also a scope in &#x60;disabled_scopes&#x60;) · &#x60;tier_required&#x60; (+&#x60;scope&#x60;; derived on every request; also a key minted for a third-party &#x60;orders:pii&#x60; recipient — &#x60;details[pii_recipient: pii_third_party_pending_counsel]&#x60;, D7, C59) · &#x60;key_suspended&#x60; (+&#x60;suspended_until&#x60;, &#x60;Retry-After&#x60;, &#x60;Dona-Rate-Limited-Reason: suspended&#x60;) · &#x60;api_blocked&#x60; · &#x60;ip_not_allowed&#x60; (judged on the trusted client IP only) · &#x60;seller_not_approved&#x60; (shop closed/blocked/suspended/restricted) · &#x60;not_a_seller&#x60; (never on this tree; the portal&#39;s owner doors) · &#x60;app_frozen&#x60; (S6: every key of a frozen vendor app, from the next request) · &#x60;agreement_required&#x60; (+&#x60;accept_url&#x60;: the shop owner has not accepted the CURRENT Annex 2 «API and automated access» — the version in force or, while none is, the earliest announced; accepted once in Settings › API, then every door admits the key again. Checked after the sanctions, before the scopes). |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |
| **404** | &#x60;not_found&#x60; — every missing OR foreign id (never 403: no existence oracle). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **409** | &#x60;idempotency_in_progress&#x60; (+&#x60;Retry-After: 2&#x60;) · &#x60;idempotency_mismatch&#x60; · &#x60;version_conflict&#x60; · &#x60;ai_review_open&#x60; (publish of a product whose Dona AI review case is open — the review decides its status) · order codes &#x60;order_not_acceptable&#x60;, &#x60;no_pickup_address&#x60;, &#x60;order_not_shippable&#x60;, &#x60;order_awaiting_courier&#x60;, &#x60;order_not_cancellable&#x60;, &#x60;order_has_active_return&#x60; · document codes &#x60;no_tracking_number&#x60; (+&#x60;orders&#x60;), &#x60;no_items_selected&#x60;, &#x60;all_items_delayed&#x60; (S4, C53) · a replay of a rejected held write. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Cache-Control -  <br>  |
| **429** | &#x60;rate_limited&#x60; (with &#x60;Dona-Rate-Limited-Reason: app-rate&#x60;: a vendor app&#39;s bucket, shared by all its installs — S6) · &#x60;write_rate_limited&#x60; · &#x60;concurrency_limited&#x60; · &#x60;seller_rate_limited&#x60; · &#x60;object_cooldown&#x60; · &#x60;api_busy&#x60;. Always a JSON body + &#x60;Retry-After&#x60; from the origin (an edge 429 from Cloudflare has NO body — treat it as &#x60;Retry-After: 60&#x60;). Costs 0 and never counts toward the breaker. &#x60;rate_limited&#x60; is also the pre-auth ADDRESS guard, answered before the key is read: an address over 1 200 requests a minute that were not admitted (no key, a public route, a malformed, unknown or refused key — admitted requests never count), or one tarpitted at 60/min for 15 min after ≥ 20 unknown keys in a minute. No key is ever suspended by traffic that did not prove it. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * Cache-Control -  <br>  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **503** | &#x60;auth_unavailable&#x60; (key lookup failed — fail closed) · &#x60;limits_unavailable&#x60; (limiter blind on a write/MCP call, or a kill switch is off: &#x60;enabled&#x60;, &#x60;writes_enabled&#x60;, &#x60;webhooks_enabled&#x60;; &#x60;Retry-After: 30&#x60;) · &#x60;attention_busy&#x60; (an acknowledgement that resolves an item could not take the attention writer lock within 2 s — nothing was written; retry after &#x60;Retry-After: 2&#x60;) · &#x60;wallet_unavailable&#x60; (&#x60;/finance/_*&#x60;: the wallet could not answer for the shop; &#x60;Retry-After: 30&#x60;; its body is never relayed or error-copied — S4, C57) · &#x60;role_unavailable&#x60; (+ &#x60;served_by: \&quot;marketplace\&quot;&#x60;: a SERVER_ROLE&#x3D;seller-api server does not serve decline / cancel or &#x60;/finance/_*&#x60;; answered before any read or write, nothing changed; no &#x60;Retry-After&#x60; — D3). Costs 0. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="cancelorder"></a>
# **CancelOrder**
> OrderTransition CancelOrder (Guid id, string idempotencyKey, DeclineRequest declineRequest, string donaDryRun = null, string dryRun = null, string acceptLanguage = null, Guid donaSeller = null, string xDonaIntegration = null)

Cancel (after acceptance) — money-reversing

An ACCEPTED order: the portal seller-cancel's own statements (`order.SellerCancelOrderTx`) — same reasons (C15) and money effects as `decline`. The reason is stored in the order's `cancel_reason` (with the comment), NOT in `decline_reason_code`, which stays `null` (C52); the `cancelled`/`seller` timeline row, the card refund and the buyer notice run after the commit. 409 `order_not_cancellable` — a delivered or cancelled order, or one NOT YET ACCEPTED (`details[{field:\"status\", code:\"not_accepted\"}]`: decline it) — and `order_has_active_return`. Kill switch: `writes_enabled`. `503 role_unavailable` from a SERVER_ROLE=seller-api server, as `decline`.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** | Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. |  |
| **idempotencyKey** | **string** | 1–255 chars. Scope &#x3D; this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ &#x60;400 invalid_body&#x60; with &#x60;details[{field:\&quot;Idempotency-Key\&quot;,code:\&quot;required\&quot;}]&#x60;. |  |
| **declineRequest** | [**DeclineRequest**](DeclineRequest.md) |  |  |
| **donaDryRun** | **string** | &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. Only the literal &#x60;true&#x60; / &#x60;false&#x60;; any other value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Dry-Run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). | [optional]  |
| **dryRun** | **string** | Alias of the &#x60;Dona-Dry-Run&#x60; header. Only the literal strings &#x60;true&#x60; / &#x60;false&#x60; — &#x60;1&#x60;, &#x60;0&#x60;, &#x60;TRUE&#x60;, &#x60;yes&#x60;, an empty value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;dry_run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). A string enum, not a boolean, so no SDK generator serialises it as &#x60;1&#x60;/&#x60;0&#x60;. | [optional]  |
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |
| **donaSeller** | **Guid** | Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional]  |
| **xDonaIntegration** | **string** | &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional]  |

### Return type

[**OrderTransition**](OrderTransition.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Dona-Request-Id -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * X-Dona-Key-Expires -  <br>  * Dona-API-Warn -  <br>  * Deprecation -  <br>  * Sunset -  <br>  * Cache-Control -  <br>  |
| **400** | &#x60;invalid_body&#x60; — malformed JSON, a missing &#x60;Idempotency-Key&#x60;, validation (&#x60;details[]&#x60; carries field codes such as &#x60;ikpu_required&#x60;, &#x60;cursor_expired&#x60;), a &#x60;dry_run&#x60; / &#x60;Dona-Dry-Run&#x60; that is not the literal &#x60;true&#x60;/&#x60;false&#x60; (&#x60;details[{field, code:\&quot;invalid\&quot;}]&#x60;, C51), a vendor-app install key without &#x60;Dona-Seller&#x60; (&#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;, S6) or with a repeated / non-canonical one (&#x60;code:\&quot;invalid\&quot;&#x60;), or an op-specific 400 (&#x60;invalid_decline_reason&#x60;). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **401** | &#x60;api_key_malformed&#x60; (checksum fails — refused before any DB read) · &#x60;api_key_expired&#x60; (+&#x60;rotate_url&#x60;, no grace) · &#x60;api_key_revoked&#x60; (also a vendor-app key whose install was uninstalled — S6) · &#x60;key_kind_not_accepted&#x60; (an agent key &#x60;ak&#x60; on this tree) · &#x60;use_authorization_header&#x60; (&#x60;X-Api-Key&#x60; or a query-string key) · a seller/app/staff JWT on this tree. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **403** | &#x60;insufficient_scope&#x60; (+&#x60;required_scope&#x60;; also a scope in &#x60;disabled_scopes&#x60;) · &#x60;tier_required&#x60; (+&#x60;scope&#x60;; derived on every request; also a key minted for a third-party &#x60;orders:pii&#x60; recipient — &#x60;details[pii_recipient: pii_third_party_pending_counsel]&#x60;, D7, C59) · &#x60;key_suspended&#x60; (+&#x60;suspended_until&#x60;, &#x60;Retry-After&#x60;, &#x60;Dona-Rate-Limited-Reason: suspended&#x60;) · &#x60;api_blocked&#x60; · &#x60;ip_not_allowed&#x60; (judged on the trusted client IP only) · &#x60;seller_not_approved&#x60; (shop closed/blocked/suspended/restricted) · &#x60;not_a_seller&#x60; (never on this tree; the portal&#39;s owner doors) · &#x60;app_frozen&#x60; (S6: every key of a frozen vendor app, from the next request) · &#x60;agreement_required&#x60; (+&#x60;accept_url&#x60;: the shop owner has not accepted the CURRENT Annex 2 «API and automated access» — the version in force or, while none is, the earliest announced; accepted once in Settings › API, then every door admits the key again. Checked after the sanctions, before the scopes). |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |
| **404** | &#x60;not_found&#x60; — every missing OR foreign id (never 403: no existence oracle). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **409** | &#x60;idempotency_in_progress&#x60; (+&#x60;Retry-After: 2&#x60;) · &#x60;idempotency_mismatch&#x60; · &#x60;version_conflict&#x60; · &#x60;ai_review_open&#x60; (publish of a product whose Dona AI review case is open — the review decides its status) · order codes &#x60;order_not_acceptable&#x60;, &#x60;no_pickup_address&#x60;, &#x60;order_not_shippable&#x60;, &#x60;order_awaiting_courier&#x60;, &#x60;order_not_cancellable&#x60;, &#x60;order_has_active_return&#x60; · document codes &#x60;no_tracking_number&#x60; (+&#x60;orders&#x60;), &#x60;no_items_selected&#x60;, &#x60;all_items_delayed&#x60; (S4, C53) · a replay of a rejected held write. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Cache-Control -  <br>  |
| **429** | &#x60;rate_limited&#x60; (with &#x60;Dona-Rate-Limited-Reason: app-rate&#x60;: a vendor app&#39;s bucket, shared by all its installs — S6) · &#x60;write_rate_limited&#x60; · &#x60;concurrency_limited&#x60; · &#x60;seller_rate_limited&#x60; · &#x60;object_cooldown&#x60; · &#x60;api_busy&#x60;. Always a JSON body + &#x60;Retry-After&#x60; from the origin (an edge 429 from Cloudflare has NO body — treat it as &#x60;Retry-After: 60&#x60;). Costs 0 and never counts toward the breaker. &#x60;rate_limited&#x60; is also the pre-auth ADDRESS guard, answered before the key is read: an address over 1 200 requests a minute that were not admitted (no key, a public route, a malformed, unknown or refused key — admitted requests never count), or one tarpitted at 60/min for 15 min after ≥ 20 unknown keys in a minute. No key is ever suspended by traffic that did not prove it. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * Cache-Control -  <br>  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **503** | &#x60;auth_unavailable&#x60; (key lookup failed — fail closed) · &#x60;limits_unavailable&#x60; (limiter blind on a write/MCP call, or a kill switch is off: &#x60;enabled&#x60;, &#x60;writes_enabled&#x60;, &#x60;webhooks_enabled&#x60;; &#x60;Retry-After: 30&#x60;) · &#x60;attention_busy&#x60; (an acknowledgement that resolves an item could not take the attention writer lock within 2 s — nothing was written; retry after &#x60;Retry-After: 2&#x60;) · &#x60;wallet_unavailable&#x60; (&#x60;/finance/_*&#x60;: the wallet could not answer for the shop; &#x60;Retry-After: 30&#x60;; its body is never relayed or error-copied — S4, C57) · &#x60;role_unavailable&#x60; (+ &#x60;served_by: \&quot;marketplace\&quot;&#x60;: a SERVER_ROLE&#x3D;seller-api server does not serve decline / cancel or &#x60;/finance/_*&#x60;; answered before any read or write, nothing changed; no &#x60;Retry-After&#x60; — D3). Costs 0. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="declineorder"></a>
# **DeclineOrder**
> OrderTransition DeclineOrder (Guid id, string idempotencyKey, DeclineRequest declineRequest, string donaDryRun = null, string dryRun = null, string acceptLanguage = null, Guid donaSeller = null, string xDonaIntegration = null)

Decline (before acceptance) — money-reversing

An order NOT YET ACCEPTED. The portal decline's own body (`order.DeclineOrderInTx`) on the marketplace pool, in the write pipeline (stamped transaction, wallet-cutover fence): restock, the buyer's kiwi/vouchers/delivery money back, the `declined`/`seller` timeline row; the card refund at the provider and the buyer notice run after the commit (never on a dry run). The reason is stored in `decline_reason_code`. ADVANCED, derived on THIS request (a documents-waived or downgraded shop is `403 tier_required`). 400 `invalid_decline_reason` (`details[comment: required]` for `other` without words); 409 `order_not_acceptable` (an accepted or closed order — the portal names it `order_not_decidable`; cancel an accepted one), `order_has_active_return`. Another shop's order ⇒ `404`. Kill switch: `writes_enabled`. Served by the marketplace process only: a SERVER_ROLE=seller-api server answers `503 role_unavailable` (after the key, scope and tier; before the dry-run flag, the switch, the body and the idempotency claim — nothing changes; D3).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** | Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. |  |
| **idempotencyKey** | **string** | 1–255 chars. Scope &#x3D; this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ &#x60;400 invalid_body&#x60; with &#x60;details[{field:\&quot;Idempotency-Key\&quot;,code:\&quot;required\&quot;}]&#x60;. |  |
| **declineRequest** | [**DeclineRequest**](DeclineRequest.md) |  |  |
| **donaDryRun** | **string** | &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. Only the literal &#x60;true&#x60; / &#x60;false&#x60;; any other value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Dry-Run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). | [optional]  |
| **dryRun** | **string** | Alias of the &#x60;Dona-Dry-Run&#x60; header. Only the literal strings &#x60;true&#x60; / &#x60;false&#x60; — &#x60;1&#x60;, &#x60;0&#x60;, &#x60;TRUE&#x60;, &#x60;yes&#x60;, an empty value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;dry_run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). A string enum, not a boolean, so no SDK generator serialises it as &#x60;1&#x60;/&#x60;0&#x60;. | [optional]  |
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |
| **donaSeller** | **Guid** | Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional]  |
| **xDonaIntegration** | **string** | &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional]  |

### Return type

[**OrderTransition**](OrderTransition.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Dona-Request-Id -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * X-Dona-Key-Expires -  <br>  * Dona-API-Warn -  <br>  * Deprecation -  <br>  * Sunset -  <br>  * Cache-Control -  <br>  |
| **400** | &#x60;invalid_body&#x60; — malformed JSON, a missing &#x60;Idempotency-Key&#x60;, validation (&#x60;details[]&#x60; carries field codes such as &#x60;ikpu_required&#x60;, &#x60;cursor_expired&#x60;), a &#x60;dry_run&#x60; / &#x60;Dona-Dry-Run&#x60; that is not the literal &#x60;true&#x60;/&#x60;false&#x60; (&#x60;details[{field, code:\&quot;invalid\&quot;}]&#x60;, C51), a vendor-app install key without &#x60;Dona-Seller&#x60; (&#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;, S6) or with a repeated / non-canonical one (&#x60;code:\&quot;invalid\&quot;&#x60;), or an op-specific 400 (&#x60;invalid_decline_reason&#x60;). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **401** | &#x60;api_key_malformed&#x60; (checksum fails — refused before any DB read) · &#x60;api_key_expired&#x60; (+&#x60;rotate_url&#x60;, no grace) · &#x60;api_key_revoked&#x60; (also a vendor-app key whose install was uninstalled — S6) · &#x60;key_kind_not_accepted&#x60; (an agent key &#x60;ak&#x60; on this tree) · &#x60;use_authorization_header&#x60; (&#x60;X-Api-Key&#x60; or a query-string key) · a seller/app/staff JWT on this tree. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **403** | &#x60;insufficient_scope&#x60; (+&#x60;required_scope&#x60;; also a scope in &#x60;disabled_scopes&#x60;) · &#x60;tier_required&#x60; (+&#x60;scope&#x60;; derived on every request; also a key minted for a third-party &#x60;orders:pii&#x60; recipient — &#x60;details[pii_recipient: pii_third_party_pending_counsel]&#x60;, D7, C59) · &#x60;key_suspended&#x60; (+&#x60;suspended_until&#x60;, &#x60;Retry-After&#x60;, &#x60;Dona-Rate-Limited-Reason: suspended&#x60;) · &#x60;api_blocked&#x60; · &#x60;ip_not_allowed&#x60; (judged on the trusted client IP only) · &#x60;seller_not_approved&#x60; (shop closed/blocked/suspended/restricted) · &#x60;not_a_seller&#x60; (never on this tree; the portal&#39;s owner doors) · &#x60;app_frozen&#x60; (S6: every key of a frozen vendor app, from the next request) · &#x60;agreement_required&#x60; (+&#x60;accept_url&#x60;: the shop owner has not accepted the CURRENT Annex 2 «API and automated access» — the version in force or, while none is, the earliest announced; accepted once in Settings › API, then every door admits the key again. Checked after the sanctions, before the scopes). |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |
| **404** | &#x60;not_found&#x60; — every missing OR foreign id (never 403: no existence oracle). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **409** | &#x60;idempotency_in_progress&#x60; (+&#x60;Retry-After: 2&#x60;) · &#x60;idempotency_mismatch&#x60; · &#x60;version_conflict&#x60; · &#x60;ai_review_open&#x60; (publish of a product whose Dona AI review case is open — the review decides its status) · order codes &#x60;order_not_acceptable&#x60;, &#x60;no_pickup_address&#x60;, &#x60;order_not_shippable&#x60;, &#x60;order_awaiting_courier&#x60;, &#x60;order_not_cancellable&#x60;, &#x60;order_has_active_return&#x60; · document codes &#x60;no_tracking_number&#x60; (+&#x60;orders&#x60;), &#x60;no_items_selected&#x60;, &#x60;all_items_delayed&#x60; (S4, C53) · a replay of a rejected held write. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Cache-Control -  <br>  |
| **429** | &#x60;rate_limited&#x60; (with &#x60;Dona-Rate-Limited-Reason: app-rate&#x60;: a vendor app&#39;s bucket, shared by all its installs — S6) · &#x60;write_rate_limited&#x60; · &#x60;concurrency_limited&#x60; · &#x60;seller_rate_limited&#x60; · &#x60;object_cooldown&#x60; · &#x60;api_busy&#x60;. Always a JSON body + &#x60;Retry-After&#x60; from the origin (an edge 429 from Cloudflare has NO body — treat it as &#x60;Retry-After: 60&#x60;). Costs 0 and never counts toward the breaker. &#x60;rate_limited&#x60; is also the pre-auth ADDRESS guard, answered before the key is read: an address over 1 200 requests a minute that were not admitted (no key, a public route, a malformed, unknown or refused key — admitted requests never count), or one tarpitted at 60/min for 15 min after ≥ 20 unknown keys in a minute. No key is ever suspended by traffic that did not prove it. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * Cache-Control -  <br>  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **503** | &#x60;auth_unavailable&#x60; (key lookup failed — fail closed) · &#x60;limits_unavailable&#x60; (limiter blind on a write/MCP call, or a kill switch is off: &#x60;enabled&#x60;, &#x60;writes_enabled&#x60;, &#x60;webhooks_enabled&#x60;; &#x60;Retry-After: 30&#x60;) · &#x60;attention_busy&#x60; (an acknowledgement that resolves an item could not take the attention writer lock within 2 s — nothing was written; retry after &#x60;Retry-After: 2&#x60;) · &#x60;wallet_unavailable&#x60; (&#x60;/finance/_*&#x60;: the wallet could not answer for the shop; &#x60;Retry-After: 30&#x60;; its body is never relayed or error-copied — S4, C57) · &#x60;role_unavailable&#x60; (+ &#x60;served_by: \&quot;marketplace\&quot;&#x60;: a SERVER_ROLE&#x3D;seller-api server does not serve decline / cancel or &#x60;/finance/_*&#x60;; answered before any read or write, nothing changed; no &#x60;Retry-After&#x60; — D3). Costs 0. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getorder"></a>
# **GetOrder**
> GetOrder200Response GetOrder (Guid id, string acceptLanguage = null, Guid donaSeller = null, string xDonaIntegration = null)

Get an order (PII only with orders:pii)

`orders:read` ⇒ `Order`. A key that ALSO holds `orders:pii` (ADVANCED, `sk` only, S4) gets `OrderWithPii` (adds `recipient`) and the call is logged `pii=true`. When the `orders:pii` door would refuse this request (the shop is not ADVANCED now, or the key's recipient is third-party — D7) the ORDER is still answered, without `recipient`, and `Dona-API-Warn: recipient withheld: <tier_required|pii_third_party_pending_counsel|…>` says why (C59).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** | Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. |  |
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |
| **donaSeller** | **Guid** | Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional]  |
| **xDonaIntegration** | **string** | &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional]  |

### Return type

[**GetOrder200Response**](GetOrder200Response.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Dona-Request-Id -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * X-Dona-Key-Expires -  <br>  * Dona-API-Warn -  <br>  * Deprecation -  <br>  * Sunset -  <br>  * Cache-Control -  <br>  |
| **401** | &#x60;api_key_malformed&#x60; (checksum fails — refused before any DB read) · &#x60;api_key_expired&#x60; (+&#x60;rotate_url&#x60;, no grace) · &#x60;api_key_revoked&#x60; (also a vendor-app key whose install was uninstalled — S6) · &#x60;key_kind_not_accepted&#x60; (an agent key &#x60;ak&#x60; on this tree) · &#x60;use_authorization_header&#x60; (&#x60;X-Api-Key&#x60; or a query-string key) · a seller/app/staff JWT on this tree. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **403** | &#x60;insufficient_scope&#x60; (+&#x60;required_scope&#x60;; also a scope in &#x60;disabled_scopes&#x60;) · &#x60;tier_required&#x60; (+&#x60;scope&#x60;; derived on every request; also a key minted for a third-party &#x60;orders:pii&#x60; recipient — &#x60;details[pii_recipient: pii_third_party_pending_counsel]&#x60;, D7, C59) · &#x60;key_suspended&#x60; (+&#x60;suspended_until&#x60;, &#x60;Retry-After&#x60;, &#x60;Dona-Rate-Limited-Reason: suspended&#x60;) · &#x60;api_blocked&#x60; · &#x60;ip_not_allowed&#x60; (judged on the trusted client IP only) · &#x60;seller_not_approved&#x60; (shop closed/blocked/suspended/restricted) · &#x60;not_a_seller&#x60; (never on this tree; the portal&#39;s owner doors) · &#x60;app_frozen&#x60; (S6: every key of a frozen vendor app, from the next request) · &#x60;agreement_required&#x60; (+&#x60;accept_url&#x60;: the shop owner has not accepted the CURRENT Annex 2 «API and automated access» — the version in force or, while none is, the earliest announced; accepted once in Settings › API, then every door admits the key again. Checked after the sanctions, before the scopes). |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |
| **404** | &#x60;not_found&#x60; — every missing OR foreign id (never 403: no existence oracle). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **429** | &#x60;rate_limited&#x60; (with &#x60;Dona-Rate-Limited-Reason: app-rate&#x60;: a vendor app&#39;s bucket, shared by all its installs — S6) · &#x60;write_rate_limited&#x60; · &#x60;concurrency_limited&#x60; · &#x60;seller_rate_limited&#x60; · &#x60;object_cooldown&#x60; · &#x60;api_busy&#x60;. Always a JSON body + &#x60;Retry-After&#x60; from the origin (an edge 429 from Cloudflare has NO body — treat it as &#x60;Retry-After: 60&#x60;). Costs 0 and never counts toward the breaker. &#x60;rate_limited&#x60; is also the pre-auth ADDRESS guard, answered before the key is read: an address over 1 200 requests a minute that were not admitted (no key, a public route, a malformed, unknown or refused key — admitted requests never count), or one tarpitted at 60/min for 15 min after ≥ 20 unknown keys in a minute. No key is ever suspended by traffic that did not prove it. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * Cache-Control -  <br>  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **503** | &#x60;auth_unavailable&#x60; (key lookup failed — fail closed) · &#x60;limits_unavailable&#x60; (limiter blind on a write/MCP call, or a kill switch is off: &#x60;enabled&#x60;, &#x60;writes_enabled&#x60;, &#x60;webhooks_enabled&#x60;; &#x60;Retry-After: 30&#x60;) · &#x60;attention_busy&#x60; (an acknowledgement that resolves an item could not take the attention writer lock within 2 s — nothing was written; retry after &#x60;Retry-After: 2&#x60;) · &#x60;wallet_unavailable&#x60; (&#x60;/finance/_*&#x60;: the wallet could not answer for the shop; &#x60;Retry-After: 30&#x60;; its body is never relayed or error-copied — S4, C57) · &#x60;role_unavailable&#x60; (+ &#x60;served_by: \&quot;marketplace\&quot;&#x60;: a SERVER_ROLE&#x3D;seller-api server does not serve decline / cancel or &#x60;/finance/_*&#x60;; answered before any read or write, nothing changed; no &#x60;Retry-After&#x60; — D3). Costs 0. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getorderinvoice"></a>
# **GetOrderInvoice**
> string GetOrderInvoice (Guid id, string acceptLanguage = null, Guid donaSeller = null, string xDonaIntegration = null)

Invoice (PDF, contains PII)

The invoice for one order, drawn as a PDF from the SAME figures as the portal's invoice page (one loader). Doors, 409s and the `429 api_busy` bound as `label.pdf` (C53, C54). ⚠ PII set WIDER than the label's: like the portal's invoice it prints the PURCHASER's account name and phone (the buyer who is invoiced) — on a gift order that is not the recipient the label and the `recipient` block name (Form A Q12 states both).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** | Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. |  |
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |
| **donaSeller** | **Guid** | Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional]  |
| **xDonaIntegration** | **string** | &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional]  |

### Return type

**string**

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Dona-Request-Id -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * X-Dona-Key-Expires -  <br>  * Dona-API-Warn -  <br>  * Deprecation -  <br>  * Sunset -  <br>  * Cache-Control -  <br>  |
| **401** | &#x60;api_key_malformed&#x60; (checksum fails — refused before any DB read) · &#x60;api_key_expired&#x60; (+&#x60;rotate_url&#x60;, no grace) · &#x60;api_key_revoked&#x60; (also a vendor-app key whose install was uninstalled — S6) · &#x60;key_kind_not_accepted&#x60; (an agent key &#x60;ak&#x60; on this tree) · &#x60;use_authorization_header&#x60; (&#x60;X-Api-Key&#x60; or a query-string key) · a seller/app/staff JWT on this tree. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **403** | &#x60;insufficient_scope&#x60; (+&#x60;required_scope&#x60;; also a scope in &#x60;disabled_scopes&#x60;) · &#x60;tier_required&#x60; (+&#x60;scope&#x60;; derived on every request; also a key minted for a third-party &#x60;orders:pii&#x60; recipient — &#x60;details[pii_recipient: pii_third_party_pending_counsel]&#x60;, D7, C59) · &#x60;key_suspended&#x60; (+&#x60;suspended_until&#x60;, &#x60;Retry-After&#x60;, &#x60;Dona-Rate-Limited-Reason: suspended&#x60;) · &#x60;api_blocked&#x60; · &#x60;ip_not_allowed&#x60; (judged on the trusted client IP only) · &#x60;seller_not_approved&#x60; (shop closed/blocked/suspended/restricted) · &#x60;not_a_seller&#x60; (never on this tree; the portal&#39;s owner doors) · &#x60;app_frozen&#x60; (S6: every key of a frozen vendor app, from the next request) · &#x60;agreement_required&#x60; (+&#x60;accept_url&#x60;: the shop owner has not accepted the CURRENT Annex 2 «API and automated access» — the version in force or, while none is, the earliest announced; accepted once in Settings › API, then every door admits the key again. Checked after the sanctions, before the scopes). |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |
| **404** | &#x60;not_found&#x60; — every missing OR foreign id (never 403: no existence oracle). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **409** | &#x60;idempotency_in_progress&#x60; (+&#x60;Retry-After: 2&#x60;) · &#x60;idempotency_mismatch&#x60; · &#x60;version_conflict&#x60; · &#x60;ai_review_open&#x60; (publish of a product whose Dona AI review case is open — the review decides its status) · order codes &#x60;order_not_acceptable&#x60;, &#x60;no_pickup_address&#x60;, &#x60;order_not_shippable&#x60;, &#x60;order_awaiting_courier&#x60;, &#x60;order_not_cancellable&#x60;, &#x60;order_has_active_return&#x60; · document codes &#x60;no_tracking_number&#x60; (+&#x60;orders&#x60;), &#x60;no_items_selected&#x60;, &#x60;all_items_delayed&#x60; (S4, C53) · a replay of a rejected held write. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Cache-Control -  <br>  |
| **429** | &#x60;rate_limited&#x60; (with &#x60;Dona-Rate-Limited-Reason: app-rate&#x60;: a vendor app&#39;s bucket, shared by all its installs — S6) · &#x60;write_rate_limited&#x60; · &#x60;concurrency_limited&#x60; · &#x60;seller_rate_limited&#x60; · &#x60;object_cooldown&#x60; · &#x60;api_busy&#x60;. Always a JSON body + &#x60;Retry-After&#x60; from the origin (an edge 429 from Cloudflare has NO body — treat it as &#x60;Retry-After: 60&#x60;). Costs 0 and never counts toward the breaker. &#x60;rate_limited&#x60; is also the pre-auth ADDRESS guard, answered before the key is read: an address over 1 200 requests a minute that were not admitted (no key, a public route, a malformed, unknown or refused key — admitted requests never count), or one tarpitted at 60/min for 15 min after ≥ 20 unknown keys in a minute. No key is ever suspended by traffic that did not prove it. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * Cache-Control -  <br>  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **503** | &#x60;auth_unavailable&#x60; (key lookup failed — fail closed) · &#x60;limits_unavailable&#x60; (limiter blind on a write/MCP call, or a kill switch is off: &#x60;enabled&#x60;, &#x60;writes_enabled&#x60;, &#x60;webhooks_enabled&#x60;; &#x60;Retry-After: 30&#x60;) · &#x60;attention_busy&#x60; (an acknowledgement that resolves an item could not take the attention writer lock within 2 s — nothing was written; retry after &#x60;Retry-After: 2&#x60;) · &#x60;wallet_unavailable&#x60; (&#x60;/finance/_*&#x60;: the wallet could not answer for the shop; &#x60;Retry-After: 30&#x60;; its body is never relayed or error-copied — S4, C57) · &#x60;role_unavailable&#x60; (+ &#x60;served_by: \&quot;marketplace\&quot;&#x60;: a SERVER_ROLE&#x3D;seller-api server does not serve decline / cancel or &#x60;/finance/_*&#x60;; answered before any read or write, nothing changed; no &#x60;Retry-After&#x60; — D3). Costs 0. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getorderlabel"></a>
# **GetOrderLabel**
> string GetOrderLabel (Guid id, string acceptLanguage = null, Guid donaSeller = null, string xDonaIntegration = null)

Shipping label (PDF, contains PII)

The portal's sticker for one order: prints the buyer's name, phone and address. `sk` keys only (`orders:pii` on any other kind ⇒ `403 insufficient_scope` + `details[scope_not_allowed_for_kind]`); ADVANCED now (`403 tier_required`); a key minted for a THIRD-PARTY recipient ⇒ `403 tier_required` + `details[pii_recipient: pii_third_party_pending_counsel]` (D7). Logged `pii=true` (always journaled, never sampled); never stored by the API. Normal key-rate bucket (C54). 409 `no_tracking_number` (+ `orders`: the order codes without a carrier number yet — print later), `no_items_selected`, `all_items_delayed` (nothing left to put in the parcel) (C53). A server draws at most 2 documents at once: past that `429 api_busy` (`Dona-Rate-Limited-Reason: global`, `Retry-After: 2`) before any read, and a batch is not charged.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** | Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. |  |
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |
| **donaSeller** | **Guid** | Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional]  |
| **xDonaIntegration** | **string** | &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional]  |

### Return type

**string**

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Dona-Request-Id -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * X-Dona-Key-Expires -  <br>  * Dona-API-Warn -  <br>  * Deprecation -  <br>  * Sunset -  <br>  * Cache-Control -  <br>  |
| **401** | &#x60;api_key_malformed&#x60; (checksum fails — refused before any DB read) · &#x60;api_key_expired&#x60; (+&#x60;rotate_url&#x60;, no grace) · &#x60;api_key_revoked&#x60; (also a vendor-app key whose install was uninstalled — S6) · &#x60;key_kind_not_accepted&#x60; (an agent key &#x60;ak&#x60; on this tree) · &#x60;use_authorization_header&#x60; (&#x60;X-Api-Key&#x60; or a query-string key) · a seller/app/staff JWT on this tree. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **403** | &#x60;insufficient_scope&#x60; (+&#x60;required_scope&#x60;; also a scope in &#x60;disabled_scopes&#x60;) · &#x60;tier_required&#x60; (+&#x60;scope&#x60;; derived on every request; also a key minted for a third-party &#x60;orders:pii&#x60; recipient — &#x60;details[pii_recipient: pii_third_party_pending_counsel]&#x60;, D7, C59) · &#x60;key_suspended&#x60; (+&#x60;suspended_until&#x60;, &#x60;Retry-After&#x60;, &#x60;Dona-Rate-Limited-Reason: suspended&#x60;) · &#x60;api_blocked&#x60; · &#x60;ip_not_allowed&#x60; (judged on the trusted client IP only) · &#x60;seller_not_approved&#x60; (shop closed/blocked/suspended/restricted) · &#x60;not_a_seller&#x60; (never on this tree; the portal&#39;s owner doors) · &#x60;app_frozen&#x60; (S6: every key of a frozen vendor app, from the next request) · &#x60;agreement_required&#x60; (+&#x60;accept_url&#x60;: the shop owner has not accepted the CURRENT Annex 2 «API and automated access» — the version in force or, while none is, the earliest announced; accepted once in Settings › API, then every door admits the key again. Checked after the sanctions, before the scopes). |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |
| **404** | &#x60;not_found&#x60; — every missing OR foreign id (never 403: no existence oracle). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **409** | &#x60;idempotency_in_progress&#x60; (+&#x60;Retry-After: 2&#x60;) · &#x60;idempotency_mismatch&#x60; · &#x60;version_conflict&#x60; · &#x60;ai_review_open&#x60; (publish of a product whose Dona AI review case is open — the review decides its status) · order codes &#x60;order_not_acceptable&#x60;, &#x60;no_pickup_address&#x60;, &#x60;order_not_shippable&#x60;, &#x60;order_awaiting_courier&#x60;, &#x60;order_not_cancellable&#x60;, &#x60;order_has_active_return&#x60; · document codes &#x60;no_tracking_number&#x60; (+&#x60;orders&#x60;), &#x60;no_items_selected&#x60;, &#x60;all_items_delayed&#x60; (S4, C53) · a replay of a rejected held write. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Cache-Control -  <br>  |
| **429** | &#x60;rate_limited&#x60; (with &#x60;Dona-Rate-Limited-Reason: app-rate&#x60;: a vendor app&#39;s bucket, shared by all its installs — S6) · &#x60;write_rate_limited&#x60; · &#x60;concurrency_limited&#x60; · &#x60;seller_rate_limited&#x60; · &#x60;object_cooldown&#x60; · &#x60;api_busy&#x60;. Always a JSON body + &#x60;Retry-After&#x60; from the origin (an edge 429 from Cloudflare has NO body — treat it as &#x60;Retry-After: 60&#x60;). Costs 0 and never counts toward the breaker. &#x60;rate_limited&#x60; is also the pre-auth ADDRESS guard, answered before the key is read: an address over 1 200 requests a minute that were not admitted (no key, a public route, a malformed, unknown or refused key — admitted requests never count), or one tarpitted at 60/min for 15 min after ≥ 20 unknown keys in a minute. No key is ever suspended by traffic that did not prove it. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * Cache-Control -  <br>  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **503** | &#x60;auth_unavailable&#x60; (key lookup failed — fail closed) · &#x60;limits_unavailable&#x60; (limiter blind on a write/MCP call, or a kill switch is off: &#x60;enabled&#x60;, &#x60;writes_enabled&#x60;, &#x60;webhooks_enabled&#x60;; &#x60;Retry-After: 30&#x60;) · &#x60;attention_busy&#x60; (an acknowledgement that resolves an item could not take the attention writer lock within 2 s — nothing was written; retry after &#x60;Retry-After: 2&#x60;) · &#x60;wallet_unavailable&#x60; (&#x60;/finance/_*&#x60;: the wallet could not answer for the shop; &#x60;Retry-After: 30&#x60;; its body is never relayed or error-copied — S4, C57) · &#x60;role_unavailable&#x60; (+ &#x60;served_by: \&quot;marketplace\&quot;&#x60;: a SERVER_ROLE&#x3D;seller-api server does not serve decline / cancel or &#x60;/finance/_*&#x60;; answered before any read or write, nothing changed; no &#x60;Retry-After&#x60; — D3). Costs 0. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getordertimeline"></a>
# **GetOrderTimeline**
> OrderTimeline GetOrderTimeline (Guid id, string acceptLanguage = null, Guid donaSeller = null, string xDonaIntegration = null)

Order timeline

`order_events` in order.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** | Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. |  |
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |
| **donaSeller** | **Guid** | Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional]  |
| **xDonaIntegration** | **string** | &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional]  |

### Return type

[**OrderTimeline**](OrderTimeline.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Dona-Request-Id -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * X-Dona-Key-Expires -  <br>  * Dona-API-Warn -  <br>  * Deprecation -  <br>  * Sunset -  <br>  * Cache-Control -  <br>  |
| **401** | &#x60;api_key_malformed&#x60; (checksum fails — refused before any DB read) · &#x60;api_key_expired&#x60; (+&#x60;rotate_url&#x60;, no grace) · &#x60;api_key_revoked&#x60; (also a vendor-app key whose install was uninstalled — S6) · &#x60;key_kind_not_accepted&#x60; (an agent key &#x60;ak&#x60; on this tree) · &#x60;use_authorization_header&#x60; (&#x60;X-Api-Key&#x60; or a query-string key) · a seller/app/staff JWT on this tree. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **403** | &#x60;insufficient_scope&#x60; (+&#x60;required_scope&#x60;; also a scope in &#x60;disabled_scopes&#x60;) · &#x60;tier_required&#x60; (+&#x60;scope&#x60;; derived on every request; also a key minted for a third-party &#x60;orders:pii&#x60; recipient — &#x60;details[pii_recipient: pii_third_party_pending_counsel]&#x60;, D7, C59) · &#x60;key_suspended&#x60; (+&#x60;suspended_until&#x60;, &#x60;Retry-After&#x60;, &#x60;Dona-Rate-Limited-Reason: suspended&#x60;) · &#x60;api_blocked&#x60; · &#x60;ip_not_allowed&#x60; (judged on the trusted client IP only) · &#x60;seller_not_approved&#x60; (shop closed/blocked/suspended/restricted) · &#x60;not_a_seller&#x60; (never on this tree; the portal&#39;s owner doors) · &#x60;app_frozen&#x60; (S6: every key of a frozen vendor app, from the next request) · &#x60;agreement_required&#x60; (+&#x60;accept_url&#x60;: the shop owner has not accepted the CURRENT Annex 2 «API and automated access» — the version in force or, while none is, the earliest announced; accepted once in Settings › API, then every door admits the key again. Checked after the sanctions, before the scopes). |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |
| **404** | &#x60;not_found&#x60; — every missing OR foreign id (never 403: no existence oracle). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **429** | &#x60;rate_limited&#x60; (with &#x60;Dona-Rate-Limited-Reason: app-rate&#x60;: a vendor app&#39;s bucket, shared by all its installs — S6) · &#x60;write_rate_limited&#x60; · &#x60;concurrency_limited&#x60; · &#x60;seller_rate_limited&#x60; · &#x60;object_cooldown&#x60; · &#x60;api_busy&#x60;. Always a JSON body + &#x60;Retry-After&#x60; from the origin (an edge 429 from Cloudflare has NO body — treat it as &#x60;Retry-After: 60&#x60;). Costs 0 and never counts toward the breaker. &#x60;rate_limited&#x60; is also the pre-auth ADDRESS guard, answered before the key is read: an address over 1 200 requests a minute that were not admitted (no key, a public route, a malformed, unknown or refused key — admitted requests never count), or one tarpitted at 60/min for 15 min after ≥ 20 unknown keys in a minute. No key is ever suspended by traffic that did not prove it. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * Cache-Control -  <br>  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **503** | &#x60;auth_unavailable&#x60; (key lookup failed — fail closed) · &#x60;limits_unavailable&#x60; (limiter blind on a write/MCP call, or a kill switch is off: &#x60;enabled&#x60;, &#x60;writes_enabled&#x60;, &#x60;webhooks_enabled&#x60;; &#x60;Retry-After: 30&#x60;) · &#x60;attention_busy&#x60; (an acknowledgement that resolves an item could not take the attention writer lock within 2 s — nothing was written; retry after &#x60;Retry-After: 2&#x60;) · &#x60;wallet_unavailable&#x60; (&#x60;/finance/_*&#x60;: the wallet could not answer for the shop; &#x60;Retry-After: 30&#x60;; its body is never relayed or error-copied — S4, C57) · &#x60;role_unavailable&#x60; (+ &#x60;served_by: \&quot;marketplace\&quot;&#x60;: a SERVER_ROLE&#x3D;seller-api server does not serve decline / cancel or &#x60;/finance/_*&#x60;; answered before any read or write, nothing changed; no &#x60;Retry-After&#x60; — D3). Costs 0. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="handoverorder"></a>
# **HandoverOrder**
> OrderTransition HandoverOrder (Guid id, string idempotencyKey, string donaDryRun = null, string dryRun = null, string acceptLanguage = null, Guid donaSeller = null, string xDonaIntegration = null)

Hand over to the courier

`sellerMayTransitionSQL` rules. 409: `order_not_shippable`. Kill switch: `writes_enabled`.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** | Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. |  |
| **idempotencyKey** | **string** | 1–255 chars. Scope &#x3D; this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ &#x60;400 invalid_body&#x60; with &#x60;details[{field:\&quot;Idempotency-Key\&quot;,code:\&quot;required\&quot;}]&#x60;. |  |
| **donaDryRun** | **string** | &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. Only the literal &#x60;true&#x60; / &#x60;false&#x60;; any other value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Dry-Run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). | [optional]  |
| **dryRun** | **string** | Alias of the &#x60;Dona-Dry-Run&#x60; header. Only the literal strings &#x60;true&#x60; / &#x60;false&#x60; — &#x60;1&#x60;, &#x60;0&#x60;, &#x60;TRUE&#x60;, &#x60;yes&#x60;, an empty value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;dry_run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). A string enum, not a boolean, so no SDK generator serialises it as &#x60;1&#x60;/&#x60;0&#x60;. | [optional]  |
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |
| **donaSeller** | **Guid** | Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional]  |
| **xDonaIntegration** | **string** | &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional]  |

### Return type

[**OrderTransition**](OrderTransition.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Dona-Request-Id -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * X-Dona-Key-Expires -  <br>  * Dona-API-Warn -  <br>  * Deprecation -  <br>  * Sunset -  <br>  * Cache-Control -  <br>  |
| **400** | &#x60;invalid_body&#x60; — malformed JSON, a missing &#x60;Idempotency-Key&#x60;, validation (&#x60;details[]&#x60; carries field codes such as &#x60;ikpu_required&#x60;, &#x60;cursor_expired&#x60;), a &#x60;dry_run&#x60; / &#x60;Dona-Dry-Run&#x60; that is not the literal &#x60;true&#x60;/&#x60;false&#x60; (&#x60;details[{field, code:\&quot;invalid\&quot;}]&#x60;, C51), a vendor-app install key without &#x60;Dona-Seller&#x60; (&#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;, S6) or with a repeated / non-canonical one (&#x60;code:\&quot;invalid\&quot;&#x60;), or an op-specific 400 (&#x60;invalid_decline_reason&#x60;). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **401** | &#x60;api_key_malformed&#x60; (checksum fails — refused before any DB read) · &#x60;api_key_expired&#x60; (+&#x60;rotate_url&#x60;, no grace) · &#x60;api_key_revoked&#x60; (also a vendor-app key whose install was uninstalled — S6) · &#x60;key_kind_not_accepted&#x60; (an agent key &#x60;ak&#x60; on this tree) · &#x60;use_authorization_header&#x60; (&#x60;X-Api-Key&#x60; or a query-string key) · a seller/app/staff JWT on this tree. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **403** | &#x60;insufficient_scope&#x60; (+&#x60;required_scope&#x60;; also a scope in &#x60;disabled_scopes&#x60;) · &#x60;tier_required&#x60; (+&#x60;scope&#x60;; derived on every request; also a key minted for a third-party &#x60;orders:pii&#x60; recipient — &#x60;details[pii_recipient: pii_third_party_pending_counsel]&#x60;, D7, C59) · &#x60;key_suspended&#x60; (+&#x60;suspended_until&#x60;, &#x60;Retry-After&#x60;, &#x60;Dona-Rate-Limited-Reason: suspended&#x60;) · &#x60;api_blocked&#x60; · &#x60;ip_not_allowed&#x60; (judged on the trusted client IP only) · &#x60;seller_not_approved&#x60; (shop closed/blocked/suspended/restricted) · &#x60;not_a_seller&#x60; (never on this tree; the portal&#39;s owner doors) · &#x60;app_frozen&#x60; (S6: every key of a frozen vendor app, from the next request) · &#x60;agreement_required&#x60; (+&#x60;accept_url&#x60;: the shop owner has not accepted the CURRENT Annex 2 «API and automated access» — the version in force or, while none is, the earliest announced; accepted once in Settings › API, then every door admits the key again. Checked after the sanctions, before the scopes). |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |
| **404** | &#x60;not_found&#x60; — every missing OR foreign id (never 403: no existence oracle). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **409** | &#x60;idempotency_in_progress&#x60; (+&#x60;Retry-After: 2&#x60;) · &#x60;idempotency_mismatch&#x60; · &#x60;version_conflict&#x60; · &#x60;ai_review_open&#x60; (publish of a product whose Dona AI review case is open — the review decides its status) · order codes &#x60;order_not_acceptable&#x60;, &#x60;no_pickup_address&#x60;, &#x60;order_not_shippable&#x60;, &#x60;order_awaiting_courier&#x60;, &#x60;order_not_cancellable&#x60;, &#x60;order_has_active_return&#x60; · document codes &#x60;no_tracking_number&#x60; (+&#x60;orders&#x60;), &#x60;no_items_selected&#x60;, &#x60;all_items_delayed&#x60; (S4, C53) · a replay of a rejected held write. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Cache-Control -  <br>  |
| **429** | &#x60;rate_limited&#x60; (with &#x60;Dona-Rate-Limited-Reason: app-rate&#x60;: a vendor app&#39;s bucket, shared by all its installs — S6) · &#x60;write_rate_limited&#x60; · &#x60;concurrency_limited&#x60; · &#x60;seller_rate_limited&#x60; · &#x60;object_cooldown&#x60; · &#x60;api_busy&#x60;. Always a JSON body + &#x60;Retry-After&#x60; from the origin (an edge 429 from Cloudflare has NO body — treat it as &#x60;Retry-After: 60&#x60;). Costs 0 and never counts toward the breaker. &#x60;rate_limited&#x60; is also the pre-auth ADDRESS guard, answered before the key is read: an address over 1 200 requests a minute that were not admitted (no key, a public route, a malformed, unknown or refused key — admitted requests never count), or one tarpitted at 60/min for 15 min after ≥ 20 unknown keys in a minute. No key is ever suspended by traffic that did not prove it. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * Cache-Control -  <br>  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **503** | &#x60;auth_unavailable&#x60; (key lookup failed — fail closed) · &#x60;limits_unavailable&#x60; (limiter blind on a write/MCP call, or a kill switch is off: &#x60;enabled&#x60;, &#x60;writes_enabled&#x60;, &#x60;webhooks_enabled&#x60;; &#x60;Retry-After: 30&#x60;) · &#x60;attention_busy&#x60; (an acknowledgement that resolves an item could not take the attention writer lock within 2 s — nothing was written; retry after &#x60;Retry-After: 2&#x60;) · &#x60;wallet_unavailable&#x60; (&#x60;/finance/_*&#x60;: the wallet could not answer for the shop; &#x60;Retry-After: 30&#x60;; its body is never relayed or error-copied — S4, C57) · &#x60;role_unavailable&#x60; (+ &#x60;served_by: \&quot;marketplace\&quot;&#x60;: a SERVER_ROLE&#x3D;seller-api server does not serve decline / cancel or &#x60;/finance/_*&#x60;; answered before any read or write, nothing changed; no &#x60;Retry-After&#x60; — D3). Costs 0. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="listorders"></a>
# **ListOrders**
> OrderPage ListOrders (string cursor = null, int page = null, int limit = null, string updatedSince = null, string status = null, string scheme = null, DateTimeOffset from = null, DateTimeOffset to = null, string acceptLanguage = null, Guid donaSeller = null, string xDonaIntegration = null)

List orders (no buyer PII)

The `orders:read` projection. `status` takes the portal buckets (`all`, `pending`, `paid`, `ready_to_ship`, `to_ship`, `shipped`, `delivered`, `cancelled`, `return_refund`). `from`/`to` span ≤ 90 d, `to` exclusive.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **cursor** | **string** | Opaque keyset cursor from &#x60;next_cursor&#x60;. | [optional]  |
| **page** | **int** | 0-based page alias (Uzum parity) — slower than &#x60;cursor&#x60;, ≤ 1 000 pages; mutually exclusive with &#x60;cursor&#x60;. | [optional]  |
| **limit** | **int** | Page size, default 50, max 100 (clamped, with &#x60;Dona-API-Warn&#x60;). &#x60;limit &gt; 50&#x60; costs &#x60;1 + ceil(limit/50)&#x60;. | [optional] [default to 50] |
| **updatedSince** | **string** | ISO 8601 with offset, or epoch milliseconds. The visible high-water mark is capped at &#x60;now() − 10 s&#x60; so a slow transaction is never skipped. | [optional]  |
| **status** | **string** | Portal bucket. | [optional]  |
| **scheme** | **string** | Derived fulfilment scheme. | [optional]  |
| **from** | **DateTimeOffset** | created_at ≥ from. | [optional]  |
| **to** | **DateTimeOffset** | created_at &lt; to. | [optional]  |
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |
| **donaSeller** | **Guid** | Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional]  |
| **xDonaIntegration** | **string** | &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional]  |

### Return type

[**OrderPage**](OrderPage.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Dona-Request-Id -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * X-Dona-Key-Expires -  <br>  * Dona-API-Warn -  <br>  * Deprecation -  <br>  * Sunset -  <br>  * Cache-Control -  <br>  |
| **400** | &#x60;invalid_body&#x60; — malformed JSON, a missing &#x60;Idempotency-Key&#x60;, validation (&#x60;details[]&#x60; carries field codes such as &#x60;ikpu_required&#x60;, &#x60;cursor_expired&#x60;), a &#x60;dry_run&#x60; / &#x60;Dona-Dry-Run&#x60; that is not the literal &#x60;true&#x60;/&#x60;false&#x60; (&#x60;details[{field, code:\&quot;invalid\&quot;}]&#x60;, C51), a vendor-app install key without &#x60;Dona-Seller&#x60; (&#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;, S6) or with a repeated / non-canonical one (&#x60;code:\&quot;invalid\&quot;&#x60;), or an op-specific 400 (&#x60;invalid_decline_reason&#x60;). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **401** | &#x60;api_key_malformed&#x60; (checksum fails — refused before any DB read) · &#x60;api_key_expired&#x60; (+&#x60;rotate_url&#x60;, no grace) · &#x60;api_key_revoked&#x60; (also a vendor-app key whose install was uninstalled — S6) · &#x60;key_kind_not_accepted&#x60; (an agent key &#x60;ak&#x60; on this tree) · &#x60;use_authorization_header&#x60; (&#x60;X-Api-Key&#x60; or a query-string key) · a seller/app/staff JWT on this tree. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **403** | &#x60;insufficient_scope&#x60; (+&#x60;required_scope&#x60;; also a scope in &#x60;disabled_scopes&#x60;) · &#x60;tier_required&#x60; (+&#x60;scope&#x60;; derived on every request; also a key minted for a third-party &#x60;orders:pii&#x60; recipient — &#x60;details[pii_recipient: pii_third_party_pending_counsel]&#x60;, D7, C59) · &#x60;key_suspended&#x60; (+&#x60;suspended_until&#x60;, &#x60;Retry-After&#x60;, &#x60;Dona-Rate-Limited-Reason: suspended&#x60;) · &#x60;api_blocked&#x60; · &#x60;ip_not_allowed&#x60; (judged on the trusted client IP only) · &#x60;seller_not_approved&#x60; (shop closed/blocked/suspended/restricted) · &#x60;not_a_seller&#x60; (never on this tree; the portal&#39;s owner doors) · &#x60;app_frozen&#x60; (S6: every key of a frozen vendor app, from the next request) · &#x60;agreement_required&#x60; (+&#x60;accept_url&#x60;: the shop owner has not accepted the CURRENT Annex 2 «API and automated access» — the version in force or, while none is, the earliest announced; accepted once in Settings › API, then every door admits the key again. Checked after the sanctions, before the scopes). |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |
| **429** | &#x60;rate_limited&#x60; (with &#x60;Dona-Rate-Limited-Reason: app-rate&#x60;: a vendor app&#39;s bucket, shared by all its installs — S6) · &#x60;write_rate_limited&#x60; · &#x60;concurrency_limited&#x60; · &#x60;seller_rate_limited&#x60; · &#x60;object_cooldown&#x60; · &#x60;api_busy&#x60;. Always a JSON body + &#x60;Retry-After&#x60; from the origin (an edge 429 from Cloudflare has NO body — treat it as &#x60;Retry-After: 60&#x60;). Costs 0 and never counts toward the breaker. &#x60;rate_limited&#x60; is also the pre-auth ADDRESS guard, answered before the key is read: an address over 1 200 requests a minute that were not admitted (no key, a public route, a malformed, unknown or refused key — admitted requests never count), or one tarpitted at 60/min for 15 min after ≥ 20 unknown keys in a minute. No key is ever suspended by traffic that did not prove it. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * Cache-Control -  <br>  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **503** | &#x60;auth_unavailable&#x60; (key lookup failed — fail closed) · &#x60;limits_unavailable&#x60; (limiter blind on a write/MCP call, or a kill switch is off: &#x60;enabled&#x60;, &#x60;writes_enabled&#x60;, &#x60;webhooks_enabled&#x60;; &#x60;Retry-After: 30&#x60;) · &#x60;attention_busy&#x60; (an acknowledgement that resolves an item could not take the attention writer lock within 2 s — nothing was written; retry after &#x60;Retry-After: 2&#x60;) · &#x60;wallet_unavailable&#x60; (&#x60;/finance/_*&#x60;: the wallet could not answer for the shop; &#x60;Retry-After: 30&#x60;; its body is never relayed or error-copied — S4, C57) · &#x60;role_unavailable&#x60; (+ &#x60;served_by: \&quot;marketplace\&quot;&#x60;: a SERVER_ROLE&#x3D;seller-api server does not serve decline / cancel or &#x60;/finance/_*&#x60;; answered before any read or write, nothing changed; no &#x60;Retry-After&#x60; — D3). Costs 0. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="markorderready"></a>
# **MarkOrderReady**
> OrderTransition MarkOrderReady (Guid id, string idempotencyKey, string donaDryRun = null, string dryRun = null, string acceptLanguage = null, Guid donaSeller = null, string xDonaIntegration = null)

Mark ready to ship

Sets `ready_to_ship`. 409: `order_not_shippable`. Kill switch: `writes_enabled`.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** | Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. |  |
| **idempotencyKey** | **string** | 1–255 chars. Scope &#x3D; this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ &#x60;400 invalid_body&#x60; with &#x60;details[{field:\&quot;Idempotency-Key\&quot;,code:\&quot;required\&quot;}]&#x60;. |  |
| **donaDryRun** | **string** | &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. Only the literal &#x60;true&#x60; / &#x60;false&#x60;; any other value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Dry-Run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). | [optional]  |
| **dryRun** | **string** | Alias of the &#x60;Dona-Dry-Run&#x60; header. Only the literal strings &#x60;true&#x60; / &#x60;false&#x60; — &#x60;1&#x60;, &#x60;0&#x60;, &#x60;TRUE&#x60;, &#x60;yes&#x60;, an empty value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;dry_run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). A string enum, not a boolean, so no SDK generator serialises it as &#x60;1&#x60;/&#x60;0&#x60;. | [optional]  |
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |
| **donaSeller** | **Guid** | Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional]  |
| **xDonaIntegration** | **string** | &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional]  |

### Return type

[**OrderTransition**](OrderTransition.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Dona-Request-Id -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * X-Dona-Key-Expires -  <br>  * Dona-API-Warn -  <br>  * Deprecation -  <br>  * Sunset -  <br>  * Cache-Control -  <br>  |
| **400** | &#x60;invalid_body&#x60; — malformed JSON, a missing &#x60;Idempotency-Key&#x60;, validation (&#x60;details[]&#x60; carries field codes such as &#x60;ikpu_required&#x60;, &#x60;cursor_expired&#x60;), a &#x60;dry_run&#x60; / &#x60;Dona-Dry-Run&#x60; that is not the literal &#x60;true&#x60;/&#x60;false&#x60; (&#x60;details[{field, code:\&quot;invalid\&quot;}]&#x60;, C51), a vendor-app install key without &#x60;Dona-Seller&#x60; (&#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;, S6) or with a repeated / non-canonical one (&#x60;code:\&quot;invalid\&quot;&#x60;), or an op-specific 400 (&#x60;invalid_decline_reason&#x60;). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **401** | &#x60;api_key_malformed&#x60; (checksum fails — refused before any DB read) · &#x60;api_key_expired&#x60; (+&#x60;rotate_url&#x60;, no grace) · &#x60;api_key_revoked&#x60; (also a vendor-app key whose install was uninstalled — S6) · &#x60;key_kind_not_accepted&#x60; (an agent key &#x60;ak&#x60; on this tree) · &#x60;use_authorization_header&#x60; (&#x60;X-Api-Key&#x60; or a query-string key) · a seller/app/staff JWT on this tree. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **403** | &#x60;insufficient_scope&#x60; (+&#x60;required_scope&#x60;; also a scope in &#x60;disabled_scopes&#x60;) · &#x60;tier_required&#x60; (+&#x60;scope&#x60;; derived on every request; also a key minted for a third-party &#x60;orders:pii&#x60; recipient — &#x60;details[pii_recipient: pii_third_party_pending_counsel]&#x60;, D7, C59) · &#x60;key_suspended&#x60; (+&#x60;suspended_until&#x60;, &#x60;Retry-After&#x60;, &#x60;Dona-Rate-Limited-Reason: suspended&#x60;) · &#x60;api_blocked&#x60; · &#x60;ip_not_allowed&#x60; (judged on the trusted client IP only) · &#x60;seller_not_approved&#x60; (shop closed/blocked/suspended/restricted) · &#x60;not_a_seller&#x60; (never on this tree; the portal&#39;s owner doors) · &#x60;app_frozen&#x60; (S6: every key of a frozen vendor app, from the next request) · &#x60;agreement_required&#x60; (+&#x60;accept_url&#x60;: the shop owner has not accepted the CURRENT Annex 2 «API and automated access» — the version in force or, while none is, the earliest announced; accepted once in Settings › API, then every door admits the key again. Checked after the sanctions, before the scopes). |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |
| **404** | &#x60;not_found&#x60; — every missing OR foreign id (never 403: no existence oracle). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **409** | &#x60;idempotency_in_progress&#x60; (+&#x60;Retry-After: 2&#x60;) · &#x60;idempotency_mismatch&#x60; · &#x60;version_conflict&#x60; · &#x60;ai_review_open&#x60; (publish of a product whose Dona AI review case is open — the review decides its status) · order codes &#x60;order_not_acceptable&#x60;, &#x60;no_pickup_address&#x60;, &#x60;order_not_shippable&#x60;, &#x60;order_awaiting_courier&#x60;, &#x60;order_not_cancellable&#x60;, &#x60;order_has_active_return&#x60; · document codes &#x60;no_tracking_number&#x60; (+&#x60;orders&#x60;), &#x60;no_items_selected&#x60;, &#x60;all_items_delayed&#x60; (S4, C53) · a replay of a rejected held write. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Cache-Control -  <br>  |
| **429** | &#x60;rate_limited&#x60; (with &#x60;Dona-Rate-Limited-Reason: app-rate&#x60;: a vendor app&#39;s bucket, shared by all its installs — S6) · &#x60;write_rate_limited&#x60; · &#x60;concurrency_limited&#x60; · &#x60;seller_rate_limited&#x60; · &#x60;object_cooldown&#x60; · &#x60;api_busy&#x60;. Always a JSON body + &#x60;Retry-After&#x60; from the origin (an edge 429 from Cloudflare has NO body — treat it as &#x60;Retry-After: 60&#x60;). Costs 0 and never counts toward the breaker. &#x60;rate_limited&#x60; is also the pre-auth ADDRESS guard, answered before the key is read: an address over 1 200 requests a minute that were not admitted (no key, a public route, a malformed, unknown or refused key — admitted requests never count), or one tarpitted at 60/min for 15 min after ≥ 20 unknown keys in a minute. No key is ever suspended by traffic that did not prove it. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * Cache-Control -  <br>  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **503** | &#x60;auth_unavailable&#x60; (key lookup failed — fail closed) · &#x60;limits_unavailable&#x60; (limiter blind on a write/MCP call, or a kill switch is off: &#x60;enabled&#x60;, &#x60;writes_enabled&#x60;, &#x60;webhooks_enabled&#x60;; &#x60;Retry-After: 30&#x60;) · &#x60;attention_busy&#x60; (an acknowledgement that resolves an item could not take the attention writer lock within 2 s — nothing was written; retry after &#x60;Retry-After: 2&#x60;) · &#x60;wallet_unavailable&#x60; (&#x60;/finance/_*&#x60;: the wallet could not answer for the shop; &#x60;Retry-After: 30&#x60;; its body is never relayed or error-copied — S4, C57) · &#x60;role_unavailable&#x60; (+ &#x60;served_by: \&quot;marketplace\&quot;&#x60;: a SERVER_ROLE&#x3D;seller-api server does not serve decline / cancel or &#x60;/finance/_*&#x60;; answered before any read or write, nothing changed; no &#x60;Retry-After&#x60; — D3). Costs 0. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="shiporder"></a>
# **ShipOrder**
> OrderTransition ShipOrder (Guid id, string idempotencyKey, string donaDryRun = null, string dryRun = null, string acceptLanguage = null, Guid donaSeller = null, string xDonaIntegration = null)

Ship

409: `order_not_shippable`, `order_awaiting_courier`. Kill switch: `writes_enabled`.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** | Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. |  |
| **idempotencyKey** | **string** | 1–255 chars. Scope &#x3D; this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ &#x60;400 invalid_body&#x60; with &#x60;details[{field:\&quot;Idempotency-Key\&quot;,code:\&quot;required\&quot;}]&#x60;. |  |
| **donaDryRun** | **string** | &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. Only the literal &#x60;true&#x60; / &#x60;false&#x60;; any other value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Dry-Run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). | [optional]  |
| **dryRun** | **string** | Alias of the &#x60;Dona-Dry-Run&#x60; header. Only the literal strings &#x60;true&#x60; / &#x60;false&#x60; — &#x60;1&#x60;, &#x60;0&#x60;, &#x60;TRUE&#x60;, &#x60;yes&#x60;, an empty value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;dry_run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). A string enum, not a boolean, so no SDK generator serialises it as &#x60;1&#x60;/&#x60;0&#x60;. | [optional]  |
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |
| **donaSeller** | **Guid** | Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional]  |
| **xDonaIntegration** | **string** | &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional]  |

### Return type

[**OrderTransition**](OrderTransition.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Dona-Request-Id -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * X-Dona-Key-Expires -  <br>  * Dona-API-Warn -  <br>  * Deprecation -  <br>  * Sunset -  <br>  * Cache-Control -  <br>  |
| **400** | &#x60;invalid_body&#x60; — malformed JSON, a missing &#x60;Idempotency-Key&#x60;, validation (&#x60;details[]&#x60; carries field codes such as &#x60;ikpu_required&#x60;, &#x60;cursor_expired&#x60;), a &#x60;dry_run&#x60; / &#x60;Dona-Dry-Run&#x60; that is not the literal &#x60;true&#x60;/&#x60;false&#x60; (&#x60;details[{field, code:\&quot;invalid\&quot;}]&#x60;, C51), a vendor-app install key without &#x60;Dona-Seller&#x60; (&#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;, S6) or with a repeated / non-canonical one (&#x60;code:\&quot;invalid\&quot;&#x60;), or an op-specific 400 (&#x60;invalid_decline_reason&#x60;). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **401** | &#x60;api_key_malformed&#x60; (checksum fails — refused before any DB read) · &#x60;api_key_expired&#x60; (+&#x60;rotate_url&#x60;, no grace) · &#x60;api_key_revoked&#x60; (also a vendor-app key whose install was uninstalled — S6) · &#x60;key_kind_not_accepted&#x60; (an agent key &#x60;ak&#x60; on this tree) · &#x60;use_authorization_header&#x60; (&#x60;X-Api-Key&#x60; or a query-string key) · a seller/app/staff JWT on this tree. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **403** | &#x60;insufficient_scope&#x60; (+&#x60;required_scope&#x60;; also a scope in &#x60;disabled_scopes&#x60;) · &#x60;tier_required&#x60; (+&#x60;scope&#x60;; derived on every request; also a key minted for a third-party &#x60;orders:pii&#x60; recipient — &#x60;details[pii_recipient: pii_third_party_pending_counsel]&#x60;, D7, C59) · &#x60;key_suspended&#x60; (+&#x60;suspended_until&#x60;, &#x60;Retry-After&#x60;, &#x60;Dona-Rate-Limited-Reason: suspended&#x60;) · &#x60;api_blocked&#x60; · &#x60;ip_not_allowed&#x60; (judged on the trusted client IP only) · &#x60;seller_not_approved&#x60; (shop closed/blocked/suspended/restricted) · &#x60;not_a_seller&#x60; (never on this tree; the portal&#39;s owner doors) · &#x60;app_frozen&#x60; (S6: every key of a frozen vendor app, from the next request) · &#x60;agreement_required&#x60; (+&#x60;accept_url&#x60;: the shop owner has not accepted the CURRENT Annex 2 «API and automated access» — the version in force or, while none is, the earliest announced; accepted once in Settings › API, then every door admits the key again. Checked after the sanctions, before the scopes). |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |
| **404** | &#x60;not_found&#x60; — every missing OR foreign id (never 403: no existence oracle). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **409** | &#x60;idempotency_in_progress&#x60; (+&#x60;Retry-After: 2&#x60;) · &#x60;idempotency_mismatch&#x60; · &#x60;version_conflict&#x60; · &#x60;ai_review_open&#x60; (publish of a product whose Dona AI review case is open — the review decides its status) · order codes &#x60;order_not_acceptable&#x60;, &#x60;no_pickup_address&#x60;, &#x60;order_not_shippable&#x60;, &#x60;order_awaiting_courier&#x60;, &#x60;order_not_cancellable&#x60;, &#x60;order_has_active_return&#x60; · document codes &#x60;no_tracking_number&#x60; (+&#x60;orders&#x60;), &#x60;no_items_selected&#x60;, &#x60;all_items_delayed&#x60; (S4, C53) · a replay of a rejected held write. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Cache-Control -  <br>  |
| **429** | &#x60;rate_limited&#x60; (with &#x60;Dona-Rate-Limited-Reason: app-rate&#x60;: a vendor app&#39;s bucket, shared by all its installs — S6) · &#x60;write_rate_limited&#x60; · &#x60;concurrency_limited&#x60; · &#x60;seller_rate_limited&#x60; · &#x60;object_cooldown&#x60; · &#x60;api_busy&#x60;. Always a JSON body + &#x60;Retry-After&#x60; from the origin (an edge 429 from Cloudflare has NO body — treat it as &#x60;Retry-After: 60&#x60;). Costs 0 and never counts toward the breaker. &#x60;rate_limited&#x60; is also the pre-auth ADDRESS guard, answered before the key is read: an address over 1 200 requests a minute that were not admitted (no key, a public route, a malformed, unknown or refused key — admitted requests never count), or one tarpitted at 60/min for 15 min after ≥ 20 unknown keys in a minute. No key is ever suspended by traffic that did not prove it. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * Cache-Control -  <br>  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **503** | &#x60;auth_unavailable&#x60; (key lookup failed — fail closed) · &#x60;limits_unavailable&#x60; (limiter blind on a write/MCP call, or a kill switch is off: &#x60;enabled&#x60;, &#x60;writes_enabled&#x60;, &#x60;webhooks_enabled&#x60;; &#x60;Retry-After: 30&#x60;) · &#x60;attention_busy&#x60; (an acknowledgement that resolves an item could not take the attention writer lock within 2 s — nothing was written; retry after &#x60;Retry-After: 2&#x60;) · &#x60;wallet_unavailable&#x60; (&#x60;/finance/_*&#x60;: the wallet could not answer for the shop; &#x60;Retry-After: 30&#x60;; its body is never relayed or error-copied — S4, C57) · &#x60;role_unavailable&#x60; (+ &#x60;served_by: \&quot;marketplace\&quot;&#x60;: a SERVER_ROLE&#x3D;seller-api server does not serve decline / cancel or &#x60;/finance/_*&#x60;; answered before any read or write, nothing changed; no &#x60;Retry-After&#x60; — D3). Costs 0. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)


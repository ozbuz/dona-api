# Dona.Api.Api.ReturnsApi

All URIs are relative to *https://api.dona.im/seller-api/v1*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetReturn**](ReturnsApi.md#getreturn) | **GET** /returns/{id} | Get a return |
| [**ListReturns**](ReturnsApi.md#listreturns) | **GET** /returns | List returns |

<a id="getreturn"></a>
# **GetReturn**
> Return GetReturn (Guid id, string acceptLanguage = null, Guid donaSeller = null, string xDonaIntegration = null)

Get a return

Includes the buyer's `reason_text` (detail only).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** | Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. |  |
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |
| **donaSeller** | **Guid** | Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional]  |
| **xDonaIntegration** | **string** | &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional]  |

### Return type

[**Return**](Return.md)

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

<a id="listreturns"></a>
# **ListReturns**
> ReturnPage ListReturns (string cursor = null, int limit = null, string updatedSince = null, string status = null, string acceptLanguage = null, Guid donaSeller = null, string xDonaIntegration = null)

List returns

Read-only in v1 — approving a return is `orders.refund`, never issuable.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **cursor** | **string** | Opaque keyset cursor from &#x60;next_cursor&#x60;. | [optional]  |
| **limit** | **int** | Page size, default 50, max 100 (clamped, with &#x60;Dona-API-Warn&#x60;). &#x60;limit &gt; 50&#x60; costs &#x60;1 + ceil(limit/50)&#x60;. | [optional] [default to 50] |
| **updatedSince** | **string** | ISO 8601 with offset, or epoch milliseconds. The visible high-water mark is capped at &#x60;now() − 10 s&#x60; so a slow transaction is never skipped. | [optional]  |
| **status** | **string** | Exact. | [optional]  |
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |
| **donaSeller** | **Guid** | Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional]  |
| **xDonaIntegration** | **string** | &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional]  |

### Return type

[**ReturnPage**](ReturnPage.md)

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


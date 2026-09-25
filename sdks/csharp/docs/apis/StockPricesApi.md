# Dona.Api.Api.StockPricesApi

All URIs are relative to *https://api.dona.im/seller-api/v1*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**ListStock**](StockPricesApi.md#liststock) | **GET** /stock | Stock, SKU-level |
| [**SetPrices**](StockPricesApi.md#setprices) | **POST** /prices | Set absolute prices (≤ 1 000 lines) |
| [**SetStock**](StockPricesApi.md#setstock) | **POST** /stock | Set absolute stock (≤ 1 000 lines) |

<a id="liststock"></a>
# **ListStock**
> StockLineViewPage ListStock (string cursor = null, int page = null, int limit = null, string updatedSince = null, string sellerSku = null, string ifNoneMatch = null, string acceptLanguage = null, Guid donaSeller = null, string xDonaIntegration = null)

Stock, SKU-level

One row per product without variants, one per variant otherwise. `cursor` or 0-based `page` (slower).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **cursor** | **string** | Opaque keyset cursor from &#x60;next_cursor&#x60;. | [optional]  |
| **page** | **int** | 0-based page alias (Uzum parity) — slower than &#x60;cursor&#x60;, ≤ 1 000 pages; mutually exclusive with &#x60;cursor&#x60;. | [optional]  |
| **limit** | **int** | Page size, default 50, max 100 (clamped, with &#x60;Dona-API-Warn&#x60;). &#x60;limit &gt; 50&#x60; costs &#x60;1 + ceil(limit/50)&#x60;. | [optional] [default to 50] |
| **updatedSince** | **string** | ISO 8601 with offset, or epoch milliseconds. The visible high-water mark is capped at &#x60;now() − 10 s&#x60; so a slow transaction is never skipped. | [optional]  |
| **sellerSku** | **string** | Exact. | [optional]  |
| **ifNoneMatch** | **string** | An &#x60;ETag&#x60; from a previous identical request ⇒ &#x60;304&#x60; with rate headers (cost 0.5). | [optional]  |
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |
| **donaSeller** | **Guid** | Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional]  |
| **xDonaIntegration** | **string** | &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional]  |

### Return type

[**StockLineViewPage**](StockLineViewPage.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Dona-Request-Id -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * X-Dona-Key-Expires -  <br>  * Dona-API-Warn -  <br>  * Deprecation -  <br>  * Sunset -  <br>  * Cache-Control -  <br>  * ETag -  <br>  |
| **304** | &#x60;If-None-Match&#x60; matched. Rate headers present; costs 0.5. |  * Dona-Request-Id -  <br>  * ETag -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  |
| **400** | &#x60;invalid_body&#x60; — malformed JSON, a missing &#x60;Idempotency-Key&#x60;, validation (&#x60;details[]&#x60; carries field codes such as &#x60;ikpu_required&#x60;, &#x60;cursor_expired&#x60;), a &#x60;dry_run&#x60; / &#x60;Dona-Dry-Run&#x60; that is not the literal &#x60;true&#x60;/&#x60;false&#x60; (&#x60;details[{field, code:\&quot;invalid\&quot;}]&#x60;, C51), a vendor-app install key without &#x60;Dona-Seller&#x60; (&#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;, S6) or with a repeated / non-canonical one (&#x60;code:\&quot;invalid\&quot;&#x60;), or an op-specific 400 (&#x60;invalid_decline_reason&#x60;). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **401** | &#x60;api_key_malformed&#x60; (checksum fails — refused before any DB read) · &#x60;api_key_expired&#x60; (+&#x60;rotate_url&#x60;, no grace) · &#x60;api_key_revoked&#x60; (also a vendor-app key whose install was uninstalled — S6) · &#x60;key_kind_not_accepted&#x60; (an agent key &#x60;ak&#x60; on this tree) · &#x60;use_authorization_header&#x60; (&#x60;X-Api-Key&#x60; or a query-string key) · a seller/app/staff JWT on this tree. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **403** | &#x60;insufficient_scope&#x60; (+&#x60;required_scope&#x60;; also a scope in &#x60;disabled_scopes&#x60;) · &#x60;tier_required&#x60; (+&#x60;scope&#x60;; derived on every request; also a key minted for a third-party &#x60;orders:pii&#x60; recipient — &#x60;details[pii_recipient: pii_third_party_pending_counsel]&#x60;, D7, C59) · &#x60;key_suspended&#x60; (+&#x60;suspended_until&#x60;, &#x60;Retry-After&#x60;, &#x60;Dona-Rate-Limited-Reason: suspended&#x60;) · &#x60;api_blocked&#x60; · &#x60;ip_not_allowed&#x60; (judged on the trusted client IP only) · &#x60;seller_not_approved&#x60; (shop closed/blocked/suspended/restricted) · &#x60;not_a_seller&#x60; (never on this tree; the portal&#39;s owner doors) · &#x60;app_frozen&#x60; (S6: every key of a frozen vendor app, from the next request) · &#x60;agreement_required&#x60; (+&#x60;accept_url&#x60;: the shop owner has not accepted the CURRENT Annex 2 «API and automated access» — the version in force or, while none is, the earliest announced; accepted once in Settings › API, then every door admits the key again. Checked after the sanctions, before the scopes). |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |
| **429** | &#x60;rate_limited&#x60; (with &#x60;Dona-Rate-Limited-Reason: app-rate&#x60;: a vendor app&#39;s bucket, shared by all its installs — S6) · &#x60;write_rate_limited&#x60; · &#x60;concurrency_limited&#x60; · &#x60;seller_rate_limited&#x60; · &#x60;object_cooldown&#x60; · &#x60;api_busy&#x60;. Always a JSON body + &#x60;Retry-After&#x60; from the origin (an edge 429 from Cloudflare has NO body — treat it as &#x60;Retry-After: 60&#x60;). Costs 0 and never counts toward the breaker. &#x60;rate_limited&#x60; is also the pre-auth ADDRESS guard, answered before the key is read: an address over 1 200 requests a minute that were not admitted (no key, a public route, a malformed, unknown or refused key — admitted requests never count), or one tarpitted at 60/min for 15 min after ≥ 20 unknown keys in a minute. No key is ever suspended by traffic that did not prove it. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * Cache-Control -  <br>  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **503** | &#x60;auth_unavailable&#x60; (key lookup failed — fail closed) · &#x60;limits_unavailable&#x60; (limiter blind on a write/MCP call, or a kill switch is off: &#x60;enabled&#x60;, &#x60;writes_enabled&#x60;, &#x60;webhooks_enabled&#x60;; &#x60;Retry-After: 30&#x60;) · &#x60;attention_busy&#x60; (an acknowledgement that resolves an item could not take the attention writer lock within 2 s — nothing was written; retry after &#x60;Retry-After: 2&#x60;) · &#x60;wallet_unavailable&#x60; (&#x60;/finance/_*&#x60;: the wallet could not answer for the shop; &#x60;Retry-After: 30&#x60;; its body is never relayed or error-copied — S4, C57) · &#x60;role_unavailable&#x60; (+ &#x60;served_by: \&quot;marketplace\&quot;&#x60;: a SERVER_ROLE&#x3D;seller-api server does not serve decline / cancel or &#x60;/finance/_*&#x60;; answered before any read or write, nothing changed; no &#x60;Retry-After&#x60; — D3). Costs 0. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="setprices"></a>
# **SetPrices**
> BulkResult SetPrices (string idempotencyKey, PriceRequest priceRequest, bool atomic = null, string donaDryRun = null, string dryRun = null, string acceptLanguage = null, Guid donaSeller = null, string xDonaIntegration = null)

Set absolute prices (≤ 1 000 lines)

As `POST /stock`. Price < `catalog.price_floor_uzs` (1 000) or > 100× drop vs current/last-sold ⇒ `held`; `compare_at_uzs` must exceed `price_uzs`. Kill switch: `writes_enabled`.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | 1–255 chars. Scope &#x3D; this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ &#x60;400 invalid_body&#x60; with &#x60;details[{field:\&quot;Idempotency-Key\&quot;,code:\&quot;required\&quot;}]&#x60;. |  |
| **priceRequest** | [**PriceRequest**](PriceRequest.md) |  |  |
| **atomic** | **bool** | All-or-nothing. | [optional]  |
| **donaDryRun** | **string** | &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. Only the literal &#x60;true&#x60; / &#x60;false&#x60;; any other value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Dry-Run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). | [optional]  |
| **dryRun** | **string** | Alias of the &#x60;Dona-Dry-Run&#x60; header. Only the literal strings &#x60;true&#x60; / &#x60;false&#x60; — &#x60;1&#x60;, &#x60;0&#x60;, &#x60;TRUE&#x60;, &#x60;yes&#x60;, an empty value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;dry_run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). A string enum, not a boolean, so no SDK generator serialises it as &#x60;1&#x60;/&#x60;0&#x60;. | [optional]  |
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |
| **donaSeller** | **Guid** | Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional]  |
| **xDonaIntegration** | **string** | &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional]  |

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Dona-Request-Id -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * X-Dona-Key-Expires -  <br>  * Dona-API-Warn -  <br>  * Deprecation -  <br>  * Sunset -  <br>  * Cache-Control -  <br>  |
| **202** | &#x60;atomic&#x3D;true&#x60; and a line was held — nothing written. |  * Dona-Request-Id -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * X-Dona-Key-Expires -  <br>  * Dona-API-Warn -  <br>  * Deprecation -  <br>  * Sunset -  <br>  * Cache-Control -  <br>  |
| **400** | &#x60;invalid_body&#x60; — malformed JSON, a missing &#x60;Idempotency-Key&#x60;, validation (&#x60;details[]&#x60; carries field codes such as &#x60;ikpu_required&#x60;, &#x60;cursor_expired&#x60;), a &#x60;dry_run&#x60; / &#x60;Dona-Dry-Run&#x60; that is not the literal &#x60;true&#x60;/&#x60;false&#x60; (&#x60;details[{field, code:\&quot;invalid\&quot;}]&#x60;, C51), a vendor-app install key without &#x60;Dona-Seller&#x60; (&#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;, S6) or with a repeated / non-canonical one (&#x60;code:\&quot;invalid\&quot;&#x60;), or an op-specific 400 (&#x60;invalid_decline_reason&#x60;). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **401** | &#x60;api_key_malformed&#x60; (checksum fails — refused before any DB read) · &#x60;api_key_expired&#x60; (+&#x60;rotate_url&#x60;, no grace) · &#x60;api_key_revoked&#x60; (also a vendor-app key whose install was uninstalled — S6) · &#x60;key_kind_not_accepted&#x60; (an agent key &#x60;ak&#x60; on this tree) · &#x60;use_authorization_header&#x60; (&#x60;X-Api-Key&#x60; or a query-string key) · a seller/app/staff JWT on this tree. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **403** | &#x60;insufficient_scope&#x60; (+&#x60;required_scope&#x60;; also a scope in &#x60;disabled_scopes&#x60;) · &#x60;tier_required&#x60; (+&#x60;scope&#x60;; derived on every request; also a key minted for a third-party &#x60;orders:pii&#x60; recipient — &#x60;details[pii_recipient: pii_third_party_pending_counsel]&#x60;, D7, C59) · &#x60;key_suspended&#x60; (+&#x60;suspended_until&#x60;, &#x60;Retry-After&#x60;, &#x60;Dona-Rate-Limited-Reason: suspended&#x60;) · &#x60;api_blocked&#x60; · &#x60;ip_not_allowed&#x60; (judged on the trusted client IP only) · &#x60;seller_not_approved&#x60; (shop closed/blocked/suspended/restricted) · &#x60;not_a_seller&#x60; (never on this tree; the portal&#39;s owner doors) · &#x60;app_frozen&#x60; (S6: every key of a frozen vendor app, from the next request) · &#x60;agreement_required&#x60; (+&#x60;accept_url&#x60;: the shop owner has not accepted the CURRENT Annex 2 «API and automated access» — the version in force or, while none is, the earliest announced; accepted once in Settings › API, then every door admits the key again. Checked after the sanctions, before the scopes). |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |
| **409** | &#x60;idempotency_in_progress&#x60; (+&#x60;Retry-After: 2&#x60;) · &#x60;idempotency_mismatch&#x60; · &#x60;version_conflict&#x60; · &#x60;ai_review_open&#x60; (publish of a product whose Dona AI review case is open — the review decides its status) · order codes &#x60;order_not_acceptable&#x60;, &#x60;no_pickup_address&#x60;, &#x60;order_not_shippable&#x60;, &#x60;order_awaiting_courier&#x60;, &#x60;order_not_cancellable&#x60;, &#x60;order_has_active_return&#x60; · document codes &#x60;no_tracking_number&#x60; (+&#x60;orders&#x60;), &#x60;no_items_selected&#x60;, &#x60;all_items_delayed&#x60; (S4, C53) · a replay of a rejected held write. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Cache-Control -  <br>  |
| **413** | &#x60;payload_too_large&#x60; — body &gt; 256 KiB (4 MiB on bulk stock/prices/batch), or &gt; 1 000 lines. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **422** | &#x60;webhook_url_invalid&#x60; (+&#x60;details[].code&#x60; ∈ &#x60;timeout&#x60;, &#x60;status_&lt;n&gt;&#x60;, &#x60;tls&#x60;, &#x60;dns&#x60;, &#x60;private_address&#x60;, &#x60;scheme&#x60;) · &#x60;warehouse_unsupported&#x60;. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **429** | &#x60;rate_limited&#x60; (with &#x60;Dona-Rate-Limited-Reason: app-rate&#x60;: a vendor app&#39;s bucket, shared by all its installs — S6) · &#x60;write_rate_limited&#x60; · &#x60;concurrency_limited&#x60; · &#x60;seller_rate_limited&#x60; · &#x60;object_cooldown&#x60; · &#x60;api_busy&#x60;. Always a JSON body + &#x60;Retry-After&#x60; from the origin (an edge 429 from Cloudflare has NO body — treat it as &#x60;Retry-After: 60&#x60;). Costs 0 and never counts toward the breaker. &#x60;rate_limited&#x60; is also the pre-auth ADDRESS guard, answered before the key is read: an address over 1 200 requests a minute that were not admitted (no key, a public route, a malformed, unknown or refused key — admitted requests never count), or one tarpitted at 60/min for 15 min after ≥ 20 unknown keys in a minute. No key is ever suspended by traffic that did not prove it. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * Cache-Control -  <br>  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **503** | &#x60;auth_unavailable&#x60; (key lookup failed — fail closed) · &#x60;limits_unavailable&#x60; (limiter blind on a write/MCP call, or a kill switch is off: &#x60;enabled&#x60;, &#x60;writes_enabled&#x60;, &#x60;webhooks_enabled&#x60;; &#x60;Retry-After: 30&#x60;) · &#x60;attention_busy&#x60; (an acknowledgement that resolves an item could not take the attention writer lock within 2 s — nothing was written; retry after &#x60;Retry-After: 2&#x60;) · &#x60;wallet_unavailable&#x60; (&#x60;/finance/_*&#x60;: the wallet could not answer for the shop; &#x60;Retry-After: 30&#x60;; its body is never relayed or error-copied — S4, C57) · &#x60;role_unavailable&#x60; (+ &#x60;served_by: \&quot;marketplace\&quot;&#x60;: a SERVER_ROLE&#x3D;seller-api server does not serve decline / cancel or &#x60;/finance/_*&#x60;; answered before any read or write, nothing changed; no &#x60;Retry-After&#x60; — D3). Costs 0. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="setstock"></a>
# **SetStock**
> BulkResult SetStock (string idempotencyKey, StockRequest stockRequest, bool atomic = null, string donaDryRun = null, string dryRun = null, string acceptLanguage = null, Guid donaSeller = null, string xDonaIntegration = null)

Set absolute stock (≤ 1 000 lines)

Synchronous, through `catalog.ApplyGuardedStockPrice`. `200` with per-line results — the request is refused whole only for shape/budget (400/413/422). `?atomic=true` = all-or-nothing (any held line ⇒ `202` for the batch). |Δ| > 10× and > 1 000, or zeroing > 50 % of lines ⇒ `held`. One object ≤ 1 write / 10 s ⇒ line `error: object_cooldown`. Kill switch: `writes_enabled`.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | 1–255 chars. Scope &#x3D; this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ &#x60;400 invalid_body&#x60; with &#x60;details[{field:\&quot;Idempotency-Key\&quot;,code:\&quot;required\&quot;}]&#x60;. |  |
| **stockRequest** | [**StockRequest**](StockRequest.md) |  |  |
| **atomic** | **bool** | All-or-nothing (Yandex default). | [optional]  |
| **donaDryRun** | **string** | &#x60;true&#x60; ⇒ validate + guard + compute the effect, then roll back. Zero side-effect rows (no events, no activity, no counters). Same as &#x60;?dry_run&#x3D;true&#x60;. Only the literal &#x60;true&#x60; / &#x60;false&#x60;; any other value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Dry-Run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). | [optional]  |
| **dryRun** | **string** | Alias of the &#x60;Dona-Dry-Run&#x60; header. Only the literal strings &#x60;true&#x60; / &#x60;false&#x60; — &#x60;1&#x60;, &#x60;0&#x60;, &#x60;TRUE&#x60;, &#x60;yes&#x60;, an empty value ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;dry_run\&quot;, code:\&quot;invalid\&quot;}]&#x60; (C51). A string enum, not a boolean, so no SDK generator serialises it as &#x60;1&#x60;/&#x60;0&#x60;. | [optional]  |
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |
| **donaSeller** | **Guid** | Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional]  |
| **xDonaIntegration** | **string** | &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional]  |

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Dona-Request-Id -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * X-Dona-Key-Expires -  <br>  * Dona-API-Warn -  <br>  * Deprecation -  <br>  * Sunset -  <br>  * Cache-Control -  <br>  |
| **202** | &#x60;atomic&#x3D;true&#x60; and a line was held — nothing written. |  * Dona-Request-Id -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * X-Dona-Key-Expires -  <br>  * Dona-API-Warn -  <br>  * Deprecation -  <br>  * Sunset -  <br>  * Cache-Control -  <br>  |
| **400** | &#x60;invalid_body&#x60; — malformed JSON, a missing &#x60;Idempotency-Key&#x60;, validation (&#x60;details[]&#x60; carries field codes such as &#x60;ikpu_required&#x60;, &#x60;cursor_expired&#x60;), a &#x60;dry_run&#x60; / &#x60;Dona-Dry-Run&#x60; that is not the literal &#x60;true&#x60;/&#x60;false&#x60; (&#x60;details[{field, code:\&quot;invalid\&quot;}]&#x60;, C51), a vendor-app install key without &#x60;Dona-Seller&#x60; (&#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;, S6) or with a repeated / non-canonical one (&#x60;code:\&quot;invalid\&quot;&#x60;), or an op-specific 400 (&#x60;invalid_decline_reason&#x60;). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **401** | &#x60;api_key_malformed&#x60; (checksum fails — refused before any DB read) · &#x60;api_key_expired&#x60; (+&#x60;rotate_url&#x60;, no grace) · &#x60;api_key_revoked&#x60; (also a vendor-app key whose install was uninstalled — S6) · &#x60;key_kind_not_accepted&#x60; (an agent key &#x60;ak&#x60; on this tree) · &#x60;use_authorization_header&#x60; (&#x60;X-Api-Key&#x60; or a query-string key) · a seller/app/staff JWT on this tree. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **403** | &#x60;insufficient_scope&#x60; (+&#x60;required_scope&#x60;; also a scope in &#x60;disabled_scopes&#x60;) · &#x60;tier_required&#x60; (+&#x60;scope&#x60;; derived on every request; also a key minted for a third-party &#x60;orders:pii&#x60; recipient — &#x60;details[pii_recipient: pii_third_party_pending_counsel]&#x60;, D7, C59) · &#x60;key_suspended&#x60; (+&#x60;suspended_until&#x60;, &#x60;Retry-After&#x60;, &#x60;Dona-Rate-Limited-Reason: suspended&#x60;) · &#x60;api_blocked&#x60; · &#x60;ip_not_allowed&#x60; (judged on the trusted client IP only) · &#x60;seller_not_approved&#x60; (shop closed/blocked/suspended/restricted) · &#x60;not_a_seller&#x60; (never on this tree; the portal&#39;s owner doors) · &#x60;app_frozen&#x60; (S6: every key of a frozen vendor app, from the next request) · &#x60;agreement_required&#x60; (+&#x60;accept_url&#x60;: the shop owner has not accepted the CURRENT Annex 2 «API and automated access» — the version in force or, while none is, the earliest announced; accepted once in Settings › API, then every door admits the key again. Checked after the sanctions, before the scopes). |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |
| **409** | &#x60;idempotency_in_progress&#x60; (+&#x60;Retry-After: 2&#x60;) · &#x60;idempotency_mismatch&#x60; · &#x60;version_conflict&#x60; · &#x60;ai_review_open&#x60; (publish of a product whose Dona AI review case is open — the review decides its status) · order codes &#x60;order_not_acceptable&#x60;, &#x60;no_pickup_address&#x60;, &#x60;order_not_shippable&#x60;, &#x60;order_awaiting_courier&#x60;, &#x60;order_not_cancellable&#x60;, &#x60;order_has_active_return&#x60; · document codes &#x60;no_tracking_number&#x60; (+&#x60;orders&#x60;), &#x60;no_items_selected&#x60;, &#x60;all_items_delayed&#x60; (S4, C53) · a replay of a rejected held write. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Cache-Control -  <br>  |
| **413** | &#x60;payload_too_large&#x60; — body &gt; 256 KiB (4 MiB on bulk stock/prices/batch), or &gt; 1 000 lines. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **422** | &#x60;webhook_url_invalid&#x60; (+&#x60;details[].code&#x60; ∈ &#x60;timeout&#x60;, &#x60;status_&lt;n&gt;&#x60;, &#x60;tls&#x60;, &#x60;dns&#x60;, &#x60;private_address&#x60;, &#x60;scheme&#x60;) · &#x60;warehouse_unsupported&#x60;. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **429** | &#x60;rate_limited&#x60; (with &#x60;Dona-Rate-Limited-Reason: app-rate&#x60;: a vendor app&#39;s bucket, shared by all its installs — S6) · &#x60;write_rate_limited&#x60; · &#x60;concurrency_limited&#x60; · &#x60;seller_rate_limited&#x60; · &#x60;object_cooldown&#x60; · &#x60;api_busy&#x60;. Always a JSON body + &#x60;Retry-After&#x60; from the origin (an edge 429 from Cloudflare has NO body — treat it as &#x60;Retry-After: 60&#x60;). Costs 0 and never counts toward the breaker. &#x60;rate_limited&#x60; is also the pre-auth ADDRESS guard, answered before the key is read: an address over 1 200 requests a minute that were not admitted (no key, a public route, a malformed, unknown or refused key — admitted requests never count), or one tarpitted at 60/min for 15 min after ≥ 20 unknown keys in a minute. No key is ever suspended by traffic that did not prove it. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * Cache-Control -  <br>  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **503** | &#x60;auth_unavailable&#x60; (key lookup failed — fail closed) · &#x60;limits_unavailable&#x60; (limiter blind on a write/MCP call, or a kill switch is off: &#x60;enabled&#x60;, &#x60;writes_enabled&#x60;, &#x60;webhooks_enabled&#x60;; &#x60;Retry-After: 30&#x60;) · &#x60;attention_busy&#x60; (an acknowledgement that resolves an item could not take the attention writer lock within 2 s — nothing was written; retry after &#x60;Retry-After: 2&#x60;) · &#x60;wallet_unavailable&#x60; (&#x60;/finance/_*&#x60;: the wallet could not answer for the shop; &#x60;Retry-After: 30&#x60;; its body is never relayed or error-copied — S4, C57) · &#x60;role_unavailable&#x60; (+ &#x60;served_by: \&quot;marketplace\&quot;&#x60;: a SERVER_ROLE&#x3D;seller-api server does not serve decline / cancel or &#x60;/finance/_*&#x60;; answered before any read or write, nothing changed; no &#x60;Retry-After&#x60; — D3). Costs 0. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)


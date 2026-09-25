# Dona.Api.Api.JobsApi

All URIs are relative to *https://api.dona.im/seller-api/v1*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**DownloadJobFile**](JobsApi.md#downloadjobfile) | **GET** /jobs/{id}/download | Download an export&#39;s file |
| [**ExportOrders**](JobsApi.md#exportorders) | **POST** /exports/orders | Export orders (async, no PII) |
| [**ExportProducts**](JobsApi.md#exportproducts) | **POST** /exports/products | Export products (async) |
| [**GetJob**](JobsApi.md#getjob) | **GET** /jobs/{id} | Poll a job |

<a id="downloadjobfile"></a>
# **DownloadJobFile**
> string DownloadJobFile (Guid id, string token, string acceptLanguage = null, Guid donaSeller = null, string xDonaIntegration = null)

Download an export's file

What a ready export's `file_url` points at. Needs BOTH a key of the job's shop that holds the scope the job's kind needs (any key of the shop — the file is the shop's; a key of another shop is `404 not_found` whatever token it carries) AND the job's own `token` from `file_url`, valid 15 min (`401 download_token_invalid` when absent, forged or another job's; `401 download_token_expired` past its time — re-read `GET /jobs/{id}` for a fresh one). The file is never on a public origin — it is in Dona's private exports bucket (`302` to a presigned GET valid 15 min, issued only after both checks above — D24, 2026-09-26) or, where the bucket is not configured, in the database (`200` with the bytes). Follow the redirect WITHOUT the `Authorization` header (the signed URL carries its own authority; most HTTP clients drop the header on a cross-host redirect). Swept with its job after `expires_at` (7 d) ⇒ `404 not_found`. Not gated by `writes_enabled`.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** | Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. |  |
| **token** | **string** | The download token &#x60;file_url&#x60; carries (&#x60;v1.&lt;unix expiry&gt;.&lt;mac&gt;&#x60;), bound to this job and this shop. |  |
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |
| **donaSeller** | **Guid** | Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional]  |
| **xDonaIntegration** | **string** | &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional]  |

### Return type

**string**

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-ndjson, text/csv, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The file, as an attachment (&#x60;Content-Disposition&#x60;, &#x60;X-Content-Type-Options: nosniff&#x60;). |  * Dona-Request-Id -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * X-Dona-Key-Expires -  <br>  * Dona-API-Warn -  <br>  * Deprecation -  <br>  * Sunset -  <br>  * Cache-Control -  <br>  * Content-Disposition - &#x60;attachment; filename&#x3D;\&quot;dona-&lt;products|orders&gt;-&lt;job id&gt;.&lt;jsonl|csv&gt;\&quot;&#x60; <br>  |
| **302** | The file is in Dona&#39;s private exports bucket — &#x60;Location&#x60; is a presigned GET of exactly this job&#39;s object, valid 15 minutes, that downloads it as an attachment (&#x60;dona-&lt;products|orders&gt;-&lt;job id&gt;.&lt;jsonl|csv&gt;&#x60;). Issued only after the key and token checks; never cacheable. |  * Location - The presigned object URL (&#x60;https://…amazonaws.com/…?X-Amz-Signature&#x3D;…&amp;X-Amz-Expires&#x3D;900…&#x60;). Opaque — do not parse, store or share it; request a new one through &#x60;GET /jobs/{id}&#x60; once it lapses. <br>  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **401** | &#x60;api_key_malformed&#x60; (checksum fails — refused before any DB read) · &#x60;api_key_expired&#x60; (+&#x60;rotate_url&#x60;, no grace) · &#x60;api_key_revoked&#x60; (also a vendor-app key whose install was uninstalled — S6) · &#x60;key_kind_not_accepted&#x60; (an agent key &#x60;ak&#x60; on this tree) · &#x60;use_authorization_header&#x60; (&#x60;X-Api-Key&#x60; or a query-string key) · a seller/app/staff JWT on this tree. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **403** | &#x60;insufficient_scope&#x60; (+&#x60;required_scope&#x60;; also a scope in &#x60;disabled_scopes&#x60;) · &#x60;tier_required&#x60; (+&#x60;scope&#x60;; derived on every request; also a key minted for a third-party &#x60;orders:pii&#x60; recipient — &#x60;details[pii_recipient: pii_third_party_pending_counsel]&#x60;, D7, C59) · &#x60;key_suspended&#x60; (+&#x60;suspended_until&#x60;, &#x60;Retry-After&#x60;, &#x60;Dona-Rate-Limited-Reason: suspended&#x60;) · &#x60;api_blocked&#x60; · &#x60;ip_not_allowed&#x60; (judged on the trusted client IP only) · &#x60;seller_not_approved&#x60; (shop closed/blocked/suspended/restricted) · &#x60;not_a_seller&#x60; (never on this tree; the portal&#39;s owner doors) · &#x60;app_frozen&#x60; (S6: every key of a frozen vendor app, from the next request) · &#x60;agreement_required&#x60; (+&#x60;accept_url&#x60;: the shop owner has not accepted the CURRENT Annex 2 «API and automated access» — the version in force or, while none is, the earliest announced; accepted once in Settings › API, then every door admits the key again. Checked after the sanctions, before the scopes). |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |
| **404** | &#x60;not_found&#x60; — every missing OR foreign id (never 403: no existence oracle). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **429** | &#x60;rate_limited&#x60; (with &#x60;Dona-Rate-Limited-Reason: app-rate&#x60;: a vendor app&#39;s bucket, shared by all its installs — S6) · &#x60;write_rate_limited&#x60; · &#x60;concurrency_limited&#x60; · &#x60;seller_rate_limited&#x60; · &#x60;object_cooldown&#x60; · &#x60;api_busy&#x60;. Always a JSON body + &#x60;Retry-After&#x60; from the origin (an edge 429 from Cloudflare has NO body — treat it as &#x60;Retry-After: 60&#x60;). Costs 0 and never counts toward the breaker. &#x60;rate_limited&#x60; is also the pre-auth ADDRESS guard, answered before the key is read: an address over 1 200 requests a minute that were not admitted (no key, a public route, a malformed, unknown or refused key — admitted requests never count), or one tarpitted at 60/min for 15 min after ≥ 20 unknown keys in a minute. No key is ever suspended by traffic that did not prove it. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * Cache-Control -  <br>  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **503** | &#x60;auth_unavailable&#x60; (key lookup failed — fail closed) · &#x60;limits_unavailable&#x60; (limiter blind on a write/MCP call, or a kill switch is off: &#x60;enabled&#x60;, &#x60;writes_enabled&#x60;, &#x60;webhooks_enabled&#x60;; &#x60;Retry-After: 30&#x60;) · &#x60;attention_busy&#x60; (an acknowledgement that resolves an item could not take the attention writer lock within 2 s — nothing was written; retry after &#x60;Retry-After: 2&#x60;) · &#x60;wallet_unavailable&#x60; (&#x60;/finance/_*&#x60;: the wallet could not answer for the shop; &#x60;Retry-After: 30&#x60;; its body is never relayed or error-copied — S4, C57) · &#x60;role_unavailable&#x60; (+ &#x60;served_by: \&quot;marketplace\&quot;&#x60;: a SERVER_ROLE&#x3D;seller-api server does not serve decline / cancel or &#x60;/finance/_*&#x60;; answered before any read or write, nothing changed; no &#x60;Retry-After&#x60; — D3). Costs 0. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="exportorders"></a>
# **ExportOrders**
> JobAccepted ExportOrders (string idempotencyKey, ExportRequest exportRequest, string acceptLanguage = null, Guid donaSeller = null, string xDonaIntegration = null)

Export orders (async, no PII)

The `orders:read` projection only — an export never carries `recipient`.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | 1–255 chars. Scope &#x3D; this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ &#x60;400 invalid_body&#x60; with &#x60;details[{field:\&quot;Idempotency-Key\&quot;,code:\&quot;required\&quot;}]&#x60;. |  |
| **exportRequest** | [**ExportRequest**](ExportRequest.md) |  |  |
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |
| **donaSeller** | **Guid** | Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional]  |
| **xDonaIntegration** | **string** | &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional]  |

### Return type

[**JobAccepted**](JobAccepted.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  * Location -  <br>  * Retry-After -  <br>  * Dona-Request-Id -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * X-Dona-Key-Expires -  <br>  * Dona-API-Warn -  <br>  * Deprecation -  <br>  * Sunset -  <br>  * Cache-Control -  <br>  |
| **400** | &#x60;invalid_body&#x60; — malformed JSON, a missing &#x60;Idempotency-Key&#x60;, validation (&#x60;details[]&#x60; carries field codes such as &#x60;ikpu_required&#x60;, &#x60;cursor_expired&#x60;), a &#x60;dry_run&#x60; / &#x60;Dona-Dry-Run&#x60; that is not the literal &#x60;true&#x60;/&#x60;false&#x60; (&#x60;details[{field, code:\&quot;invalid\&quot;}]&#x60;, C51), a vendor-app install key without &#x60;Dona-Seller&#x60; (&#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;, S6) or with a repeated / non-canonical one (&#x60;code:\&quot;invalid\&quot;&#x60;), or an op-specific 400 (&#x60;invalid_decline_reason&#x60;). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **401** | &#x60;api_key_malformed&#x60; (checksum fails — refused before any DB read) · &#x60;api_key_expired&#x60; (+&#x60;rotate_url&#x60;, no grace) · &#x60;api_key_revoked&#x60; (also a vendor-app key whose install was uninstalled — S6) · &#x60;key_kind_not_accepted&#x60; (an agent key &#x60;ak&#x60; on this tree) · &#x60;use_authorization_header&#x60; (&#x60;X-Api-Key&#x60; or a query-string key) · a seller/app/staff JWT on this tree. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **403** | &#x60;insufficient_scope&#x60; (+&#x60;required_scope&#x60;; also a scope in &#x60;disabled_scopes&#x60;) · &#x60;tier_required&#x60; (+&#x60;scope&#x60;; derived on every request; also a key minted for a third-party &#x60;orders:pii&#x60; recipient — &#x60;details[pii_recipient: pii_third_party_pending_counsel]&#x60;, D7, C59) · &#x60;key_suspended&#x60; (+&#x60;suspended_until&#x60;, &#x60;Retry-After&#x60;, &#x60;Dona-Rate-Limited-Reason: suspended&#x60;) · &#x60;api_blocked&#x60; · &#x60;ip_not_allowed&#x60; (judged on the trusted client IP only) · &#x60;seller_not_approved&#x60; (shop closed/blocked/suspended/restricted) · &#x60;not_a_seller&#x60; (never on this tree; the portal&#39;s owner doors) · &#x60;app_frozen&#x60; (S6: every key of a frozen vendor app, from the next request) · &#x60;agreement_required&#x60; (+&#x60;accept_url&#x60;: the shop owner has not accepted the CURRENT Annex 2 «API and automated access» — the version in force or, while none is, the earliest announced; accepted once in Settings › API, then every door admits the key again. Checked after the sanctions, before the scopes). |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |
| **409** | &#x60;idempotency_in_progress&#x60; (+&#x60;Retry-After: 2&#x60;) · &#x60;idempotency_mismatch&#x60; · &#x60;version_conflict&#x60; · &#x60;ai_review_open&#x60; (publish of a product whose Dona AI review case is open — the review decides its status) · order codes &#x60;order_not_acceptable&#x60;, &#x60;no_pickup_address&#x60;, &#x60;order_not_shippable&#x60;, &#x60;order_awaiting_courier&#x60;, &#x60;order_not_cancellable&#x60;, &#x60;order_has_active_return&#x60; · document codes &#x60;no_tracking_number&#x60; (+&#x60;orders&#x60;), &#x60;no_items_selected&#x60;, &#x60;all_items_delayed&#x60; (S4, C53) · a replay of a rejected held write. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Cache-Control -  <br>  |
| **429** | &#x60;rate_limited&#x60; (with &#x60;Dona-Rate-Limited-Reason: app-rate&#x60;: a vendor app&#39;s bucket, shared by all its installs — S6) · &#x60;write_rate_limited&#x60; · &#x60;concurrency_limited&#x60; · &#x60;seller_rate_limited&#x60; · &#x60;object_cooldown&#x60; · &#x60;api_busy&#x60;. Always a JSON body + &#x60;Retry-After&#x60; from the origin (an edge 429 from Cloudflare has NO body — treat it as &#x60;Retry-After: 60&#x60;). Costs 0 and never counts toward the breaker. &#x60;rate_limited&#x60; is also the pre-auth ADDRESS guard, answered before the key is read: an address over 1 200 requests a minute that were not admitted (no key, a public route, a malformed, unknown or refused key — admitted requests never count), or one tarpitted at 60/min for 15 min after ≥ 20 unknown keys in a minute. No key is ever suspended by traffic that did not prove it. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * Cache-Control -  <br>  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **503** | &#x60;auth_unavailable&#x60; (key lookup failed — fail closed) · &#x60;limits_unavailable&#x60; (limiter blind on a write/MCP call, or a kill switch is off: &#x60;enabled&#x60;, &#x60;writes_enabled&#x60;, &#x60;webhooks_enabled&#x60;; &#x60;Retry-After: 30&#x60;) · &#x60;attention_busy&#x60; (an acknowledgement that resolves an item could not take the attention writer lock within 2 s — nothing was written; retry after &#x60;Retry-After: 2&#x60;) · &#x60;wallet_unavailable&#x60; (&#x60;/finance/_*&#x60;: the wallet could not answer for the shop; &#x60;Retry-After: 30&#x60;; its body is never relayed or error-copied — S4, C57) · &#x60;role_unavailable&#x60; (+ &#x60;served_by: \&quot;marketplace\&quot;&#x60;: a SERVER_ROLE&#x3D;seller-api server does not serve decline / cancel or &#x60;/finance/_*&#x60;; answered before any read or write, nothing changed; no &#x60;Retry-After&#x60; — D3). Costs 0. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="exportproducts"></a>
# **ExportProducts**
> JobAccepted ExportProducts (string idempotencyKey, ExportRequest exportRequest, string acceptLanguage = null, Guid donaSeller = null, string xDonaIntegration = null)

Export products (async)

CSV or JSONL. ≤ 2 running jobs per key, ≤ 20/day per shop. Not gated by `writes_enabled`.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **idempotencyKey** | **string** | 1–255 chars. Scope &#x3D; this key × route. Terminal 2xx/4xx replayed byte-identical for 24 h; a 5xx is never stored. Missing ⇒ &#x60;400 invalid_body&#x60; with &#x60;details[{field:\&quot;Idempotency-Key\&quot;,code:\&quot;required\&quot;}]&#x60;. |  |
| **exportRequest** | [**ExportRequest**](ExportRequest.md) |  |  |
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |
| **donaSeller** | **Guid** | Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional]  |
| **xDonaIntegration** | **string** | &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional]  |

### Return type

[**JobAccepted**](JobAccepted.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  * Location -  <br>  * Retry-After -  <br>  * Dona-Request-Id -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * X-Dona-Key-Expires -  <br>  * Dona-API-Warn -  <br>  * Deprecation -  <br>  * Sunset -  <br>  * Cache-Control -  <br>  |
| **400** | &#x60;invalid_body&#x60; — malformed JSON, a missing &#x60;Idempotency-Key&#x60;, validation (&#x60;details[]&#x60; carries field codes such as &#x60;ikpu_required&#x60;, &#x60;cursor_expired&#x60;), a &#x60;dry_run&#x60; / &#x60;Dona-Dry-Run&#x60; that is not the literal &#x60;true&#x60;/&#x60;false&#x60; (&#x60;details[{field, code:\&quot;invalid\&quot;}]&#x60;, C51), a vendor-app install key without &#x60;Dona-Seller&#x60; (&#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;, S6) or with a repeated / non-canonical one (&#x60;code:\&quot;invalid\&quot;&#x60;), or an op-specific 400 (&#x60;invalid_decline_reason&#x60;). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **401** | &#x60;api_key_malformed&#x60; (checksum fails — refused before any DB read) · &#x60;api_key_expired&#x60; (+&#x60;rotate_url&#x60;, no grace) · &#x60;api_key_revoked&#x60; (also a vendor-app key whose install was uninstalled — S6) · &#x60;key_kind_not_accepted&#x60; (an agent key &#x60;ak&#x60; on this tree) · &#x60;use_authorization_header&#x60; (&#x60;X-Api-Key&#x60; or a query-string key) · a seller/app/staff JWT on this tree. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **403** | &#x60;insufficient_scope&#x60; (+&#x60;required_scope&#x60;; also a scope in &#x60;disabled_scopes&#x60;) · &#x60;tier_required&#x60; (+&#x60;scope&#x60;; derived on every request; also a key minted for a third-party &#x60;orders:pii&#x60; recipient — &#x60;details[pii_recipient: pii_third_party_pending_counsel]&#x60;, D7, C59) · &#x60;key_suspended&#x60; (+&#x60;suspended_until&#x60;, &#x60;Retry-After&#x60;, &#x60;Dona-Rate-Limited-Reason: suspended&#x60;) · &#x60;api_blocked&#x60; · &#x60;ip_not_allowed&#x60; (judged on the trusted client IP only) · &#x60;seller_not_approved&#x60; (shop closed/blocked/suspended/restricted) · &#x60;not_a_seller&#x60; (never on this tree; the portal&#39;s owner doors) · &#x60;app_frozen&#x60; (S6: every key of a frozen vendor app, from the next request) · &#x60;agreement_required&#x60; (+&#x60;accept_url&#x60;: the shop owner has not accepted the CURRENT Annex 2 «API and automated access» — the version in force or, while none is, the earliest announced; accepted once in Settings › API, then every door admits the key again. Checked after the sanctions, before the scopes). |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |
| **409** | &#x60;idempotency_in_progress&#x60; (+&#x60;Retry-After: 2&#x60;) · &#x60;idempotency_mismatch&#x60; · &#x60;version_conflict&#x60; · &#x60;ai_review_open&#x60; (publish of a product whose Dona AI review case is open — the review decides its status) · order codes &#x60;order_not_acceptable&#x60;, &#x60;no_pickup_address&#x60;, &#x60;order_not_shippable&#x60;, &#x60;order_awaiting_courier&#x60;, &#x60;order_not_cancellable&#x60;, &#x60;order_has_active_return&#x60; · document codes &#x60;no_tracking_number&#x60; (+&#x60;orders&#x60;), &#x60;no_items_selected&#x60;, &#x60;all_items_delayed&#x60; (S4, C53) · a replay of a rejected held write. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Cache-Control -  <br>  |
| **429** | &#x60;rate_limited&#x60; (with &#x60;Dona-Rate-Limited-Reason: app-rate&#x60;: a vendor app&#39;s bucket, shared by all its installs — S6) · &#x60;write_rate_limited&#x60; · &#x60;concurrency_limited&#x60; · &#x60;seller_rate_limited&#x60; · &#x60;object_cooldown&#x60; · &#x60;api_busy&#x60;. Always a JSON body + &#x60;Retry-After&#x60; from the origin (an edge 429 from Cloudflare has NO body — treat it as &#x60;Retry-After: 60&#x60;). Costs 0 and never counts toward the breaker. &#x60;rate_limited&#x60; is also the pre-auth ADDRESS guard, answered before the key is read: an address over 1 200 requests a minute that were not admitted (no key, a public route, a malformed, unknown or refused key — admitted requests never count), or one tarpitted at 60/min for 15 min after ≥ 20 unknown keys in a minute. No key is ever suspended by traffic that did not prove it. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * Cache-Control -  <br>  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **503** | &#x60;auth_unavailable&#x60; (key lookup failed — fail closed) · &#x60;limits_unavailable&#x60; (limiter blind on a write/MCP call, or a kill switch is off: &#x60;enabled&#x60;, &#x60;writes_enabled&#x60;, &#x60;webhooks_enabled&#x60;; &#x60;Retry-After: 30&#x60;) · &#x60;attention_busy&#x60; (an acknowledgement that resolves an item could not take the attention writer lock within 2 s — nothing was written; retry after &#x60;Retry-After: 2&#x60;) · &#x60;wallet_unavailable&#x60; (&#x60;/finance/_*&#x60;: the wallet could not answer for the shop; &#x60;Retry-After: 30&#x60;; its body is never relayed or error-copied — S4, C57) · &#x60;role_unavailable&#x60; (+ &#x60;served_by: \&quot;marketplace\&quot;&#x60;: a SERVER_ROLE&#x3D;seller-api server does not serve decline / cancel or &#x60;/finance/_*&#x60;; answered before any read or write, nothing changed; no &#x60;Retry-After&#x60; — D3). Costs 0. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getjob"></a>
# **GetJob**
> Job GetJob (Guid id, string acceptLanguage = null, Guid donaSeller = null, string xDonaIntegration = null)

Poll a job

Readable by any key of the shop that holds the scope the job's kind needs (`catalog:read` for `export_products`, `orders:read` for `export_orders`, `catalog:write` for `products_batch`); otherwise `404 not_found`. Poll ≥ 5 s (`Retry-After` is set while pending/running). After `expires_at` (7 d) ⇒ `404 not_found`.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **id** | **Guid** | Resource id (UUIDv7). A foreign or missing id is always &#x60;404 not_found&#x60;. |  |
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |
| **donaSeller** | **Guid** | Vendor-app install keys only (&#x60;dona_it_live_…&#x60;, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;required\&quot;}]&#x60;; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no &#x60;urn:uuid:&#x60;, no padding) ⇒ &#x60;400 invalid_body&#x60; + &#x60;details[{field:\&quot;Dona-Seller\&quot;, code:\&quot;invalid\&quot;}]&#x60;; naming any other shop — even one that installed the same app ⇒ &#x60;404 not_found&#x60; (never 403; nothing is read). Ignored on a seller key (&#x60;dona_sk_&#x60;). | [optional]  |
| **xDonaIntegration** | **string** | &#x60;name/version&#x60; of the calling integration; stored (≤ 128 chars) and searchable in the request journal. | [optional]  |

### Return type

[**Job**](Job.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Dona-Request-Id -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * X-Dona-Key-Expires -  <br>  * Dona-API-Warn -  <br>  * Deprecation -  <br>  * Sunset -  <br>  * Cache-Control -  <br>  * Retry-After -  <br>  |
| **401** | &#x60;api_key_malformed&#x60; (checksum fails — refused before any DB read) · &#x60;api_key_expired&#x60; (+&#x60;rotate_url&#x60;, no grace) · &#x60;api_key_revoked&#x60; (also a vendor-app key whose install was uninstalled — S6) · &#x60;key_kind_not_accepted&#x60; (an agent key &#x60;ak&#x60; on this tree) · &#x60;use_authorization_header&#x60; (&#x60;X-Api-Key&#x60; or a query-string key) · a seller/app/staff JWT on this tree. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **403** | &#x60;insufficient_scope&#x60; (+&#x60;required_scope&#x60;; also a scope in &#x60;disabled_scopes&#x60;) · &#x60;tier_required&#x60; (+&#x60;scope&#x60;; derived on every request; also a key minted for a third-party &#x60;orders:pii&#x60; recipient — &#x60;details[pii_recipient: pii_third_party_pending_counsel]&#x60;, D7, C59) · &#x60;key_suspended&#x60; (+&#x60;suspended_until&#x60;, &#x60;Retry-After&#x60;, &#x60;Dona-Rate-Limited-Reason: suspended&#x60;) · &#x60;api_blocked&#x60; · &#x60;ip_not_allowed&#x60; (judged on the trusted client IP only) · &#x60;seller_not_approved&#x60; (shop closed/blocked/suspended/restricted) · &#x60;not_a_seller&#x60; (never on this tree; the portal&#39;s owner doors) · &#x60;app_frozen&#x60; (S6: every key of a frozen vendor app, from the next request) · &#x60;agreement_required&#x60; (+&#x60;accept_url&#x60;: the shop owner has not accepted the CURRENT Annex 2 «API and automated access» — the version in force or, while none is, the earliest announced; accepted once in Settings › API, then every door admits the key again. Checked after the sanctions, before the scopes). |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |
| **404** | &#x60;not_found&#x60; — every missing OR foreign id (never 403: no existence oracle). |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **429** | &#x60;rate_limited&#x60; (with &#x60;Dona-Rate-Limited-Reason: app-rate&#x60;: a vendor app&#39;s bucket, shared by all its installs — S6) · &#x60;write_rate_limited&#x60; · &#x60;concurrency_limited&#x60; · &#x60;seller_rate_limited&#x60; · &#x60;object_cooldown&#x60; · &#x60;api_busy&#x60;. Always a JSON body + &#x60;Retry-After&#x60; from the origin (an edge 429 from Cloudflare has NO body — treat it as &#x60;Retry-After: 60&#x60;). Costs 0 and never counts toward the breaker. &#x60;rate_limited&#x60; is also the pre-auth ADDRESS guard, answered before the key is read: an address over 1 200 requests a minute that were not admitted (no key, a public route, a malformed, unknown or refused key — admitted requests never count), or one tarpitted at 60/min for 15 min after ≥ 20 unknown keys in a minute. No key is ever suspended by traffic that did not prove it. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * RateLimit-Policy -  <br>  * RateLimit -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * Cache-Control -  <br>  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **503** | &#x60;auth_unavailable&#x60; (key lookup failed — fail closed) · &#x60;limits_unavailable&#x60; (limiter blind on a write/MCP call, or a kill switch is off: &#x60;enabled&#x60;, &#x60;writes_enabled&#x60;, &#x60;webhooks_enabled&#x60;; &#x60;Retry-After: 30&#x60;) · &#x60;attention_busy&#x60; (an acknowledgement that resolves an item could not take the attention writer lock within 2 s — nothing was written; retry after &#x60;Retry-After: 2&#x60;) · &#x60;wallet_unavailable&#x60; (&#x60;/finance/_*&#x60;: the wallet could not answer for the shop; &#x60;Retry-After: 30&#x60;; its body is never relayed or error-copied — S4, C57) · &#x60;role_unavailable&#x60; (+ &#x60;served_by: \&quot;marketplace\&quot;&#x60;: a SERVER_ROLE&#x3D;seller-api server does not serve decline / cancel or &#x60;/finance/_*&#x60;; answered before any read or write, nothing changed; no &#x60;Retry-After&#x60; — D3). Costs 0. |  * Dona-Request-Id -  <br>  * Retry-After -  <br>  * Dona-Rate-Limited-Reason -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)


# Dona.Api.Api.MetaApi

All URIs are relative to *https://api.dona.im/seller-api/v1*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetChangelog**](MetaApi.md#getchangelog) | **GET** /changelog | Changelog (JSON, or RSS with Accept) |
| [**GetLlmsTxt**](MetaApi.md#getllmstxt) | **GET** /llms.txt | llms.txt index for AI agents |
| [**GetOpenApi**](MetaApi.md#getopenapi) | **GET** /openapi.json | This document |
| [**GetStatus**](MetaApi.md#getstatus) | **GET** /status | Service status |
| [**Ping**](MetaApi.md#ping) | **GET** /ping | Liveness (key optional) |

<a id="getchangelog"></a>
# **GetChangelog**
> ChangelogEntryPage GetChangelog (string cursor = null, int limit = null, string acceptLanguage = null)

Changelog (JSON, or RSS with Accept)

Public. `Accept: application/rss+xml` returns RSS. Backed by `seller_api_changelog` (0465, S4) — an empty list until then.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **cursor** | **string** | Opaque keyset cursor from &#x60;next_cursor&#x60;. | [optional]  |
| **limit** | **int** | Page size, default 50, max 100 (clamped, with &#x60;Dona-API-Warn&#x60;). &#x60;limit &gt; 50&#x60; costs &#x60;1 + ceil(limit/50)&#x60;. | [optional] [default to 50] |
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |

### Return type

[**ChangelogEntryPage**](ChangelogEntryPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/rss+xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Dona-Request-Id -  <br>  |
| **429** | Cloudflare edge, per-IP 60/min on public routes. **No JSON body** (the edge eats it) — treat as &#x60;Retry-After: 60&#x60;. |  -  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getllmstxt"></a>
# **GetLlmsTxt**
> string GetLlmsTxt (string acceptLanguage = null)

llms.txt index for AI agents

Plain-text index of the docs + spec links (`llms-full.txt` beside it).


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |

### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Dona-Request-Id -  <br>  |
| **429** | Cloudflare edge, per-IP 60/min on public routes. **No JSON body** (the edge eats it) — treat as &#x60;Retry-After: 60&#x60;. |  -  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getopenapi"></a>
# **GetOpenApi**
> Object GetOpenApi (string acceptLanguage = null)

This document

OpenAPI 3.1, public, `Cache-Control: public, max-age=300`.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Dona-Request-Id -  <br>  |
| **429** | Cloudflare edge, per-IP 60/min on public routes. **No JSON body** (the edge eats it) — treat as &#x60;Retry-After: 60&#x60;. |  -  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="getstatus"></a>
# **GetStatus**
> Status GetStatus (string acceptLanguage = null)

Service status

Public; edge-cacheable 60 s; linked from every 503's `doc_url`.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Dona-Request-Id -  <br>  |
| **429** | Cloudflare edge, per-IP 60/min on public routes. **No JSON body** (the edge eats it) — treat as &#x60;Retry-After: 60&#x60;. |  -  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

<a id="ping"></a>
# **Ping**
> Ping Ping (string acceptLanguage = null)

Liveness (key optional)

Public. Without `Authorization` it answers `authenticated:false`. With a key the key is fully verified — a bad key is `401`, never a silent `false`.


### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **acceptLanguage** | **string** | Localises &#x60;message&#x60; in error bodies and single-language renderings. Default &#x60;uz&#x60;. | [optional] [default to &quot;uz&quot;] |

### Return type

[**Ping**](Ping.md)

### Authorization

[bearerKey](../README.md#bearerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Dona-Request-Id -  <br>  |
| **401** | &#x60;api_key_malformed&#x60; (checksum fails — refused before any DB read) · &#x60;api_key_expired&#x60; (+&#x60;rotate_url&#x60;, no grace) · &#x60;api_key_revoked&#x60; · &#x60;use_authorization_header&#x60; (&#x60;X-Api-Key&#x60; or a query-string key) · a seller/app/staff JWT on this tree. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |
| **500** | &#x60;internal_error&#x60; — details are in the redacted error copy, never here. Costs 0. |  * Dona-Request-Id -  <br>  * Cache-Control -  <br>  |

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)


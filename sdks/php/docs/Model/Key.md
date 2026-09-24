# Key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**name** | **string** |  |
**kind** | **string** | &#x60;sk&#x60; seller integration · &#x60;ak&#x60; AI agent (MCP) · &#x60;it&#x60; vendor install (S6). Known values (open set — tolerate new ones): &#x60;sk&#x60;, &#x60;ak&#x60;, &#x60;it&#x60;. |
**env** | **string** | Known values (open set — tolerate new ones): &#x60;live&#x60;. |
**prefix** | **string** |  |
**last4** | **string** |  |
**scopes** | **string[]** |  |
**state** | **string** | Known values (open set — tolerate new ones): &#x60;active&#x60;, &#x60;suspended&#x60;, &#x60;revoked&#x60;, &#x60;expired&#x60;. |
**expiring_soon** | **bool** | True in the last 30 days (the first &#x60;key_expiring&#x60; step). |
**expires_at** | **\DateTime** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). |
**last_used_at** | **\DateTime** |  |
**ip_allow** | **string[]** |  |
**rotated_from** | **string** |  |
**overlap_until** | **\DateTime** |  |
**suspended_until** | **\DateTime** |  |
**created_at** | **\DateTime** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

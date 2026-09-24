# WebhookWithSecret

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**url** | **string** |  |
**event_types** | **string[]** | Exact event names or prefixes (&#x60;order.*&#x60;); &#x60;[\&quot;*\&quot;]&#x60; (or omitted on create) &#x3D; every event. |
**status** | **string** | Known values (open set — tolerate new ones): &#x60;active&#x60;, &#x60;paused&#x60;, &#x60;disabled&#x60;. |
**failing_since** | **\DateTime** |  |
**disabled_reason** | **string** | Known values (open set — tolerate new ones): &#x60;ladder_exhausted&#x60;, &#x60;success_rate&#x60;, &#x60;owner&#x60;, &#x60;staff&#x60;, &#x60;ssrf_recheck&#x60;. |
**consecutive_failures** | **int** |  |
**last_delivered_at** | **\DateTime** |  |
**success_rate_24h** | **float** |  |
**secret_rotating_until** | **\DateTime** | While set, deliveries carry two signatures. |
**created_at** | **\DateTime** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). |
**updated_at** | **\DateTime** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). |
**secret** | **string** | &#x60;whsec_…&#x60; — shown ONCE. An idempotent replay of this call returns &#x60;null&#x60;: the secret is never stored in the replay table. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

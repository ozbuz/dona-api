# Dona.Api.Model.WebhookWithSecret

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**Url** | **string** |  | 
**EventTypes** | **List&lt;string&gt;** | Exact event names or prefixes (&#x60;order.*&#x60;); &#x60;[\&quot;*\&quot;]&#x60; (or omitted on create) &#x3D; every event. | 
**Status** | **string** | Known values (open set — tolerate new ones): &#x60;active&#x60;, &#x60;paused&#x60;, &#x60;disabled&#x60;. | 
**FailingSince** | **DateTimeOffset** |  | 
**DisabledReason** | **string** | Known values (open set — tolerate new ones): &#x60;ladder_exhausted&#x60;, &#x60;success_rate&#x60;, &#x60;owner&#x60;, &#x60;staff&#x60;, &#x60;ssrf_recheck&#x60;. | 
**ConsecutiveFailures** | **int** |  | 
**LastDeliveredAt** | **DateTimeOffset** |  | 
**SuccessRate24h** | **decimal** |  | 
**SecretRotatingUntil** | **DateTimeOffset** | While set, deliveries carry two signatures. | 
**CreatedAt** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). | 
**UpdatedAt** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). | 
**Secret** | **string** | &#x60;whsec_…&#x60; — shown ONCE. An idempotent replay of this call returns &#x60;null&#x60;: the secret is never stored in the replay table. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


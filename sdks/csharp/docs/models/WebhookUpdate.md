# Dona.Api.Model.WebhookUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Url** | **string** |  | [optional] 
**EventTypes** | **List&lt;string&gt;** | Exact event names or prefixes (&#x60;order.*&#x60;); &#x60;[\&quot;*\&quot;]&#x60; (or omitted on create) &#x3D; every event. | [optional] 
**Status** | **string** | &#x60;paused&#x60; &#x3D; seller-side pause (deliveries accrue 30 d); &#x60;active&#x60; resumes a paused endpoint. A &#x60;disabled&#x60; endpoint is re-enabled only by a successful &#x60;/ping&#x60;. Known values (open set — tolerate new ones): &#x60;active&#x60;, &#x60;paused&#x60;. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


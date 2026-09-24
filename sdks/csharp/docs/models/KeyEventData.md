# Dona.Api.Model.KeyEventData
Never the secret.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**KeyId** | **Guid** |  | 
**Prefix** | **string** |  | 
**ExpiresAt** | **DateTimeOffset** |  | [optional] 
**SuspendedUntil** | **DateTimeOffset** |  | [optional] 
**ReasonCode** | **string** | &#x60;key.suspended&#x60; only: the suspension&#39;s code (&#x60;error_storm&#x60;, &#x60;ip_blocked&#x60;, &#x60;staff&#x60;, …) — never the words staff typed (an internal note); null for anything outside the vocabulary. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


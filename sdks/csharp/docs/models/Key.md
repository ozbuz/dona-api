# Dona.Api.Model.Key
Never a secret: no field of any GET matches `dona_(sk|ak|it)_live_` beyond `prefix`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**Name** | **string** |  | 
**Kind** | **string** | &#x60;sk&#x60; seller integration · &#x60;ak&#x60; AI agent (MCP) · &#x60;it&#x60; vendor install (S6). Known values (open set — tolerate new ones): &#x60;sk&#x60;, &#x60;ak&#x60;, &#x60;it&#x60;. | 
**Env** | **string** | Known values (open set — tolerate new ones): &#x60;live&#x60;. | 
**Prefix** | **string** |  | 
**Last4** | **string** |  | 
**Scopes** | **List&lt;string&gt;** |  | 
**State** | **string** | Known values (open set — tolerate new ones): &#x60;active&#x60;, &#x60;suspended&#x60;, &#x60;revoked&#x60;, &#x60;expired&#x60;. | 
**ExpiringSoon** | **bool** | True in the last 30 days (the first &#x60;key_expiring&#x60; step). | 
**ExpiresAt** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). | 
**IpAllow** | **List&lt;string&gt;** |  | 
**CreatedAt** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). | 
**LastUsedAt** | **DateTimeOffset** |  | 
**RotatedFrom** | **Guid** |  | 
**OverlapUntil** | **DateTimeOffset** |  | 
**SuspendedUntil** | **DateTimeOffset** |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


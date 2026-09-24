# Dona.Api.Model.MeKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**Name** | **string** |  | 
**Kind** | **string** | &#x60;sk&#x60; seller integration · &#x60;ak&#x60; AI agent (MCP) · &#x60;it&#x60; vendor install (S6). Known values (open set — tolerate new ones): &#x60;sk&#x60;, &#x60;ak&#x60;, &#x60;it&#x60;. | 
**Prefix** | **string** | First 16 characters; not a secret. | 
**Scopes** | **List&lt;string&gt;** |  | 
**ExpiresAt** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). | 
**IpAllow** | **List&lt;string&gt;** |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


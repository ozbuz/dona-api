# Dona.Api.Model.ChangelogEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**VarVersion** | **string** |  | 
**Kind** | **string** | Known values (open set — tolerate new ones): &#x60;added&#x60;, &#x60;changed&#x60;, &#x60;deprecated&#x60;, &#x60;removed&#x60;, &#x60;fixed&#x60;, &#x60;security&#x60;. | 
**Title** | [**LocalizedText**](LocalizedText.md) |  | 
**Body** | [**LocalizedText**](LocalizedText.md) |  | 
**AffectsScopes** | **List&lt;string&gt;** |  | 
**PublishedAt** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). | 
**SunsetAt** | **DateTimeOffset** |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


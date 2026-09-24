# Dona.Api.Model.Status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**VarStatus** | **string** | Known values (open set — tolerate new ones): &#x60;operational&#x60;, &#x60;degraded&#x60;, &#x60;outage&#x60;. | 
**Components** | [**StatusComponents**](StatusComponents.md) |  | 
**Incidents** | [**List&lt;StatusIncidentsInner&gt;**](StatusIncidentsInner.md) |  | 
**UpdatedAt** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


# Dona.Api.Model.OrderTimelineEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**Type** | **string** | &#x60;placed&#x60;, &#x60;paid&#x60;, &#x60;accepted&#x60;, &#x60;declined&#x60;, &#x60;shipped&#x60;, &#x60;delivered&#x60;, &#x60;cancelled&#x60;, &#x60;line_cancelled&#x60;, … | 
**Actor** | **string** | &#x60;system&#x60;, &#x60;seller&#x60;, &#x60;buyer&#x60;, &#x60;courier&#x60;, &#x60;support&#x60; | 
**OccurredAt** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). | 
**Note** | **string** | Dona/staff-authored only; buyer text never appears here. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


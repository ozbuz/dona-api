# Dona.Api.Model.OrderEventData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**OrderId** | **Guid** |  | 
**Status** | **string** |  | 
**PaymentStatus** | **string** |  | 
**PaymentMethod** | **string** |  | 
**Scheme** | **string** | Known values (open set — tolerate new ones): &#x60;own_fleet&#x60;, &#x60;third_party&#x60;. | 
**TotalUzs** | **long** | Integer soʻm (no decimals). | 
**UpdatedAt** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). | 
**AcceptDeadline** | **DateTimeOffset** |  | [optional] 
**ShipByDeadline** | **DateTimeOffset** |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


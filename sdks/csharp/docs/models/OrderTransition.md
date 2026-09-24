# Dona.Api.Model.OrderTransition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**Status** | **string** |  | 
**PaymentStatus** | **string** |  | 
**UpdatedAt** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). | 
**AcceptedAt** | **DateTimeOffset** |  | 
**ShippedAt** | **DateTimeOffset** |  | 
**CancelledBy** | **string** | Known values (open set — tolerate new ones): &#x60;seller&#x60;, &#x60;buyer&#x60;, &#x60;system&#x60;. | 
**DeclineReasonCode** | **string** |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


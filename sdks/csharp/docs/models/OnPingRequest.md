# Dona.Api.Model.OnPingRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** | uuidv7 — also the &#x60;/events&#x60; cursor and the webhook &#x60;webhook-id&#x60;. | 
**Type** | **string** |  | 
**OccurredAt** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). | 
**SellerId** | **Guid** |  | 
**ApiVersion** | **string** |  | 
**Data** | [**PingEventData**](PingEventData.md) |  | 
**Links** | [**EventLinks**](EventLinks.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


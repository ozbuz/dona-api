# Dona.Api.Model.Order
The `orders:read` projection — built from an explicit column list. No `buyer`, `phone`, `address`, `recipient` key exists (JSON-schema test at the S3 gate).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**OrderCode** | **string** | Display handle (0164), e.g. &#x60;AB1765543210XZ&#x60;; never a route param. | 
**Status** | **string** | &#x60;pending&#x60;, &#x60;paid&#x60;, &#x60;ready_to_ship&#x60;, &#x60;shipped&#x60;, &#x60;delivered&#x60;, &#x60;cancelled&#x60;; tolerate new values. | 
**PaymentStatus** | **string** |  | 
**PaymentMethod** | **string** |  | 
**Scheme** | **string** | Derived: &#x60;own_fleet&#x60; when the shipment rides the default channel, else &#x60;third_party&#x60;. Known values (open set — tolerate new ones): &#x60;own_fleet&#x60;, &#x60;third_party&#x60;. | 
**TotalUzs** | **long** | Integer soʻm (no decimals). | 
**Items** | [**List&lt;OrderItem&gt;**](OrderItem.md) |  | 
**Meta** | [**OrderMeta**](OrderMeta.md) |  | 
**CreatedAt** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). | 
**UpdatedAt** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). | 
**AcceptedAt** | **DateTimeOffset** |  | 
**DeclinedAt** | **DateTimeOffset** |  | 
**ShippedAt** | **DateTimeOffset** |  | 
**DeliveredAt** | **DateTimeOffset** |  | 
**CancelledBy** | **string** | Known values (open set — tolerate new ones): &#x60;seller&#x60;, &#x60;buyer&#x60;, &#x60;system&#x60;. | 
**DeclineReasonCode** | **string** |  | 
**AcceptDeadline** | **DateTimeOffset** |  | 
**ShipByDeadline** | **DateTimeOffset** |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


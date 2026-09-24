# Dona.Api.Model.Return

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**OrderId** | **Guid** |  | 
**Status** | **string** | Known values (open set — tolerate new ones): &#x60;requested&#x60;, &#x60;approved&#x60;, &#x60;refunded&#x60;, &#x60;rejected&#x60;, &#x60;disputed&#x60;, &#x60;closed&#x60;. | 
**Type** | **string** |  | 
**ReasonCode** | **string** |  | 
**RefundUzs** | **long** | Integer soʻm (no decimals). | 
**Items** | [**List&lt;ReturnItemsInner&gt;**](ReturnItemsInner.md) |  | 
**CreatedAt** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). | 
**UpdatedAt** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). | 
**DueAt** | **DateTimeOffset** |  | 
**ReasonText** | **string** | Buyer-authored; detail only (null on lists). | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


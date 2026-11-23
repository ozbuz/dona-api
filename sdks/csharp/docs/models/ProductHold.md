# Dona.Api.Model.ProductHold

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Reason** | **string** | &#x60;shop_not_activated&#x60; — a pending shop&#39;s publish waits in &#x60;product_shop_holds&#x60;. &#x60;unfulfilled_order&#x60; — an order the shop did not fulfil took the product off sale (fulfilment holds); it stays off sale whatever its status until the seller re-enables it at &#x60;ack_url&#x60;. | 
**AckUrl** | **string** | With &#x60;reason&#x3D;unfulfilled_order&#x60; only: the seller portal page that releases the product (&#x60;https://seller.dona.uz/products/{id}?release&#x3D;1&#x60;). The API never releases a fulfilment hold — the seller acknowledges in the portal or the app. | [optional] 
**Since** | **DateTimeOffset** | With &#x60;reason&#x3D;unfulfilled_order&#x60; on a product read: when the fulfilment hold began (ISO 8601, Tashkent &#x60;+05:00&#x60;). | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


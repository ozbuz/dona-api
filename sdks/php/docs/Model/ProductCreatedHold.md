# ProductCreatedHold

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **string** | &#x60;shop_not_activated&#x60; · a category requirement · &#x60;unfulfilled_order&#x60; (a fulfilment hold keeps it off sale: the write succeeded; release at &#x60;ack_url&#x60;). |
**ack_url** | **string** | With &#x60;reason&#x3D;unfulfilled_order&#x60; only: the seller portal page that releases the product (&#x60;https://seller.dona.uz/products/{id}?release&#x3D;1&#x60;). The API never releases a fulfilment hold — the seller acknowledges in the portal or the app. | [optional]
**since** | **\DateTime** | With &#x60;reason&#x3D;unfulfilled_order&#x60; on a product read: when the fulfilment hold began (ISO 8601, Tashkent &#x60;+05:00&#x60;). | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

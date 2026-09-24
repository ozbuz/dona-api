# StockLine

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **string** |  | [optional]
**seller_sku** | **string** |  | [optional]
**barcode** | **string** |  | [optional]
**external_id** | **string** |  | [optional]
**variant_id** | **string** |  | [optional]
**quantity** | **int** | ABSOLUTE stock (not a delta). |
**version** | **string** | Optional; stale ⇒ line &#x60;error: version_conflict&#x60;. | [optional]
**warehouse** | **string** | Reserved — one stock location per shop. Any value ⇒ the whole request &#x60;422 warehouse_unsupported&#x60;. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

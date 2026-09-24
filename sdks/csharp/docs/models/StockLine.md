# Dona.Api.Model.StockLine
Exactly ONE of `product_id` · `seller_sku` · `barcode` · `external_id`, plus optional `variant_id`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Quantity** | **int** | ABSOLUTE stock (not a delta). | 
**ProductId** | **Guid** |  | [optional] 
**SellerSku** | **string** |  | [optional] 
**Barcode** | **string** |  | [optional] 
**ExternalId** | **string** |  | [optional] 
**VariantId** | **Guid** |  | [optional] 
**VarVersion** | **string** | Optional; stale ⇒ line &#x60;error: version_conflict&#x60;. | [optional] 
**Warehouse** | **string** | Reserved — one stock location per shop. Any value ⇒ the whole request &#x60;422 warehouse_unsupported&#x60;. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


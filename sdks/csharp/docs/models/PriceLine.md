# Dona.Api.Model.PriceLine
Exactly ONE of `product_id` · `seller_sku` · `barcode` · `external_id`, plus optional `variant_id`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**PriceUzs** | **long** | ABSOLUTE price. | 
**ProductId** | **Guid** |  | [optional] 
**SellerSku** | **string** |  | [optional] 
**Barcode** | **string** |  | [optional] 
**ExternalId** | **string** |  | [optional] 
**VariantId** | **Guid** |  | [optional] 
**CompareAtUzs** | **long** | Must exceed &#x60;price_uzs&#x60;; &#x60;null&#x60; clears. | [optional] 
**VarVersion** | **string** |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


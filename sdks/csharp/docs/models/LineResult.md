# Dona.Api.Model.LineResult
Echoes the line's key fields as sent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Index** | **int** |  | 
**Status** | **string** | Known values (open set — tolerate new ones): &#x60;ok&#x60;, &#x60;error&#x60;, &#x60;held&#x60;. | 
**ProductId** | **Guid** |  | [optional] 
**VariantId** | **Guid** |  | [optional] 
**SellerSku** | **string** |  | [optional] 
**Barcode** | **string** |  | [optional] 
**ExternalId** | **string** |  | [optional] 
**Quantity** | **int** |  | [optional] 
**PriceUzs** | **long** |  | [optional] 
**CompareAtUzs** | **long** |  | [optional] 
**VarVersion** | **string** | New version after an &#x60;ok&#x60; line. | [optional] 
**Error** | **string** | On &#x60;status&#x3D;error&#x60;: &#x60;version_conflict&#x60;, &#x60;object_cooldown&#x60;, &#x60;not_found&#x60;, &#x60;stock_not_editable&#x60;, &#x60;invalid_body&#x60;, … | [optional] 
**Message** | **string** |  | [optional] 
**RetryAfterSeconds** | **int** | On &#x60;object_cooldown&#x60;. | [optional] 
**ApprovalId** | **Guid** |  | [optional] 
**Rule** | **string** | Known values (open set — tolerate new ones): &#x60;price_floor&#x60;, &#x60;drop_100x&#x60;, &#x60;stock_jump_10x&#x60;, &#x60;mass_zero_50pct&#x60;, &#x60;delist_30pct&#x60;, &#x60;confirmation_required&#x60;. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


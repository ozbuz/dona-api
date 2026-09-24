# LineResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  |
**status** | **string** | Known values (open set — tolerate new ones): &#x60;ok&#x60;, &#x60;error&#x60;, &#x60;held&#x60;. |
**product_id** | **string** |  | [optional]
**variant_id** | **string** |  | [optional]
**seller_sku** | **string** |  | [optional]
**barcode** | **string** |  | [optional]
**external_id** | **string** |  | [optional]
**quantity** | **int** |  | [optional]
**price_uzs** | **int** |  | [optional]
**compare_at_uzs** | **int** |  | [optional]
**version** | **string** | New version after an &#x60;ok&#x60; line. | [optional]
**error** | **string** | On &#x60;status&#x3D;error&#x60;: &#x60;version_conflict&#x60;, &#x60;object_cooldown&#x60;, &#x60;not_found&#x60;, &#x60;stock_not_editable&#x60;, &#x60;invalid_body&#x60;, … | [optional]
**message** | **string** |  | [optional]
**retry_after_seconds** | **int** | On &#x60;object_cooldown&#x60;. | [optional]
**approval_id** | **string** |  | [optional]
**rule** | **string** | Known values (open set — tolerate new ones): &#x60;price_floor&#x60;, &#x60;drop_100x&#x60;, &#x60;stock_jump_10x&#x60;, &#x60;mass_zero_50pct&#x60;, &#x60;delist_30pct&#x60;, &#x60;confirmation_required&#x60;. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

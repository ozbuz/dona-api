# WriteEventData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_id** | **string** |  |
**kind** | **string** | Known values (open set — tolerate new ones): &#x60;price&#x60;, &#x60;stock&#x60;, &#x60;product&#x60;, &#x60;delist&#x60;. |
**subject_type** | **string** | Known values (open set — tolerate new ones): &#x60;product&#x60;, &#x60;product_variant&#x60;, &#x60;batch&#x60;. |
**subject_id** | **string** |  |
**rule** | **string** | Known values (open set — tolerate new ones): &#x60;price_floor&#x60;, &#x60;drop_100x&#x60;, &#x60;stock_jump_10x&#x60;, &#x60;mass_zero_50pct&#x60;, &#x60;delist_30pct&#x60;, &#x60;confirmation_required&#x60;. |
**decided_by_kind** | **string** | Known values (open set — tolerate new ones): &#x60;owner&#x60;, &#x60;staff&#x60;. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

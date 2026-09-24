# Dona.Api.Model.WriteEventData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ApprovalId** | **Guid** |  | 
**Kind** | **string** | Known values (open set — tolerate new ones): &#x60;price&#x60;, &#x60;stock&#x60;, &#x60;product&#x60;, &#x60;delist&#x60;. | 
**SubjectType** | **string** | Known values (open set — tolerate new ones): &#x60;product&#x60;, &#x60;product_variant&#x60;, &#x60;batch&#x60;. | 
**Rule** | **string** | Known values (open set — tolerate new ones): &#x60;price_floor&#x60;, &#x60;drop_100x&#x60;, &#x60;stock_jump_10x&#x60;, &#x60;mass_zero_50pct&#x60;, &#x60;delist_30pct&#x60;, &#x60;confirmation_required&#x60;. | 
**SubjectId** | **Guid** |  | 
**DecidedByKind** | **string** | Known values (open set — tolerate new ones): &#x60;owner&#x60;, &#x60;staff&#x60;. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


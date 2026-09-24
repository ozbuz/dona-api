# Dona.Api.Model.CategoryRequirements
The live `GET /catalog/categories/{id}/requirements` payload (`internal/catalog/requirements.go`), resolved through the tree — one shape for the form and the API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CategoryId** | **Guid** |  | 
**Status** | **string** |  | 
**ListingPolicy** | **string** | &#x60;open&#x60; default; &#x60;approval_required&#x60;, &#x60;licensed&#x60;, &#x60;restricted&#x60;, &#x60;prohibited&#x60;. | 
**IsLeaf** | **bool** |  | 
**CanList** | **bool** | &#x60;status&#x3D;active AND is_leaf AND listing_policy &lt;&gt; prohibited&#x60;. | 
**MinImages** | **int** |  | 
**RequiresDimensions** | **bool** |  | 
**RequiresBrand** | **bool** |  | 
**RequiresSizeChart** | **bool** |  | 
**Attributes** | [**List&lt;CategoryAttribute&gt;**](CategoryAttribute.md) |  | 
**CommissionPct** | **decimal** |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


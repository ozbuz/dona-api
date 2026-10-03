# Dona.Api.Model.CategoryRequirements
The live `GET /catalog/categories/{id}/requirements` payload (`internal/catalog/requirements.go`), resolved through the tree — one shape for the form and the API, plus the two per-shop commission fields.

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
**EffectiveCommissionPct** | **decimal** | The rate a sale in this category is charged for the key&#39;s shop: the category rate (or the platform default), then the highest-ranked commission rule for this shop (a launch offer, a cohort, a shop-specific rate, a rule scoped to this category), then the shop&#39;s commission campaigns (the lowest of the general rate, each exclusive campaign alone and the stack of combinable ones — never above the general rate). A shop on a 0 % offer reads 0. Equals the seller portal&#39;s number and what checkout charges. | 
**Attributes** | [**List&lt;CategoryAttribute&gt;**](CategoryAttribute.md) |  | 
**CommissionPct** | **decimal** | The category&#39;s own rate (nearest ancestor with a rate), the same for every shop; &#x60;null&#x60; when the tree carries none (the platform default then applies). | 
**CommissionOfferEndsAt** | **DateTimeOffset** | When the rule or campaign behind &#x60;effective_commission_pct&#x60; stops applying (orders placed before it keep their rate; a campaign&#39;s is its last second). &#x60;null&#x60; when none applies, it has no end, or the offer is still promised (the shop has not opened). | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


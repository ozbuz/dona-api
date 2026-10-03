# Dona.Api.Model.CommissionRoot
One active top-level category and the range of its active leaves' rates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**Slug** | **string** |  | 
**Name** | [**LocalizedText**](LocalizedText.md) |  | 
**MinPct** | **decimal** |  | 
**MaxPct** | **decimal** |  | 
**LeafCount** | **long** |  | 
**L2Names** | [**List&lt;LocalizedText&gt;**](LocalizedText.md) |  | 
**EffectiveMinPct** | **decimal** | This shop&#39;s lowest rate in the category after its commission rules and campaigns (what a sale is charged). &#x60;min_pct&#x60; / &#x60;max_pct&#x60; stay the platform&#39;s card. | 
**EffectiveMaxPct** | **decimal** | This shop&#39;s highest rate in the category after its commission rules and campaigns. | 
**ThumbUrl** | **string** |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


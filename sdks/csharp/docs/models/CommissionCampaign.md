# Dona.Api.Model.CommissionCampaign

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CampaignId** | **Guid** |  | 
**GrantId** | **Guid** |  | 
**Code** | **string** | The campaign&#39;s handle (e.g. &#x60;LAUNCH-0&#x60;). | 
**Name** | [**LocalizedText**](LocalizedText.md) |  | 
**Kind** | **string** | Known values (open set — tolerate new ones): &#x60;new_registration&#x60;, &#x60;existing_seller&#x60;, &#x60;invite&#x60;, &#x60;sales_target&#x60;. | 
**State** | **string** | &#x60;running&#x60;: the grant prices the shop now (a grant that starts later is listed from its start). &#x60;promised&#x60;: it opens the day the shop opens; nothing is dated until then. Known values (open set — tolerate new ones): &#x60;running&#x60;, &#x60;promised&#x60;. | 
**Scope** | **string** | Known values (open set — tolerate new ones): &#x60;all&#x60;, &#x60;categories&#x60;. | 
**Categories** | [**List&lt;CommissionCampaignCategory&gt;**](CommissionCampaignCategory.md) | Every category-scoped rate of the campaign (each covers its category&#39;s subtree). | 
**EffectType** | **string** | Known values (open set — tolerate new ones): &#x60;absolute_pct&#x60;, &#x60;relative_discount_pct&#x60;. | 
**EffectPct** | **decimal** | The all-categories rate when &#x60;scope&#x60; is &#x60;all&#x60;, else the first category&#39;s. | 
**Combinable** | **bool** |  | 
**Days** | **int** | The whole days the grant runs (a promise — the days it will run from the shop&#39;s opening). | 
**StartsAt** | **DateTimeOffset** |  | 
**EndsAt** | **DateTimeOffset** | The last second the grant prices (23:59:59 Tashkent on its last day); &#x60;null&#x60; &#x3D; until the campaign closes, or a promise. | 
**DaysLeft** | **int** | Whole days left, counted to the grant&#39;s anchor + &#x60;days&#x60; (the count a cohort offer shows), never past &#x60;ends_at&#x60;; &#x60;null&#x60; for a promise. | 
**Progress** | **Object** | Invite or sales-target progress; &#x60;null&#x60; until those campaign types ship. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


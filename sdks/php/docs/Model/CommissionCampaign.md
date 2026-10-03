# CommissionCampaign

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **string** |  |
**grant_id** | **string** |  |
**code** | **string** | The campaign&#39;s handle (e.g. &#x60;LAUNCH-0&#x60;). |
**name** | [**\Dona\Api\Model\LocalizedText**](LocalizedText.md) |  |
**kind** | **string** | Known values (open set — tolerate new ones): &#x60;new_registration&#x60;, &#x60;existing_seller&#x60;, &#x60;invite&#x60;, &#x60;sales_target&#x60;. |
**state** | **string** | &#x60;running&#x60;: the grant prices the shop now (a grant that starts later is listed from its start). &#x60;promised&#x60;: it opens the day the shop opens; nothing is dated until then. Known values (open set — tolerate new ones): &#x60;running&#x60;, &#x60;promised&#x60;. |
**scope** | **string** | Known values (open set — tolerate new ones): &#x60;all&#x60;, &#x60;categories&#x60;. |
**categories** | [**\Dona\Api\Model\CommissionCampaignCategory[]**](CommissionCampaignCategory.md) | Every category-scoped rate of the campaign (each covers its category&#39;s subtree). |
**effect_type** | **string** | Known values (open set — tolerate new ones): &#x60;absolute_pct&#x60;, &#x60;relative_discount_pct&#x60;. |
**effect_pct** | **float** | The all-categories rate when &#x60;scope&#x60; is &#x60;all&#x60;, else the first category&#39;s. |
**combinable** | **bool** |  |
**days** | **int** | The whole days the grant runs (a promise — the days it will run from the shop&#39;s opening). |
**starts_at** | **\DateTime** |  |
**ends_at** | **\DateTime** | The last second the grant prices (23:59:59 Tashkent on its last day); &#x60;null&#x60; &#x3D; until the campaign closes, or a promise. |
**days_left** | **int** | Whole days left, counted to the grant&#39;s anchor + &#x60;days&#x60; (the count a cohort offer shows), never past &#x60;ends_at&#x60;; &#x60;null&#x60; for a promise. |
**progress** | **object** | Invite or sales-target progress; &#x60;null&#x60; until those campaign types ship. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

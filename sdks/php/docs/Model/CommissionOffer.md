# CommissionOffer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **string** | &#x60;campaign&#x60; · &#x60;launch_v1&#x60; · &#x60;cohort_new&#x60; · &#x60;cohort_existing&#x60; · &#x60;seller&#x60; · &#x60;seller_group&#x60; · &#x60;country&#x60; · &#x60;platform&#x60;. |
**rule_id** | **string** | The commission rule; empty while a launch offer is promised (its rule is created the day the shop opens) and for a &#x60;campaign&#x60; (a campaign is not a rule). |
**campaign_id** | **string** | Only when &#x60;code&#x60; is &#x60;campaign&#x60;. | [optional]
**name** | [**\Dona\Api\Model\LocalizedText**](LocalizedText.md) | The campaign&#39;s name; only when &#x60;code&#x60; is &#x60;campaign&#x60;. | [optional]
**state** | **string** | Known values (open set — tolerate new ones): &#x60;running&#x60;, &#x60;promised&#x60;. |
**effect_type** | **string** | Known values (open set — tolerate new ones): &#x60;absolute_pct&#x60;, &#x60;relative_discount_pct&#x60;. |
**effect_pct** | **float** | &#x60;absolute_pct&#x60;: the rate. &#x60;relative_discount_pct&#x60;: the share taken off each category rate. |
**days** | **int** |  |
**starts_at** | **\DateTime** |  |
**ends_at** | **\DateTime** | Every &#x60;code&#x60; but &#x60;campaign&#x60;: exclusive — orders placed before it keep the offer&#39;s rate. &#x60;campaign&#x60;: the LAST second the campaign&#39;s grant prices (23:59:59 Tashkent on its last day — the grant ends at the 00:00 after it), the same instant as that grant&#39;s &#x60;campaigns[].ends_at&#x60;. |
**days_left** | **int** |  |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

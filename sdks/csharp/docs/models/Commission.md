# Dona.Api.Model.Commission
The seller portal's `GET /seller/commission` body, byte for byte.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SellerId** | **Guid** |  | 
**DefaultPct** | **decimal** | The platform rate when a category tree carries none. | 
**StartPct** | **decimal** | The lowest rate on the card (MIN of &#x60;roots[].min_pct&#x60;; &#x60;default_pct&#x60; when there are no roots). | 
**Roots** | [**List&lt;CommissionRoot&gt;**](CommissionRoot.md) |  | 
**Campaigns** | [**List&lt;CommissionCampaign&gt;**](CommissionCampaign.md) | Every promised or running grant whose campaign prices this shop now (a paused campaign disappears at once). Empty while campaigns do not apply to the shop. | 
**Offer** | [**CommissionOffer**](CommissionOffer.md) |  | 
**SavedUzs** | **long** | What the launch offer and the commission campaigns spared this shop so far (orders not cancelled), in som, from the order-line snapshots only. A number while &#x60;offer.code&#x60; is &#x60;launch_v1&#x60; or the shop has a campaign-priced line; otherwise &#x60;null&#x60;. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


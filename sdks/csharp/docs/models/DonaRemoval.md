# Dona.Api.Model.DonaRemoval
Why Dona keeps a product off sale and what clears it (OZB architecture/DB/catalog/removed-by-dona-marker.md). Tolerate new values in every enum-like field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Source** | **string** | &#x60;moderation_ban&#x60; · &#x60;ip_notice&#x60; · &#x60;staff_delist&#x60; · &#x60;staff_hide&#x60; · &#x60;ai_review&#x60;. | 
**By** | **string** | &#x60;dona_team&#x60; · &#x60;dona_ai&#x60;. | 
**ReasonCode** | **string** | &#x60;prohibited_goods&#x60; · &#x60;unsafe_product&#x60; · &#x60;adult_content&#x60; · &#x60;violence_hate&#x60; · &#x60;misleading_listing&#x60; · &#x60;intellectual_property&#x60; · &#x60;duplicate_spam&#x60; · &#x60;other&#x60; · &#x60;shop_closing&#x60; · &#x60;listing_review&#x60;. | 
**Reason** | [**LocalizedText**](LocalizedText.md) |  | 
**Title** | [**LocalizedText**](LocalizedText.md) |  | 
**ClearsBy** | **string** | &#x60;staff&#x60; · &#x60;seller&#x60;. | 
**Action** | **string** | &#x60;contact_support&#x60; · &#x60;dispute&#x60; · &#x60;wait&#x60; · &#x60;fix_review&#x60;. | 
**Note** | **string** | The Dona team&#39;s explanation to the seller (a ban, a staff removal); null otherwise. | 
**Since** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60;); null when nothing recorded the start. | 
**State** | **string** | The ban notice&#39;s state or the listing review&#39;s state; null otherwise. | 
**Ref** | **Guid** | The ban / review case / staff removal id; null for an IP notice. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


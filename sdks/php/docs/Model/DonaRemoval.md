# DonaRemoval

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **string** | &#x60;moderation_ban&#x60; · &#x60;ip_notice&#x60; · &#x60;staff_delist&#x60; · &#x60;staff_hide&#x60; · &#x60;ai_review&#x60;. |
**by** | **string** | &#x60;dona_team&#x60; · &#x60;dona_ai&#x60;. |
**reason_code** | **string** | &#x60;prohibited_goods&#x60; · &#x60;unsafe_product&#x60; · &#x60;adult_content&#x60; · &#x60;violence_hate&#x60; · &#x60;misleading_listing&#x60; · &#x60;intellectual_property&#x60; · &#x60;duplicate_spam&#x60; · &#x60;other&#x60; · &#x60;shop_closing&#x60; · &#x60;listing_review&#x60;. |
**reason** | [**\Dona\Api\Model\LocalizedText**](LocalizedText.md) |  |
**title** | [**\Dona\Api\Model\LocalizedText**](LocalizedText.md) |  |
**note** | **string** | The Dona team&#39;s explanation to the seller (a ban, a staff removal); null otherwise. |
**since** | **\DateTime** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60;); null when nothing recorded the start. |
**state** | **string** | The ban notice&#39;s state or the listing review&#39;s state; null otherwise. |
**clears_by** | **string** | &#x60;staff&#x60; · &#x60;seller&#x60;. |
**action** | **string** | &#x60;contact_support&#x60; · &#x60;dispute&#x60; · &#x60;wait&#x60; · &#x60;fix_review&#x60;. |
**ref** | **string** | The ban / review case / staff removal id; null for an IP notice. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

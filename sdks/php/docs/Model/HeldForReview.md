# HeldForReview

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **string** |  |
**status** | **string** |  |
**approval_id** | **string** | &#x60;seller_api_held_writes.id&#x60; — follow &#x60;write.approved|rejected|expired&#x60; events. |
**rule** | **string** | Known values (open set — tolerate new ones): &#x60;price_floor&#x60;, &#x60;drop_100x&#x60;, &#x60;stock_jump_10x&#x60;, &#x60;mass_zero_50pct&#x60;, &#x60;delist_30pct&#x60;, &#x60;confirmation_required&#x60;. |
**kind** | **string** | Known values (open set — tolerate new ones): &#x60;price&#x60;, &#x60;stock&#x60;, &#x60;product&#x60;, &#x60;delist&#x60;. |
**subject** | [**\Dona\Api\Model\HeldForReviewSubject**](HeldForReviewSubject.md) |  |
**approver** | **string** | &#x60;owner&#x60; when the value effect ≤ &#x60;owner_approval_max_uzs&#x60; (D18) and no repeat/suspension/health rule applies; else &#x60;staff&#x60; (&#x60;api.approve&#x60;). Known values (open set — tolerate new ones): &#x60;owner&#x60;, &#x60;staff&#x60;. |
**expires_at** | **\DateTime** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). |
**message** | **string** |  |
**request_id** | **string** |  |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

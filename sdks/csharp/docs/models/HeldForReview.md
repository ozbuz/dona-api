# Dona.Api.Model.HeldForReview
`202` success envelope — `error` is ABSENT. Nothing was written. A replay of the same `Idempotency-Key` re-derives from the held row (approved ⇒ the applied outcome · rejected ⇒ 409 · pending ⇒ this 202 again) — never a second hold.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Code** | **string** |  | 
**Status** | **string** |  | 
**ApprovalId** | **Guid** | &#x60;seller_api_held_writes.id&#x60; — follow &#x60;write.approved|rejected|expired&#x60; events. | 
**Rule** | **string** | Known values (open set — tolerate new ones): &#x60;price_floor&#x60;, &#x60;drop_100x&#x60;, &#x60;stock_jump_10x&#x60;, &#x60;mass_zero_50pct&#x60;, &#x60;delist_30pct&#x60;, &#x60;confirmation_required&#x60;. | 
**Kind** | **string** | Known values (open set — tolerate new ones): &#x60;price&#x60;, &#x60;stock&#x60;, &#x60;product&#x60;, &#x60;delist&#x60;. | 
**Subject** | [**HeldForReviewSubject**](HeldForReviewSubject.md) |  | 
**Approver** | **string** | &#x60;owner&#x60; when the value effect ≤ &#x60;owner_approval_max_uzs&#x60; (D18) and no repeat/suspension/health rule applies; else &#x60;staff&#x60; (&#x60;api.approve&#x60;). Known values (open set — tolerate new ones): &#x60;owner&#x60;, &#x60;staff&#x60;. | 
**ExpiresAt** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). | 
**Message** | **string** |  | 
**RequestId** | **string** |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


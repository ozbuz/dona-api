# AttentionItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**kind** | **string** | Known values (open set — tolerate new ones): &#x60;documents_pending&#x60;, &#x60;documents_rejected&#x60;, &#x60;kyc_reopened&#x60;, &#x60;bank_pending&#x60;, &#x60;agreement_owed&#x60;, &#x60;shop_suspended&#x60;, &#x60;shop_restricted&#x60;, &#x60;shop_blocked&#x60;, &#x60;suppressed&#x60;, &#x60;penalty_points&#x60;, &#x60;product_held&#x60;, &#x60;product_rejected&#x60;, &#x60;product_violation&#x60;, &#x60;listing_issue&#x60;, &#x60;order_accept_due&#x60;, &#x60;order_ship_overdue&#x60;, &#x60;return_decision_due&#x60;, &#x60;stock_out&#x60;, &#x60;stock_low&#x60;, &#x60;health_warning&#x60;, &#x60;health_suppressed&#x60;, &#x60;live_ban&#x60;, &#x60;live_strike&#x60;, &#x60;write_held&#x60;, &#x60;key_expiring&#x60;, &#x60;key_suspended&#x60;, &#x60;key_dormant&#x60;, &#x60;ip_blocked&#x60;, &#x60;webhook_failing&#x60;, &#x60;api_anomaly&#x60;. |
**severity** | **string** | Known values (open set — tolerate new ones): &#x60;low&#x60;, &#x60;medium&#x60;, &#x60;high&#x60;, &#x60;critical&#x60;. |
**action_required** | **bool** | True only when the SELLER can clear it. |
**resolves_by** | **string** | Known values (open set — tolerate new ones): &#x60;condition&#x60;, &#x60;decision&#x60;, &#x60;deadline&#x60;, &#x60;expiry&#x60;, &#x60;ack&#x60;. |
**subject** | [**\Dona\Api\Model\AttentionItemSubject**](AttentionItemSubject.md) |  |
**title** | [**\Dona\Api\Model\LocalizedText**](LocalizedText.md) |  |
**body** | [**\Dona\Api\Model\LocalizedText**](LocalizedText.md) |  |
**deadline_at** | **\DateTime** |  |
**action_url** | **string** | Portal deep link. |
**opened_at** | **\DateTime** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). |
**updated_at** | **\DateTime** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). |
**acked_at** | **\DateTime** |  |
**acked_via** | **string** | Known values (open set — tolerate new ones): &#x60;portal&#x60;, &#x60;api&#x60;, &#x60;mcp&#x60;. |
**resolved_at** | **\DateTime** |  |
**resolved_reason** | **string** | Known values (open set — tolerate new ones): &#x60;condition_cleared&#x60;, &#x60;decided&#x60;, &#x60;deadline_passed&#x60;, &#x60;expired&#x60;, &#x60;acked&#x60;. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

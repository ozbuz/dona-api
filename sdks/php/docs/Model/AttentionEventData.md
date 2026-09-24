# AttentionEventData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attention_id** | **string** |  |
**kind** | **string** | Known values (open set — tolerate new ones): &#x60;documents_pending&#x60;, &#x60;documents_rejected&#x60;, &#x60;kyc_reopened&#x60;, &#x60;bank_pending&#x60;, &#x60;agreement_owed&#x60;, &#x60;shop_suspended&#x60;, &#x60;shop_restricted&#x60;, &#x60;shop_blocked&#x60;, &#x60;suppressed&#x60;, &#x60;penalty_points&#x60;, &#x60;product_held&#x60;, &#x60;product_rejected&#x60;, &#x60;product_violation&#x60;, &#x60;listing_issue&#x60;, &#x60;order_accept_due&#x60;, &#x60;order_ship_overdue&#x60;, &#x60;return_decision_due&#x60;, &#x60;stock_out&#x60;, &#x60;stock_low&#x60;, &#x60;health_warning&#x60;, &#x60;health_suppressed&#x60;, &#x60;live_ban&#x60;, &#x60;live_strike&#x60;, &#x60;write_held&#x60;, &#x60;key_expiring&#x60;, &#x60;key_suspended&#x60;, &#x60;key_dormant&#x60;, &#x60;ip_blocked&#x60;, &#x60;webhook_failing&#x60;, &#x60;api_anomaly&#x60;. |
**severity** | **string** | Known values (open set — tolerate new ones): &#x60;low&#x60;, &#x60;medium&#x60;, &#x60;high&#x60;, &#x60;critical&#x60;. |
**action_required** | **bool** |  |
**subject** | [**\Dona\Api\Model\AttentionEventDataSubject**](AttentionEventDataSubject.md) |  |
**deadline_at** | **\DateTime** |  | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

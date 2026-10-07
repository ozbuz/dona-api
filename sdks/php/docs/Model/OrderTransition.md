# OrderTransition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**status** | **string** |  |
**payment_status** | **string** |  |
**accepted_at** | **\DateTime** |  |
**shipped_at** | **\DateTime** |  |
**cancelled_by** | **string** | Known values (open set — tolerate new ones): &#x60;seller&#x60;, &#x60;buyer&#x60;, &#x60;system&#x60;. |
**decline_reason_code** | **string** |  |
**updated_at** | **\DateTime** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). |
**refund_uzs** | **int** | Only on a decline / cancel, only where the stock effect applies to the shop (it comes with the three keys below): the integer soʻm the buyer gets back — 0 for a cash-on-delivery or unpaid order, never null. | [optional]
**stock_effects** | [**\Dona\Api\Model\StockEffect[]**](StockEffect.md) | Only on a decline / cancel, only where the stock effect applies to the shop: one entry per line the move was about (&#x60;unavailable_item_ids&#x60;, or the one live line) — what became of its product. &#x60;[]&#x60; for a reason that takes nothing off sale. | [optional]
**other_open_orders** | [**\Dona\Api\Model\OtherOpenOrder[]**](OtherOpenOrder.md) | The shop&#39;s OTHER open orders (not cancelled, shipped or delivered; at most 50) holding a product or variation the move took off sale — to review; nothing cancels them. Read right AFTER the commit: if that read fails the key is absent, which means \&quot;not known\&quot;, never \&quot;none\&quot;. Absent on a dry run. | [optional]
**marking_needed** | **bool** | true when the reason takes stock off sale, the order had SEVERAL live lines and &#x60;unavailable_item_ids&#x60; was not sent: no product was taken off sale (the units went back on the shelf as before) and the question \&quot;which line was it?\&quot; stays open for 24 hours on Dona&#39;s side. Send &#x60;unavailable_item_ids&#x60; with the call to name the lines. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

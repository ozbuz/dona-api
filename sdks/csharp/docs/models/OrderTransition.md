# Dona.Api.Model.OrderTransition
The order as a decline / cancel left it. `refund_uzs`, `stock_effects`, `other_open_orders` and `marking_needed` are optional and additive: they appear only for a shop where Dona applies the out-of-stock rule (see `declineOrder`) — every other shop gets exactly the eight required keys.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**Status** | **string** |  | 
**PaymentStatus** | **string** |  | 
**UpdatedAt** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). | 
**AcceptedAt** | **DateTimeOffset** |  | 
**ShippedAt** | **DateTimeOffset** |  | 
**CancelledBy** | **string** | Known values (open set — tolerate new ones): &#x60;seller&#x60;, &#x60;buyer&#x60;, &#x60;system&#x60;. | 
**DeclineReasonCode** | **string** |  | 
**RefundUzs** | **long** | Only on a decline / cancel, only where the stock effect applies to the shop (it comes with the three keys below): the integer soʻm the buyer gets back — 0 for a cash-on-delivery or unpaid order, never null. | [optional] 
**StockEffects** | [**List&lt;StockEffect&gt;**](StockEffect.md) | Only on a decline / cancel, only where the stock effect applies to the shop: one entry per line the move was about (&#x60;unavailable_item_ids&#x60;, or the one live line) — what became of its product. &#x60;[]&#x60; for a reason that takes nothing off sale. | [optional] 
**OtherOpenOrders** | [**List&lt;OtherOpenOrder&gt;**](OtherOpenOrder.md) | The shop&#39;s OTHER open orders (not cancelled, shipped or delivered; at most 50) holding a product or variation the move took off sale — to review; nothing cancels them. Read right AFTER the commit: if that read fails the key is absent, which means \&quot;not known\&quot;, never \&quot;none\&quot;. Absent on a dry run. | [optional] 
**MarkingNeeded** | **bool** | true when the reason takes stock off sale, the order had SEVERAL live lines and &#x60;unavailable_item_ids&#x60; was not sent: no product was taken off sale (the units went back on the shelf as before) and the question \&quot;which line was it?\&quot; stays open for 24 hours on Dona&#39;s side. Send &#x60;unavailable_item_ids&#x60; with the call to name the lines. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


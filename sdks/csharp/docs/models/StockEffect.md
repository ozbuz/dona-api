# Dona.Api.Model.StockEffect
What a decline / cancel did to one line's product, under the 24-hour out-of-stock rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**OrderItemId** | **Guid** | The order line (&#x60;items[].id&#x60;) the entry is about. | 
**ProductId** | **Guid** |  | 
**Scope** | **string** | &#x60;variant&#x60;: one variation is out of stock and locked; &#x60;product&#x60;: the whole product is (it has no variations, or only one active variation). Known values (open set — tolerate new ones): &#x60;variant&#x60;, &#x60;product&#x60;. | 
**Result** | **string** | &#x60;zeroed&#x60; — taken to stock 0 and locked; &#x60;already_zero&#x60; — it was at 0, now locked; &#x60;variant_not_found&#x60; — no variation of this shop matched the line, nothing zeroed or locked; &#x60;not_applied&#x60; — see &#x60;why&#x60;. Known values (open set — tolerate new ones): &#x60;zeroed&#x60;, &#x60;already_zero&#x60;, &#x60;variant_not_found&#x60;, &#x60;not_applied&#x60;. | 
**UnitsRemoved** | **int** | Units taken off sale by this entry. | 
**VariantId** | **Guid** | The variation the line resolved to when the lock is one variation&#39;s (&#x60;scope: variant&#x60;), else &#x60;null&#x60;. | 
**VariantLabel** | **string** |  | 
**Why** | **string** | Only with &#x60;result: not_applied&#x60;: &#x60;shipped&#x60; (a shipped order — the goods come back) or &#x60;legacy_multi_line&#x60; (an order with several lines and no &#x60;unavailable_item_ids&#x60;). Known values (open set — tolerate new ones): &#x60;shipped&#x60;, &#x60;legacy_multi_line&#x60;. | 
**LockedUntil** | **DateTimeOffset** | When the product (or variation) may be put back on sale: RFC 3339, UTC (&#x60;…Z&#x60;), whole seconds. &#x60;null&#x60; when nothing was locked. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


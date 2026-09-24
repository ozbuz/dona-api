# DeclineRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **string** | Uzum subset (&#x60;OUT_OF_STOCK&#x60;, &#x60;OUT_OF_PACKAGE&#x60;, &#x60;OUT_OF_TIME&#x60;, &#x60;OTHER&#x60;) mapped onto the native &#x60;declineReasons&#x60;, OR a native lowercase code. &#x60;OTHER&#x60;/&#x60;other&#x60; needs &#x60;comment&#x60;. Unknown ⇒ &#x60;400 invalid_decline_reason&#x60;. Known values (open set — tolerate new ones): &#x60;OUT_OF_STOCK&#x60;, &#x60;OUT_OF_PACKAGE&#x60;, &#x60;OUT_OF_TIME&#x60;, &#x60;OTHER&#x60;, &#x60;out_of_stock&#x60;, &#x60;inventory_mismatch&#x60;, &#x60;product_damaged&#x60;, &#x60;store_unavailable&#x60;, &#x60;cannot_fulfill_in_time&#x60;, &#x60;duplicate_order&#x60;, &#x60;fraud_suspected&#x60;, &#x60;other&#x60;. |
**comment** | **string** |  | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

# Dona.Api.Model.ErrorDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Code** | **string** | Stable field-level code, e.g. &#x60;required&#x60;, &#x60;ikpu_required&#x60;, &#x60;cursor_expired&#x60;, &#x60;stock_locked&#x60;. | 
**Message** | **string** | Localised by &#x60;Accept-Language&#x60;. | 
**Index** | **int** | Line index in a bulk body. | [optional] 
**Field** | **string** | Field or header name. | [optional] 
**LockedUntil** | **DateTimeOffset** | With &#x60;code: stock_locked&#x60; — the line of an atomic &#x60;POST /stock&#x60; that the 24-hour out-of-stock lock refused: when that lock ends (the same wire shape as &#x60;Error.locked_until&#x60;). | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


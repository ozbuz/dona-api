# Dona.Api.Model.Settlement
One ledger line of the shop's payable account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**TxnId** | **Guid** |  | 
**Direction** | **string** | Known values (open set — tolerate new ones): &#x60;credit&#x60;, &#x60;debit&#x60;. | 
**AmountUzs** | **long** | Integer soʻm (no decimals). | 
**SignedAmountUzs** | **long** |  | 
**Memo** | **string** |  | 
**CreatedAt** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). | 
**OrderId** | **Guid** |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


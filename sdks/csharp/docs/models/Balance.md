# Dona.Api.Model.Balance
The wallet's figures for the shop (the portal's `/sellers/me/finance/wallet`). No lifetime totals — the wallet has none, and the portal's balance drops them for the same reason (C57). No requisites, PAN or statement URLs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AvailableUzs** | **long** | Integer soʻm (no decimals). | 
**HeldUzs** | **long** | Integer soʻm — earned, still inside the admin hold (not yet withdrawable). | 
**ExpectedUzs** | **long** | Integer soʻm — orders in flight, not yet earned. | 
**Currency** | **string** |  | 
**AsOf** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


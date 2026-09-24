# Dona.Api.Model.ProductUpdate
Partial update: an absent field is unchanged.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Title** | [**LocalizedText**](LocalizedText.md) |  | [optional] 
**Description** | [**LocalizedText**](LocalizedText.md) |  | [optional] 
**CategoryId** | **Guid** |  | [optional] 
**Brand** | **string** |  | [optional] 
**Barcode** | **string** |  | [optional] 
**ExternalId** | **string** |  | [optional] 
**PriceUzs** | **long** |  | [optional] 
**CompareAtUzs** | **long** |  | [optional] 
**Stock** | **int** | Refused (&#x60;details[].code&#x3D;stock_not_editable&#x60;) when the product has variants — use &#x60;POST /stock&#x60; with &#x60;variant_id&#x60;. | [optional] 
**Ikpu** | **string** |  | [optional] 
**PackageCode** | **string** |  | [optional] 
**ImageUrls** | **List&lt;string&gt;** |  | [optional] 
**VideoUrl** | **string** |  | [optional] 
**Attributes** | **Dictionary&lt;string, Object&gt;** |  | [optional] 
**VarVersion** | **string** | Optional optimistic lock; stale ⇒ &#x60;409 version_conflict&#x60;. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


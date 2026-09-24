# Dona.Api.Model.ProductCreate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Title** | [**LocalizedText**](LocalizedText.md) |  | 
**CategoryId** | **Guid** |  | 
**SellerSku** | **string** |  | 
**PriceUzs** | **long** |  | 
**Stock** | **int** |  | 
**Description** | [**LocalizedText**](LocalizedText.md) |  | [optional] 
**Brand** | **string** |  | [optional] 
**Barcode** | **string** |  | [optional] 
**ExternalId** | **string** | Your system&#39;s id, e.g. &#x60;1c:0f2a…&#x60;. | [optional] 
**CompareAtUzs** | **long** |  | [optional] 
**Ikpu** | **string** |  | [optional] 
**PackageCode** | **string** |  | [optional] 
**ImageUrls** | **List&lt;string&gt;** |  | [optional] 
**VideoUrl** | **string** |  | [optional] 
**Attributes** | **Dictionary&lt;string, Object&gt;** |  | [optional] 
**Variants** | [**List&lt;VariantInput&gt;**](VariantInput.md) |  | [optional] 
**Publish** | **bool** | Ask to publish after create; a pending shop&#39;s product is held until documents approval. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


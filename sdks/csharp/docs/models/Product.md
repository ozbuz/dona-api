# Dona.Api.Model.Product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**Title** | [**LocalizedText**](LocalizedText.md) |  | 
**Status** | **string** | &#x60;draft&#x60;, &#x60;ai_review&#x60;, &#x60;active&#x60;, &#x60;hidden&#x60; today; tolerate new values. | 
**PriceUzs** | **long** | Integer soʻm (no decimals). | 
**Stock** | **int** | Sum over variants when &#x60;has_variants&#x60;. | 
**HasVariants** | **bool** |  | 
**Variants** | [**List&lt;Variant&gt;**](Variant.md) |  | 
**ImageUrls** | **List&lt;string&gt;** |  | 
**Attributes** | **Dictionary&lt;string, Object&gt;** |  | 
**CreatedVia** | **string** | &#x60;manual&#x60;, &#x60;mass_upload&#x60;, &#x60;api&#x60;, … (products_created_via_check). | 
**OpenIssues** | **int** | Open &#x60;listing_issues&#x60; + &#x60;product_violations&#x60;. | 
**VarVersion** | **string** | Opaque (today the full-precision &#x60;updated_at&#x60;); echo verbatim. | 
**CreatedAt** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). | 
**UpdatedAt** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). | 
**Description** | [**LocalizedText**](LocalizedText.md) |  | 
**CategoryId** | **Guid** |  | 
**Brand** | **string** |  | 
**SellerSku** | **string** |  | 
**Barcode** | **string** |  | 
**ExternalId** | **string** |  | 
**CompareAtUzs** | **long** | Must exceed &#x60;price_uzs&#x60; (0020 CHECK). | 
**Ikpu** | **string** |  | 
**PackageCode** | **string** |  | 
**VideoUrl** | **string** |  | 
**Hold** | [**ProductHold**](ProductHold.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


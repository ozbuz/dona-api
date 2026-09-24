# ProductCreate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | [**\Dona\Api\Model\LocalizedText**](LocalizedText.md) |  |
**description** | [**\Dona\Api\Model\LocalizedText**](LocalizedText.md) |  | [optional]
**category_id** | **string** |  |
**brand** | **string** |  | [optional]
**seller_sku** | **string** |  |
**barcode** | **string** |  | [optional]
**external_id** | **string** | Your system&#39;s id, e.g. &#x60;1c:0f2a…&#x60;. | [optional]
**price_uzs** | **int** |  |
**compare_at_uzs** | **int** |  | [optional]
**stock** | **int** |  |
**ikpu** | **string** |  | [optional]
**package_code** | **string** |  | [optional]
**image_urls** | **string[]** |  | [optional]
**video_url** | **string** |  | [optional]
**attributes** | **array<string,mixed>** |  | [optional]
**variants** | [**\Dona\Api\Model\VariantInput[]**](VariantInput.md) |  | [optional]
**publish** | **bool** | Ask to publish after create; a pending shop&#39;s product is held until documents approval. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

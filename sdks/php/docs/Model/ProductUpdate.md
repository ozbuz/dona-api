# ProductUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | [**\Dona\Api\Model\LocalizedText**](LocalizedText.md) |  | [optional]
**description** | [**\Dona\Api\Model\LocalizedText**](LocalizedText.md) |  | [optional]
**category_id** | **string** |  | [optional]
**brand** | **string** |  | [optional]
**barcode** | **string** |  | [optional]
**external_id** | **string** |  | [optional]
**price_uzs** | **int** |  | [optional]
**compare_at_uzs** | **int** |  | [optional]
**stock** | **int** | Refused (&#x60;details[].code&#x3D;stock_not_editable&#x60;) when the product has variants — use &#x60;POST /stock&#x60; with &#x60;variant_id&#x60;. | [optional]
**ikpu** | **string** |  | [optional]
**package_code** | **string** |  | [optional]
**image_urls** | **string[]** |  | [optional]
**video_url** | **string** |  | [optional]
**attributes** | **array<string,mixed>** |  | [optional]
**version** | **string** | Optional optimistic lock; stale ⇒ &#x60;409 version_conflict&#x60;. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

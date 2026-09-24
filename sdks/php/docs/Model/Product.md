# Product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**title** | [**\Dona\Api\Model\LocalizedText**](LocalizedText.md) |  |
**description** | [**\Dona\Api\Model\LocalizedText**](LocalizedText.md) |  |
**status** | **string** | &#x60;draft&#x60;, &#x60;ai_review&#x60;, &#x60;active&#x60;, &#x60;hidden&#x60; today; tolerate new values. |
**category_id** | **string** |  |
**brand** | **string** |  |
**seller_sku** | **string** |  |
**barcode** | **string** |  |
**external_id** | **string** |  |
**price_uzs** | **int** | Integer soʻm (no decimals). |
**compare_at_uzs** | **int** | Must exceed &#x60;price_uzs&#x60; (0020 CHECK). |
**stock** | **int** | Sum over variants when &#x60;has_variants&#x60;. |
**has_variants** | **bool** |  |
**variants** | [**\Dona\Api\Model\Variant[]**](Variant.md) |  |
**ikpu** | **string** |  |
**package_code** | **string** |  |
**image_urls** | **string[]** |  |
**video_url** | **string** |  |
**attributes** | **array<string,mixed>** |  |
**created_via** | **string** | &#x60;manual&#x60;, &#x60;mass_upload&#x60;, &#x60;api&#x60;, … (products_created_via_check). |
**hold** | [**\Dona\Api\Model\ProductHold**](ProductHold.md) |  |
**open_issues** | **int** | Open &#x60;listing_issues&#x60; + &#x60;product_violations&#x60;. |
**version** | **string** | Opaque (today the full-precision &#x60;updated_at&#x60;); echo verbatim. |
**created_at** | **\DateTime** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). |
**updated_at** | **\DateTime** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

# CategoryRequirements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **string** |  |
**status** | **string** |  |
**listing_policy** | **string** | &#x60;open&#x60; default; &#x60;approval_required&#x60;, &#x60;licensed&#x60;, &#x60;restricted&#x60;, &#x60;prohibited&#x60;. |
**is_leaf** | **bool** |  |
**can_list** | **bool** | &#x60;status&#x3D;active AND is_leaf AND listing_policy &lt;&gt; prohibited&#x60;. |
**min_images** | **int** |  |
**requires_dimensions** | **bool** |  |
**requires_brand** | **bool** |  |
**requires_size_chart** | **bool** |  |
**commission_pct** | **float** |  |
**attributes** | [**\Dona\Api\Model\CategoryAttribute[]**](CategoryAttribute.md) |  |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

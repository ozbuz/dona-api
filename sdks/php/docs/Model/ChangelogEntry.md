# ChangelogEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**version** | **string** |  |
**kind** | **string** | Known values (open set — tolerate new ones): &#x60;added&#x60;, &#x60;changed&#x60;, &#x60;deprecated&#x60;, &#x60;removed&#x60;, &#x60;fixed&#x60;, &#x60;security&#x60;. |
**title** | [**\Dona\Api\Model\LocalizedText**](LocalizedText.md) |  |
**body** | [**\Dona\Api\Model\LocalizedText**](LocalizedText.md) |  |
**affects_scopes** | **string[]** |  |
**sunset_at** | **\DateTime** |  |
**published_at** | **\DateTime** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

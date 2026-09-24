# OrderTimelineEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**type** | **string** | &#x60;placed&#x60;, &#x60;paid&#x60;, &#x60;accepted&#x60;, &#x60;declined&#x60;, &#x60;shipped&#x60;, &#x60;delivered&#x60;, &#x60;cancelled&#x60;, &#x60;line_cancelled&#x60;, … |
**actor** | **string** | &#x60;system&#x60;, &#x60;seller&#x60;, &#x60;buyer&#x60;, &#x60;courier&#x60;, &#x60;support&#x60; |
**note** | **string** | Dona/staff-authored only; buyer text never appears here. |
**occurred_at** | **\DateTime** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

# OrderEventData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **string** |  |
**status** | **string** |  |
**payment_status** | **string** |  |
**payment_method** | **string** |  |
**scheme** | **string** | Known values (open set — tolerate new ones): &#x60;own_fleet&#x60;, &#x60;third_party&#x60;. |
**total_uzs** | **int** | Integer soʻm (no decimals). |
**accept_deadline** | **\DateTime** |  | [optional]
**ship_by_deadline** | **\DateTime** |  | [optional]
**updated_at** | **\DateTime** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

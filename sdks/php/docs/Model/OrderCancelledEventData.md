# OrderCancelledEventData

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
**cancelled_by** | **string** | Known values (open set — tolerate new ones): &#x60;seller&#x60;, &#x60;buyer&#x60;, &#x60;system&#x60;. |
**reason_code** | **string** | A code from the order vocabularies (the buyer&#39;s, the seller&#39;s decline set, system, support), or null. Free text is never pushed — a stored reason that is not a code is null here and &#x60;comment_present&#x60; is true. |
**comment_present** | **bool** | The comment text is fetched, never pushed. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

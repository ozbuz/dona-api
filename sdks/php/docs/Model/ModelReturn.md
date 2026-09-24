# ModelReturn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**order_id** | **string** |  |
**status** | **string** | Known values (open set — tolerate new ones): &#x60;requested&#x60;, &#x60;approved&#x60;, &#x60;refunded&#x60;, &#x60;rejected&#x60;, &#x60;disputed&#x60;, &#x60;closed&#x60;. |
**type** | **string** |  |
**reason_code** | **string** |  |
**refund_uzs** | **int** | Integer soʻm (no decimals). |
**due_at** | **\DateTime** |  |
**items** | [**\Dona\Api\Model\ReturnItemsInner[]**](ReturnItemsInner.md) |  |
**reason_text** | **string** | Buyer-authored; detail only (null on lists). |
**created_at** | **\DateTime** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). |
**updated_at** | **\DateTime** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

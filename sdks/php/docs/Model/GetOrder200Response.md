# GetOrder200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**order_code** | **string** | Display handle (0164), e.g. &#x60;AB1765543210XZ&#x60;; never a route param. |
**status** | **string** | &#x60;pending&#x60;, &#x60;paid&#x60;, &#x60;ready_to_ship&#x60;, &#x60;shipped&#x60;, &#x60;delivered&#x60;, &#x60;cancelled&#x60;; tolerate new values. |
**payment_status** | **string** |  |
**payment_method** | **string** |  |
**scheme** | **string** | Derived: &#x60;own_fleet&#x60; when the shipment rides the default channel, else &#x60;third_party&#x60;. Known values (open set — tolerate new ones): &#x60;own_fleet&#x60;, &#x60;third_party&#x60;. |
**total_uzs** | **int** | Integer soʻm (no decimals). |
**accepted_at** | **\DateTime** |  |
**declined_at** | **\DateTime** |  |
**shipped_at** | **\DateTime** |  |
**delivered_at** | **\DateTime** |  |
**cancelled_by** | **string** | Known values (open set — tolerate new ones): &#x60;seller&#x60;, &#x60;buyer&#x60;, &#x60;system&#x60;. |
**decline_reason_code** | **string** |  |
**accept_deadline** | **\DateTime** |  |
**ship_by_deadline** | **\DateTime** |  |
**items** | [**\Dona\Api\Model\OrderItem[]**](OrderItem.md) |  |
**meta** | [**\Dona\Api\Model\OrderMeta**](OrderMeta.md) |  |
**created_at** | **\DateTime** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). |
**updated_at** | **\DateTime** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). |
**recipient** | [**\Dona\Api\Model\Recipient**](Recipient.md) |  |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

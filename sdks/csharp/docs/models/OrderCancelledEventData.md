# Dona.Api.Model.OrderCancelledEventData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**OrderId** | **Guid** |  | 
**Status** | **string** |  | 
**PaymentStatus** | **string** |  | 
**PaymentMethod** | **string** |  | 
**Scheme** | **string** | Known values (open set — tolerate new ones): &#x60;own_fleet&#x60;, &#x60;third_party&#x60;. | 
**TotalUzs** | **long** | Integer soʻm (no decimals). | 
**UpdatedAt** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). | 
**CancelledBy** | **string** | Known values (open set — tolerate new ones): &#x60;seller&#x60;, &#x60;buyer&#x60;, &#x60;system&#x60;. | 
**CommentPresent** | **bool** | The comment text is fetched, never pushed. | 
**AcceptDeadline** | **DateTimeOffset** |  | [optional] 
**ShipByDeadline** | **DateTimeOffset** |  | [optional] 
**ReasonCode** | **string** | A code from the order vocabularies (the buyer&#39;s, the seller&#39;s decline set, system, support), or null. Free text is never pushed — a stored reason that is not a code is null here and &#x60;comment_present&#x60; is true. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


# Dona.Api.Model.EventPage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**List&lt;Event&gt;**](Event.md) |  | 
**HasMore** | **bool** | True ⇒ call again immediately. | 
**NextCursor** | **string** | The id of the LAST event returned (or your own cursor echoed when &#x60;items&#x60; is empty). Store it after your batch commits; never null once you have seen an event. | 
**Meta** | **Dictionary&lt;string, Object&gt;** | Endpoint-specific facts; clients must tolerate unknown keys. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


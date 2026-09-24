# EventPage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**\Dona\Api\Model\Event[]**](Event.md) |  |
**next_cursor** | **string** | The id of the LAST event returned (or your own cursor echoed when &#x60;items&#x60; is empty). Store it after your batch commits; never null once you have seen an event. |
**has_more** | **bool** | True ⇒ call again immediately. |
**meta** | **array<string,mixed>** | Endpoint-specific facts; clients must tolerate unknown keys. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

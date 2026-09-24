# KeyEventData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **string** |  |
**prefix** | **string** |  |
**expires_at** | **\DateTime** |  | [optional]
**suspended_until** | **\DateTime** |  | [optional]
**reason_code** | **string** | &#x60;key.suspended&#x60; only: the suspension&#39;s code (&#x60;error_storm&#x60;, &#x60;ip_blocked&#x60;, &#x60;staff&#x60;, …) — never the words staff typed (an internal note); null for anything outside the vocabulary. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

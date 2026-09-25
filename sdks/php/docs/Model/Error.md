# Error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **string** | Stable code (glossary / docs/error-codes.md). Clients branch on this, never on &#x60;message&#x60;. |
**message** | **string** | Localised by &#x60;Accept-Language&#x60; (uz default). |
**request_id** | **string** |  |
**details** | [**\Dona\Api\Model\ErrorDetail[]**](ErrorDetail.md) | Always present; &#x60;[]&#x60; when there is nothing field-level. |
**doc_url** | **string** | Anchor into the docs for this code: &#x60;https://dona.uz/&lt;lang&gt;/developers/errors#&lt;code&gt;&#x60; — &#x60;&lt;lang&gt;&#x60; is the key owner&#39;s language (uz | ru | en) when a key authenticated the request, else &#x60;Accept-Language&#x60;, else &#x60;uz&#x60;. The docs site is per language; there is no language-less &#x60;/developers&#x60; page. |
**retry_after_seconds** | **int** | Mirrors &#x60;Retry-After&#x60; on 429/503/&#x60;key_suspended&#x60;. | [optional]
**required_scope** | **string** | The 14 issuable scopes (glossary). &#x60;returns:write&#x60; is reserved and unissued. Known values (open set — tolerate new ones): &#x60;catalog:read&#x60;, &#x60;catalog:stock&#x60;, &#x60;catalog:write&#x60;, &#x60;orders:read&#x60;, &#x60;orders:write&#x60;, &#x60;orders:cancel&#x60;, &#x60;orders:pii&#x60;, &#x60;returns:read&#x60;, &#x60;health:read&#x60;, &#x60;attention:read&#x60;, &#x60;events:read&#x60;, &#x60;webhooks:manage&#x60;, &#x60;finance:read&#x60;, &#x60;mcp&#x60;. | [optional]
**rotate_url** | **string** | On &#x60;401 api_key_expired&#x60;: the portal page to mint a successor. | [optional]
**suspended_until** | **\DateTime** | On &#x60;403 key_suspended&#x60;. | [optional]
**reason** | **string** | On &#x60;403 key_suspended&#x60; / &#x60;403 api_blocked&#x60;: why (&#x60;error_storm&#x60;, &#x60;unauthorized_storm&#x60;, &#x60;ip_blocked&#x60;, &#x60;credential_stuffing&#x60;, &#x60;leak_reported&#x60;, &#x60;staff&#x60;). | [optional]
**meta** | [**\Dona\Api\Model\ErrorMeta**](ErrorMeta.md) |  | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

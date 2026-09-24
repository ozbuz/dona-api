# Dona.Api.Model.Me

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Key** | [**MeKey**](MeKey.md) |  | 
**Shop** | [**MeShop**](MeShop.md) |  | 
**Tier** | **string** | Key tier, derived per request (never cached): ADVANCED &#x3D; kyc approved AND documents approved (a waiver never counts) AND shop approved AND no active punishment; &#x60;seller_api_access.tier_override&#x60; may lower or raise it but never lifts a sanction. Known values (open set — tolerate new ones): &#x60;basic&#x60;, &#x60;advanced&#x60;. | 
**ApiAccess** | [**MeApiAccess**](MeApiAccess.md) |  | 
**WritesEnabled** | **bool** | &#x60;app_config.seller_api.writes_enabled&#x60; (seeded false until D5). | 
**Limits** | [**Limits**](Limits.md) |  | 
**Attention** | [**MeAttention**](MeAttention.md) |  | 
**DocsUrl** | **string** |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


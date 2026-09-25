# Me

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**\Dona\Api\Model\MeKey**](MeKey.md) |  |
**shop** | [**\Dona\Api\Model\MeShop**](MeShop.md) |  |
**tier** | **string** | Key tier, derived per request (never cached): ADVANCED &#x3D; kyc approved AND documents approved (a waiver never counts) AND shop approved AND no active punishment; &#x60;seller_api_access.tier_override&#x60; may lower or raise it but never lifts a sanction. Known values (open set — tolerate new ones): &#x60;basic&#x60;, &#x60;advanced&#x60;. |
**api_access** | [**\Dona\Api\Model\MeApiAccess**](MeApiAccess.md) |  |
**writes_enabled** | **bool** | &#x60;app_config.seller_api.writes_enabled&#x60; (seeded false until D5). |
**limits** | [**\Dona\Api\Model\Limits**](Limits.md) |  |
**attention** | [**\Dona\Api\Model\MeAttention**](MeAttention.md) |  |
**docs_url** | **string** | The developer docs home in the key owner&#39;s language (&#x60;https://dona.uz/&lt;uz|ru|en&gt;/developers&#x60;; the owner&#39;s &#x60;users.language&#x60;, else &#x60;Accept-Language&#x60;, else uz). |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

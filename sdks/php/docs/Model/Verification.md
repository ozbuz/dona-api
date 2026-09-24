# Verification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **string** | Known values (open set — tolerate new ones): &#x60;pending&#x60;, &#x60;approved&#x60;, &#x60;suspended&#x60;, &#x60;blocked&#x60;, &#x60;restricted&#x60;, &#x60;closed&#x60;. |
**documents_status** | **string** |  |
**kyc_status** | **string** |  |
**documents_waived** | **bool** |  |
**bank_confirmed** | **bool** |  |
**can_sell** | **bool** |  |
**tier** | **string** | Key tier, derived per request (never cached): ADVANCED &#x3D; kyc approved AND documents approved (a waiver never counts) AND shop approved AND no active punishment; &#x60;seller_api_access.tier_override&#x60; may lower or raise it but never lifts a sanction. Known values (open set — tolerate new ones): &#x60;basic&#x60;, &#x60;advanced&#x60;. |
**tier_missing** | **string[]** | Empty when ADVANCED. A waiver never satisfies &#x60;documents_approved&#x60;. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

# Dona.Api.Model.MeShop

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**Name** | **string** |  | 
**Status** | **string** | Known values (open set — tolerate new ones): &#x60;pending&#x60;, &#x60;approved&#x60;, &#x60;suspended&#x60;, &#x60;blocked&#x60;, &#x60;restricted&#x60;, &#x60;closed&#x60;. | 
**DocumentsStatus** | **string** |  | 
**KycStatus** | **string** |  | 
**CanSell** | **bool** | Documents verdict approved (or waived) AND status approved — &#x60;selleraccess.ShopCanList&#x60;. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


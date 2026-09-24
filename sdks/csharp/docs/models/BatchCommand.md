# Dona.Api.Model.BatchCommand

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Op** | **string** | Known values (open set — tolerate new ones): &#x60;create&#x60;, &#x60;update&#x60;. | 
**ProductId** | **Guid** | Required when &#x60;op&#x3D;update&#x60;. | [optional] 
**Create** | [**ProductCreate**](ProductCreate.md) |  | [optional] 
**Update** | [**ProductUpdate**](ProductUpdate.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


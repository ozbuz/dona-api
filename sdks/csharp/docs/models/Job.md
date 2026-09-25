# Dona.Api.Model.Job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **Guid** |  | 
**Kind** | **string** | Known values (open set — tolerate new ones): &#x60;export_products&#x60;, &#x60;export_orders&#x60;, &#x60;products_batch&#x60;. | 
**Status** | **string** | Known values (open set — tolerate new ones): &#x60;pending&#x60;, &#x60;running&#x60;, &#x60;ready&#x60;, &#x60;failed&#x60;. | 
**Progress** | [**JobProgress**](JobProgress.md) |  | 
**CreatedAt** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). | 
**ExpiresAt** | **DateTimeOffset** | Row + file swept after this (7 d); then &#x60;404 not_found&#x60;. | 
**FileUrl** | **string** | &#x60;GET /jobs/{id}/download?token&#x3D;…&#x60; — the token is valid 15 min from this response and only for a key of this shop (never a public or pre-signed object URL); re-read the job for a fresh one. | 
**FileExpiresAt** | **DateTimeOffset** |  | 
**Results** | [**List&lt;LineResult&gt;**](LineResult.md) | &#x60;products_batch&#x60; only: the per-line shape. | 
**Error** | **string** | Our code only. | 
**FinishedAt** | **DateTimeOffset** |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


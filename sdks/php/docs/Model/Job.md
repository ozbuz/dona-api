# Job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  |
**kind** | **string** | Known values (open set — tolerate new ones): &#x60;export_products&#x60;, &#x60;export_orders&#x60;, &#x60;products_batch&#x60;. |
**status** | **string** | Known values (open set — tolerate new ones): &#x60;pending&#x60;, &#x60;running&#x60;, &#x60;ready&#x60;, &#x60;failed&#x60;. |
**progress** | [**\Dona\Api\Model\JobProgress**](JobProgress.md) |  |
**file_url** | **string** | &#x60;GET /jobs/{id}/download?token&#x3D;…&#x60; — the token is valid 15 min from this response and only for a key of this shop (never a public or pre-signed object URL); re-read the job for a fresh one. |
**file_expires_at** | **\DateTime** |  |
**results** | [**\Dona\Api\Model\LineResult[]**](LineResult.md) | &#x60;products_batch&#x60; only: the per-line shape. |
**error** | **string** | Our code only. |
**created_at** | **\DateTime** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). |
**finished_at** | **\DateTime** |  |
**expires_at** | **\DateTime** | Row + file swept after this (7 d); then &#x60;404 not_found&#x60;. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

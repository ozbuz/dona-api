# HealthSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health_label** | **string** | Known values (open set — tolerate new ones): &#x60;good&#x60;, &#x60;fair&#x60;, &#x60;poor&#x60;. |
**reputation_score** | **float** |  |
**penalty_points** | **int** |  |
**penalty_max** | **int** |  |
**punishment_active** | **bool** |  |
**suppression** | [**\Dona\Api\Model\HealthSummarySuppression**](HealthSummarySuppression.md) |  |
**metrics** | [**\Dona\Api\Model\Metric[]**](Metric.md) |  |
**open_attention** | **int** |  |
**computed_at** | **\DateTime** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

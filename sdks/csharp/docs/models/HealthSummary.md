# Dona.Api.Model.HealthSummary
Projection of `accounthealth.BuildSummary` (extracted in S0 from the portal `summary` handler; the portal JSON stays byte-identical).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**HealthLabel** | **string** | Known values (open set — tolerate new ones): &#x60;good&#x60;, &#x60;fair&#x60;, &#x60;poor&#x60;. | 
**PenaltyPoints** | **int** |  | 
**PenaltyMax** | **int** |  | 
**PunishmentActive** | **bool** |  | 
**Metrics** | [**List&lt;Metric&gt;**](Metric.md) |  | 
**OpenAttention** | **int** |  | 
**ComputedAt** | **DateTimeOffset** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). | 
**ReputationScore** | **decimal** |  | 
**Suppression** | [**HealthSummarySuppression**](HealthSummarySuppression.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


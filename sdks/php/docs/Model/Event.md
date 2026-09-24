# Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** | uuidv7 — also the &#x60;/events&#x60; cursor and the webhook &#x60;webhook-id&#x60;. |
**type** | **string** | The glossary event catalogue. New types are additive. Known values (open set — tolerate new ones): &#x60;order.created&#x60;, &#x60;order.paid&#x60;, &#x60;order.accepted&#x60;, &#x60;order.declined&#x60;, &#x60;order.ready&#x60;, &#x60;order.shipped&#x60;, &#x60;order.delivered&#x60;, &#x60;order.cancelled&#x60;, &#x60;order.line_cancelled&#x60;, &#x60;order.accept_due_soon&#x60;, &#x60;order.ship_overdue&#x60;, &#x60;return.requested&#x60;, &#x60;return.status_changed&#x60;, &#x60;product.published&#x60;, &#x60;product.held&#x60;, &#x60;product.rejected&#x60;, &#x60;product.demoted&#x60;, &#x60;product.violation&#x60;, &#x60;product.deleted&#x60;, &#x60;stock.low&#x60;, &#x60;stock.out&#x60;, &#x60;write.held&#x60;, &#x60;write.approved&#x60;, &#x60;write.rejected&#x60;, &#x60;write.expired&#x60;, &#x60;account.status_changed&#x60;, &#x60;account.documents_decided&#x60;, &#x60;account.kyc_reopened&#x60;, &#x60;account.suppressed&#x60;, &#x60;account.health_changed&#x60;, &#x60;account.agreement_owed&#x60;, &#x60;live.access_changed&#x60;, &#x60;live.strike&#x60;, &#x60;attention.opened&#x60;, &#x60;attention.resolved&#x60;, &#x60;key.expiring&#x60;, &#x60;key.suspended&#x60;, &#x60;key.unsuspended&#x60;, &#x60;webhook.failing&#x60;, &#x60;webhook.disabled&#x60;, &#x60;ping&#x60;. |
**occurred_at** | **\DateTime** | ISO 8601 with offset (Tashkent &#x60;+05:00&#x60; on output). |
**seller_id** | **string** |  |
**api_version** | **string** |  |
**data** | **array<string,mixed>** | Thin payload per &#x60;type&#x60; (ids + new state, never PII) — see the top-level &#x60;webhooks&#x60; for each shape. |
**links** | [**\Dona\Api\Model\EventLinks**](EventLinks.md) |  |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

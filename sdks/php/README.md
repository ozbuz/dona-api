# dona-api

Dona API v1 (https://api.dona.im/seller-api/v1) — client generated from the OpenAPI contract. Conventions (auth, errors, idempotency, dry_run, rate limits, 202 held_for_review): https://github.com/ozbuz/dona-api#readme · contract: https://api.dona.im/seller-api/v1/openapi.json

For more information, please visit [https://dona.uz/uz/developers](https://dona.uz/uz/developers).

## Installation & Usage

### Requirements

PHP 8.1 and later.

### Composer

To install the bindings via [Composer](https://getcomposer.org/), add the following to `composer.json`:

```json
{
  "repositories": [
    {
      "type": "vcs",
      "url": "https://github.com/ozbuz/dona-api.git"
    }
  ],
  "require": {
    "ozbuz/dona-api": "*@dev"
  }
}
```

Then run `composer install`

### Manual Installation

Download the files and include `autoload.php`:

```php
<?php
require_once('/path/to/dona-api/vendor/autoload.php');
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



// Configure Bearer (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>) authorization: bearerKey
$config = Dona\Api\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Dona\Api\Api\AccountApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$accept_language = 'uz'; // string | Localises `message` in error bodies and single-language renderings. Default `uz`.
$dona_seller = 'dona_seller_example'; // string | Vendor-app install keys only (`dona_it_live_…`, S6) — and then REQUIRED on every request, public routes included: the id of the shop the install key belongs to. Missing ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"required\"}]`; sent more than once, or not ONE id in the canonical form the API prints (lower-case, 36 characters — no braces, no `urn:uuid:`, no padding) ⇒ `400 invalid_body` + `details[{field:\"Dona-Seller\", code:\"invalid\"}]`; naming any other shop — even one that installed the same app ⇒ `404 not_found` (never 403; nothing is read). Ignored on a seller key (`dona_sk_`).
$x_dona_integration = billz-connector/2.4.1; // string | `name/version` of the calling integration; stored (≤ 128 chars) and searchable in the request journal.

try {
    $result = $apiInstance->getMe($accept_language, $dona_seller, $x_dona_integration);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccountApi->getMe: ', $e->getMessage(), PHP_EOL;
}

```

## API Endpoints

All URIs are relative to *https://api.dona.im/seller-api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**getMe**](docs/Api/AccountApi.md#getme) | **GET** /me | Who am I — key, shop, tier, limits
*AttentionApi* | [**ackAttention**](docs/Api/AttentionApi.md#ackattention) | **POST** /attention/{id}/ack | Acknowledge
*AttentionApi* | [**getAttention**](docs/Api/AttentionApi.md#getattention) | **GET** /attention/{id} | One attention item
*AttentionApi* | [**listAttention**](docs/Api/AttentionApi.md#listattention) | **GET** /attention | Errors, warnings, attention required
*CatalogApi* | [**batchProducts**](docs/Api/CatalogApi.md#batchproducts) | **POST** /products/batch | Batch create/update (async job)
*CatalogApi* | [**createMediaUploadUrl**](docs/Api/CatalogApi.md#createmediauploadurl) | **POST** /media/upload-url | Presigned media upload
*CatalogApi* | [**createProduct**](docs/Api/CatalogApi.md#createproduct) | **POST** /products | Create a product (lands as draft / ai_review)
*CatalogApi* | [**delistProduct**](docs/Api/CatalogApi.md#delistproduct) | **POST** /products/{id}/delist | Delist (hide) — never a hard delete
*CatalogApi* | [**getProduct**](docs/Api/CatalogApi.md#getproduct) | **GET** /products/{id} | Get a product
*CatalogApi* | [**getProductIssues**](docs/Api/CatalogApi.md#getproductissues) | **GET** /products/{id}/issues | Why a product is held, rejected or flagged
*CatalogApi* | [**listDeletedProducts**](docs/Api/CatalogApi.md#listdeletedproducts) | **GET** /products/deleted | Tombstones since a time
*CatalogApi* | [**listProducts**](docs/Api/CatalogApi.md#listproducts) | **GET** /products | List products
*CatalogApi* | [**publishProduct**](docs/Api/CatalogApi.md#publishproduct) | **POST** /products/{id}/publish | Publish
*CatalogApi* | [**updateProduct**](docs/Api/CatalogApi.md#updateproduct) | **PATCH** /products/{id} | Update a product
*EventsApi* | [**listEvents**](docs/Api/EventsApi.md#listevents) | **GET** /events | The change feed (primary channel)
*FinanceApi* | [**getBalance**](docs/Api/FinanceApi.md#getbalance) | **GET** /finance/balance | Balance
*FinanceApi* | [**listSettlements**](docs/Api/FinanceApi.md#listsettlements) | **GET** /finance/settlements | Settlement lines
*HealthApi* | [**getAccountHealth**](docs/Api/HealthApi.md#getaccounthealth) | **GET** /account/health | Account health summary
*HealthApi* | [**getAccountMetric**](docs/Api/HealthApi.md#getaccountmetric) | **GET** /account/metrics/{metric_id} | One metric with weekly history
*HealthApi* | [**getAccountVerification**](docs/Api/HealthApi.md#getaccountverification) | **GET** /account/verification | The three verdicts and what ADVANCED still needs
*JobsApi* | [**downloadJobFile**](docs/Api/JobsApi.md#downloadjobfile) | **GET** /jobs/{id}/download | Download an export&#39;s file
*JobsApi* | [**exportOrders**](docs/Api/JobsApi.md#exportorders) | **POST** /exports/orders | Export orders (async, no PII)
*JobsApi* | [**exportProducts**](docs/Api/JobsApi.md#exportproducts) | **POST** /exports/products | Export products (async)
*JobsApi* | [**getJob**](docs/Api/JobsApi.md#getjob) | **GET** /jobs/{id} | Poll a job
*KeysApi* | [**listKeys**](docs/Api/KeysApi.md#listkeys) | **GET** /keys | The shop&#39;s keys (read-only; management is portal-only)
*MetaApi* | [**getChangelog**](docs/Api/MetaApi.md#getchangelog) | **GET** /changelog | Changelog (JSON, or RSS with Accept)
*MetaApi* | [**getLlmsTxt**](docs/Api/MetaApi.md#getllmstxt) | **GET** /llms.txt | llms.txt index for AI agents
*MetaApi* | [**getOpenApi**](docs/Api/MetaApi.md#getopenapi) | **GET** /openapi.json | This document
*MetaApi* | [**getStatus**](docs/Api/MetaApi.md#getstatus) | **GET** /status | Service status
*MetaApi* | [**ping**](docs/Api/MetaApi.md#ping) | **GET** /ping | Liveness (key optional)
*OrdersApi* | [**acceptOrder**](docs/Api/OrdersApi.md#acceptorder) | **POST** /orders/{id}/accept | Accept
*OrdersApi* | [**addOrderNote**](docs/Api/OrdersApi.md#addordernote) | **POST** /orders/{id}/notes | Add a seller note
*OrdersApi* | [**batchOrderLabels**](docs/Api/OrdersApi.md#batchorderlabels) | **POST** /orders/labels | Labels for ≤ 100 orders (one PDF)
*OrdersApi* | [**cancelOrder**](docs/Api/OrdersApi.md#cancelorder) | **POST** /orders/{id}/cancel | Cancel (after acceptance) — money-reversing
*OrdersApi* | [**declineOrder**](docs/Api/OrdersApi.md#declineorder) | **POST** /orders/{id}/decline | Decline (before acceptance) — money-reversing
*OrdersApi* | [**getOrder**](docs/Api/OrdersApi.md#getorder) | **GET** /orders/{id} | Get an order (PII only with orders:pii)
*OrdersApi* | [**getOrderInvoice**](docs/Api/OrdersApi.md#getorderinvoice) | **GET** /orders/{id}/invoice.pdf | Invoice (PDF, contains PII)
*OrdersApi* | [**getOrderLabel**](docs/Api/OrdersApi.md#getorderlabel) | **GET** /orders/{id}/label.pdf | Shipping label (PDF, contains PII)
*OrdersApi* | [**getOrderTimeline**](docs/Api/OrdersApi.md#getordertimeline) | **GET** /orders/{id}/timeline | Order timeline
*OrdersApi* | [**handoverOrder**](docs/Api/OrdersApi.md#handoverorder) | **POST** /orders/{id}/handover | Hand over to the courier
*OrdersApi* | [**listOrders**](docs/Api/OrdersApi.md#listorders) | **GET** /orders | List orders (no buyer PII)
*OrdersApi* | [**markOrderReady**](docs/Api/OrdersApi.md#markorderready) | **POST** /orders/{id}/ready | Mark ready to ship
*OrdersApi* | [**shipOrder**](docs/Api/OrdersApi.md#shiporder) | **POST** /orders/{id}/ship | Ship
*ReturnsApi* | [**getReturn**](docs/Api/ReturnsApi.md#getreturn) | **GET** /returns/{id} | Get a return
*ReturnsApi* | [**listReturns**](docs/Api/ReturnsApi.md#listreturns) | **GET** /returns | List returns
*StockPricesApi* | [**listStock**](docs/Api/StockPricesApi.md#liststock) | **GET** /stock | Stock, SKU-level
*StockPricesApi* | [**setPrices**](docs/Api/StockPricesApi.md#setprices) | **POST** /prices | Set absolute prices (≤ 1 000 lines)
*StockPricesApi* | [**setStock**](docs/Api/StockPricesApi.md#setstock) | **POST** /stock | Set absolute stock (≤ 1 000 lines)
*TaxonomyApi* | [**getCategoryRequirements**](docs/Api/TaxonomyApi.md#getcategoryrequirements) | **GET** /categories/{id}/requirements | What a product in this leaf needs
*TaxonomyApi* | [**listCategories**](docs/Api/TaxonomyApi.md#listcategories) | **GET** /categories | Category tree (platform-owned)
*TaxonomyApi* | [**searchBrands**](docs/Api/TaxonomyApi.md#searchbrands) | **GET** /brands | Brand search
*TaxonomyApi* | [**searchIkpu**](docs/Api/TaxonomyApi.md#searchikpu) | **GET** /ikpu | IKPU (tax classifier) search
*WebhooksApi* | [**createWebhook**](docs/Api/WebhooksApi.md#createwebhook) | **POST** /webhooks | Register an endpoint (secret shown once)
*WebhooksApi* | [**deleteWebhook**](docs/Api/WebhooksApi.md#deletewebhook) | **DELETE** /webhooks/{id} | Remove an endpoint
*WebhooksApi* | [**getWebhook**](docs/Api/WebhooksApi.md#getwebhook) | **GET** /webhooks/{id} | Get an endpoint
*WebhooksApi* | [**listWebhookDeliveries**](docs/Api/WebhooksApi.md#listwebhookdeliveries) | **GET** /webhooks/{id}/deliveries | Delivery log (30 d)
*WebhooksApi* | [**listWebhooks**](docs/Api/WebhooksApi.md#listwebhooks) | **GET** /webhooks | List endpoints (≤ 5)
*WebhooksApi* | [**pingWebhook**](docs/Api/WebhooksApi.md#pingwebhook) | **POST** /webhooks/{id}/ping | Re-run the verification ping
*WebhooksApi* | [**redeliverWebhookDelivery**](docs/Api/WebhooksApi.md#redeliverwebhookdelivery) | **POST** /webhooks/{id}/deliveries/{delivery_id}/redeliver | Redeliver one delivery
*WebhooksApi* | [**rotateWebhookSecret**](docs/Api/WebhooksApi.md#rotatewebhooksecret) | **POST** /webhooks/{id}/rotate-secret | Rotate the signing secret (24 h dual signing)
*WebhooksApi* | [**updateWebhook**](docs/Api/WebhooksApi.md#updatewebhook) | **PATCH** /webhooks/{id} | Change url / event types / pause

## Models

- [AccountAgreementEventData](docs/Model/AccountAgreementEventData.md)
- [AccountDocumentsEventData](docs/Model/AccountDocumentsEventData.md)
- [AccountHealthEventData](docs/Model/AccountHealthEventData.md)
- [AccountKycEventData](docs/Model/AccountKycEventData.md)
- [AccountStatusEventData](docs/Model/AccountStatusEventData.md)
- [AccountSuppressedEventData](docs/Model/AccountSuppressedEventData.md)
- [AttentionCounts](docs/Model/AttentionCounts.md)
- [AttentionCountsBySeverity](docs/Model/AttentionCountsBySeverity.md)
- [AttentionEventData](docs/Model/AttentionEventData.md)
- [AttentionEventDataSubject](docs/Model/AttentionEventDataSubject.md)
- [AttentionItem](docs/Model/AttentionItem.md)
- [AttentionItemSubject](docs/Model/AttentionItemSubject.md)
- [AttentionPage](docs/Model/AttentionPage.md)
- [Balance](docs/Model/Balance.md)
- [BatchCommand](docs/Model/BatchCommand.md)
- [BatchRequest](docs/Model/BatchRequest.md)
- [Brand](docs/Model/Brand.md)
- [BrandPage](docs/Model/BrandPage.md)
- [BulkResult](docs/Model/BulkResult.md)
- [BulkResultSummary](docs/Model/BulkResultSummary.md)
- [Category](docs/Model/Category.md)
- [CategoryAttribute](docs/Model/CategoryAttribute.md)
- [CategoryAttributeOptionsInner](docs/Model/CategoryAttributeOptionsInner.md)
- [CategoryPage](docs/Model/CategoryPage.md)
- [CategoryRequirements](docs/Model/CategoryRequirements.md)
- [ChangelogEntry](docs/Model/ChangelogEntry.md)
- [ChangelogEntryPage](docs/Model/ChangelogEntryPage.md)
- [DeclineRequest](docs/Model/DeclineRequest.md)
- [Delivery](docs/Model/Delivery.md)
- [DeliveryPage](docs/Model/DeliveryPage.md)
- [Error](docs/Model/Error.md)
- [ErrorDetail](docs/Model/ErrorDetail.md)
- [ErrorMeta](docs/Model/ErrorMeta.md)
- [Event](docs/Model/Event.md)
- [EventLinks](docs/Model/EventLinks.md)
- [EventPage](docs/Model/EventPage.md)
- [ExportRequest](docs/Model/ExportRequest.md)
- [ExportRequestFilters](docs/Model/ExportRequestFilters.md)
- [GetOrder200Response](docs/Model/GetOrder200Response.md)
- [HealthSummary](docs/Model/HealthSummary.md)
- [HealthSummarySuppression](docs/Model/HealthSummarySuppression.md)
- [HeldForReview](docs/Model/HeldForReview.md)
- [HeldForReviewSubject](docs/Model/HeldForReviewSubject.md)
- [Ikpu](docs/Model/Ikpu.md)
- [IkpuPackagesInner](docs/Model/IkpuPackagesInner.md)
- [IkpuPage](docs/Model/IkpuPage.md)
- [Issue](docs/Model/Issue.md)
- [Job](docs/Model/Job.md)
- [JobAccepted](docs/Model/JobAccepted.md)
- [JobAcceptedLinks](docs/Model/JobAcceptedLinks.md)
- [JobProgress](docs/Model/JobProgress.md)
- [Key](docs/Model/Key.md)
- [KeyEventData](docs/Model/KeyEventData.md)
- [KeyPage](docs/Model/KeyPage.md)
- [LabelsRequest](docs/Model/LabelsRequest.md)
- [Limits](docs/Model/Limits.md)
- [LimitsRemaining](docs/Model/LimitsRemaining.md)
- [LineResult](docs/Model/LineResult.md)
- [LiveAccessEventData](docs/Model/LiveAccessEventData.md)
- [LiveStrikeEventData](docs/Model/LiveStrikeEventData.md)
- [LocalizedText](docs/Model/LocalizedText.md)
- [Me](docs/Model/Me.md)
- [MeApiAccess](docs/Model/MeApiAccess.md)
- [MeAttention](docs/Model/MeAttention.md)
- [MeKey](docs/Model/MeKey.md)
- [MeShop](docs/Model/MeShop.md)
- [MediaUploadRequest](docs/Model/MediaUploadRequest.md)
- [MediaUploadUrl](docs/Model/MediaUploadUrl.md)
- [Metric](docs/Model/Metric.md)
- [MetricDetail](docs/Model/MetricDetail.md)
- [MetricDetailAllOfHistory](docs/Model/MetricDetailAllOfHistory.md)
- [ModelReturn](docs/Model/ModelReturn.md)
- [NoteCreated](docs/Model/NoteCreated.md)
- [NoteRequest](docs/Model/NoteRequest.md)
- [OnAccountAgreementOwedRequest](docs/Model/OnAccountAgreementOwedRequest.md)
- [OnAccountDocumentsDecidedRequest](docs/Model/OnAccountDocumentsDecidedRequest.md)
- [OnAccountHealthChangedRequest](docs/Model/OnAccountHealthChangedRequest.md)
- [OnAccountKycReopenedRequest](docs/Model/OnAccountKycReopenedRequest.md)
- [OnAccountStatusChangedRequest](docs/Model/OnAccountStatusChangedRequest.md)
- [OnAccountSuppressedRequest](docs/Model/OnAccountSuppressedRequest.md)
- [OnAttentionOpenedRequest](docs/Model/OnAttentionOpenedRequest.md)
- [OnKeyExpiringRequest](docs/Model/OnKeyExpiringRequest.md)
- [OnLiveAccessChangedRequest](docs/Model/OnLiveAccessChangedRequest.md)
- [OnLiveStrikeRequest](docs/Model/OnLiveStrikeRequest.md)
- [OnOrderAcceptDueSoonRequest](docs/Model/OnOrderAcceptDueSoonRequest.md)
- [OnOrderCreatedRequest](docs/Model/OnOrderCreatedRequest.md)
- [OnOrderDeclinedRequest](docs/Model/OnOrderDeclinedRequest.md)
- [OnOrderLineCancelledRequest](docs/Model/OnOrderLineCancelledRequest.md)
- [OnPingRequest](docs/Model/OnPingRequest.md)
- [OnProductHeldRequest](docs/Model/OnProductHeldRequest.md)
- [OnProductPublishedRequest](docs/Model/OnProductPublishedRequest.md)
- [OnReturnRequestedRequest](docs/Model/OnReturnRequestedRequest.md)
- [OnStockLowRequest](docs/Model/OnStockLowRequest.md)
- [OnWebhookFailingRequest](docs/Model/OnWebhookFailingRequest.md)
- [OnWriteHeldRequest](docs/Model/OnWriteHeldRequest.md)
- [Order](docs/Model/Order.md)
- [OrderCancelledEventData](docs/Model/OrderCancelledEventData.md)
- [OrderDeadlineEventData](docs/Model/OrderDeadlineEventData.md)
- [OrderEventData](docs/Model/OrderEventData.md)
- [OrderItem](docs/Model/OrderItem.md)
- [OrderLineCancelledEventData](docs/Model/OrderLineCancelledEventData.md)
- [OrderMeta](docs/Model/OrderMeta.md)
- [OrderPage](docs/Model/OrderPage.md)
- [OrderTimeline](docs/Model/OrderTimeline.md)
- [OrderTimelineEntry](docs/Model/OrderTimelineEntry.md)
- [OrderTransition](docs/Model/OrderTransition.md)
- [OrderWithPii](docs/Model/OrderWithPii.md)
- [Ping](docs/Model/Ping.md)
- [PingEventData](docs/Model/PingEventData.md)
- [PriceLine](docs/Model/PriceLine.md)
- [PriceRequest](docs/Model/PriceRequest.md)
- [Product](docs/Model/Product.md)
- [ProductCreate](docs/Model/ProductCreate.md)
- [ProductCreated](docs/Model/ProductCreated.md)
- [ProductCreatedHold](docs/Model/ProductCreatedHold.md)
- [ProductHold](docs/Model/ProductHold.md)
- [ProductIssueEventData](docs/Model/ProductIssueEventData.md)
- [ProductIssues](docs/Model/ProductIssues.md)
- [ProductPage](docs/Model/ProductPage.md)
- [ProductState](docs/Model/ProductState.md)
- [ProductStatusEventData](docs/Model/ProductStatusEventData.md)
- [ProductUpdate](docs/Model/ProductUpdate.md)
- [Recipient](docs/Model/Recipient.md)
- [ReturnEventData](docs/Model/ReturnEventData.md)
- [ReturnItemsInner](docs/Model/ReturnItemsInner.md)
- [ReturnPage](docs/Model/ReturnPage.md)
- [Settlement](docs/Model/Settlement.md)
- [SettlementPage](docs/Model/SettlementPage.md)
- [Status](docs/Model/Status.md)
- [StatusComponents](docs/Model/StatusComponents.md)
- [StatusIncidentsInner](docs/Model/StatusIncidentsInner.md)
- [StockEventData](docs/Model/StockEventData.md)
- [StockLine](docs/Model/StockLine.md)
- [StockLineView](docs/Model/StockLineView.md)
- [StockLineViewPage](docs/Model/StockLineViewPage.md)
- [StockRequest](docs/Model/StockRequest.md)
- [Tombstone](docs/Model/Tombstone.md)
- [TombstonePage](docs/Model/TombstonePage.md)
- [Variant](docs/Model/Variant.md)
- [VariantInput](docs/Model/VariantInput.md)
- [Verification](docs/Model/Verification.md)
- [Webhook](docs/Model/Webhook.md)
- [WebhookCreate](docs/Model/WebhookCreate.md)
- [WebhookEventData](docs/Model/WebhookEventData.md)
- [WebhookPage](docs/Model/WebhookPage.md)
- [WebhookPing](docs/Model/WebhookPing.md)
- [WebhookUpdate](docs/Model/WebhookUpdate.md)
- [WebhookWithSecret](docs/Model/WebhookWithSecret.md)
- [WriteEventData](docs/Model/WriteEventData.md)

## Authorization

Authentication schemes defined for the API:
### bearerKey

- **Type**: Bearer authentication (dona_<sk|ak|it>_live_<43 base62><6 base62 CRC32>)

## Tests

To run the tests, use:

```bash
composer install
vendor/bin/phpunit
```

## Author



## About this package

This PHP package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: `v1 (frozen 2026-09-24)`
    - Package version: `0.1.0`
    - Generator version: `7.25.0`
- Build package: `org.openapitools.codegen.languages.PhpClientCodegen`

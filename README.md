# Dona API — SDKs and examples

Typed clients for the **Dona API** (`https://api.dona.im/seller-api/v1`) in **TypeScript, Python, Go,
PHP and C#**, generated from one OpenAPI 3.1 contract, plus runnable examples for each.

[Oʻzbekcha](#oʻzbekcha) · [Русский](#русский) · [English](#english)

| | |
|---|---|
| Contract | [`spec/openapi.yaml`](spec/openapi.yaml) — the same document the API serves at [`/seller-api/v1/openapi.json`](https://api.dona.im/seller-api/v1/openapi.json) (CI proves it) |
| SDKs | [`sdks/`](sdks/) — **generated, never edited by hand** (CI regenerates and fails on any difference) |
| Examples | [`examples/`](examples/) — `GET /me` → `GET /products?limit=5` → `POST /stock` (`dry_run`) + a webhook signature verifier, per language |
| Status | **Pre-release (0.1.0).** The API is deployed but not yet enabled for sellers (until then a valid key gets `503 limits_unavailable`); `POST /stock` ships in increment S3. Packages are **not yet published** — install from this repository (below). |

## Install · Oʻrnatish · Установка

Until the packages are published (S6), install from a clone of this repository
(`git clone git@github.com:ozbuz/dona-api.git`):

| Language | Now (from the repo) | After publication (S6) |
|---|---|---|
| **TypeScript** (Node ≥ 20) | `cd sdks/typescript && npm install && npm run build && npm pack` → `npm install /path/to/dona-api-0.1.0.tgz` | `npm install @dona/api` |
| **Python** (≥ 3.11) | `pip install "dona-api @ git+ssh://git@github.com/ozbuz/dona-api.git#subdirectory=sdks/python"` | `pip install dona-api` |
| **Go** (≥ 1.27) | `GOPRIVATE=github.com/ozbuz/* go get github.com/ozbuz/dona-api/sdks/go@main` | `go get github.com/ozbuz/dona-api/sdks/go@v0.1.0` |
| **PHP** (≥ 8.1, Guzzle 7) | composer `"repositories": [{"type": "path", "url": "/path/to/dona-api/sdks/php"}]` + `"require": {"ozbuz/dona-api": "*@dev"}` | `composer require ozbuz/dona-api` |
| **C#** (.NET 10) | `dotnet add reference /path/to/dona-api/sdks/csharp/src/Dona.Api/Dona.Api.csproj` | `dotnet add package Dona.Api` |

Each SDK's first call, and the complete runnable version, is in [`examples/`](examples/README.md).

---

## Oʻzbekcha

**Manzil.** Barcha soʻrovlar: `https://api.dona.im/seller-api/v1`. Boshqa muhit yoʻq — sinov uchun
`dry_run` ishlatiladi.

**Kalit.** Doʻkon **egasi** kalitni seller portalda yaratadi: *Sozlamalar › API*. Kalit
(`dona_sk_live_…`) faqat **bir marta** koʻrsatiladi. Har bir soʻrovda:
`Authorization: Bearer dona_sk_live_…`. `X-Api-Key` sarlavhasi yoki URL ichidagi kalit qabul
qilinmaydi (`401 use_authorization_header`). Kalit — doʻkonning oʻzi: yoʻlda doʻkon ID yoʻq.

**Chegaralar.** Har bir javobda `RateLimit-Policy`, `RateLimit`, `X-RateLimit-Limit`,
`X-RateLimit-Remaining`, `X-RateLimit-Reset` bor. `429`/`503` da `Retry-After` (soniya) va
`Dona-Rate-Limited-Reason` qoʻshiladi — shuncha kutib, qayta yuboring. Limitlar IP boʻyicha emas,
**kalit va doʻkon** boʻyicha hisoblanadi. `GET /me` joriy limit va qolgan hajmni koʻrsatadi.

**Idempotentlik.** Har bir `POST`/`PATCH` uchun `Idempotency-Key` (1–255 belgi) **majburiy**.
Bitta mantiqiy yozuv — bitta kalit; tarmoq xatosida **oʻsha kalit** bilan qayta yuboring: 24 soat
davomida javob aynan takrorlanadi, yozuv ikki marta bajarilmaydi. `409 idempotency_in_progress` —
birinchi soʻrov hali tugamagan; `409 idempotency_mismatch` — kalit boshqa tana bilan ishlatilgan.

**`dry_run`.** Istalgan yozuvga `?dry_run=true` (yoki `Dona-Dry-Run: true`) qoʻshing: tekshiruv,
himoya va natija hisoblanadi, soʻng hammasi bekor qilinadi — **hech narsa yozilmaydi**. Integratsiyani
shu bilan sinab koʻring.

**`202 held_for_review`.** Bu xato emas: narx yoki qoldiqdagi keskin oʻzgarishni himoya tizimi
ushlab qoldi va **hech narsa yozilmadi**. Tanada `error` yoʻq; `code: "held_for_review"`,
`approval_id`, `rule` (masalan `drop_100x`, `stock_jump_10x`), `approver` (`owner` | `staff`),
`expires_at`. Natijani `write.approved` / `write.rejected` / `write.expired` hodisalaridan kuting.
Xatolarda har doim `error` kodiga qarab tarmoqlaning, `message` matniga emas.

**Webhooklar** Standard Webhooks boʻyicha imzolanadi (`webhook-id`, `webhook-timestamp`,
`webhook-signature`). Imzoni **xom** tana baytlari boʻyicha tekshiring — har bir tildagi tayyor
tekshiruvchi: [`examples/`](examples/README.md).

**Hujjatlar:** [OpenAPI](https://api.dona.im/seller-api/v1/openapi.json) ·
[llms.txt](https://api.dona.im/seller-api/v1/llms.txt) · seller portal › *Sozlamalar › API* ·
`dona.uz/developers` (S6 da ochiladi).

## Русский

**Адрес.** Все запросы: `https://api.dona.im/seller-api/v1`. Другой среды нет — для проверки
используйте `dry_run`.

**Ключ.** Ключ создаёт **владелец** магазина в кабинете продавца: *Sozlamalar › API*. Ключ
(`dona_sk_live_…`) показывается **один раз**. В каждом запросе:
`Authorization: Bearer dona_sk_live_…`. Заголовок `X-Api-Key` или ключ в URL не принимаются
(`401 use_authorization_header`). Ключ и есть магазин: ID магазина в пути нет.

**Лимиты.** Каждый ответ содержит `RateLimit-Policy`, `RateLimit`, `X-RateLimit-Limit`,
`X-RateLimit-Remaining`, `X-RateLimit-Reset`. На `429`/`503` добавляются `Retry-After` (секунды) и
`Dona-Rate-Limited-Reason` — подождите указанное время и повторите. Лимиты считаются по **ключу и
магазину**, не по IP. `GET /me` показывает текущие лимиты и остаток.

**Идемпотентность.** `Idempotency-Key` (1–255 символов) **обязателен** для каждого `POST`/`PATCH`.
Одна логическая запись — один ключ; при сетевой ошибке повторяйте с **тем же ключом**: 24 часа ответ
воспроизводится байт в байт, запись не выполняется дважды. `409 idempotency_in_progress` — первый
запрос ещё выполняется; `409 idempotency_mismatch` — ключ уже использован с другим телом.

**`dry_run`.** Добавьте к любой записи `?dry_run=true` (или `Dona-Dry-Run: true`): проверка, защита
и расчёт результата выполняются, затем всё откатывается — **ничего не записывается**. Так проверяют
интеграцию.

**`202 held_for_review`.** Это не ошибка: защита задержала резкое изменение цены или остатка, и
**ничего не записано**. В теле нет `error`; есть `code: "held_for_review"`, `approval_id`, `rule`
(например `drop_100x`, `stock_jump_10x`), `approver` (`owner` | `staff`), `expires_at`. Итог
приходит событиями `write.approved` / `write.rejected` / `write.expired`. В ошибках ветвитесь по коду
`error`, а не по тексту `message`.

**Вебхуки** подписываются по Standard Webhooks (`webhook-id`, `webhook-timestamp`,
`webhook-signature`). Проверяйте подпись по **сырым** байтам тела — готовые проверки для каждого
языка: [`examples/`](examples/README.md).

**Документация:** [OpenAPI](https://api.dona.im/seller-api/v1/openapi.json) ·
[llms.txt](https://api.dona.im/seller-api/v1/llms.txt) · кабинет продавца › *Sozlamalar › API* ·
`dona.uz/developers` (откроется на этапе S6).

## English

**Base URL.** `https://api.dona.im/seller-api/v1` — the only environment; `dry_run` is the rehearsal.

**Key.** The shop **owner** mints keys in the seller portal (*Sozlamalar › API*); a key
(`dona_sk_live_…`) is shown **once**. Send it on every request as
`Authorization: Bearer dona_sk_live_…`. `X-Api-Key` or a key in the query string is refused
(`401 use_authorization_header`). The key *is* the tenant — no shop id appears in any path.

**Rate limits.** Every response carries `RateLimit-Policy` (every bucket the key is subject to),
`RateLimit` (the bucket closest to exhaustion: `r` remaining, `t` seconds to reset) and the legacy
mirrors `X-RateLimit-Limit` / `-Remaining` / `-Reset`. Every `429`/`503` adds `Retry-After` (seconds)
and `Dona-Rate-Limited-Reason` — wait that long, then retry. Limits are per **key and shop**, never
per IP. `GET /me` returns the live limits and the remaining budget.

**Idempotency.** `Idempotency-Key` (1–255 chars) is **required** on every `POST`/`PATCH` (except the
few operations the contract marks as naturally idempotent). One logical write, one key; on a network
error retry with the **same** key — a terminal 2xx/4xx is replayed byte-identical for 24 h and the
write never happens twice (a 5xx is never stored). `409 idempotency_in_progress`: the first attempt is
still running. `409 idempotency_mismatch`: the key was used with a different body.

**`dry_run`.** Add `?dry_run=true` (or `Dona-Dry-Run: true`) to any write: validation, the guard and
the effect are computed, then rolled back — **nothing is written**, no events, no counters. Build and
test integrations this way.

**`202 held_for_review`.** A *success* envelope, not an error: the plausibility guard held a
suspicious price/stock change and **nothing was written**. The body has no `error`:

```json
{ "code": "held_for_review", "status": "held", "approval_id": "01997b31-…", "rule": "drop_100x",
  "kind": "price", "subject": { "type": "product", "id": "0199612e-…" }, "approver": "owner",
  "expires_at": "2026-10-08T14:05:12+05:00", "message": "…", "request_id": "req_…" }
```

Follow `write.approved` / `write.rejected` / `write.expired` events for the outcome. Replaying the same
`Idempotency-Key` re-derives from the held row (approved ⇒ the applied result, rejected ⇒ `409`,
pending ⇒ this `202` again) — never a second hold. On errors, branch on `error` (a stable code), never
on `message` (localised by `Accept-Language`). Enums are **open**: tolerate values you do not know —
the SDKs type them as strings for that reason.

**Webhooks** are signed per [Standard Webhooks](https://www.standardwebhooks.com)
(`webhook-id`, `webhook-timestamp`, `webhook-signature`; tolerance 300 s; two signatures for 24 h
after a secret rotation). Verify the **raw** body bytes and dedupe on `webhook-id`. Each language's
verifier in [`examples/`](examples/README.md) passes the same 12 vectors, including the Standard
Webhooks reference vector.

**Docs:** [OpenAPI](https://api.dona.im/seller-api/v1/openapi.json) ·
[llms.txt](https://api.dona.im/seller-api/v1/llms.txt) · seller portal › *Sozlamalar › API* ·
`dona.uz/developers` (opens at S6).

### How this repository works (maintainers)

```
spec/openapi.yaml        byte-identical copy of the contract (source of truth: OZB architecture/DB/seller-api/contract/)
spec/*.sha256            its sha, and ozb-backend's checked-in sha of the served JSON (CI holds us to both)
tools/clientview         spec → the view the generators read (open enums, presence rules, short info)
tools/openapi2json       verbatim copy of the backend's YAML→JSON converter (the drift proof)
tools/mockapi            local stand-in answering the contract's own examples (examples smoke test)
generators/versions.env  EVERY generator / toolchain version, pinned in one place
generators/<lang>/       one generate.sh per language
sdks/<lang>/             GENERATED output — committed, never hand-edited
examples/<lang>/         hand-written, runnable; compiled, type-checked and smoke-tested in CI
```

| Language | Generator (pinned in `generators/versions.env`) | Runtime |
|---|---|---|
| TypeScript | `openapi-typescript` 7.13.0 (types) + `openapi-fetch` 0.17.0 | fetch, zero other deps |
| Python | `openapi-python-client` 0.29.1 (ruff 0.16.9 formats) | httpx + attrs, sync + asyncio |
| Go | `oapi-codegen` v2.8.0 (runtime v1.7.0) | net/http |
| PHP | `openapi-generator` 7.25.0 (`php`) | Guzzle 7 |
| C# | `openapi-generator` 7.25.0 (`csharp`, `generichost`) | .NET 10, System.Text.Json |

- **Contract changed?** `scripts/sync-spec.sh` (copies the YAML, records both shas, refuses when the
  backend has not synced yet — backend first), then `make generate`, commit `spec/` + `sdks/` together.
- **CI** (`.github/workflows/generate.yml`, required on `main`): `make spec-check generate verify-clean
  check smoke` — contract drift, regeneration diff, `tsc` / `mypy` + import / `go vet` + build /
  `php -l` / `dotnet build`, webhook vectors in all five languages, and every quickstart against
  `tools/mockapi` (asserting the key header, `limit=5`, `Idempotency-Key` and `dry_run=true`).
- **Locally**: Go, Node ≥ 24, `uv`, Docker. `make all` then `make smoke`.

### Publishing (S6 — not done; nothing in CI publishes)

Decided at S6, with Bek: the package names (`@dona/api` needs the npm org `dona`; Packagist has no
subdirectory support), the version, and making this repository **public** (Bek's action:
`gh repo edit ozbuz/dona-api --visibility public --accept-visibility-change-consequences`).

```bash
# npm — first drop "private": true from generators/typescript/template/package.json and regenerate
cd sdks/typescript && npm ci && npm run build && npm publish --access public --provenance
# PyPI (trusted publishing from a release workflow)
cd sdks/python && uv build && uv publish
# Go — the module lives in a subdirectory, so the tag carries its path (needs the repo public for proxy.golang.org)
git tag sdks/go/v0.1.0 && git push origin sdks/go/v0.1.0
# Packagist — needs composer.json at a repository root: split sdks/php into its own repo, then submit it
git subtree split --prefix sdks/php -b php-release && git push git@github.com:ozbuz/dona-api-php.git php-release:main
# NuGet
dotnet pack sdks/csharp/src/Dona.Api/Dona.Api.csproj -c Release -o out
dotnet nuget push out/Dona.Api.0.1.0.nupkg --api-key "$NUGET_API_KEY" --source https://api.nuget.org/v3/index.json
```

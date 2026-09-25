# Dona API — SDKs and examples

Typed clients for the **Dona API** (`https://api.dona.im/seller-api/v1`) in **TypeScript, Python, Go,
PHP and C#**, generated from one OpenAPI 3.1 contract, plus runnable examples for each.

[Oʻzbekcha](#oʻzbekcha) · [Русский](#русский) · [English](#english)

| | |
|---|---|
| Contract | [`spec/openapi.yaml`](spec/openapi.yaml) — the same document the API serves at [`/seller-api/v1/openapi.json`](https://api.dona.im/seller-api/v1/openapi.json) (CI proves it) |
| SDKs | [`sdks/`](sdks/) — **generated, never edited by hand** (CI regenerates and fails on any difference) |
| Examples | [`examples/`](examples/) — `GET /me` → `GET /products?limit=5` → `POST /stock` (`dry_run`) + a webhook signature verifier, per language |
| Status | **Pre-release (0.1.0).** The API is deployed but not yet enabled for sellers (until then a valid key gets `503 limits_unavailable`). The contract now covers S1–S7: reads, writes (`POST /stock` etc., gated on `writes_enabled`), webhooks, an MCP door for AI agents (`dona_ak_live_…`) with write tools + owner confirmation, an OAuth 2.1 door for connectors (read-only), and vendor-app install keys (`dona_it_live_…`, `Dona-Seller` header). **The repository is public** (2026-09-26); registry packages (npm/PyPI/NuGet/Packagist) are **not yet published** — the token for each is still missing, see [`.github/workflows/publish.yml`](.github/workflows/publish.yml). Install from the repo below; Go and Python need no clone, TypeScript/PHP/C# do (their tooling has no git-subdirectory-install support) — none need auth. |

## Install · Oʻrnatish · Установка

The repository is public — no SSH key, no `GOPRIVATE`, and no registry account needed for any
language. Each command below was actually run against the public, merged `main`:

| Language | Works today (from this repo) | After a registry token is added |
|---|---|---|
| **Go** (≥ 1.26) | `go get github.com/ozbuz/dona-api/sdks/go@main` | `go get github.com/ozbuz/dona-api/sdks/go@v0.1.0` (a `sdks/go/vX.Y.Z` tag) |
| **Python** (≥ 3.11) | `pip install "dona-api @ git+https://github.com/ozbuz/dona-api.git@main#subdirectory=sdks/python"` | `pip install dona-api` |
| **TypeScript** (Node ≥ 20) | **Needs a local clone** — npm's git-dependency syntax has no subdirectory support (only `#<commit-ish>`/`#semver:`, verified against `npm help install`; unlike pip's `#subdirectory=`), and this monorepo has no root `package.json`, so `npm install github:ozbuz/dona-api` cannot work: `git clone https://github.com/ozbuz/dona-api.git && cd dona-api/sdks/typescript && npm install` (builds `dist/` automatically — an npm `prepare` hook — nothing extra to run by hand), then from your project `npm install ../dona-api/sdks/typescript` (or `npm pack` it first for a tarball) | `npm install @dona/api` |
| **PHP** (≥ 8.1, Guzzle 7) | **Needs a local clone** — composer has no subdirectory support for a git dependency (only Packagist-style repos at their own root), so this monorepo cannot be `composer require`d directly yet: `git clone https://github.com/ozbuz/dona-api.git && cd your-project && composer config repositories.dona-api path ../dona-api/sdks/php && composer require ozbuz/dona-api:*@dev` | `composer require ozbuz/dona-api` (once [`ozbuz/dona-api-php`](https://github.com/ozbuz/dona-api-php) exists and is submitted to Packagist — see the workflow) |
| **C#** (.NET 10) | `git clone https://github.com/ozbuz/dona-api.git && dotnet add reference path/to/dona-api/sdks/csharp/src/Dona.Api/Dona.Api.csproj` — no registry-free git-reference mechanism in .NET, so a clone (or `git submodule add`) is the only option today | `dotnet add package Dona.Api` |

Each SDK's first call, and the complete runnable version, is in [`examples/`](examples/README.md).

---

## Oʻzbekcha

**Manzil.** Barcha soʻrovlar: `https://api.dona.im/seller-api/v1`. Boshqa muhit yoʻq — sinov uchun
`dry_run` ishlatiladi.

**Kalit.** Doʻkon **egasi** kalitni seller portalda yaratadi: *Sozlamalar › API*. Kalit
(`dona_sk_live_…`) faqat **bir marta** koʻrsatiladi. Har bir soʻrovda:
`Authorization: Bearer dona_sk_live_…`. `X-Api-Key` sarlavhasi yoki URL ichidagi kalit qabul
qilinmaydi (`401 use_authorization_header`). Kalit — doʻkonning oʻzi: yoʻlda doʻkon ID yoʻq. Uch xil
kalit: `sk` sotuvchi (shu REST daraxti) · `ak` agent (faqat MCP eshigi) · `it` vendor-ilova
oʻrnatmasi — bunday kalit har bir soʻrovda `Dona-Seller: <shop-id>` yuborishi shart (yoʻq/notoʻgʻri
⇒ `400 invalid_body`; boshqa doʻkon ⇒ `404 not_found`) va hech qachon `orders:pii`, `finance:read`,
`mcp` yoki `webhooks:manage` ololmaydi.

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
shu bilan sinab koʻring. Faqat **`true` / `false` soʻzma-soʻz satrlar** qabul qilinadi — bu string
enum, boolean emas; `1`, `0`, `yes`, `TRUE`, boʻsh qiymat — barchasi `400 invalid_body`. Shu sababli
SDK'lar bu parametrni satr sifatida tiplaydi.

**`202 held_for_review`.** Bu xato emas: narx yoki qoldiqdagi keskin oʻzgarishni himoya tizimi
ushlab qoldi va **hech narsa yozilmadi**. Tanada `error` yoʻq; `code: "held_for_review"`,
`approval_id`, `rule` (masalan `drop_100x`, `stock_jump_10x`), `approver` (`owner` | `staff`),
`expires_at`. Natijani `write.approved` / `write.rejected` / `write.expired` hodisalaridan kuting.
Xatolarda har doim `error` kodiga qarab tarmoqlaning, `message` matniga emas.

**Webhooklar** Standard Webhooks boʻyicha imzolanadi (`webhook-id`, `webhook-timestamp`,
`webhook-signature`). Imzoni **xom** tana baytlari boʻyicha tekshiring — har bir tildagi tayyor
tekshiruvchi: [`examples/`](examples/README.md).

**MCP** (`https://api.dona.im/seller-api/mcp`, Streamable HTTP / JSON-RPC 2.0) — AI agentlar uchun
alohida eshik, agent kaliti bilan (`dona_ak_live_…`, scope `mcp`); `sk`/`it` kalitlar u yerda rad
etiladi, `ak` kalit esa REST daraxtida rad etiladi. Oʻqish vositalari doim mavjud; **yozish
vositalari** (`dona.catalog.update_stock`, `dona.catalog.update_price`, `dona.orders.ship`,
`dona.orders.cancel`) faqat ADVANCED doʻkon uchun, `writes_enabled` yoqilganda, va birinchi
chaqiruvda hech qachon bajarilmaydi: form elicitation qoʻllab-quvvatlovchi klient tasdiqlash formasi
va bir martalik `requestState` oladi; boshqa har qanday klient `approval_required` oladi — yozuv
doʻkon **egasi** *Sozlamalar › API › Kutilayotgan yozuvlar*da tasdiqlaydigan kutilayotgan niyatga
aylanadi; agent natijani bilish uchun xuddi shu `request_id` bilan qayta chaqiradi.

**OAuth** (`https://api.dona.im/seller-api/oauth`, RFC 8414/9728 boʻyicha discovery) claude.ai yoki
ChatGPT kabi konnektorlarga kalitsiz MCP eshigiga kirish imkonini beradi: PKCE `S256`, Dona ruxsat
roʻyxatidagi Client ID Metadata Document, doʻkon **egasi** seller portalda rozilik beradi
(*Sozlamalar › API › Ulangan ilovalar*, istalgan vaqtda uzish mumkin). **v1'da faqat oʻqish**: har
qanday yozish vositasi OAuth tokeniga `403 insufficient_scope` bilan javob beradi — yozish agent
kalitlarida qoladi.

**Hujjatlar:** [OpenAPI](https://api.dona.im/seller-api/v1/openapi.json) ·
[llms.txt](https://api.dona.im/seller-api/v1/llms.txt) · seller portal › *Sozlamalar › API* ·
`dona.uz/developers` (S6 da ochiladi).

## Русский

**Адрес.** Все запросы: `https://api.dona.im/seller-api/v1`. Другой среды нет — для проверки
используйте `dry_run`.

**Ключ.** Ключ создаёт **владелец** магазина в кабинете продавца: *Sozlamalar › API*. Ключ
(`dona_sk_live_…`) показывается **один раз**. В каждом запросе:
`Authorization: Bearer dona_sk_live_…`. Заголовок `X-Api-Key` или ключ в URL не принимаются
(`401 use_authorization_header`). Ключ и есть магазин: ID магазина в пути нет. Три вида ключей: `sk`
продавец (это REST-дерево) · `ak` агент (только дверь MCP) · `it` установка приложения-вендора —
такой ключ обязан слать `Dona-Seller: <shop-id>` в каждом запросе (нет/неверен ⇒
`400 invalid_body`; чужой магазин ⇒ `404 not_found`) и никогда не получает `orders:pii`,
`finance:read`, `mcp` или `webhooks:manage`.

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
интеграцию. Принимаются **только буквальные строки `true` / `false`** — это строковый enum, а не
булево значение; `1`, `0`, `yes`, `TRUE`, пустое значение — везде `400 invalid_body`. Поэтому SDK
типизируют параметр как строку.

**`202 held_for_review`.** Это не ошибка: защита задержала резкое изменение цены или остатка, и
**ничего не записано**. В теле нет `error`; есть `code: "held_for_review"`, `approval_id`, `rule`
(например `drop_100x`, `stock_jump_10x`), `approver` (`owner` | `staff`), `expires_at`. Итог
приходит событиями `write.approved` / `write.rejected` / `write.expired`. В ошибках ветвитесь по коду
`error`, а не по тексту `message`.

**Вебхуки** подписываются по Standard Webhooks (`webhook-id`, `webhook-timestamp`,
`webhook-signature`). Проверяйте подпись по **сырым** байтам тела — готовые проверки для каждого
языка: [`examples/`](examples/README.md).

**MCP** (`https://api.dona.im/seller-api/mcp`, Streamable HTTP / JSON-RPC 2.0) — отдельная дверь для
AI-агентов, ключ агента (`dona_ak_live_…`, scope `mcp`); ключи `sk`/`it` там отклоняются, а ключ `ak`
отклоняется на REST-дереве. Инструменты чтения доступны всегда; **инструменты записи**
(`dona.catalog.update_stock`, `dona.catalog.update_price`, `dona.orders.ship`,
`dona.orders.cancel`) — только для магазина уровня ADVANCED при включённом `writes_enabled`, и
никогда не выполняются с первого вызова: клиент с form elicitation получает форму подтверждения и
одноразовый `requestState`; любой другой клиент получает `approval_required` — запись становится
ожидающим намерением, которое подтверждает **владелец** магазина в *Sozlamalar › API › Kutilayotgan
yozuvlar*; агент повторяет вызов с тем же `request_id`, чтобы узнать результат.

**OAuth** (`https://api.dona.im/seller-api/oauth`, discovery по RFC 8414/9728) позволяет коннекторам
вроде claude.ai или ChatGPT достучаться до двери MCP без вставленного ключа: PKCE `S256`, Client ID
Metadata Document из списка разрешённых Dona, согласие даёт **владелец** магазина в кабинете
продавца (*Sozlamalar › API › Ulangan ilovalar*, отключить можно в любой момент). **В v1 — только
чтение**: любой инструмент записи отвечает токену OAuth `403 insufficient_scope`; запись остаётся за
ключами агентов.

**Документация:** [OpenAPI](https://api.dona.im/seller-api/v1/openapi.json) ·
[llms.txt](https://api.dona.im/seller-api/v1/llms.txt) · кабинет продавца › *Sozlamalar › API* ·
`dona.uz/developers` (откроется на этапе S6).

## English

**Base URL.** `https://api.dona.im/seller-api/v1` — the only environment; `dry_run` is the rehearsal.

**Key.** The shop **owner** mints keys in the seller portal (*Sozlamalar › API*); a key
(`dona_sk_live_…`) is shown **once**. Send it on every request as
`Authorization: Bearer dona_sk_live_…`. `X-Api-Key` or a key in the query string is refused
(`401 use_authorization_header`). The key *is* the tenant — no shop id appears in any path. Three
kinds: `sk` seller (this REST tree) · `ak` agent (MCP door only) · `it` vendor-app install, which
must also send `Dona-Seller: <shop-id>` on every request (missing/invalid ⇒ `400 invalid_body`;
another shop's id ⇒ `404 not_found`) and can never hold `orders:pii`, `finance:read`, `mcp` or
`webhooks:manage`.

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
test integrations this way. **Only the literal strings `true` / `false`** are accepted, in either
place — it is a string enum, not a boolean; `1`, `0`, `yes`, `TRUE`, an empty value all get
`400 invalid_body`. The SDKs type the parameter as a string for this reason.

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

**MCP** (`https://api.dona.im/seller-api/mcp`, Streamable HTTP / JSON-RPC 2.0) is a separate door for
AI agents, authenticated with an agent key (`dona_ak_live_…`, scope `mcp`) — `sk`/`it` keys are
refused there, and an `ak` key is refused on the REST tree. Read tools are always available; **write
tools** (`dona.catalog.update_stock`, `dona.catalog.update_price`, `dona.orders.ship`,
`dona.orders.cancel`) exist only for an ADVANCED shop while `writes_enabled` is on, and never execute
on the first call: a client with form elicitation gets a confirmation form and a single-use
`requestState`; any other client gets `approval_required` and the write becomes a pending intent the
shop **owner** confirms in *Sozlamalar › API › Kutilayotgan yozuvlar* — the agent re-calls with the
same `request_id` to learn the outcome.

**OAuth** (`https://api.dona.im/seller-api/oauth`, RFC 8414/9728 discovery) lets connectors such as
claude.ai or ChatGPT reach the MCP door without a pasted key: PKCE `S256`, a Client ID Metadata
Document on Dona's allow-list, and the shop **owner** consents in the seller portal (*Sozlamalar ›
API › Ulangan ilovalar*, disconnect any time). **Reads only in v1** — every write tool answers an
OAuth token `403 insufficient_scope`; writes stay with agent keys.

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

### Publishing (repo public 2026-09-26; registry tokens still pending)

The repository is public. `.github/workflows/publish.yml` (manual `workflow_dispatch` or a `v*` tag)
has one job per registry — npm, PyPI, NuGet, and a Packagist mirror — and each is gated on that
registry's token secret existing on this repo; missing it, the job prints a clear skip notice instead
of failing. **No token exists yet for any of the four** (`gh secret list --repo ozbuz/dona-api` is
empty) — adding one is Bek's action, no code change needed after. Nothing here creates a registry
account.

| Registry | Secret it needs | What ships |
|---|---|---|
| npm | `NPM_TOKEN` (org `dona`, publish rights to `@dona/api`) | `sdks/typescript` — `private: true` already dropped |
| PyPI | `PYPI_TOKEN`, or Trusted Publishing configured on the `dona-api` project (no secret) | `sdks/python` |
| NuGet | `NUGET_API_KEY` | `sdks/csharp` (`Dona.Api`) |
| Packagist | `PACKAGIST_MIRROR_TOKEN` (a GitHub PAT with push to `ozbuz/dona-api-php`, which does not exist yet) | mirrors `sdks/php` into that split repo; submitting it to packagist.org is a separate, one-time, human step |

Go needs no registry or token — once the repo is public, tagging **is** publishing:

```bash
# the module lives in a subdirectory, so the tag carries its path; proxy.golang.org needs the repo public (done)
git tag sdks/go/v0.1.0 && git push origin sdks/go/v0.1.0
```

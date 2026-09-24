# Dona API examples

One folder per language. Each has the **same two programs**:

| Program | What it does |
|---|---|
| **quickstart** | `GET /me` → `GET /products?limit=5` → `POST /stock?dry_run=true` with an `Idempotency-Key`, re-sending the first product's **current** stock (a rehearsal: validated, guarded, rolled back — nothing is written). Prints the rate-limit headers, and the error envelope (`error` code) on failure. |
| **webhook verifier** | Standard Webhooks signature check (`webhook-id` · `webhook-timestamp` · `webhook-signature`, 300 s tolerance, rotation) + a self-test over the shared vectors in [`testdata/webhook-vectors.json`](testdata/webhook-vectors.json), which include the Standard Webhooks reference vector. |

Every quickstart reads `DONA_API_KEY` (required, `dona_sk_live_…`, minted by the shop owner in
*Sozlamalar › API*) and `DONA_API_BASE_URL` (optional; defaults to `https://api.dona.im/seller-api/v1`).
No key is ever written in code.

| Language | Quickstart | Webhook verifier + self-test |
|---|---|---|
| TypeScript (Node ≥ 24) | `cd typescript && npm install && DONA_API_KEY=… npm run quickstart` | `src/webhook.ts` · `npm run webhook-selftest` |
| Python (≥ 3.11) | `cd python && DONA_API_KEY=… uv run --with ../../sdks/python python quickstart.py` | `webhook.py` · `python webhook_selftest.py` |
| Go (≥ 1.27) | `cd go && DONA_API_KEY=… go run ./cmd/quickstart` | `webhook/` · `go test ./webhook` |
| PHP (≥ 8.1) | `cd php && composer install && DONA_API_KEY=… php quickstart.php` | `webhook.php` · `php webhook_selftest.php` |
| C# (.NET 10) | `cd csharp && DONA_API_KEY=… dotnet run -- quickstart` | `Webhook.cs` · `dotnet run -- webhook-selftest` |

(The TypeScript example needs the SDK built once: `cd ../sdks/typescript && npm install && npm run build`.
`make -C examples deps` does that and the PHP `composer install`.)

## How they are kept honest (CI)

- `make -C examples check` — `tsc` · `ruff` + `mypy --strict` · `gofmt` + `go vet` + `go test` · `php -l` ·
  `dotnet build` (warnings are errors), then every language's verifier runs the shared vectors.
- `make -C examples smoke` — every quickstart runs against [`tools/mockapi`](../tools/mockapi/main.go),
  which answers the contract's own 200 examples and refuses a missing key / missing `Idempotency-Key`
  the way the contract says. [`smoke_assert.py`](smoke_assert.py) then asserts what each language
  **sent**: the Bearer key, `limit=5`, a non-empty `Idempotency-Key`, `dry_run=true`; and that a
  malformed key stops the program with exit 1 on the `401` envelope.

⚠ Two traps the smoke test caught, worth knowing in your own code:
- **PHP**: the generated client's default serialises query booleans as `1`/`0`; this repository's
  generator flips it to `true`/`false` (`generators/php/generate.sh`) so `dry_run=true` is really sent.
  If you build your own `Configuration`, keep `setBooleanFormatForQueryString(Configuration::BOOLEAN_FORMAT_STRING)`.
- **PHP**: response header names arrive in the server's casing (`X-Ratelimit-Limit`); PHP array keys
  are case-sensitive, so normalise with `array_change_key_case()` before reading them.

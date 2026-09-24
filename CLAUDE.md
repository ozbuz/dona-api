# dona-api — working guide (AI + humans)

Generated **Dona API SDKs** (TypeScript · Python · Go · PHP · C#) and runnable examples. Private in
`ozbuz` until Bek makes it public; nothing is published to a registry yet (S6).
Design: `OZB/architecture/DB/seller-api/docs-portal.md` §5 (internal workspace).

## The one rule

**`sdks/` is generated. Never edit it by hand** — CI regenerates it and fails on any difference.
To change an SDK, change one of:
1. the **contract** — `OZB/architecture/DB/seller-api/contract/openapi.yaml` first, then ozb-backend's
   `scripts/openapi-sync.sh` (backend first), then here `scripts/sync-spec.sh`;
2. the **client view** — `tools/clientview` (what the generators read: open enums, presence rules);
3. a **generator** — `generators/<lang>/generate.sh`, `generators/versions.env`;
then `make generate` and commit `spec/` + `sdks/` + the change **together**.

## How to work here

- `make all` (spec-check → generate → check) then `make smoke`. Needs Go, Node ≥ 24, `uv`, Docker.
- `make verify-clean` after `make generate` must pass before a push — that is CI's gate.
- **Versions**: every generator/toolchain is pinned in `generators/versions.env` (rule 14: latest
  stable, verified before pinning). A bump is a PR that regenerates `sdks/` in the same commit.
- Output must be **deterministic** (C# `packageGuid` is pinned for this; Python is formatted by a pinned
  ruff). Prove it: generate twice, `git status` stays clean.
- Examples (`examples/`) are hand-written, take `DONA_API_KEY` from the env, never hold a key, and are
  compiled + smoke-tested in CI against `tools/mockapi`. A new example step needs a `smoke_assert.py` line.
- Containers run as the calling user (`--user $(id -u):$(id -g)`) — root-owned `bin/ obj/ vendor/`
  would break `git clean` on the persistent self-hosted runner.
- ⛔ Never publish from here or from CI (npm / PyPI / Packagist / NuGet / Go tags) — S6, Bek decides.
- ⛔ Never make the repo public — Bek's click.
- ⛔ Never put a real `dona_sk_live_…` key or `whsec_…` secret in a file, test or log.

## Git

`main` is protected: branch → PR → `generate` green → up to date → squash-merge. Stage explicit
paths (never `git add -A`); shared clones, concurrent sessions. History for this repo lives in OZB:
`project/ozb-mvp/dona-api/log/YYYY-MM-DD.md`.

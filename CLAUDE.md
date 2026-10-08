# dona-api — working guide (AI + humans)

> ⛔ **OZB WORKSPACE RULES APPLY HERE — read `/Users/bekyu/GitHub/OZB/CLAUDE.md` first, in full, and follow ONLY it**
> (partition · git · definition of done · 🧠 agents · tokens · coordination · IaC-only · credentials). This file is the repo's working
> guide, never a substitute. The committed `.claude/settings.json` + `.codex/hooks.json` load OZB's gates by absolute path, so a session
> opened here **or on a `.wt-*` worktree** is gated like one opened on OZB: claim before you edit (`ozbq claim`), `ci-green --gate` after
> the review gate and the coordinator merges, no `git push` while this branch's CI runs, no CI polling, `model` + `effort` on every agent,
> research once. Codex: `AGENTS.md` here points the same way. `[Bek 2026-10-08]`


Generated **Dona API SDKs** (TypeScript · Python · Go · PHP · C#) and runnable examples. **Public**
since 2026-09-26 (Bek's approval); `.github/workflows/publish.yml` exists but every registry job
skips until Bek adds that registry's token secret — nothing has been published to a registry yet.
Design: `OZB/architecture/DB/seller-api/docs-portal.md` §5.

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
- ⛔ `publish.yml` only runs a registry job once ITS token secret exists — adding a secret is Bek's
  action; don't hand-trigger a publish by working around the skip guard.
- ⛔ Never put a real `dona_sk_live_…` key or `whsec_…` secret in a file, test or log.
- The Go module directive (`sdks/go/go.mod`, and `tools/go.mod` / `examples/go/go.mod` which are not
  templated) tracks the toolchain minimum the code needs, not necessarily the newest release — a
  directive newer than what `actions/setup-go`/most installs have forces every `go get` (and this
  repo's own CI, which runs `GOTOOLCHAIN: local`) to fail instead of silently downloading. Bump it only
  with a reason, and keep `generators/versions.env`'s `GO_VERSION` in sync with both.

## Git

`main` is protected: branch → PR → `generate` green → up to date → squash-merge. Stage explicit
paths (never `git add -A`); shared clones, concurrent sessions. History for this repo lives in OZB:
`project/ozb-mvp/dona-api/log/YYYY-MM-DD.md`.

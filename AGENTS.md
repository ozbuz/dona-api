# dona-api — Codex pointer (OZB workspace)  `[Bek, 2026-10-08]`

⛔ This repository belongs to the **OZB workspace** (Dona · GitHub org `ozbuz`). Its rules do not live here.

1. **Read `/Users/bekyu/GitHub/OZB/AGENTS.md` first, in full.** It points at `/Users/bekyu/GitHub/OZB/CLAUDE.md` — the ONLY source of
   rules (partition · git · definition of done · 🧠 agents · tokens · coordination · IaC-only · credentials). Follow it and nothing else.
2. Then read this repo's `CLAUDE.md` — the working guide for the code.
3. **The gates are committed here** — `.codex/hooks.json` (Codex) and `.claude/settings.json` (Claude Code) load OZB's hook scripts by
   absolute path, so a session opened on this repo **or on any `.wt-*` worktree of it** is gated exactly like one opened on OZB:
   - claim before you edit: `python3 /Users/bekyu/GitHub/OZB/orchestration/bin/ozbq claim --repo dona-api --paths '<globs>' --intent '…' --session-id <the id the SessionStart hook printed>`
   - after the review gate: `ozbq status <claim> ci-green --pr N --gate <findings file|C>` — the coordinator merges (`gh pr merge` is gated)
   - no `git push` while this branch's CI is running · no CI polling (`gh run watch`, sleep loops) · model + reasoning effort on every subagent
   - research once (`/Users/bekyu/GitHub/OZB/orchestration/research/ledger.md`) · log + `## Lessons` in OZB's `project/` before you report
4. Codex spends the **ChatGPT pool** — read `/status`; the Claude fleet ledger is separate. Priority words (P0/P1) are Bek's alone.

When Codex asks to trust this project's hooks, say yes — they are OZB's own scripts under `/Users/bekyu/GitHub/OZB/orchestration/hooks/`.

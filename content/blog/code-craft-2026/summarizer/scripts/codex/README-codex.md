# Codex CLI — join a talks-outline batch (same commands as Claude)

Codex runs on your machine, so it can fetch YouTube captions and work the same shared queue
as your Claude Code workers. The command name and arguments are **identical** on both tools.

## Same usage across Claude and Codex
| What you want | Claude Code | Codex CLI |
|---|---|---|
| Outline some links | `/talks-outline <link> <link>` | `codex "/talks-outline <link> <link>"` |
| Seed from a urls.txt | `/talks-outline seed ~/Downloads/talks-outlines/urls.txt` | `codex "/talks-outline seed ~/Downloads/talks-outlines/urls.txt"` |
| Work an already-seeded queue | `/talks-outline work-queue` | `codex "/talks-outline work-queue codex-1"` |
| Re-enrich thin outlines (Mode B) | `/talks-outline reenrich ~/Downloads/talks-outlines/summaries` | `codex "/talks-outline reenrich ~/Downloads/talks-outlines/summaries"` |
Both write to `~/Downloads/talks-outlines/summaries/` and share `/tmp/talks-queue.tsv`, so a Claude
worker and a Codex worker can run the same batch at once.

## Prerequisite: run the installer (sets up both Claude + Codex)
```bash
bash ~/.claude/skills/talks-outline/install.sh
```
This installs the skill, venv, Claude agent def, Codex custom prompt
(`~/.codex/prompts/talks-outline.md`), AGENTS.md in the output dir, permissions, and
output directories — all in one step. Safe to re-run.

## Run
```bash
export QUEUE_TSV=/tmp/talks-queue.tsv
codex "/talks-outline seed ~/talks/urls.txt"          # seeds, then works the queue
# more workers on the same queue, unique tag each:
codex "/talks-outline work-queue codex-2"
```
Add `--full-auto` (or approve the fetch/write commands once) so it runs unattended. 4–6 total
workers across Claude+Codex is the sweet spot; more hits YouTube rate limits.

## Alternative: AGENTS.md (scoped by folder only)
If you prefer AGENTS.md, put it ONLY in a folder used for nothing else — never at
`~/.codex/AGENTS.md` (that's global and affects every session):
```bash
mkdir -p ~/talks-batch && cp AGENTS.md ~/talks-batch/AGENTS.md && cd ~/talks-batch
codex exec --full-auto "/talks-outline seed ~/talks/urls.txt"
```

## Notes
- Flag names vary by Codex version — if `codex "/talks-outline …"` or `--full-auto` errors,
  check `codex --help` for the prompt/flag syntax on your build.
- Watch progress: `~/.claude/skills/talks-outline/scripts/talks-queue.sh stats`.

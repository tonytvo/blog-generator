# Usage — running a batch across multiple AI agents

Goal: hand a list of YouTube talks to several agents at once (Claude Code, Codex CLI,
Gemini CLI, a second machine…) and have them chew through it without stepping on each
other or outlining the same talk twice.

Three pieces make that work:

| Piece | What it is |
|---|---|
| `/tmp/talks-queue.tsv` | the shared work list — the single source of truth |
| `scripts/talks-queue.sh` | the only thing allowed to mutate it, serialized with `flock` |
| `talks-outline-index.md` | the human-readable roll-up, appended under its own lock |

---

## Step 1 — one-time setup (per machine)

```bash
bash ~/.claude/skills/talks-outline/install.sh
```
Sets up Claude Code + Codex CLI in one step (agent def, venv, prompts, permissions,
output dirs). Safe to re-run. See `README.md` for details or manual steps.

## Step 2 — write your URL list

Any text file, one URL per line. `#` comments and blank lines are ignored. Optional
second column = domain hint (`software` / `investing` / `self-help` / `auto`), optional
third = exact filename if you want to control it:

```
# ~/Downloads/talks-outlines/urls.txt
https://www.youtube.com/watch?v=u45c_nVV0Sk&t=142s          software
https://youtu.be/7JwAGvoSwgg                                investing
https://www.youtube.com/watch?v=6AgndHSkHFI                 self-help   toan-canh-bds-tap2-2026-09-12.md
https://www.youtube.com/playlist?list=PLxxxxxxxx            software
```

Playlist URLs, `&list=` params, `&t=` timestamps, `youtu.be`, and `/shorts/` all work —
seeding strips each to the bare 11-character video id, so `yt-dlp` never crawls a playlist
by accident.

## Step 3 — seed the queue (once, from any machine)

```bash
export QUEUE_TSV=/tmp/talks-queue.tsv
~/.claude/skills/talks-outline/scripts/talks-queue.sh seed-urls ~/talks/urls.txt
~/.claude/skills/talks-outline/scripts/talks-queue.sh status
```

Each line becomes `id⇥filename⇥domain⇥Pending`. Re-seeding the same file is safe —
already-queued ids are skipped, so you can keep appending new links to `urls.txt` between
runs.

**Re-enrich mode** (thin outlines you already have, keep their filenames):
```bash
talks-queue.sh seed-dir ~/Downloads/talks-outlines/summaries
```

## Step 4 — launch the agents

Every agent needs three things: a **unique tag**, the `QUEUE_TSV` path, and `AGENT-BRIEF.md`.
Aim for 4–6 workers; beyond that YouTube rate-limits the transcript fetches.

**Claude Code** (has the skill — it reads the brief itself):
```bash
cd ~/talks
claude -p "/talks-outline work-queue --tag claude-1" --permission-mode acceptEdits
claude -p "/talks-outline work-queue --tag claude-2" --permission-mode acceptEdits
```
Or from one interactive session: `/talks-outline work-queue` — it spawns N tagged
subagents against the same queue.

**Codex CLI / Gemini CLI / Cursor / Aider** (no skill — paste the brief):
```bash
codex exec "$(cat ~/.claude/skills/talks-outline/AGENT-BRIEF.md)

Your TAG is codex-1. QUEUE_TSV=/tmp/talks-queue.tsv. Start the loop now."
```
```bash
gemini -p "$(cat ~/.claude/skills/talks-outline/AGENT-BRIEF.md)

Your TAG is gemini-1. QUEUE_TSV=/tmp/talks-queue.tsv. Start the loop now."
```
The brief is self-contained — it carries the full depth bar, the language rule, the file
format, and the locking protocol, so a non-Claude agent produces the same output shape.

**Background them all, then wait:**
```bash
for t in claude-1 claude-2 codex-1 gemini-1; do
  (launch command for $t) > /tmp/log-$t.txt 2>&1 &
done
wait
```

## Step 5 — watch it

```bash
talks-queue.sh stats      # Pending / In Progress (tag) / Complete counts
talks-queue.sh status     # full queue
ls ~/Downloads/talks-outlines/summaries/
```
Done when `stats` shows only `Complete`, or every worker prints `QUEUE_EMPTY`.

---

## Why it's safe

| Risk | Protection |
|---|---|
| Two agents outline the same talk | `claim` marks the row `In Progress (tag)` inside an exclusive `flock`; only one caller can win |
| Two agents append to the index at once | Each append takes `/tmp/talks-index.lock`, held only for the append |
| A reader sees half a file | Each outline is written in **one** write |
| Two agents write different outlines simultaneously | Different files — no lock needed, genuinely parallel |
| A worker crashes mid-talk | Row stays `In Progress`; `talks-queue.sh reset <id>` returns it to `Pending` |
| A talk has no captions | Retried once, then marked `Complete` with a Skipped row — nobody retries it forever |

## Limits worth knowing

- `flock` is reliable on a **local** filesystem. A queue on Dropbox/Drive/NFS is
  best-effort — for genuine multi-machine runs, put `QUEUE_TSV` on one machine and have
  the others reach it over SSH, or give each machine its own disjoint URL list.
- `/tmp` is wiped on reboot. Rebuild with `seed-dir` (already-done talks are detected from
  their provenance footers) or keep the TSV somewhere persistent.
- YouTube rate-limits transcript fetches from one IP; 4–6 concurrent workers is the sweet
  spot, and the fetcher backs off on 429/403.

## Cross-checking after a batch

Each outline tags claims `[V]/[D]/[P]/[E]` and carries a Critical observations section, so
after the run you can grep for disagreements across agents:
```bash
grep -l '\[E\]' ~/Downloads/talks-outlines/summaries/*.md
grep -h '^| .*\[P\]' ~/Downloads/talks-outlines/summaries/*.md | head -40
```

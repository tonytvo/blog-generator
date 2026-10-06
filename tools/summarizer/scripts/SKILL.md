---
name: talks-outline
description: Turn talks — YouTube links, a URL-list file, pasted transcripts, or uploaded transcript files (software engineering, value investing / finance / real estate, self-help) — into exhaustive, deeply-nested markdown outlines exported as .md files the user can read and share. Outlines many talks in parallel through a shared work queue that other AI agents (Codex CLI, Gemini CLI, a second machine) can join. Use this whenever the user pastes YouTube URLs (youtube.com, youtu.be), a playlist, a urls.txt, or a transcript and asks for a summary, outline, notes, key takeaways, "detail summary", "detail outline", or "tóm tắt" — even with no instructions. Also use to re-enrich existing outlines, or to work/continue a batch queue.
---

# talks-outline — exhaustive outlines of talks, in parallel, exported as markdown

Every run ends with one `.md` file per talk in `~/Downloads/talks-outlines/summaries/` plus a
row in `talks-outline-index.md`. The outline is the deliverable; the chat reply is just the
index.
**Depth is the whole point** — a thin, table-heavy summary is a failure (see Depth bar).

## Inputs
| Input | How handled |
|---|---|
| YouTube link(s) / playlist | fetched via `scripts/fetch_transcript.py` (Claude Code, or any env with network to YouTube) |
| A `urls.txt` file (one URL/line, optional `domain` and `filename` columns) | seeded into the queue with `scripts/talks-queue.sh seed-urls` |
| `work-queue` (continue an already-seeded queue) | claim-loop only; no new seeding |
| Transcript pasted in the message | save to `./talks-work/<slug>/transcript.txt`, then outline |
| Uploaded `.txt/.md/.pdf/.docx` transcript | read it (file-reading skill if needed), save as above |
| An existing outline folder to re-enrich (**Mode B**) | seeded with `seed-dir`; filenames and index left untouched |

If a link can't be fetched (no network, no captions), skip it, record it under **Skipped**
in the index, mark it done in the queue, and continue. Never outline from a title alone.

## Two modes
- **Mode A — new work.** URLs/transcripts with no existing outline -> *create* one `.md` per
  talk and *append* a row to `talks-outline-index.md`.
- **Mode B — re-enrich.** The user points at existing outline files that are thin -> rewrite
  each body in place to meet the depth bar, **keep the existing filename**, and **do not add
  index rows** (update the row's Summarized date only if asked).
Both run the same pipeline and depth bar; they differ only in seeding and whether new index
rows are added. Auto-detect: bare links -> A; "re-enrich/improve these" or a folder of
existing outlines -> B.

## Unattended mode — never ask, always decide
Often run while the user is away. Do not use AskUserQuestion, do not end a turn with a
question, do not wait for confirmation. Resolve every ambiguity with these defaults and note
the choice in the index:
| Situation | Default |
|---|---|
| Domain unclear | `auto`; the worker decides from the transcript |
| Language | the transcript's spoken language (see Language rule) — never from title/channel |
| Playlist > 30 videos | queue the first 30 in order; list the rest under **Not processed** |
| Fetch fails / no captions | retry once, then skip + log + mark done |
| Worker fails or returns partial | reset the row once; if it fails again, log under **Failed** |
| Outline file already exists (same day) | overwrite; a later day makes a new dated file |
| Zero links or transcripts found | write nothing; reply one line saying no input was found |
| Missing Python deps | print the one-time setup from README.md and stop; never auto-install |
Only an unsafe/impossible request ends the run early — and even then finish the other talks.

## Workflow

### 1. Collect & seed the queue
Extract every YouTube URL (`watch?v=`, `youtu.be/`, `shorts/`, `live/`, `embed/`,
`playlist?list=`) and every pasted/attached transcript. Expand a playlist first:
`<skill-dir>/.venv/bin/python <skill-dir>/scripts/fetch_transcript.py --expand <url>`.

Seed the shared queue (one source of truth, safe for many agents):
```bash
export QUEUE_TSV=/tmp/talks-queue.tsv
<skill-dir>/scripts/talks-queue.sh seed-urls <urls.txt>     # from a file
# or, for a handful of links, write them to a temp file and seed that
<skill-dir>/scripts/talks-queue.sh seed-dir  ~/Downloads/talks-outlines/summaries   # Mode B
```
Each row is `id<TAB>filename<TAB>domain<TAB>Pending`; `filename=PENDING_TITLE` means the
worker derives it. Seeding is idempotent — already-queued ids are skipped, so re-seeding a
growing `urls.txt` is safe. For pasted/uploaded transcripts there is no id to fetch: write
the transcript + a `meta.json` yourself and outline directly (no queue needed for a single
paste).

### 2. Outline — parallel workers claiming the queue
**Subagents available (Claude Code, Cowork):** spawn `talks-outliner` **once per worker slot,
all in one turn** (4–6 slots — YouTube rate-limits beyond that), each with a unique tag. Each
worker loops: `claim -> fetch -> exhaustive outline -> enrich pass -> single-write ->
index row -> done`, until `QUEUE_EMPTY`. Do not fetch or outline in the main session.
Delegation prompt per worker:
```
Work the talks queue until empty. Your tag: <worker-N>.
- Queue helper: <skill-dir>/scripts/talks-queue.sh   (export QUEUE_TSV=/tmp/talks-queue.tsv)
- Fetcher:      <skill-dir>/.venv/bin/python <skill-dir>/scripts/fetch_transcript.py
- Out dir:      ~/Downloads/talks-outlines/summaries
- Mode:         <A create+index | B re-enrich, keep filename, no new index row>
- Follow references/outline-format.md exactly (depth bar). Language = spoken language.
- Return only: talks completed, files written, total [E] flags, or FAILED <reason>.
<any extra user instructions, verbatim>
```
**No subagents (Claude.ai web / mobile):** fetch in parallel, then outline each talk yourself
sequentially at full depth:
```bash
<skill-dir>/.venv/bin/python <skill-dir>/scripts/fetch_transcript.py --out ./talks-work --jobs 4 <url> ...
```

### 3. Export — mandatory
- One `.md` per talk in `~/Downloads/talks-outlines/summaries/` (expand `~`, create if
  missing). This is the single collection point across all projects — never write into the
  current repo.
- **Mode A filename:** `<slug>-<YYYY-MM-DD>.md` (slug = 4–6 title words, kebab, ASCII; date =
  day produced). **Mode B:** keep the existing filename exactly.
- **Index:** append/update `~/Downloads/talks-outlines/summaries/talks-outline-index.md` under
  `flock /tmp/talks-index.lock` (the only shared-write file). Columns: Summarized date, Talk
  title, Speaker/channel, Domain, Lang, Outline link, Video link. Skipped / Failed /
  Not-processed go in a second table with reasons. Newest rows at the top of the body.
- **Claude.ai:** write to `/mnt/user-data/outputs/` and call `present_files` on every outline
  and the index so the user gets download cards.

### 4. Reply
Short: the index table (or one line for a single talk), the file names, and one sentence on
the most important `[E]` or critical observation. Don't paste outline bodies into chat.

## Depth bar (the point of the whole exercise)
Depth comes from **granularity**, not word count. Enforced in `references/outline-format.md`;
as orchestrator, before accepting a worker's file confirm it has:
- A **framing blockquote** (speaker, venue, format, the talk's own structure).
- A **deep decimal hierarchy** — one `###` per distinct sub-topic/example/step; a long talk
  has **25+** `###`, not 3. Enumerations (patterns, steps, rules, companies) each get their
  own numbered `###`; a summary table may *add* to but never *replace* the per-item sections.
- **One idea per bullet.** Worked examples decomposed step by step. **Q&A one `###` per
  question** (Q5/Q5a), asker named. Quotes attributed, each under 15 words.
- A **"People & References Cited"** index at the end; exact provenance footer.
- **Shape matches the talk:** a 90-min workshop -> very long; a narrative keynote is shorter
  at the same fidelity — expected, not a defect. Panels/podcasts -> topic-threaded; if a
  guest was absent, say so, never fabricate.
Plus the analytical layer this skill adds on top of the playbook: claim tags `[V]` verifiable
· `[D]` speaker estimate · `[P]` pending · `[E]` error/contradiction; a **Critical
observations** section (analysis not in the talk); a **Pending verification** table. If a
worker's file misses any of this, reset its row or message it to fix the file.

## Language rule
Transcript **and** outline are in the language spoken in the talk. The fetcher only ever
saves original-language captions (manual first, else auto), so `meta.json` `language` is the
spoken language; the worker verifies against the body and trusts the body on conflict. Write
the *entire* file in that language — headers, tables, tags, observations. Vietnamese talk ->
Vietnamese transcript and file; Japanese -> Japanese. Only an explicit user override changes
it, and then the header records "translated from <language>".

## Parallel-safety rules
- The queue TSV is mutated **only** through `talks-queue.sh` (flock-serialized) — never hand-
  edit it while workers run.
- The index is the one shared-write file — always `flock /tmp/talks-index.lock`, briefly.
- Writing **different** outline files concurrently needs no lock.
- Each outline is written in **one** write, never incrementally.
- Locks (queue, index) are separate and never nested; held only for their tiny section.
- A crashed worker leaves a row `In Progress`; `talks-queue.sh reset <id>` requeues it.
- Transcripts are scratch in `/tmp` (or `./talks-work/`) — never committed anywhere.

## Cross-AI batches
Any agent (Codex CLI, Gemini CLI, Cursor, a second machine) can join the same queue: give it
a unique tag and `AGENT-BRIEF.md` (self-contained — full depth bar, language rule, file
format, locking). See `USAGE.md` for launch commands and `AGENT-BRIEF.md` for the worker
contract.

## Files in this skill
- `scripts/fetch_transcript.py` — original-language transcript + metadata fetcher, playlist expander, parallel `--jobs`
- `scripts/talks-queue.sh` — flock-serialized work queue (seed-urls / seed-dir / claim / done / reset / status / stats)
- `references/outline-format.md` — the depth bar and per-domain section blocks (worker preloads this)
- `agents/talks-outliner.md` — subagent worker definition; copy to `~/.claude/agents/`
- `AGENT-BRIEF.md` — paste into non-Claude agents so they can work the queue
- `USAGE.md` — end-to-end multi-agent run guide

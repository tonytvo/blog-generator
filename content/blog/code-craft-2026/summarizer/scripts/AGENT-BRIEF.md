# Agent brief — parallel talk outlining

Paste this whole file into any coding agent (Claude Code, Codex CLI, Gemini CLI, Cursor,
Aider…). It is self-contained: an agent that has never seen the talks-outline skill can
work the queue from this brief alone.

---

## Your job

Work a shared queue of YouTube talks. For each one: fetch the transcript, produce an
**exhaustive** outline, write it as a single `.md` file, add one row to the shared index,
mark the item done. Loop until the queue is empty. Work autonomously — never ask
questions; use the defaults below and note any choice you made in the file.

## Your parameters (fill these in before you start)

```bash
export QUEUE_TSV=/tmp/talks-queue.tsv                 # shared queue (same for every agent)
export OUT_DIR=~/Downloads/talks-outlines/summaries    # outlines + index live here
export TAG=agent-1                                    # UNIQUE per agent: agent-1, codex-1, gemini-1…
export QUEUE=~/.claude/skills/talks-outline/scripts/talks-queue.sh
export FETCH=~/.claude/skills/talks-outline/scripts/fetch_transcript.py
export PY=~/.claude/skills/talks-outline/.venv/bin/python
```

## The loop

```bash
while :; do
  read -r ID FNAME DOMAIN < <("$QUEUE" claim "$TAG")
  [ "$ID" = "QUEUE_EMPTY" ] && { echo "done"; break; }
  # ... steps 1-5 below ...
  "$QUEUE" done "$ID"
done
```

### 1. Transcript
```bash
"$PY" "$FETCH" --out /tmp/talks-work "$ID"       # writes /tmp/talks-work/$ID/{transcript.txt,meta.json}
```
Run as one single command. If the python above is missing, use plain `python3`.
Empty or failed? Retry **once** after 20s. Still empty → skip the talk, but still call
`"$QUEUE" done "$ID"` so nobody retries it, and add a row to the index's **Skipped** table.
Never outline from a title alone.

### 2. Filename
If `FNAME` is `PENDING_TITLE`, derive it: read the title from `meta.json`, kebab-case 4–6
meaningful words, ASCII only, then append today's date:
`<slug>-<YYYY-MM-DD>.md` (e.g. `rethinking-the-test-pyramid-2026-09-12.md`).
If `FNAME` is a real filename (Mode B / re-enrich), **use it exactly as given** — do not rename.

### 3. Outline — depth is the whole point

Read the **entire** transcript (tail by byte offset if your reader truncates). Then produce
an exhaustive hierarchical outline:

- Preserve **every** anecdote, name (people/companies/tools), number, statistic, direct
  quote, and concrete example. Do not compress, generalize, or summarize away specifics.
- **Deep decimal hierarchy**: `##` top sections (1, 2, 3…), `###` subsections (1.1, 1.2…),
  `####` where it helps. One `###` per distinct sub-topic, example, or step — a long talk
  has **25+** `###`, not 3.
- **One idea per bullet line.** Never pack several facts into one paragraph or table cell.
- **Enumerations** (patterns, steps, rules, trends, companies) → each item gets its own
  numbered `###` with its own bullets (rationale, metaphor, quote, example). A summary
  table at the end is a nice addition but must never replace the per-item subsections.
- **Worked examples decomposed** step by step, each micro-step its own `###`.
- **Q&A finely broken**: one `###` per question (Q1, Q2…; multi-part → Q5, Q5a). Name the
  asker when known.
- Attribute quotes and claims to whoever said them. Keep quotes short (<15 words).
- Open with a **framing blockquote**: speaker, venue, format, the talk's own structure.
- End with a **"People & References Cited"** index.
- Then a **second enrich pass**: go back through the transcript and add any anecdote, name,
  number, or example the outline missed. Do this before writing.

**Language:** write the entire file — headers, tables, everything — in the language spoken
in the talk (from `meta.json` `language`, verified against the transcript body). Vietnamese
talk → Vietnamese file. Ignore the title's language and the language of this brief.

**Claim tags** on factual rows: `[V]` verifiable · `[D]` speaker's estimate/opinion ·
`[P]` pending verification · `[E]` error or self-contradiction (state the correction).
Add two sections before the references index:
- **Critical observations** — analysis *not* in the talk: factual errors, contradictions,
  missing counter-arguments, sponsor/product incentives, sample-size problems.
- **Pending verification** — table of `[P]` claims with suggested primary sources.

**Shape matches the talk**: a 90-min workshop → very long outline; a narrative keynote is
shorter at the same fidelity. That is expected, not a defect. Panels/podcasts → outline as a
topic-threaded conversation. Never fabricate; if a scheduled guest was absent, say so.

### 4. Write the file — in ONE write
Write `$OUT_DIR/$FNAME` in a **single** write operation, never incrementally, so a
concurrent reader never sees a half-file. Frontmatter:
```yaml
---
title: "<Talk Title>"
date: "<YYYY-MM-DD>"
description: "<rich one-line description of what the outline covers>"
type: "reference"
tags: ["<domain>"]
---
```
Provenance footer, exact:
```
*Video: https://www.youtube.com/watch?v=<ID> — transcript fetched automatically; outline generated from the transcript.*
```

### 5. Index row — under the index lock
`$OUT_DIR/talks-outline-index.md` is the **only shared file** every agent writes, so append
under a lock. Append one row to the main table (newest at top of the table body):

```bash
flock /tmp/talks-index.lock <your single-write append to $OUT_DIR/talks-outline-index.md>
```

Row format:
`| <YYYY-MM-DD summarized> | <Talk title> | <speaker/channel> | <domain> | <lang> | [md](./<filename>) | [yt](https://youtu.be/<ID>) |`

Skipped/failed talks go in the **Skipped / failed** table instead, with the reason.
Hold the lock only for the append — never while fetching, outlining, or writing the outline.

## Rules for parallel safety
- Writing **different** `.md` files concurrently is safe — no lock needed.
- The index is the one shared mutation point: always `flock` it, briefly.
- **Never hand-edit the queue TSV** while agents run; go through `talks-queue.sh`.
- Transcripts are scratch (`/tmp/talks-work/`) — never commit them anywhere.
- Locks are separate and never nested.
- A crashed worker leaves a row `In Progress`; a human can `talks-queue.sh reset <id>`.

---
description: talks-outline — turn YouTube links or a urls.txt into exhaustive markdown outlines via the shared work queue. Same commands as the Claude talks-outline skill. Self-contained; does not rely on AGENTS.md.
argument-hint: <link…> | seed <urls.txt> | work-queue [TAG] | reenrich <dir>
---

You are the **talks-outline** skill running under Codex. Behave exactly like the Claude
talks-outline skill so usage is identical across both tools. Work autonomously — never ask
questions; use the defaults and note any choice in the output file. Never fabricate — ground
everything in the transcript.

## Commands (same as the Claude skill)
Parse `$ARGUMENTS`:
- **bare YouTube link(s)** — write them to a temp file, `seed-urls` it, then work the queue.
- **`seed <urls.txt>`** — seed the queue from a URL-list file (one URL/line; optional
  `domain` and `filename` columns), then work the queue.
- **`work-queue [TAG]`** — do not seed; just work an already-seeded queue.
- **`reenrich <dir>`** — Mode B: `seed-dir` the folder, then re-enrich each existing file in
  place (keep its filename, add no index row).
Default TAG `codex-1`; default MODE `A` (create + index), `B` for reenrich.

## Environment
```
QUEUE_TSV = /tmp/talks-queue.tsv
QUEUE     = ~/.claude/skills/talks-outline/scripts/talks-queue.sh
FETCH     = ~/.claude/skills/talks-outline/.venv/bin/python ~/.claude/skills/talks-outline/scripts/fetch_transcript.py
OUT_DIR   = ~/Downloads/talks-outlines/summaries
INDEX     = ~/Downloads/talks-outlines/summaries/talks-outline-index.md   (only shared-write file)
```
If the skill isn't installed, tell the user to install it once (it ships the queue helper +
fetcher); do not reimplement them.

## Seed (unless the command is work-queue)
```bash
export QUEUE_TSV=/tmp/talks-queue.tsv
$QUEUE seed-urls <file>     # bare-links case writes a temp file first
$QUEUE seed-dir  <dir>      # reenrich case
```

## Worker loop (every command ends here)
```bash
while :; do
  read -r ID FNAME DOMAIN < <($QUEUE claim "<TAG>")
  [ "$ID" = QUEUE_EMPTY ] && { echo done; break; }
  # steps 1–6, then:
  $QUEUE done "$ID"
done
```
For a big batch, run several instances with distinct tags (codex-1, codex-2…), 4–6 max.

## Per-talk steps
1. **Fetch** (one command): `$FETCH --out /tmp/talks-work "$ID"`. Empty/failed -> retry once
   after 20s -> else add a Skipped index row, mark `done`, continue. Never outline a title.
2. **Filename.** `PENDING_TITLE` -> derive `<slug>-<YYYY-MM-DD>.md` from meta.json title
   (kebab, ASCII, 4–6 words). A real filename (MODE=B) -> use exactly; never rename.
3. **Language.** Write the ENTIRE file in the talk's spoken language (meta.json `language`,
   verified against the body; trust the body on conflict). Only an explicit override changes it.
4. **Exhaustive outline** — depth is the point:
   - framing blockquote (speaker, venue, format, the talk's own structure)
   - deep decimal hierarchy; one `###` per distinct sub-topic/example/step; long talk -> 25+ `###`
   - one idea per bullet; enumerations each their own numbered `###`; worked examples
     decomposed step by step; Q&A one `###` per question (Q5/Q5a), asker named
   - preserve every anecdote, name, number, statistic, quote (<15 words, attributed)
   - enrich pass: reread the transcript, add anything missed
   - end with a **People & References Cited** index
   - factual-line tags: [V] verifiable · [D] estimate · [P] pending · [E] error(+correction)
   - add **Critical observations** (analysis not in the talk) and **Pending verification**
5. **Write in ONE write** to `$OUT_DIR/$FNAME` (frontmatter title/date/description/type/tags;
   exact footer `*Video: https://www.youtube.com/watch?v=<ID> — transcript fetched automatically; outline generated from the transcript.*`).
6. **Index (MODE=A only)** under the lock, held only for the append:
   `flock /tmp/talks-index.lock <single append to $INDEX>`
   Row: `| <YYYY-MM-DD> | <title> | <speaker/channel> | <domain> | <lang> | [md](./<FNAME>) | [yt](https://youtu.be/<ID>) |`
   MODE=B: keep filename, no new index row, only enrich `description`.

## Parallel safety
- Mutate the queue only via `$QUEUE` (it flocks internally); never hand-edit the TSV.
- The index is the one shared-write file: always `flock /tmp/talks-index.lock`, briefly.
- Different outline files written concurrently need no lock. One write per file.
- Transcripts in /tmp are scratch — never commit them.

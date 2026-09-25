# AGENTS.md — talks-outline worker (Codex CLI)

This directory participates in the **talks-outline** shared batch. The full worker contract
also ships as the `/talks-outline` custom prompt (`~/.codex/prompts/talks-outline.md`) — this
file duplicates it so the folder works without that prompt installed. When asked to run
`/talks-outline`, "work the talks queue", "outline these talks", or "enrich these outlines",
act as a queue worker exactly as described here. Work autonomously — never ask questions; use the
defaults and note any choice in the output file.

## Environment (assume these unless told otherwise)
```
QUEUE_TSV = /tmp/talks-queue.tsv
QUEUE     = ~/.claude/skills/talks-outline/scripts/talks-queue.sh
FETCH     = ~/.claude/skills/talks-outline/.venv/bin/python ~/.claude/skills/talks-outline/scripts/fetch_transcript.py
OUT_DIR   = ~/Downloads/talks-outlines/summaries
TAG       = codex-1        # unique per running agent
MODE      = A              # A = create + index ; B = re-enrich in place
```
If the skill isn't installed on this machine, ask the user to install it once (it ships the
queue helper + fetcher); do not reimplement them.

## The loop
```bash
export QUEUE_TSV=/tmp/talks-queue.tsv
while :; do
  read -r ID FNAME DOMAIN < <("$QUEUE" claim "$TAG")
  [ "$ID" = QUEUE_EMPTY ] && { echo done; break; }
  # steps 1–6 below, then:
  "$QUEUE" done "$ID"
done
```

## Per-talk steps
1. **Fetch** (one command): `$FETCH --out /tmp/talks-work "$ID"`. Empty/failed -> retry once
   after 20s -> else add a Skipped index row, `done "$ID"`, continue. Never outline a title.
2. **Filename.** `PENDING_TITLE` -> derive `<slug>-<YYYY-MM-DD>.md` from meta.json title
   (kebab, ASCII, 4–6 words). A real filename (MODE=B) -> use exactly, never rename.
3. **Language.** Write the whole file in the talk's spoken language (meta.json `language`,
   verified against the body; trust the body on conflict).
4. **Exhaustive outline** — depth is the point:
   - framing blockquote (speaker, venue, format, the talk's own structure)
   - deep decimal hierarchy; one `###` per distinct sub-topic/example/step; long talk -> 25+ `###`
   - one idea per bullet; enumerations each get their own numbered `###`; worked examples
     decomposed step by step; Q&A one `###` per question (Q5/Q5a), asker named
   - preserve every anecdote, name, number, statistic, quote (<15 words, attributed)
   - then an **enrich pass**: reread the transcript, add anything missed
   - end with a **People & References Cited** index
   - tags on factual rows: [V] verifiable · [D] estimate · [P] pending · [E] error(+fix)
   - add **Critical observations** (analysis not in the talk) and **Pending verification**
5. **Write in ONE write** to `$OUT_DIR/$FNAME` (frontmatter: title/date/description/type/tags;
   exact footer `*Video: https://www.youtube.com/watch?v=<ID> — transcript fetched automatically; outline generated from the transcript.*`).
   Never write incrementally.
6. **Index (MODE=A only)** under the lock, held only for the append:
   `flock /tmp/talks-index.lock <single append to $OUT_DIR/talks-outline-index.md>`
   Row: `| <YYYY-MM-DD> | <title> | <speaker/channel> | <domain> | <lang> | [md](./<FNAME>) | [yt](https://youtu.be/<ID>) |`
   MODE=B: keep the existing filename, do NOT add index rows, only enrich `description`.

## Parallel safety
- Mutate the queue only via `$QUEUE` (it flocks internally). Never hand-edit the TSV.
- The index is the one shared-write file: always `flock /tmp/talks-index.lock`, briefly.
- Different outline files written concurrently need no lock. One write per file.
- A crash leaves a row `In Progress`; a human runs `$QUEUE reset <id>`.
- Transcripts in /tmp are scratch — never commit them.

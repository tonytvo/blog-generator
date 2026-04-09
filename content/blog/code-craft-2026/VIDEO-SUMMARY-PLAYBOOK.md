---
title: "Video Summary Playbook"
date: "2026-06-04T00:00:00.000Z"
description: "video summary playbook"
type: "reference"
tags: ["softwaredevelopment", "ai"]
---

# Video → In-Depth Summary Playbook (reusable, single- or multi-agent)

A repeatable process for turning **conference-talk / YouTube videos** into deep, per-talk
summary `.md` pages linked from an index. It merges two things:

1. **The per-video pipeline** — video URL → transcript → *exhaustive* AI outline → summary `.md`
   → index entry → deploy. (Depth is the whole point; see the outline prompt + depth bar below.)
2. **An optional parallel work-queue** — a `/tmp` shared queue + `flock`-serialized deploys so **any
   number of agents** (Claude CLI, Codex CLI, …) can chew through a big batch at once, safely.

Use it for any batch. Everything is parameterized by a **job slug** (e.g. `craft2026`, `qcon2027`)
so multiple jobs never collide on queue/lock/counter files.

---

## 0. Two input modes (pick one)

- **Mode A — a list of video URLs.** You have new videos and no pages yet. The job *creates* a
  summary `.md` per video **and** appends an entry to the index.
- **Mode B — an existing index that already lists the videos + summaries.** The pages exist but the
  summaries are thin; you only need to **re-enrich the existing summary `.md` files in place**.
  In this mode you **do NOT edit `index.md`** and you do NOT add entries — you regenerate the bodies
  of the summary files the index already points at.

Both modes run the *same* per-video pipeline (§2) and the *same* depth bar (§3). They differ only in
**how the work list is seeded** (§5.2) and **whether the index is touched** (Mode A: yes; Mode B: no).

---

## 1. Setup — parameters for this job

Set these once at the top of a run (shell vars make the later commands copy-paste-able):

```bash
JOB=craft2026                                             # short slug; namespaces all /tmp state
CONTENT_DIR=/home/tvo/dev/blog-generator/content/blog/code-craft-2026
INDEX="$CONTENT_DIR/index.md"                             # the index file (Mode A appends to it)
REPO=/home/tvo/dev/blog-generator                         # deploy runs from here
GH_PAGE_REPO=/home/tvo/dev/tonytvo.github.io
POST_DATE="2026-06-04T00:00:00.000Z"                      # frontmatter date for new files
DAYS_AGO_START=81                                         # first backdated-commit offset (see §6)
```

**Tools** (already in the repo / `~/bin`):
- `yt-transcript.sh` (in `~/bin` or next to the index) — downloads a clean plain-text transcript via `yt-dlp`.
- `yt-dlp` — also used to read a video title.
- `deploy.py` (repo root) — `git add . && commit && push` + `gatsby build` + copy to the gh-pages repo + push.

---

## 2. The per-video pipeline (identical in both modes)

Do this **one talk at a time** — each talk deserves a full-attention pass.

### 2.1 (Mode A only) Get the title → used for the heading and filename
```bash
yt-dlp --get-title --skip-download --force-ipv4 "<VIDEO_ID_OR_CLEAN_URL>"
```

### 2.2 Fetch the transcript
> ⚠️ **Gotcha — strip playlist params.** A URL with `&list=…&index=…` makes `yt-dlp` crawl the
> **entire playlist** (dozens of videos) and hang. Pass the **bare 11-char video id** (or a URL with
> only `?v=…`).

```bash
# Extract the id: ...watch?v=VIDEOID&list=... → VIDEOID
"$CONTENT_DIR/yt-transcript.sh" -q -o /tmp/trans-<ID>.txt "<ID>"
```
- Transcripts can take a couple of minutes; run in the background and wait on the output file.
- **If the transcript is missing/empty:** retry once. If still empty after 2 tries, **skip that talk**
  — but in a queued run still mark it `Complete` (§5.3) so nobody retries it.
- For very long transcripts, the reader may truncate — read the remainder via a byte-offset tail so
  the outline is grounded in the *whole* transcript.

### 2.3 Outline the transcript with AI — the demanding, completeness-first prompt
The old one-liner ("please detail outline the following transcript") compresses too much → thin,
generic output. Use this instead:

> *"You're an expert in software development/investing. Produce an **exhaustive hierarchical outline** of the
> following talk transcript.*
> *- Preserve **every** anecdote, name (people/companies/tools), number, statistic, direct quote, and
>   concrete example. Do not compress, generalize, or summarize away specifics — err toward completeness.*
> *- Use a **deep, decimal-numbered hierarchy**: number top sections (1, 2, 3…) and subsections
>   (1.1, 1.2, 2.1…), going to `###` and `####` where it helps. Aim for **one `###` subsection per
>   distinct sub-topic, example, or step** — a long talk should have **25+** subsections, not 3.*
> *- **One idea per bullet line.** Do not pack several facts into one paragraph or one table cell —
>   explode them into bullets and sub-bullets.*
> *- If the talk **enumerates** things (patterns, steps, rules, trends, examples, companies), give
>   **each item its own numbered `###` subsection** with its own bullets (rationale, metaphor, quote,
>   example). A summary **table** is a nice *addition* at the end, but never let a table *replace* the
>   per-item subsections — tables compress and make the outline read thinner than it is.*
> *- **Decompose worked examples step by step** — each micro-step / micro-behaviour gets its own `###`
>   (e.g. "7.1 Extract + placeholder name", "7.2 Rename").*
> *- **Break the Q&A finely**: one numbered subsection per question (Q1, Q2…), splitting multi-part
>   questions into follow-ups (Q5, Q5a). Name the asker if known.*
> *- Attribute quotes and claims to whoever said them.*
> *- Open with a one-paragraph **blockquote framing the talk** (speaker, venue, format, the talk's own structure).*
> *- Add a **'People & References Cited'** index at the end.*
> *- Keep each line tight (no filler), but keep the outline long — depth over brevity."*

### 2.4 Second "enrich" pass (this is what closes the gap with a hand-curated summary)
> *"Go back through the transcript and add any anecdote, name, number, or example the outline missed."*

### 2.5 Write the summary `.md` (in ONE write, so it's never half-written at deploy time)
- **Filename**: kebab-case `<topic>-<speaker>-<conference>.md`
  (e.g. `high-performing-communication-techniques-pelrine-craft-2026.md`).
  In **Mode B** the filename already exists — keep it exactly.
- **Location**: `$CONTENT_DIR` (same dir as the index).
- **Frontmatter** (match sibling files; in Mode B keep the shape and `title`, only enrich `description`):
  ```yaml
  ---
  title: "<Talk Title>"
  date: "2026-06-04T00:00:00.000Z"
  description: "<rich one-line description of what the outline covers>"
  type: "reference"
  tags: ["softwaredevelopment"]          # add "ai" when the talk is AI-topic, matching siblings
  ---
  ```
- **Body**: the AI outline (heading = talk title). Transcript-grounded only — **no fabrication**.
  If a transcript name/spelling conflicts with the filename/title, note it in the blockquote and keep
  the canonical filename/title (don't silently rewrite).
- **Provenance footer** (exact):
  ```
  *Video: https://www.youtube.com/watch?v=<ID> — Transcript via yt-transcript.sh; outline generated from the transcript.*
  ```
  (For a long transcript you couldn't fully capture in one pass, add "(partial for a long transcript)".)

### 2.6 (Mode A only) Add an entry to the index
Append a block in the same shape as existing references, grouped by conference year (new entries near
the top with their year):
```markdown
# <Talk Title>

- <video URL>
- [summary](./<summary-filename>.md)
```
**Mode B: never edit `index.md`.**

### 2.7 Deploy (see §6 for the command + the days-ago counter)

---

## 3. Depth bar & quality checklist (the point of the whole exercise)

Depth comes from **granularity**, not word count. A hand-curated outline of one talk had ~the same
word count as a thin draft (~3.1k vs ~2.8k) but read far deeper because it had **29 `###` subsections
vs 3** and ~2× the bullet lines. If a draft feels thin, the fix is to **split tables/paragraphs back
into numbered subsections and per-line bullets**, not to add new facts.

Before marking a file done, confirm it has:
- [ ] A **framing blockquote** (speaker, venue, format, the talk's own structure).
- [ ] A **`###` for every distinct example, step, and Q&A question** (long talk → 25+ `###`).
- [ ] Every **enumeration** expanded into numbered `###` subsections (not hidden in a table/paragraph).
- [ ] **Worked examples decomposed** step-by-step.
- [ ] **One idea per bullet** — no multi-fact paragraphs/cells.
- [ ] A **"People & References Cited"** index at the end.
- [ ] Frontmatter shape/title preserved; `description` enriched; provenance footer present & exact.
- [ ] **Match the talk's shape**: a 90-min pattern-catalog workshop → very long outline; a narrative
      keynote/interview compresses to prose and is shorter at the *same* fidelity — expected, not a defect.
- [ ] **Panels / podcasts** → outline as a **topic-threaded conversation** (still blockquote + References
      index). If a scheduled guest was absent / it turned into a roundtable, **say so** — don't fabricate.

---

## 4. Running solo (no parallelism)

If you don't need parallelism, skip the queue entirely: seed a plain list of `<id> <filename>` (Mode A
from the URL list, Mode B from §5.2's index scan) and loop the §2 pipeline over it yourself, deploying
after each file (§6), incrementing `--days-ago` by 1 each time. That's the whole job.

Reach for the shared queue (§5) only when you want **multiple agents** working at once.

---

## 5. Running in parallel — the shared work queue (optional)

A `/tmp` state file is the **single source of truth**; every mutation is serialized under an exclusive
`flock`, so any number of agents can claim/complete items concurrently without stepping on each other.
Three **separate** locks (never nested; each held only for its tiny critical section):
- **Queue lock** — inside the queue helper, for the claim/done edit.
- **days-ago lock** — for grabbing+incrementing the shared backdate counter (§6).
- **Deploy lock** — so only one `deploy.py` runs at a time (concurrent deploys corrupt the build/push).

All `/tmp` paths are namespaced by `$JOB` so different jobs coexist.

### 5.1 Create the queue helper (once per job)
```bash
cat > /tmp/$JOB-queue.sh <<'SH'
#!/usr/bin/env bash
# Shared work-queue helper. Source of truth: the TSV (id<TAB>filename<TAB>status).
# Every mutation is serialized under an exclusive flock, so many agents can call it safely.
#   queue.sh claim <tag>  -> atomically claims the topmost Pending row, marks it "In Progress (<tag>)",
#                            prints "<id>\t<filename>". Prints "QUEUE_EMPTY" when none remain.
#   queue.sh done  <id>   -> marks that id's row "Complete".
#   queue.sh status       -> prints the whole queue.
set -euo pipefail
Q="${QUEUE_TSV:?set QUEUE_TSV}"; LOCK="$Q.lock"
exec 9>"$LOCK"; flock 9
case "${1:-}" in
  claim)
    tag=${2:-anon}
    row=$(awk -F'\t' '$3=="Pending"{print NR; exit}' "$Q")
    if [ -z "$row" ]; then echo "QUEUE_EMPTY"; exit 0; fi
    awk -F'\t' -v OFS='\t' -v r="$row" -v t="$tag" 'NR==r{$3="In Progress ("t")"} {print}' "$Q" > "$Q.tmp" && mv "$Q.tmp" "$Q"
    awk -F'\t' -v r="$row" 'NR==r{print $1"\t"$2}' "$Q" ;;
  done)
    id=${2:?usage: done <id>}
    awk -F'\t' -v OFS='\t' -v id="$id" '$1==id{$3="Complete"} {print}' "$Q" > "$Q.tmp" && mv "$Q.tmp" "$Q"
    echo "marked $id Complete" ;;
  status) cat "$Q" ;;
  *) echo "usage: $0 {claim <tag>|done <id>|status}" >&2; exit 2 ;;
esac
SH
chmod +x /tmp/$JOB-queue.sh
export QUEUE_TSV=/tmp/$JOB-queue.tsv   # every agent must export this before calling the helper
```
> The helper reads its TSV path from `$QUEUE_TSV` so it stays job-agnostic. Have each agent
> `export QUEUE_TSV=/tmp/<JOB>-queue.tsv` (or bake it into their brief).

### 5.2 Seed the queue TSV (`id<TAB>filename<TAB>Pending`)

**Mode A — from a URL list** (`/tmp/$JOB-urls.txt`, one URL per line). For each URL, strip playlist
params to the bare id, fetch the title, and derive a kebab filename `<topic>-<speaker>-<conference>.md`
(do this with judgement per video), then:
```bash
printf '%s\t%s\tPending\n' "$ID" "$FILENAME" >> /tmp/$JOB-queue.tsv
```

**Mode B — from existing summary files** (the index already points at them). Parse the video id out of
each file's provenance footer:
```bash
: > /tmp/$JOB-queue.tsv
for f in "$CONTENT_DIR"/*.md; do
  base=$(basename "$f")
  [ "$base" = "index.md" ] && continue
  id=$(grep -oE 'watch\?v=[A-Za-z0-9_-]{11}' "$f" | head -1 | sed 's/.*v=//')
  [ -n "$id" ] && printf '%s\t%s\tPending\n' "$id" "$base" >> /tmp/$JOB-queue.tsv
done
# then pre-fetch transcripts for every id (optional but nice): loop yt-transcript.sh -o /tmp/trans-<id>.txt
```
> Exclude any already-good files / files you must not touch by removing their rows before starting.
> Keep the source-of-truth in the TSV — don't hand-edit it while agents run; go through the helper.

### 5.3 The claim → work → done loop (each agent, with its own stable tag)
```bash
export QUEUE_TSV=/tmp/$JOB-queue.tsv
while :; do
  read -r ID FNAME < <(/tmp/$JOB-queue.sh claim my-tag-1)   # pick a unique tag per agent
  [ "$ID" = "QUEUE_EMPTY" ] && { echo "done"; break; }
  # 1. read /tmp/trans-$ID.txt (+ existing $CONTENT_DIR/$FNAME); refetch if empty (§2.2)
  # 2. write the exhaustive outline to $CONTENT_DIR/$FNAME in ONE write (§2.5, §3)
  # 3. deploy (§6) using a freshly-grabbed days-ago value
  /tmp/$JOB-queue.sh done "$ID"
done
```
Inspect progress any time: `/tmp/$JOB-queue.sh status`. The lock is held only for the tiny claim/done
edit — never during reading, writing, or deploying.

### 5.4 Launching the agents
Write a one-page brief telling each agent: its **tag**, the §2 pipeline, the §3 depth bar, the deploy
+ days-ago protocol (§6), and "loop until QUEUE_EMPTY." Then launch N background workers, each with a
distinct tag (`agent-1`, `agent-2`, …). Deploys serialize automatically, so extra agents just queue on
the deploy lock — a good count is ~5–7. When every worker prints `QUEUE_EMPTY`, the batch is done.

---

## 6. Deploy + the shared days-ago counter

Deploy **after each summary**. `--days-ago` only backdates the commit; a **unique value per deploy**
keeps history clean. Grab a fresh value **right before deploying** — atomically, so no two deploys
reuse a number (starts at `$DAYS_AGO_START`, auto-increments):

```bash
N=$(flock /tmp/$JOB-daysago.lock bash -c '
  f=/tmp/'"$JOB"'-daysago.counter
  [ -s "$f" ] || echo '"$DAYS_AGO_START"' > "$f"
  n=$(cat "$f"); echo $((n + 1)) > "$f"; echo "$n"
')
flock /tmp/$JOB-deploy.lock python3 "$REPO/deploy.py" --commit-message "$JOB" \
  --gh-page-repo "$GH_PAGE_REPO" --days-ago="$N"
```
- The **deploy lock** guarantees one deploy at a time across all agents (the others block).
- Because `deploy.py` does `git add .`, a deploy sweeps up **any** finished files in the tree
  (including other agents'). That's fine — write each file in a single write so it's complete. You'll
  sometimes see "nothing to commit" when a peer's deploy already staged your file; content still lands.
- **Solo mode:** skip the flocks; just pass `--days-ago=<N>` and increment N by 1 each deploy.
- Transient `gatsby build` hiccup? Re-run the flocked deploy — the source-repo push may already have
  succeeded, so the retry just finishes the build + gh-pages push. Nothing is left half-deployed.
- If a deploy is slow, give the build a generous timeout (Gatsby can exceed 2 min).

---

## 7. Rules & conventions (read for parallel safety)

- **Deploys are the only shared mutation point of the repo** — always wrap them in the deploy `flock`.
- The three locks (queue / days-ago / deploy) are **separate — never nest them**; hold each only for
  its tiny critical section.
- Writing **different** `.md` files concurrently is safe. never
  commit transcripts (they live in `/tmp`, outside the repo).
- **Never hand-edit the queue TSV** while agents run — go through the helper.
- Keep the index grouped by conference year; add new (Mode A) entries near the top with their year.
- Transcripts are scratch artifacts — don't commit them.
- Optional hardening: adding `--no-playlist` inside `yt-transcript.sh` would let full `&list=` URLs
  work without the manual video-id extraction in §2.2.
- Skip any heading containing "ignore". Work autonomously;

---

## 8. Recovery / re-runs

- If `/tmp/<JOB>-queue.tsv` is lost (cleared `/tmp`), rebuild it (§5.2) — Mode B's index/dir scan makes
  this trivial. Rows already done stay done only if you preserved the TSV; otherwise re-deriving from
  the finished files (which already have deep outlines) and re-seeding as `Pending` just re-enriches.
- To resume a partial batch, seed only the not-yet-done rows as `Pending`.

---

## 9. Quick-start checklist

1. Set §1 parameters (`JOB`, `CONTENT_DIR`, `INDEX`, `REPO`, `GH_PAGE_REPO`, `POST_DATE`, `DAYS_AGO_START`).
2. Pick **Mode A** (URL list) or **Mode B** (existing index/dir).
3. Solo → §4. Parallel → create helper (§5.1), seed TSV (§5.2), pre-fetch transcripts, launch N tagged
   workers (§5.3–5.4).
4. Each item: transcript (§2.2) → exhaustive outline + enrich pass (§2.3–2.4) → single-write `.md`
   (§2.5) → (Mode A) index entry (§2.6) → serialized deploy with fresh days-ago (§6) → mark done.
5. Verify against the §3 depth bar. Done when the queue is empty / the list is exhausted.

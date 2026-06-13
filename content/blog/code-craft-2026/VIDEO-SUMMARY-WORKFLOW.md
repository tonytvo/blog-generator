# Video → Summary Workflow

A repeatable process for turning a **list of conference talk videos** into per-talk
summary pages that are linked from an index (e.g.
`content/blog/code-craft-2026/index.md`).

Give the process a list of video URLs; for each one it fetches the transcript,
outlines it, writes a summary `.md`, and adds the title + video link + summary
link to the index file.

---

## Inputs

- **A list of video URLs** (one per line), e.g.:

  ```
  https://www.youtube.com/watch?v=3zrrE374l1M&list=PLEQ3Q_FcrvEo&index=3
  https://www.youtube.com/watch?v=BLp1Ye8d290
  ...
  ```

- **The index file** to update, e.g. `content/blog/code-craft-2026/index.md`.
- Summary `.md` files are written next to the index, in the same directory.

## Tools

- `yt-transcript.sh` (in `~/bin` or current folder of index.md) — downloads a clean plain-text transcript via `yt-dlp`.
- `yt-dlp` — also used to read the video title.

---

## Per-video steps

Repeat for each URL in the list.

### 1. Get the title (used as the section heading)

```bash
yt-dlp --get-title --skip-download --force-ipv4 "<VIDEO_ID_OR_CLEAN_URL>"
```

### 2. Fetch the transcript

> ⚠️ **Gotcha — strip playlist params.** A URL containing `&list=…&index=…`
> makes `yt-dlp` crawl the **entire playlist** (can be dozens of videos) and hang.
> Pass the **bare 11-char video ID** (or a URL with only `?v=…`) instead.

```bash
# Extract the video id from ...watch?v=VIDEOID&list=... → VIDEOID
yt-transcript.sh -q -o transcript.txt "3zrrE374l1M"
```

The transcript can take a couple of minutes; run it in the background and wait
on the output file rather than blocking a foreground call.

### 3. Outline the transcript with AI

Feed the transcript text to the model with a **demanding, completeness-first** prompt.
The old one-liner ("please detail outline the following transcript") compresses too
much — it produces a thin, generic outline. Use this instead:

> *"You're an expert in software development. Produce an **exhaustive hierarchical
> outline** of the following talk transcript.*
> *- Preserve **every** anecdote, name (people/companies/tools), number, statistic,
>   direct quote, and concrete example. Do not compress, generalize, or summarize
>   away specifics — err on the side of completeness.*
> *- Use nested `##` / `###` Markdown sections, one per topic or sub-topic.*
> *- If the talk **enumerates** things (patterns, steps, rules, trends, a list of
>   companies), give each its own subsection, and add a **summary table** at the end
>   plus a **'People & References Cited'** index.*
> *- Attribute quotes and claims to whoever said them.*
> *- Open with a one-paragraph blockquote framing the talk (speaker, venue, format,
>   the talk's own structure).*
> *- Keep the writing tight per line (no filler), but keep the outline long — depth
>   over brevity."*

**Notes to get the depth right:**
- **One talk per pass.** Don't batch many transcripts into a single request — each
  talk deserves its own full-attention pass.
- **Do a second "enrich" pass** on the draft: *"Go back through the transcript and add
  any anecdote, name, number, or example the outline missed."* This is what closes the
  gap with a hand-curated summary.
- **Match the talk's shape.** A 90-minute pattern-catalog workshop naturally expands
  into a very long outline (tables, per-pattern subsections); a narrative keynote or
  interview compresses into prose and will be shorter at the *same* fidelity — that's
  expected, not a defect.
- For very long transcripts, note "(partial for a long transcript)" in the provenance
  footer if you couldn't capture everything in one pass.

### 4. Write the summary `.md`

- **Filename**: kebab-case, `<topic>-<speaker>-<conference>.md`
  (e.g. `high-performing-communication-techniques-pelrine-craft-2026.md`).
- **Location**: same directory as the index file.
- **Frontmatter** (match the sibling summary files):

  ```yaml
  ---
  title: "<Talk Title>"
  date: "2026-06-04T00:00:00.000Z"
  description: "<one-line description>"
  type: "reference"
  tags: ["softwaredevelopment"]
  ---
  ```

- **Body**: the AI outline. The heading is the talk title.

### 5. Add an entry to the index file

Append a block in the same shape as the existing references:

```markdown
# <Talk Title>

- <video URL>
- [summary](./<summary-filename>.md)
```

---

## Notes / conventions

- Keep the index grouped by conference year; add new Craft 2026 talks near the
  top with the other 2026 entries.
- Transcripts are scratch artifacts — don't commit `transcript.txt`.
- Optional hardening: adding `--no-playlist` inside `yt-transcript.sh` would let
  full `&list=` URLs work without the manual video-ID extraction in step 2.

---

## Example (done in this repo)

- **Video**: <https://www.youtube.com/watch?v=3zrrE374l1M&list=PLEQ3Q_FcrvEo&index=3>
- **Title**: *High-performing communication techniques for high-performing teams — Joseph Pelrine | Craft 2026*
- **Summary**: `content/blog/code-craft-2026/high-performing-communication-techniques-pelrine-craft-2026.md`
- **Index updated**: `content/blog/code-craft-2026/index.md`

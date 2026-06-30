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

Feed the transcript text to the model with the prompt:

> *"You're an expert in software development, please detail outline the following transcript"*

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

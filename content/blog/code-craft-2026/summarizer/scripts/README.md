# talks-outline

Exhaustive, shareable markdown outlines of talks (YouTube links, a urls.txt, or transcripts)
in software engineering, value investing, and self-help — outlined in parallel through a
shared work queue that other AI agents can join.

Outputs: `~/Downloads/talks-outlines/summaries/<slug>-<date>.md` per talk +
`talks-outline-index.md` (one collection point across every project). Outline language =
spoken language of the talk.

## Install (Claude Code + Codex CLI — one command)
```bash
bash ~/.claude/skills/talks-outline/install.sh
```
**First-time setup / new machine:** all skill artifacts are backed up in
`~/Downloads/talks-outlines/scripts/` (synced via Google Drive). Run from there:
```bash
bash ~/Downloads/talks-outlines/scripts/install.sh
```
It copies everything into `~/.claude/skills/talks-outline/`, creates the venv, and sets up
both Claude and Codex. Works from any location.
The installer sets up both Claude Code and Codex CLI in one step:
- Claude agent definition, Python venv, output directories, permission rules
- Codex custom prompt (`~/.codex/prompts/talks-outline.md`) and AGENTS.md
- `urls.txt` template and `reenrich-prompt.md` in the output folder

Safe to re-run — every step is idempotent. Requires `python3-venv` (`sudo apt install
python3-venv` on Debian/Ubuntu). Restart Claude Code once if `~/.claude/agents/` did not
exist before.

<details><summary>Manual install (if you prefer)</summary>

```bash
mkdir -p ~/.claude/skills ~/.claude/agents ~/.codex/prompts
unzip talks-outline.skill -d ~/.claude/skills/
cp ~/.claude/skills/talks-outline/agents/talks-outliner.md ~/.claude/agents/
cp ~/.claude/skills/talks-outline/codex/talks-outline.md ~/.codex/prompts/
chmod +x ~/.claude/skills/talks-outline/scripts/talks-queue.sh
cd ~/.claude/skills/talks-outline
python3 -m venv .venv && .venv/bin/pip install youtube-transcript-api yt-dlp
mkdir -p ~/Downloads/talks-outlines/summaries
```
</details>

## Use
- Paste links, or point at a urls.txt:  `/talks-outline <link> <link>`  ·  `/talks-outline seed ~/talks/urls.txt`
- Continue a seeded batch:  `/talks-outline work-queue`
- Re-enrich thin outlines (Mode B):  `/talks-outline reenrich ~/Downloads/talks-outlines/summaries`
Each talk gets its own queue worker that fetches *and* outlines, so a batch runs in parallel
(4–6 workers; YouTube rate-limits beyond that).

**Multi-agent / cross-AI batches:** see `USAGE.md`. Any agent (Codex CLI, Gemini CLI, a second
machine) joins the same `/tmp/talks-queue.tsv` with a unique tag and `AGENT-BRIEF.md`.

## Claude.ai (web / mobile)
Click **Save skill** on the `.skill` card, then paste a transcript and say "detail outline
this". Outlines come back as downloadable `.md` files. (No YouTube fetching or parallel
subagents on this surface — paste transcripts.)

## Unattended / batch runs (nobody at the keyboard)
The skill never asks questions. To stop Claude Code itself from prompting, add these rules to
`~/.claude/settings.json` (user scope = every project):
```json
{
  "permissions": {
    "allow": [
      "Bash(~/.claude/skills/talks-outline/.venv/bin/python *)",
      "Bash(~/.claude/skills/talks-outline/scripts/talks-queue.sh *)",
      "Bash(python3 *)",
      "Bash(flock *)",
      "Edit(~/Downloads/talks-outlines/summaries/**)",
      "Edit(talks-work/**)"
    ]
  }
}
```
Notes: file rules must be `Edit(...)` — a `Write(...)` rule is accepted but never consulted.
`Bash(cmd *)` is prefix matching on the whole command, so each part of a compound command
must match a rule; the fetcher and queue helper are invoked as single commands for this
reason. Verify with `/permissions` inside Claude Code.

Start the session so edits don't prompt either:
```bash
claude remote-control --name talks --permission-mode acceptEdits    # control from the mobile app
# or headless:
claude -p "/talks-outline seed ~/talks/urls.txt" --permission-mode acceptEdits
```
macOS: background sessions need Full Disk Access (or an explicit Downloads grant) for the
terminal app before they can write to `~/Downloads`.

## Push notification when a batch finishes
In the Claude Code terminal run `/config` and turn on **Push when Claude decides** (and
**Push when actions required** to forward permission prompts). Requires the Claude mobile app
signed in to the same account, OS notifications allowed, and an active Remote Control session.
You can also add "notify me when the outlines are done" to your prompt.

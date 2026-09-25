# Remote re-enrich prompt

Paste one of these into your Claude Code remote control session from your phone.

**urls.txt lives at `~/Downloads/talks-outlines/urls.txt`** — this folder syncs via
Google Drive (Insync), so you can edit urls.txt from the Drive app on your phone
before sending the prompt. One URL per line, optional domain column:

```
# urls.txt — edit via Google Drive on your phone, then trigger the remote session
https://www.youtube.com/watch?v=XXXXXXXXXXX   software
https://www.youtube.com/watch?v=YYYYYYYYYYY   investing
https://youtu.be/ZZZZZZZZZZZ                 auto
```

---

## Option 1: Re-enrich existing outlines (Codex + Claude in parallel)

```
Seed the re-enrich queue from ~/Downloads/talks-outlines/summaries, then launch workers in parallel:

1. Seed: export QUEUE_TSV=/tmp/talks-queue.tsv && ~/.claude/skills/talks-outline/scripts/talks-queue.sh seed-dir ~/Downloads/talks-outlines/summaries
2. Launch 2 Codex workers in background via Bash (each as a separate background command):
   codex exec -s danger-full-access --skip-git-repo-check -C ~/Downloads/talks-outlines "$(cat ~/.claude/skills/talks-outline/AGENT-BRIEF.md) Your TAG is codex-1. QUEUE_TSV=/tmp/talks-queue.tsv. Re-enrich mode: read the EXISTING outline AND the transcript, rewrite with more depth."
   Same command but TAG=codex-2.
3. Then run: /talks-outline reenrich ~/Downloads/talks-outlines/summaries
4. Monitor with talks-queue.sh stats. Notify me when all Complete.
```

## Option 2: New talks from urls.txt (Codex + Claude in parallel)

Edit `~/Downloads/talks-outlines/urls.txt` via Google Drive on your phone first, then paste:

```
Process talks from ~/Downloads/talks-outlines/urls.txt with parallel workers:

1. Seed: export QUEUE_TSV=/tmp/talks-queue.tsv && ~/.claude/skills/talks-outline/scripts/talks-queue.sh seed-urls ~/path-to/urls.txt
2. Launch 2 Codex workers in background via Bash (each as a separate background command):
   codex exec -s danger-full-access --skip-git-repo-check -C ~/Downloads/talks-outlines "$(cat ~/.claude/skills/talks-outline/AGENT-BRIEF.md) Your TAG is codex-1. QUEUE_TSV=/tmp/talks-queue.tsv. Start the loop now."
   Same command but TAG=codex-2.
3. Then run: /talks-outline work-queue
4. Monitor with talks-queue.sh stats. Notify me when done.
```

## Option 3: New talks from links (Claude only, no Codex)

```
/talks-outline <paste YouTube links here>
```

---

## Setup (one-time, on the computer)

Start the remote control session before leaving:

```bash
claude remote-control --name talks --permission-mode acceptEdits \
  --add-dir <dir-here>
```

Then control it from the Claude mobile app.

#!/usr/bin/env bash
# talks-queue.sh — shared work queue for parallel talk summarization.
# Source of truth: a TSV,  id <TAB> filename <TAB> status  (status: Pending | In Progress (tag) | Complete)
# Every mutation is serialized with an exclusive flock, so any number of agents
# (Claude Code, Codex CLI, Gemini CLI, a human) can call it concurrently.
#
#   export QUEUE_TSV=/tmp/<JOB>-queue.tsv
#   talks-queue.sh seed-urls <urls.txt>   # append Pending rows from a URL list (id per line, # comments ok)
#   talks-queue.sh seed-dir  <dir>        # Mode B: rebuild from provenance footers of existing .md files
#   talks-queue.sh claim <tag>            # atomically take the topmost Pending row -> "<id><TAB><filename>"
#                                         #   prints QUEUE_EMPTY when none remain
#   talks-queue.sh done  <id>             # mark Complete (also use for permanently-skipped talks)
#   talks-queue.sh reset <id>             # put a row back to Pending (crashed worker)
#   talks-queue.sh status                 # print the queue
#   talks-queue.sh stats                  # counts by status
set -euo pipefail

Q="${QUEUE_TSV:?set QUEUE_TSV, e.g. export QUEUE_TSV=/tmp/talks-queue.tsv}"
[ -e "$Q" ] || : > "$Q"
LOCK="$Q.lock"

# id is the 11-char YouTube id; PENDING_TITLE means "worker resolves the filename"
extract_id() {  # handles watch?v=ID&list=..., youtu.be/ID?t=, shorts/ID, live/ID, bare ID
  local u="$1"
  grep -oE '(v=|youtu\.be/|shorts/|live/|embed/)[A-Za-z0-9_-]{11}' <<<"$u" \
    | head -1 | grep -oE '[A-Za-z0-9_-]{11}$' && return 0
  grep -oE '^[A-Za-z0-9_-]{11}$' <<<"$u"
}

case "${1:-}" in
  seed-urls)
    src=${2:?usage: seed-urls <urls.txt>}
    exec 9>"$LOCK"; flock 9
    added=0
    while IFS= read -r line || [ -n "$line" ]; do
      line=${line%%#*}; line=$(tr -d '\r' <<<"$line"); [ -z "${line// }" ] && continue
      read -r url dom fname <<<"$line"
      id=$(extract_id "$url") || true
      [ ${#id} -eq 11 ] || { echo "SKIP (no video id): $url" >&2; continue; }
      grep -q "^$id	" "$Q" && { echo "SKIP (already queued): $id" >&2; continue; }
      printf '%s\t%s\t%s\tPending\n' "$id" "${fname:-PENDING_TITLE}" "${dom:-auto}" >> "$Q"
      added=$((added+1))
    done < "$src"
    echo "seeded $added row(s) into $Q" ;;

  seed-dir)
    dir=${2:?usage: seed-dir <content-dir>}
    exec 9>"$LOCK"; flock 9
    added=0
    for f in "$dir"/*.md; do
      base=$(basename "$f")
      [ "$base" = "talks-outline-index.md" ] && continue
      id=$(grep -oE 'watch\?v=[A-Za-z0-9_-]{11}' "$f" | head -1 | sed 's/.*v=//') || true
      [ ${#id} -eq 11 ] || continue
      grep -q "^$id	" "$Q" && continue
      printf '%s\t%s\t%s\tPending\n' "$id" "$base" "auto" >> "$Q"
      added=$((added+1))
    done
    echo "seeded $added row(s) from $dir (Mode B: keep these filenames)" ;;

  claim)
    tag=${2:-anon}
    exec 9>"$LOCK"; flock 9
    row=$(awk -F'\t' '$4=="Pending"{print NR; exit}' "$Q")
    if [ -z "$row" ]; then echo "QUEUE_EMPTY"; exit 0; fi
    awk -F'\t' -v OFS='\t' -v r="$row" -v t="$tag" 'NR==r{$4="In Progress ("t")"} {print}' "$Q" > "$Q.tmp" && mv "$Q.tmp" "$Q"
    awk -F'\t' -v r="$row" 'NR==r{print $1"\t"$2"\t"$3}' "$Q" ;;

  done)
    id=${2:?usage: done <id>}
    exec 9>"$LOCK"; flock 9
    awk -F'\t' -v OFS='\t' -v id="$id" '$1==id{$4="Complete"} {print}' "$Q" > "$Q.tmp" && mv "$Q.tmp" "$Q"
    echo "marked $id Complete" ;;

  reset)
    id=${2:?usage: reset <id>}
    exec 9>"$LOCK"; flock 9
    awk -F'\t' -v OFS='\t' -v id="$id" '$1==id{$4="Pending"} {print}' "$Q" > "$Q.tmp" && mv "$Q.tmp" "$Q"
    echo "reset $id to Pending" ;;

  status) cat "$Q" ;;
  stats)  awk -F'\t' '{c[$4]++} END{for (s in c) printf "%-24s %d\n", s, c[s]}' "$Q" ;;
  *) echo "usage: $0 {seed-urls <f>|seed-dir <d>|claim <tag>|done <id>|reset <id>|status|stats}" >&2; exit 2 ;;
esac

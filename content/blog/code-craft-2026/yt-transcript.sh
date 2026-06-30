#!/usr/bin/env bash
#
# yt-transcript — fetch a clean, plain-text transcript from a YouTube video,
# using yt-dlp to download the subtitle track (forces IPv4 to avoid the common
# "Downloading webpage" hang).
#
# By default the transcript is saved to:
#   <videoId>-<YYYYMMDD-HHMMSS>-transcript.txt   (in the current directory)
# Use -o FILE for a custom path, or -o - to print to stdout (for piping).
#
# Progress is logged to stderr; verbose is ON by default (use -q to silence).
# If yt-dlp isn't available, a private virtualenv is created in your cache dir
# and yt-dlp is installed there (no system Python changes, PEP 668-safe).

set -euo pipefail

PROG="$(basename "$0")"
LANG_PREF="en"
OUTFILE=""
KEEP_TS=0
DO_LIST=0
USE_IPV6=0
NO_INSTALL=0
QUIET=0
TIMEOUT=30
INPUT=""
YTDLP="yt-dlp"
VENV_DIR="${XDG_CACHE_HOME:-$HOME/.cache}/yt-transcript/venv"

usage() {
cat <<EOF
yt-transcript — fetch a clean, plain-text transcript from a YouTube video (via yt-dlp).

Usage:
  $PROG [options] <youtube-url-or-id>

Options:
  -l, --lang CODE     Preferred caption language code/prefix (default: en)
  -o, --out FILE      Output path. Default: <videoId>-<YYYYMMDD-HHMMSS>-transcript.txt
                      Use '-o -' to write to stdout instead of a file.
  -t, --timestamps    Keep per-line timestamps
      --list          List available subtitle languages and exit
      --ipv6          Allow IPv6 (default forces IPv4 to avoid hangs)
      --timeout SEC   Socket timeout in seconds (default: 30; 0 = none)
  -q, --quiet         Suppress progress logging
      --no-install    Do not auto-install yt-dlp if it is missing
  -h, --help          Show this help

Examples:
  $PROG "https://www.youtube.com/watch?v=dQw4w9WgXcQ"     # -> dQw4w9WgXcQ-20260628-212233-transcript.txt
  $PROG -o talk.txt dQw4w9WgXcQ
  $PROG -o - dQw4w9WgXcQ | llm "summarize this"
EOF
}

# ---- progress logging (stderr) --------------------------------------------
log() { [ "$QUIET" -eq 1 ] && return 0; printf '[%s] %s\n' "$(date +%H:%M:%S)" "$*" >&2; }

# ---- parse args ------------------------------------------------------------
while [ $# -gt 0 ]; do
  case "$1" in
    -l|--lang)        LANG_PREF="${2:?missing lang}"; shift 2 ;;
    -o|--out)         OUTFILE="${2:?missing file}"; shift 2 ;;
    -t|--timestamps)  KEEP_TS=1; shift ;;
    --list)           DO_LIST=1; shift ;;
    --ipv6)           USE_IPV6=1; shift ;;
    --timeout)        TIMEOUT="${2:?missing seconds}"; shift 2 ;;
    -q|--quiet)       QUIET=1; shift ;;
    --no-install)     NO_INSTALL=1; shift ;;
    -h|--help)        usage; exit 0 ;;
    -*)               echo "$PROG: unknown option '$1'" >&2; exit 64 ;;
    *)                INPUT="$1"; shift ;;
  esac
done

[ -n "$INPUT" ] || { echo "$PROG: missing YouTube URL or video ID" >&2; usage; exit 64; }

# Normalise a bare 11-char video ID into a full URL.
if printf '%s' "$INPUT" | grep -Eq '^[A-Za-z0-9_-]{11}$'; then
  URL="https://www.youtube.com/watch?v=${INPUT}"
else
  URL="$INPUT"
fi

# Build common yt-dlp flag arrays.
IPV4_FLAG=(--force-ipv4)
[ "$USE_IPV6" -eq 1 ] && IPV4_FLAG=()
TO_ARGS=()
[ "$TIMEOUT" != "0" ] && TO_ARGS=(--socket-timeout "$TIMEOUT")

log "config: url='$URL' lang='$LANG_PREF' ipv4=$([ "$USE_IPV6" -eq 1 ] && echo off || echo on) timeout=${TIMEOUT}s"

# ---- ensure yt-dlp (system, else private venv) ----------------------------
ensure_ytdlp() {
  log "checking for yt-dlp…"
  if command -v yt-dlp >/dev/null 2>&1; then
    log "yt-dlp present ($(command -v yt-dlp))."
    YTDLP="yt-dlp"; return
  fi
  if [ -x "$VENV_DIR/bin/yt-dlp" ]; then
    log "yt-dlp present (cached venv)."
    YTDLP="$VENV_DIR/bin/yt-dlp"; return
  fi
  if [ "$NO_INSTALL" -eq 1 ]; then
    echo "$PROG: yt-dlp not installed. Install it with: pipx install yt-dlp" >&2
    exit 1
  fi
  command -v python3 >/dev/null 2>&1 || { echo "$PROG: python3 not found." >&2; exit 1; }
  log "yt-dlp missing — creating a private virtualenv at:"
  log "  $VENV_DIR"
  if ! python3 -m venv "$VENV_DIR" >/dev/null 2>&1; then
    echo "$PROG: could not create a virtualenv (the venv module may be missing)." >&2
    echo "       On Debian/Ubuntu: sudo apt install python3-venv python3-full" >&2
    echo "       Or install it yourself:  pipx install yt-dlp" >&2
    exit 1
  fi
  log "installing yt-dlp into the venv (one-time, may take a moment)…"
  if ! "$VENV_DIR/bin/python" -m pip install -q -U pip yt-dlp >&2; then
    echo "$PROG: failed to install yt-dlp into the venv." >&2
    exit 1
  fi
  YTDLP="$VENV_DIR/bin/yt-dlp"
  log "install complete (venv will be reused on future runs)."
}
ensure_ytdlp

# ---- list mode -------------------------------------------------------------
if [ "$DO_LIST" -eq 1 ]; then
  log "listing available subtitles…"
  "$YTDLP" "${IPV4_FLAG[@]}" "${TO_ARGS[@]}" --list-subs --skip-download "$URL"
  exit $?
fi

# ---- download subtitles ----------------------------------------------------
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

ytdlp_fetch() {  # $1 = --write-subs | --write-auto-subs
  local verbosity=()
  if [ "$QUIET" -eq 1 ]; then verbosity=(--quiet --no-warnings); fi
  # yt-dlp progress -> stderr, so our transcript stdout stays clean.
  "$YTDLP" "${IPV4_FLAG[@]}" "${TO_ARGS[@]}" \
    --skip-download "$1" \
    --sub-langs "${LANG_PREF}.*,${LANG_PREF}" \
    --sub-format "vtt/best" \
    "${verbosity[@]}" \
    -o "${WORK}/%(id)s.%(ext)s" \
    "$URL" >&2 || true
}

log "downloading manual subtitles with yt-dlp (IPv4 forced)…"
ytdlp_fetch "--write-subs"
VTT="$(ls "${WORK}"/*.vtt 2>/dev/null | head -n1 || true)"
if [ -z "$VTT" ]; then
  log "no manual captions found; trying auto-generated…"
  ytdlp_fetch "--write-auto-subs"
  VTT="$(ls "${WORK}"/*.vtt 2>/dev/null | head -n1 || true)"
fi
[ -n "$VTT" ] || {
  echo "$PROG: no subtitles found for this video (lang: $LANG_PREF)." >&2; exit 2; }

# Derive the real video ID from the downloaded filename (id.lang.vtt).
VTT_BASE="$(basename "$VTT")"
VIDEO_ID="${VTT_BASE%%.*}"
log "downloaded: $VTT_BASE (video id: $VIDEO_ID); cleaning…"

# ---- clean VTT into plain text (stdlib python; no deps) -------------------
RESULT="$(python3 - "$VTT" "$KEEP_TS" <<'PYEOF'
import re, sys

path, keep_ts = sys.argv[1], sys.argv[2] == "1"
with open(path, encoding="utf-8", errors="replace") as f:
    raw = f.read()

tag_re = re.compile(r"<[^>]+>")          # inline <00:00:00.000> and <c> tags
cues, cur_ts = [], None
for line in raw.splitlines():
    if line.startswith(("WEBVTT", "Kind:", "Language:")):
        continue
    if "-->" in line:
        cur_ts = line.split(" ", 1)[0]
        continue
    text = tag_re.sub("", line).strip()
    if text:
        cues.append((cur_ts, text))

# Collapse YouTube's rolling-window duplicates:
#   exact repeats dropped; a line that grows the previous one replaces it.
clean = []
for ts, text in cues:
    if clean:
        pts, ptext = clean[-1]
        if text == ptext:
            continue
        if text.startswith(ptext):
            clean[-1] = (pts, text)
            continue
    clean.append((ts, text))

if keep_ts:
    out = "\n".join(f"[{ts}] {t}" for ts, t in clean)
else:
    out = re.sub(r"\s+", " ", " ".join(t for _, t in clean)).strip()

sys.stdout.write(out)
PYEOF
)"
log "done: ${#RESULT} characters"

# ---- output ----------------------------------------------------------------
if [ "$OUTFILE" = "-" ]; then
  printf '%s\n' "$RESULT"
else
  if [ -z "$OUTFILE" ]; then
    OUTFILE="${VIDEO_ID}-$(date +%Y%m%d-%H%M%S)-transcript.txt"
  fi
  printf '%s\n' "$RESULT" > "$OUTFILE"
  log "saved transcript to $OUTFILE"
  echo "$PROG: saved transcript to $OUTFILE" >&2
fi

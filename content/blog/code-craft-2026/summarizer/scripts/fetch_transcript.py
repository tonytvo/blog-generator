#!/usr/bin/env python3
"""Fetch YouTube transcripts + metadata for one or more URLs.

Usage:
  python fetch_transcript.py --out ./talks-work URL [URL ...]
  python fetch_transcript.py --expand PLAYLIST_URL        # print video URLs, one per line

Per video writes:
  <out>/<video_id>/meta.json        title, channel, url, duration_s, language, source
  <out>/<video_id>/transcript.txt   plain text, one line per caption cue, "[mm:ss] text"

Prints one status line per video:  OK <id> <chars>   |   NO_TRANSCRIPT <id> <reason>

Deps:  pip install youtube-transcript-api yt-dlp
The API route is tried first (manual captions preferred over auto, preferred languages
vi, en, then anything). yt-dlp is the fallback for both captions and metadata.
"""
import argparse
import json
import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import re
import shutil
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

# No hardcoded language preference: always take the ORIGINAL spoken-language captions.
# Translated tracks are only used when nothing original exists, and are flagged as such.
FALLBACK_LANGS = ["vi", "en", "en-US", "en-GB"]
VIDEO_ID_RE = re.compile(r"(?:v=|youtu\.be/|shorts/|live/|embed/)([A-Za-z0-9_-]{11})")


def video_id(url: str) -> str | None:
    m = VIDEO_ID_RE.search(url)
    return m.group(1) if m else None


def fmt_ts(seconds: float) -> str:
    s = int(seconds)
    return f"{s // 60:02d}:{s % 60:02d}"


# ---------- metadata ----------
def meta_oembed(url: str) -> dict:
    q = urllib.parse.urlencode({"url": url, "format": "json"})
    with urllib.request.urlopen(f"https://www.youtube.com/oembed?{q}", timeout=15) as r:
        d = json.load(r)
    return {"title": d.get("title"), "channel": d.get("author_name")}


def meta_ytdlp(url: str) -> dict:
    if not shutil.which("yt-dlp"):
        return {}
    out = subprocess.run(
        ["yt-dlp", "--dump-json", "--skip-download", "--no-warnings", url],
        capture_output=True, text=True, timeout=60,
    )
    if out.returncode != 0:
        return {}
    d = json.loads(out.stdout)
    return {
        "title": d.get("title"),
        "channel": d.get("channel") or d.get("uploader"),
        "duration_s": d.get("duration"),
        "upload_date": d.get("upload_date"),
    }


# ---------- transcript via API ----------
def transcript_api(vid: str, retries: int = 3):
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        return None, "youtube_transcript_api not installed"
    last = None
    for attempt in range(retries):
        res, err = _transcript_api_once(YouTubeTranscriptApi, vid)
        if res is not None:
            return res, None
        last = err
        if "429" in err or "TooManyRequests" in err or "Forbidden" in err:
            time.sleep((2 ** attempt) + random.random())  # back off on rate limits
        else:
            break
    return None, last


def _transcript_api_once(YouTubeTranscriptApi, vid: str):
    """Pick the original-language track: manual first, then auto-generated.

    youtube_transcript_api marks translated tracks via .is_translatable/translation
    machinery; the tracks returned by list() are the ones YouTube actually published for
    the video, so the manual (human) track is the speakers' language when it exists, and
    the generated track carries the language ASR detected from the audio.
    """
    try:
        api = YouTubeTranscriptApi()
        listing = list(api.list(vid))
        manual = [t for t in listing if not t.is_generated]
        generated = [t for t in listing if t.is_generated]
        chosen = (manual or generated or listing)[0]
        # if several manual tracks exist, prefer the one matching the generated (=spoken) lang
        if len(manual) > 1 and generated:
            spoken = generated[0].language_code.split("-")[0]
            for t in manual:
                if t.language_code.split("-")[0] == spoken:
                    chosen = t
                    break
        cues = chosen.fetch()
        lines = [f"[{fmt_ts(c.start)}] {c.text.strip()}" for c in cues if c.text.strip()]
        return {
            "lines": lines,
            "language": chosen.language_code,
            "language_name": getattr(chosen, "language", None),
            "source": "auto" if chosen.is_generated else "manual",
            "available_languages": [t.language_code for t in listing],
        }, None
    except Exception as e:  # noqa: BLE001
        return None, f"{type(e).__name__}: {e}"


# ---------- transcript via yt-dlp ----------
def transcript_ytdlp(url: str, vid: str, workdir: Path):
    if not shutil.which("yt-dlp"):
        return None, "yt-dlp not installed"
    orig = (meta_ytdlp(url) or {}).get("language")  # language of the audio track
    langs = f"{orig},{orig}.*" if orig else ",".join(FALLBACK_LANGS)
    subprocess.run(
        ["yt-dlp", "--skip-download", "--write-subs", "--write-auto-subs",
         "--sub-langs", langs, "--sub-format", "vtt", "--no-warnings",
         "-o", str(workdir / "%(id)s.%(ext)s"), url],
        capture_output=True, text=True, timeout=120,
    )
    vtts = sorted(workdir.glob(f"{vid}*.vtt"))
    if not vtts:
        return None, "no captions available"
    # prefer preferred-language files in order
    # never pick an auto-translated track ("-orig" absent but lang != original)
    preferred = [orig] if orig else FALLBACK_LANGS
    vtt = next((v for l in preferred for v in vtts if l and f".{l}." in v.name), vtts[0])
    lang = vtt.name.split(".")[-2]
    lines, last = [], None
    ts_re = re.compile(r"(\d+):(\d+):(\d+)\.\d+ -->")
    cur_ts = "00:00"
    for raw in vtt.read_text(encoding="utf-8", errors="ignore").splitlines():
        m = ts_re.match(raw)
        if m:
            h, mnt, s = map(int, m.groups())
            cur_ts = fmt_ts(h * 3600 + mnt * 60 + s)
            continue
        txt = re.sub(r"<[^>]+>", "", raw).strip()
        if not txt or txt.startswith(("WEBVTT", "Kind:", "Language:")) or txt.isdigit():
            continue
        if txt != last:  # auto-subs repeat rolling lines
            lines.append(f"[{cur_ts}] {txt}")
            last = txt
    for v in vtts:
        v.unlink(missing_ok=True)
    return {"lines": lines, "language": lang, "source": "yt-dlp",
            "available_languages": [v.name.split(".")[-2] for v in vtts]}, None


# ---------- playlist ----------
def expand_playlist(url: str) -> list[str]:
    if not shutil.which("yt-dlp"):
        sys.exit("yt-dlp required for playlist expansion: pip install yt-dlp")
    out = subprocess.run(
        ["yt-dlp", "--flat-playlist", "--print", "url", "--no-warnings", url],
        capture_output=True, text=True, timeout=120,
    )
    return [u for u in out.stdout.split() if video_id(u)]


# ---------- main ----------
def process(url: str, out_root: Path) -> None:
    vid = video_id(url)
    if not vid:
        print(f"SKIP {url} (not a video url)")
        return
    d = out_root / vid
    d.mkdir(parents=True, exist_ok=True)
    canonical = f"https://www.youtube.com/watch?v={vid}"
    time.sleep(random.random() * 0.5)  # stagger parallel starts

    meta = {"url": canonical, "video_id": vid}
    try:
        meta.update(meta_oembed(canonical))
    except Exception:  # noqa: BLE001
        pass
    if not meta.get("title") or not meta.get("duration_s"):
        meta.update({k: v for k, v in meta_ytdlp(canonical).items() if v})

    tr, err = transcript_api(vid)
    if tr is None:
        tr, err2 = transcript_ytdlp(canonical, vid, d)
        err = f"{err}; {err2}" if tr is None else None
    if tr is None:
        meta["transcript"] = None
        (d / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2))
        print(f"NO_TRANSCRIPT {vid} {err}")
        return

    text = "\n".join(tr["lines"])
    (d / "transcript.txt").write_text(text, encoding="utf-8")
    meta.update({
        "language": tr["language"],                      # language actually spoken
        "language_name": tr.get("language_name"),
        "transcript_source": tr["source"],               # manual | auto | yt-dlp
        "available_languages": tr.get("available_languages"),
        "transcript_chars": len(text),
    })
    (d / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2))
    print(f"OK {vid} {len(text)} chars {tr['language']}/{tr['source']} — {meta.get('title')}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("urls", nargs="*")
    ap.add_argument("--out", default="./talks-work")
    ap.add_argument("--expand", help="playlist URL: print video URLs and exit")
    ap.add_argument("--jobs", type=int, default=4, help="parallel downloads (default 4; keep <=6 to avoid YouTube rate limits)")
    a = ap.parse_args()
    if a.expand:
        print("\n".join(expand_playlist(a.expand)))
        return
    if not a.urls:
        ap.error("no URLs given")
    out_root = Path(a.out)
    urls: list[str] = []
    for u in a.urls:
        if "list=" in u and not video_id(u):
            urls.extend(expand_playlist(u))
        else:
            urls.append(u)
    urls = list(dict.fromkeys(urls))  # dedupe, keep order
    jobs = max(1, min(a.jobs, len(urls)))
    with ThreadPoolExecutor(max_workers=jobs) as ex:
        futs = {ex.submit(process, u, out_root): u for u in urls}
        for f in as_completed(futs):
            try:
                f.result()
            except Exception as e:  # noqa: BLE001
                print(f"NO_TRANSCRIPT {video_id(futs[f]) or futs[f]} {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()

"""
Fetch YouTube transcripts for a given expert and save each as a markdown
file under research/youtube-transcripts/<author-name>/.

No API key required: video titles come from YouTube's public oEmbed
endpoint, and transcripts come from the youtube-transcript-api package
(reads publicly available captions).

Usage:
  python scripts/fetch_youtube_transcripts.py --author "Sam Dunning" \\
      --urls https://www.youtube.com/watch?v=xxxxxxxxxxx \\
             https://youtu.be/yyyyyyyyyyy
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
)

OEMBED_URL = "https://www.youtube.com/oembed?url={}&format=json"


def extract_video_id(url: str) -> str | None:
    patterns = [
        r"(?:v=|/videos/|embed/|youtu\.be/|/shorts/)([A-Za-z0-9_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def get_video_title(url: str) -> str:
    try:
        oembed_url = OEMBED_URL.format(urllib.parse.quote(url, safe=""))
        with urllib.request.urlopen(oembed_url, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("title", "untitled")
    except Exception:
        return "untitled"


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:80] or "untitled"


def fetch_transcript(video_id: str) -> tuple[str | None, str]:
    try:
        fetched = YouTubeTranscriptApi().fetch(video_id)
        return " ".join(seg.text for seg in fetched), "ok"
    except NoTranscriptFound:
        return None, "no_transcript_found"
    except TranscriptsDisabled:
        return None, "transcripts_disabled"
    except VideoUnavailable:
        return None, "video_unavailable"
    except Exception as exc:  # noqa: BLE001 - surface any other failure per-video
        return None, f"error:{exc}"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--author", required=True, help="Expert's name (used as the output folder)")
    parser.add_argument("--urls", nargs="+", required=True, help="YouTube video URLs")
    parser.add_argument(
        "--output-root", default="research/youtube-transcripts", help="Root folder for transcript output"
    )
    args = parser.parse_args()

    out_dir = Path(args.output_root) / slugify(args.author)
    out_dir.mkdir(parents=True, exist_ok=True)

    for i, url in enumerate(args.urls, 1):
        video_id = extract_video_id(url)
        if not video_id:
            print(f"  [warn] could not parse video ID from {url}", file=sys.stderr)
            continue

        title = get_video_title(url)
        transcript, status = fetch_transcript(video_id)

        file_path = out_dir / f"{slugify(title)}.md"
        with file_path.open("w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(f"- Author: {args.author}\n")
            f.write(f"- URL: {url}\n")
            f.write(f"- Transcript status: {status}\n\n")
            f.write("## Transcript\n\n")
            f.write(transcript if transcript else "_No transcript available for this video._")

        print(f"  [{i}/{len(args.urls)}] {title} -> {file_path} ({status})")

    print(f"\nDone. Saved to {out_dir}")


if __name__ == "__main__":
    main()

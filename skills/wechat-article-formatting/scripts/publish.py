#!/usr/bin/env python3
"""
Create a draft from workspace output via n8n webhook.

Usage:
  python -m scripts.publish --workspace "article_name"
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Dict

from scripts.core import create_draft
from scripts.workspace import ArticleWorkspace


def _save_json(path: Path, payload: Dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def _update_meta(ws: ArticleWorkspace, **updates: str) -> None:
    meta = ws.read_meta()
    meta.setdefault("publish", {}).update(updates)
    ws.write_meta(meta)


def main() -> None:
    parser = argparse.ArgumentParser(description="Create WeChat draft via n8n")
    parser.add_argument("--workspace", required=True, help="Workspace name or path")
    parser.add_argument("--title", help="Override draft title")
    parser.add_argument("--author", help="Override author")
    parser.add_argument("--digest", help="Override digest")
    parser.add_argument("--thumb-media-id", help="Override cover media_id")
    parser.add_argument("--source-url", help="Override content source URL")

    args = parser.parse_args()

    ws = ArticleWorkspace.load(args.workspace)
    meta = ws.read_meta()

    if not ws.article_html.exists():
        raise FileNotFoundError(f"Output missing: {ws.article_html}")

    content = ws.article_html.read_text(encoding="utf-8")

    title = args.title or meta.get("title", "Untitled")
    author = args.author or meta.get("author", "")
    digest = args.digest or meta.get("digest", "")
    thumb_media_id = args.thumb_media_id or meta.get("cover", "")
    source_url = args.source_url or meta.get("source_url", "")

    response = create_draft(
        title=title,
        content=content,
        author=author,
        digest=digest,
        thumb_media_id=thumb_media_id,
        content_source_url=source_url,
    )

    result = {
        "workspace": str(ws.path),
        "title": title,
        "created_at": datetime.now().isoformat(),
        "response": response,
    }

    publish_file = ws.publish_dir / "draft.json"
    _save_json(publish_file, result)

    _update_meta(ws, draft_created_at=datetime.now().isoformat())
    print(f"Draft result saved: {publish_file}")


if __name__ == "__main__":
    main()

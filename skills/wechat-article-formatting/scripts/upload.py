#!/usr/bin/env python3
"""
Upload images in a workspace via n8n webhook.

Usage:
  python -m scripts.upload --workspace "article_name"
"""

from __future__ import annotations

import argparse
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from typing import Dict, List

from scripts.config import Config
from scripts.core import upload_image
from scripts.workspace import ArticleWorkspace


def _collect_images(images_dir: Path) -> List[Path]:
    if not images_dir.exists():
        return []
    return [p for p in images_dir.iterdir() if p.is_file()]


def _save_json(path: Path, payload: Dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def _update_meta(ws: ArticleWorkspace, **updates: str) -> None:
    meta = ws.read_meta()
    meta.setdefault("publish", {}).update(updates)
    ws.write_meta(meta)


def main() -> None:
    parser = argparse.ArgumentParser(description="Upload workspace images via n8n")
    parser.add_argument("--workspace", required=True, help="Workspace name or path")
    parser.add_argument("--material-type", help="Override material type")
    parser.add_argument("--max-concurrent", type=int, help="Override concurrent uploads")

    args = parser.parse_args()

    ws = ArticleWorkspace.load(args.workspace)
    config = Config()

    images = _collect_images(ws.images_dir)
    if not images:
        print("No images found.")
        return

    max_workers = args.max_concurrent or config.max_concurrent
    results = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_map = {
            executor.submit(upload_image, str(path), args.material_type or config.material_type): path
            for path in images
        }
        for future in as_completed(future_map):
            path = future_map[future]
            try:
                response = future.result()
                success = bool(response.get("success", True))
                results.append(
                    {
                        "file": path.name,
                        "path": str(path),
                        "success": success,
                        "response": response,
                        "uploaded_at": datetime.now().isoformat(),
                    }
                )
                print(f"{path.name}: {'OK' if success else 'FAILED'}")
            except Exception as exc:
                results.append(
                    {
                        "file": path.name,
                        "path": str(path),
                        "success": False,
                        "error": str(exc),
                        "uploaded_at": datetime.now().isoformat(),
                    }
                )
                print(f"{path.name}: ERROR {exc}")

    output = {
        "workspace": str(ws.path),
        "count": len(results),
        "results": results,
    }
    publish_file = ws.publish_dir / "images.json"
    _save_json(publish_file, output)

    _update_meta(ws, images_uploaded_at=datetime.now().isoformat())
    print(f"Saved upload map: {publish_file}")


if __name__ == "__main__":
    main()

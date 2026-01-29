#!/usr/bin/env python3
"""
Workspace manager for WeChat articles.

Usage:
  python -m scripts.workspace init "Article Title"
  python -m scripts.workspace status <article_name>
  python -m scripts.workspace list
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List

from scripts.config import get_articles_dir


@dataclass
class ArticleWorkspace:
    path: Path

    @property
    def meta_file(self) -> Path:
        return self.path / "meta.json"

    @property
    def source_dir(self) -> Path:
        return self.path / "source"

    @property
    def images_dir(self) -> Path:
        return self.source_dir / "images"

    @property
    def output_dir(self) -> Path:
        return self.path / "output"

    @property
    def publish_dir(self) -> Path:
        return self.path / "publish"

    @property
    def article_md(self) -> Path:
        return self.source_dir / "article.md"

    @property
    def article_html(self) -> Path:
        return self.output_dir / "article.html"

    # --------- Factory ---------

    @classmethod
    def create(cls, title: str) -> "ArticleWorkspace":
        articles_dir = get_articles_dir()
        articles_dir.mkdir(parents=True, exist_ok=True)

        date_str = datetime.now().strftime("%Y-%m-%d")
        safe_title = "".join(c if c.isalnum() or c in "-_" else "_" for c in title)
        safe_title = safe_title[:50] or "article"
        dir_name = f"{date_str}_{safe_title}"

        workspace_path = articles_dir / dir_name
        counter = 1
        while workspace_path.exists():
            workspace_path = articles_dir / f"{dir_name}_{counter}"
            counter += 1

        ws = cls(workspace_path)
        ws._init_structure(title)
        return ws

    @classmethod
    def load(cls, name_or_path: str) -> "ArticleWorkspace":
        path = Path(name_or_path)
        if not path.is_absolute():
            articles_dir = get_articles_dir()
            exact = articles_dir / name_or_path
            if exact.exists():
                path = exact
            else:
                matches = list(articles_dir.glob(f"*{name_or_path}*"))
                if len(matches) == 1:
                    path = matches[0]
                elif len(matches) > 1:
                    raise ValueError("Multiple matches:\n" + "\n".join(f"- {m.name}" for m in matches))
                else:
                    raise ValueError(f"Workspace not found: {name_or_path}")

        ws = cls(path)
        if not ws.meta_file.exists():
            raise ValueError(f"Invalid workspace (missing meta.json): {path}")
        return ws

    @classmethod
    def list_all(cls) -> List["ArticleWorkspace"]:
        articles_dir = get_articles_dir()
        if not articles_dir.exists():
            return []
        return [cls(d) for d in sorted(articles_dir.iterdir(), reverse=True) if (d / "meta.json").exists()]

    # --------- Operations ---------

    def read_meta(self) -> Dict[str, str]:
        return json.loads(self.meta_file.read_text(encoding="utf-8"))

    def write_meta(self, meta: Dict[str, str]) -> None:
        meta["updated_at"] = datetime.now().isoformat()
        self.meta_file.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    def status(self) -> Dict[str, bool]:
        return {
            "has_source": self.article_md.exists(),
            "has_images": self.images_dir.exists() and any(self.images_dir.iterdir()),
            "has_output": self.article_html.exists(),
            "has_publish": self.publish_dir.exists(),
        }

    def _init_structure(self, title: str) -> None:
        self.source_dir.mkdir(parents=True, exist_ok=True)
        self.images_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.publish_dir.mkdir(parents=True, exist_ok=True)

        meta = {
            "title": title,
            "author": "",
            "digest": "",
            "cover": "",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "status": "draft",
            "tags": [],
        }
        self.write_meta(meta)

        if not self.article_md.exists():
            self.article_md.write_text(
                f"# {title}\n\n在此编写文章内容...\n",
                encoding="utf-8",
            )


# ============ CLI ============


def _cmd_init(args: argparse.Namespace) -> None:
    ws = ArticleWorkspace.create(args.title)
    print(f"Workspace created: {ws.path}")


def _cmd_list(_: argparse.Namespace) -> None:
    workspaces = ArticleWorkspace.list_all()
    if not workspaces:
        print("No workspaces found.")
        return
    for ws in workspaces:
        meta = ws.read_meta()
        print(f"- {ws.path.name} | {meta.get('title', '')}")


def _cmd_status(args: argparse.Namespace) -> None:
    ws = ArticleWorkspace.load(args.workspace)
    meta = ws.read_meta()
    status = ws.status()
    print(f"Workspace: {ws.path}")
    print(f"Title: {meta.get('title', '')}")
    for key, value in status.items():
        print(f"{key}: {value}")


def main() -> None:
    parser = argparse.ArgumentParser(description="WeChat article workspace manager")
    sub = parser.add_subparsers(dest="command")

    init_parser = sub.add_parser("init", help="Create a new workspace")
    init_parser.add_argument("title", help="Article title")
    init_parser.set_defaults(func=_cmd_init)

    list_parser = sub.add_parser("list", help="List all workspaces")
    list_parser.set_defaults(func=_cmd_list)

    status_parser = sub.add_parser("status", help="Show workspace status")
    status_parser.add_argument("workspace", help="Workspace name or path")
    status_parser.set_defaults(func=_cmd_status)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

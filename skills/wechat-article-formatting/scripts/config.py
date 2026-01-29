#!/usr/bin/env python3
"""
Configuration manager for WeChat article workspace.
"""

from __future__ import annotations

import json
import os
import shutil
from pathlib import Path
from typing import Any, Dict, Optional


# ============ Path helpers ============


def _find_project_root(start: Path) -> Path:
    """Find the nearest project root from start."""
    markers = [".git", "pnpm-workspace.yaml", "AGENTS.md", "package.json"]
    current = start.resolve()
    for parent in [current, *current.parents]:
        if any((parent / marker).exists() for marker in markers):
            return parent
    return current


def get_workspace_root() -> Path:
    """Get workspace root (current project root)."""
    if env_root := os.environ.get("WECHAT_WORKSPACE_ROOT"):
        return Path(env_root).resolve()
    return _find_project_root(Path.cwd())


def get_wechat_dir() -> Path:
    """Get .wechat directory."""
    return get_workspace_root() / ".wechat"


def get_config_path() -> Path:
    """Get config file path."""
    return get_wechat_dir() / "config.json"


def get_template_path() -> Path:
    """Get config template path in workspace."""
    return get_wechat_dir() / "config.template.json"


def get_articles_dir() -> Path:
    """Get articles directory."""
    return get_wechat_dir() / "articles"


def get_scripts_dir() -> Path:
    """Get scripts directory for bundled templates."""
    return Path(__file__).resolve().parent


# ============ Config class ============


class Config:
    """Configuration loader and validator."""

    def __init__(self, config_path: Optional[Path] = None) -> None:
        self.config_path = config_path or get_config_path()
        self._config: Dict[str, Any] = {}
        self._load()

    def _load(self) -> None:
        if not self.config_path.exists():
            raise FileNotFoundError(
                "Config file not found: {path}\n"
                "Run: python -m scripts.config init".format(path=self.config_path)
            )

        self._config = json.loads(self.config_path.read_text(encoding="utf-8"))
        self._validate()

    def _validate(self) -> None:
        required = [
            ("n8n.base_url", "n8n base URL"),
            ("n8n.webhooks.upload_image", "upload image webhook"),
            ("n8n.webhooks.create_draft", "create draft webhook"),
        ]

        for path, name in required:
            if not self._get_nested(path):
                raise ValueError(f"Missing config field: {name} ({path})")

        auth_type = self._get_nested("n8n.auth.type") or "none"
        if auth_type not in {"none", "basic", "header"}:
            raise ValueError("Invalid auth type: {auth_type}".format(auth_type=auth_type))

    def _get_nested(self, path: str) -> Any:
        value: Any = self._config
        for key in path.split("."):
            if isinstance(value, dict):
                value = value.get(key)
            else:
                return None
        return value

    # ============ Accessors ============

    @property
    def n8n_base_url(self) -> str:
        return str(self._config["n8n"]["base_url"]).rstrip("/")

    @property
    def webhook_upload_image(self) -> str:
        return str(self._config["n8n"]["webhooks"]["upload_image"])

    @property
    def webhook_create_draft(self) -> str:
        return str(self._config["n8n"]["webhooks"]["create_draft"])

    @property
    def auth_type(self) -> str:
        return str(self._config["n8n"]["auth"].get("type", "none"))

    @property
    def auth_headers(self) -> Dict[str, str]:
        auth = self._config["n8n"]["auth"]
        auth_type = auth.get("type", "none")

        if auth_type == "none":
            return {}

        if auth_type == "basic":
            import base64

            username = auth.get("basic", {}).get("username", "")
            password = auth.get("basic", {}).get("password", "")
            credentials = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("utf-8")
            return {"Authorization": f"Basic {credentials}"}

        if auth_type == "header":
            header_name = auth.get("header", {}).get("name", "")
            header_value = auth.get("header", {}).get("value", "")
            if header_name:
                return {header_name: header_value}
            return {}

        return {}

    @property
    def timeout(self) -> int:
        return int(self._config.get("n8n", {}).get("timeout", 60))

    @property
    def default_author(self) -> str:
        return str(self._config.get("wechat", {}).get("default_author", ""))

    @property
    def default_source_url(self) -> str:
        return str(self._config.get("wechat", {}).get("default_source_url", ""))

    @property
    def material_type(self) -> str:
        return str(self._config.get("upload", {}).get("material_type", "permanent"))

    @property
    def max_concurrent(self) -> int:
        return int(self._config.get("upload", {}).get("max_concurrent", 3))

    @property
    def retry_times(self) -> int:
        return int(self._config.get("upload", {}).get("retry_times", 3))


# ============ Init command ============


def init_workspace() -> None:
    """Initialize workspace config and folders."""
    wechat_dir = get_wechat_dir()
    articles_dir = get_articles_dir()
    config_path = get_config_path()
    template_path = get_template_path()

    wechat_dir.mkdir(parents=True, exist_ok=True)
    articles_dir.mkdir(parents=True, exist_ok=True)

    scripts_dir = get_scripts_dir()
    source_template = scripts_dir / "templates" / "config.template.json"

    if source_template.exists():
        shutil.copy(source_template, template_path)
        print(f"Template created: {template_path}")
    else:
        print(f"Template missing: {source_template}")

    if not config_path.exists():
        if template_path.exists():
            shutil.copy(template_path, config_path)
            print(f"Config created: {config_path}")
            print("Please edit config.json and fill n8n settings.")
        else:
            print("Template not found; cannot create config.json")
    else:
        print(f"Config already exists: {config_path}")

    gitignore_path = get_workspace_root() / ".gitignore"
    gitignore_entry = ".wechat/config.json"

    if gitignore_path.exists():
        content = gitignore_path.read_text(encoding="utf-8")
        if gitignore_entry not in content:
            print("Add to .gitignore:")
            print(f"  {gitignore_entry}")
    else:
        print("Create .gitignore and add:")
        print(f"  {gitignore_entry}")

    print("Workspace:")
    print(f"  {wechat_dir}/")
    print("  ├── config.json")
    print("  ├── config.template.json")
    print("  └── articles/")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "init":
        init_workspace()
    else:
        print("Usage: python -m scripts.config init")

#!/usr/bin/env python3
"""
Core helpers for calling n8n webhooks.
"""

from __future__ import annotations

import base64
import json
from pathlib import Path
from typing import Any, Dict, Optional
from urllib import request, error

from scripts.config import Config


MAX_IMAGE_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}

_config: Optional[Config] = None


def get_config() -> Config:
    global _config
    if _config is None:
        _config = Config()
    return _config


# ============ Utilities ============


def image_to_base64(image_path: str) -> str:
    path = Path(image_path)
    if not path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    if path.suffix.lower() not in ALLOWED_EXTENSIONS:
        raise ValueError(f"Unsupported image format: {path.suffix}")

    size = path.stat().st_size
    if size > MAX_IMAGE_SIZE:
        raise ValueError(f"Image too large: {size / 1024 / 1024:.2f}MB > 10MB")

    return base64.b64encode(path.read_bytes()).decode("utf-8")


def _post_json(url: str, payload: Dict[str, Any], headers: Dict[str, str], timeout: int) -> Dict[str, Any]:
    data = json.dumps(payload).encode("utf-8")
    req = request.Request(url, data=data, headers=headers, method="POST")

    try:
        with request.urlopen(req, timeout=timeout) as response:
            body = response.read().decode("utf-8")
            if not body:
                return {"success": True, "data": None}
            return json.loads(body)
    except error.HTTPError as exc:
        return {"success": False, "error": f"HTTP {exc.code}: {exc.reason}"}
    except error.URLError as exc:
        return {"success": False, "error": str(exc.reason)}
    except json.JSONDecodeError:
        return {"success": False, "error": "Invalid JSON response"}


def call_n8n_webhook(endpoint: str, payload: Dict[str, Any], timeout: Optional[int] = None) -> Dict[str, Any]:
    config = get_config()
    url = f"{config.n8n_base_url}{endpoint}"
    timeout = timeout or config.timeout

    headers = {
        "Content-Type": "application/json",
        **config.auth_headers,
    }

    retry_times = config.retry_times
    last_error: Optional[str] = None

    for attempt in range(retry_times):
        result = _post_json(url, payload, headers, timeout)
        if result.get("success", True):
            return result
        last_error = result.get("error", "Unknown error")

        if attempt < retry_times - 1:
            import time

            time.sleep(2 ** attempt)

    return {"success": False, "error": last_error}


# ============ Core features ============


def upload_image(image_path: str, material_type: Optional[str] = None) -> Dict[str, Any]:
    config = get_config()
    material_type = material_type or config.material_type

    image_base64 = image_to_base64(image_path)
    filename = Path(image_path).name

    payload = {
        "image": image_base64,
        "filename": filename,
        "type": material_type,
    }

    return call_n8n_webhook(config.webhook_upload_image, payload)


def create_draft(
    title: str,
    content: str,
    author: str = "",
    digest: str = "",
    thumb_media_id: str = "",
    content_source_url: str = "",
) -> Dict[str, Any]:
    config = get_config()

    if not author:
        author = config.default_author

    if not content_source_url:
        content_source_url = config.default_source_url

    payload = {
        "title": title,
        "content": content,
        "author": author,
        "digest": digest,
        "thumb_media_id": thumb_media_id,
        "content_source_url": content_source_url,
    }

    return call_n8n_webhook(config.webhook_create_draft, payload, timeout=120)

---
name: 自动发布流程
description: 基于工作区自动上传图片并创建公众号草稿
---

# 自动发布流程

上传图片与创建草稿由 CLI 脚本触发，结果写入 `publish/` 目录以便追踪。

## Usage

### 上传图片

```bash
python -m scripts.upload --workspace "文章标题"
```

成功后会生成 `publish/images.json`，记录每张图的响应结果。

### 创建草稿

```bash
python -m scripts.publish --workspace "文章标题"
```

脚本会读取 `output/article.html` 作为正文，并写入 `publish/draft.json`。

### 可选覆盖参数

```bash
python -m scripts.publish \
  --workspace "文章标题" \
  --author "作者" \
  --digest "摘要" \
  --thumb-media-id "MEDIA_ID"
```

## Key Points

- 建议先上传图片，再创建草稿，避免正文中的图片缺失。
- `meta.json` 中的 `author`、`digest`、`cover` 会作为默认值。
- 发布结果默认保存在 `publish/` 目录，便于审计与重试。

<!--
Source references:
- scripts/wechat-n8n-integration-3.md
-->

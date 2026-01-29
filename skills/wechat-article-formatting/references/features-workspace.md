---
name: 工作区管理
description: 用项目根目录的 .wechat/articles 管理文章生命周期与元数据
---

# 工作区管理

该工作区将每篇文章的素材、输出与发布记录集中在 `.wechat/articles/` 下，方便自动化脚本统一读取与写入。

## 目录结构

```text
.wechat/
└── articles/
    └── 2026-01-29_文章标题/
        ├── meta.json
        ├── source/
        │   ├── article.md
        │   └── images/
        ├── output/
        │   └── article.html
        └── publish/
            ├── images.json
            └── draft.json
```

## Usage

### 初始化工作区

```bash
# 建议在项目根目录执行
python -m scripts.workspace init "文章标题"
```

### 查看工作区状态

```bash
python -m scripts.workspace status "文章标题"
```

### 列出所有文章

```bash
python -m scripts.workspace list
```

## Key Points

- `meta.json` 保存作者、摘要、封面 media_id 等元数据，可被发布脚本复用。
- `source/` 存放原始 Markdown 与图片素材，`output/` 存放排版后的 HTML。
- `publish/` 记录上传结果和草稿创建结果，便于追溯。
- 工作区根目录默认自动探测项目根（`.git` 或 `AGENTS.md`）。必要时可设置 `WECHAT_WORKSPACE_ROOT`。

<!--
Source references:
- scripts/wechat-n8n-integration-3.md
-->

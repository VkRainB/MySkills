# 微信公众号 n8n 工作流集成规划 v4

> 创建时间：2026-01-29
> 迭代版本：v4 (工作区调整 + 配置模板)
> 状态：待确认

## 📋 确认事项

| 项目 | 确认内容 |
|------|----------|
| n8n 部署方式 | ✅ 自托管 |
| 公众号类型 | ✅ 订阅号（需认证） |
| 优先级 | ✅ 先实现图片上传 |
| 脚本实现 | ✅ Python 脚本调用 n8n 工作流 |
| 工作区管理 | ✅ 引入工作区概念 |
| **工作区位置** | ✅ 当前项目根目录 |
| **配置管理** | ✅ config.json 存放 n8n 鉴权配置 |

## 目标定义

为 `wechat-article-formatting` 技能添加 **工作区 + n8n 工作流集成**：

1. **配置管理**：统一的 config.json 管理 n8n 连接和鉴权
2. **工作区管理**：在项目根目录下管理文章排版生命周期
3. **图片资源上传**：从工作区上传图片到微信素材库
4. **草稿自动发布**：基于工作区内容创建公众号草稿

## 核心概念：工作区 (Workspace)

### 设计调整

- **工作区根目录** = 当前打开的项目根目录
- **配置目录**：`.wechat/` 存放配置和文章
- **配置文件**：`config.json` 管理 n8n 鉴权（应加入 .gitignore）
- **配置模板**：`config.template.json` 作为交付物

### 工作区目录结构

```
project/                                # 当前项目根目录 = 工作区
│
├── .wechat/                            # 📁 微信公众号工作目录
│   │
│   ├── config.json                     # 🔐 n8n 配置（用户填写，gitignore）
│   ├── config.template.json            # 📄 配置模板（交付物）
│   │
│   └── articles/                       # 📚 文章工作目录
│       │
│       └── 2026-01-29_文章标题/        # 单篇文章目录
│           ├── meta.json               # 文章元数据
│           ├── source/                 # 📥 原始素材
│           │   ├── article.md          # 原始 Markdown
│           │   └── images/             # 原始图片
│           ├── output/                 # 📤 排版输出
│           │   └── article.html        # 公众号格式 HTML
│           └── publish/                # 📡 发布状态
│               ├── images.json         # 图片上传映射
│               └── draft.json          # 草稿发布记录
│
├── .gitignore                          # 添加 .wechat/config.json
└── ...项目其他文件
```

## 配置文件设计

### config.json 结构

```json
{
  "$schema": "./config.schema.json",
  "version": "1.0",

  "n8n": {
    "base_url": "http://localhost:5678",
    "webhooks": {
      "upload_image": "/webhook/wechat-upload-image",
      "create_draft": "/webhook/wechat-create-draft"
    },
    "auth": {
      "type": "none",
      "basic": {
        "username": "",
        "password": ""
      },
      "header": {
        "name": "X-N8N-API-KEY",
        "value": ""
      }
    },
    "timeout": 60
  },

  "wechat": {
    "account_name": "我的公众号",
    "default_author": "",
    "default_source_url": ""
  },

  "upload": {
    "material_type": "permanent",
    "max_concurrent": 3,
    "retry_times": 3
  }
}
```

### 配置字段说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| **n8n.base_url** | string | ✅ | n8n 实例地址 |
| **n8n.webhooks.upload_image** | string | ✅ | 图片上传 Webhook 路径 |
| **n8n.webhooks.create_draft** | string | ✅ | 草稿创建 Webhook 路径 |
| **n8n.auth.type** | string | ✅ | 鉴权类型: `none` / `basic` / `header` |
| n8n.auth.basic.username | string | 条件 | Basic Auth 用户名 |
| n8n.auth.basic.password | string | 条件 | Basic Auth 密码 |
| n8n.auth.header.name | string | 条件 | Header 鉴权的 Header 名称 |
| n8n.auth.header.value | string | 条件 | Header 鉴权的 Header 值 |
| n8n.timeout | number | - | 请求超时时间（秒），默认 60 |
| wechat.account_name | string | - | 公众号名称（用于显示） |
| wechat.default_author | string | - | 默认作者名 |
| upload.material_type | string | - | 素材类型: `permanent` / `temporary` |
| upload.max_concurrent | number | - | 最大并发上传数 |
| upload.retry_times | number | - | 失败重试次数 |

### config.template.json（交付物）

```json
{
  "$schema": "./config.schema.json",
  "version": "1.0",

  "_注释": "请复制此文件为 config.json 并填写配置",

  "n8n": {
    "base_url": "http://localhost:5678",
    "webhooks": {
      "upload_image": "/webhook/wechat-upload-image",
      "create_draft": "/webhook/wechat-create-draft"
    },
    "auth": {
      "_说明": "鉴权类型: none=无鉴权, basic=用户名密码, header=自定义Header",
      "type": "none",
      "basic": {
        "username": "",
        "password": ""
      },
      "header": {
        "name": "X-N8N-API-KEY",
        "value": ""
      }
    },
    "timeout": 60
  },

  "wechat": {
    "account_name": "填写你的公众号名称",
    "default_author": "填写默认作者名",
    "default_source_url": ""
  },

  "upload": {
    "material_type": "permanent",
    "max_concurrent": 3,
    "retry_times": 3
  }
}
```

### n8n 鉴权类型说明

#### 1. 无鉴权 (type: "none")

适用于内网/本地部署，无需额外配置：

```json
{
  "n8n": {
    "auth": {
      "type": "none"
    }
  }
}
```

#### 2. Basic Auth (type: "basic")

n8n 开启 Basic Auth 时使用：

```json
{
  "n8n": {
    "auth": {
      "type": "basic",
      "basic": {
        "username": "admin",
        "password": "your-password"
      }
    }
  }
}
```

n8n 配置（docker-compose.yml）：
```yaml
environment:
  - N8N_BASIC_AUTH_ACTIVE=true
  - N8N_BASIC_AUTH_USER=admin
  - N8N_BASIC_AUTH_PASSWORD=your-password
```

#### 3. Header 鉴权 (type: "header")

使用自定义 Header 鉴权（推荐用于生产环境）：

```json
{
  "n8n": {
    "auth": {
      "type": "header",
      "header": {
        "name": "X-N8N-API-KEY",
        "value": "your-secret-api-key"
      }
    }
  }
}
```

n8n 工作流中验证 Header：
```javascript
// 在 Webhook 节点后添加 IF 节点
$input.first().headers['x-n8n-api-key'] === 'your-secret-api-key'
```

## 脚本架构设计

### 目录结构

```
skills/wechat-article-formatting/
├── SKILL.md                              # 技能索引（更新）
├── references/
│   ├── ...existing files...
│   ├── features-workspace.md             # 工作区使用指南（新增）
│   ├── features-n8n-integration.md       # n8n 集成指南（新增）
│   └── features-auto-publish.md          # 自动发布流程（新增）
└── scripts/
    ├── __init__.py                       # 模块初始化
    ├── core.py                           # 核心配置和 n8n 调用
    ├── config.py                         # 配置管理
    ├── workspace.py                      # 工作区管理
    ├── upload.py                         # CLI：图片上传
    ├── publish.py                        # CLI：草稿发布
    ├── templates/                        # 📦 配置模板（交付物）
    │   ├── config.template.json          # 配置模板
    │   └── config.schema.json            # 配置 JSON Schema
    └── n8n-workflows/                    # 📦 n8n 工作流模板
        ├── README.md                     # 工作流导入说明
        ├── image-upload.json             # 图片上传工作流
        └── create-draft.json             # 草稿创建工作流
```

## 脚本详细设计

### config.py - 配置管理

```python
#!/usr/bin/env python3
"""
配置管理模块

负责加载和验证 .wechat/config.json
"""

import os
import json
import shutil
from pathlib import Path
from typing import Optional, Dict, Any

# ============ 路径常量 ============

def get_workspace_root() -> Path:
    """获取工作区根目录（当前项目根目录）"""
    # 优先使用环境变量
    if env_root := os.environ.get("WECHAT_WORKSPACE_ROOT"):
        return Path(env_root)
    # 默认使用当前工作目录
    return Path.cwd()

def get_wechat_dir() -> Path:
    """获取 .wechat 目录"""
    return get_workspace_root() / ".wechat"

def get_config_path() -> Path:
    """获取配置文件路径"""
    return get_wechat_dir() / "config.json"

def get_template_path() -> Path:
    """获取配置模板路径"""
    return get_wechat_dir() / "config.template.json"

def get_articles_dir() -> Path:
    """获取文章目录"""
    return get_wechat_dir() / "articles"

# ============ 配置类 ============

class Config:
    """配置管理类"""

    def __init__(self, config_path: Optional[Path] = None):
        self.config_path = config_path or get_config_path()
        self._config: Dict[str, Any] = {}
        self._load()

    def _load(self):
        """加载配置文件"""
        if not self.config_path.exists():
            raise FileNotFoundError(
                f"配置文件不存在: {self.config_path}\n"
                f"请先运行: python -m scripts.config init"
            )

        with open(self.config_path, 'r', encoding='utf-8') as f:
            self._config = json.load(f)

        self._validate()

    def _validate(self):
        """验证配置"""
        required = [
            ("n8n.base_url", "n8n 实例地址"),
            ("n8n.webhooks.upload_image", "图片上传 Webhook 路径"),
            ("n8n.webhooks.create_draft", "草稿创建 Webhook 路径"),
        ]

        for path, name in required:
            if not self._get_nested(path):
                raise ValueError(f"配置缺失: {name} ({path})")

    def _get_nested(self, path: str) -> Any:
        """获取嵌套配置值"""
        value = self._config
        for key in path.split('.'):
            if isinstance(value, dict):
                value = value.get(key)
            else:
                return None
        return value

    # ============ 配置访问器 ============

    @property
    def n8n_base_url(self) -> str:
        return self._config["n8n"]["base_url"].rstrip('/')

    @property
    def webhook_upload_image(self) -> str:
        return self._config["n8n"]["webhooks"]["upload_image"]

    @property
    def webhook_create_draft(self) -> str:
        return self._config["n8n"]["webhooks"]["create_draft"]

    @property
    def auth_type(self) -> str:
        return self._config["n8n"]["auth"].get("type", "none")

    @property
    def auth_headers(self) -> Dict[str, str]:
        """获取鉴权 Headers"""
        auth = self._config["n8n"]["auth"]
        auth_type = auth.get("type", "none")

        if auth_type == "none":
            return {}

        elif auth_type == "basic":
            import base64
            username = auth["basic"]["username"]
            password = auth["basic"]["password"]
            credentials = base64.b64encode(f"{username}:{password}".encode()).decode()
            return {"Authorization": f"Basic {credentials}"}

        elif auth_type == "header":
            header_name = auth["header"]["name"]
            header_value = auth["header"]["value"]
            return {header_name: header_value}

        return {}

    @property
    def timeout(self) -> int:
        return self._config["n8n"].get("timeout", 60)

    @property
    def default_author(self) -> str:
        return self._config.get("wechat", {}).get("default_author", "")

    @property
    def material_type(self) -> str:
        return self._config.get("upload", {}).get("material_type", "permanent")

    @property
    def retry_times(self) -> int:
        return self._config.get("upload", {}).get("retry_times", 3)


# ============ 初始化命令 ============

def init_workspace():
    """初始化工作区配置"""
    wechat_dir = get_wechat_dir()
    articles_dir = get_articles_dir()
    config_path = get_config_path()
    template_path = get_template_path()

    # 创建目录
    wechat_dir.mkdir(exist_ok=True)
    articles_dir.mkdir(exist_ok=True)

    # 复制配置模板
    scripts_dir = Path(__file__).parent
    source_template = scripts_dir / "templates" / "config.template.json"

    if source_template.exists():
        shutil.copy(source_template, template_path)
        print(f"✅ 配置模板已创建: {template_path}")

    # 创建示例配置（如果不存在）
    if not config_path.exists():
        if template_path.exists():
            shutil.copy(template_path, config_path)
            print(f"✅ 配置文件已创建: {config_path}")
            print(f"   ⚠️ 请编辑配置文件，填写 n8n 连接信息")
        else:
            print(f"❌ 模板文件不存在: {source_template}")
    else:
        print(f"ℹ️ 配置文件已存在: {config_path}")

    # 提示添加 .gitignore
    gitignore_path = get_workspace_root() / ".gitignore"
    gitignore_entry = ".wechat/config.json"

    if gitignore_path.exists():
        content = gitignore_path.read_text(encoding='utf-8')
        if gitignore_entry not in content:
            print(f"\n⚠️ 建议将以下内容添加到 .gitignore:")
            print(f"   {gitignore_entry}")
    else:
        print(f"\n⚠️ 建议创建 .gitignore 并添加:")
        print(f"   {gitignore_entry}")

    print(f"\n📁 工作区结构:")
    print(f"   {wechat_dir}/")
    print(f"   ├── config.json          ← 编辑此文件")
    print(f"   ├── config.template.json")
    print(f"   └── articles/            ← 文章目录")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "init":
        init_workspace()
    else:
        print("用法: python -m scripts.config init")
```

### core.py - 更新支持配置

```python
#!/usr/bin/env python3
"""
微信公众号 n8n 工作流调用核心模块
"""

import base64
import requests
from pathlib import Path
from typing import Dict, Any, List, Optional

from .config import Config, get_config_path

# ============ 配置 ============

MAX_IMAGE_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}

# ============ 全局配置实例 ============

_config: Optional[Config] = None

def get_config() -> Config:
    """获取配置实例（延迟加载）"""
    global _config
    if _config is None:
        _config = Config()
    return _config

# ============ 工具函数 ============

def image_to_base64(image_path: str) -> str:
    """将图片文件转换为 Base64 编码"""
    path = Path(image_path)
    if not path.exists():
        raise FileNotFoundError(f"图片文件不存在: {image_path}")

    if path.suffix.lower() not in ALLOWED_EXTENSIONS:
        raise ValueError(f"不支持的图片格式: {path.suffix}")

    size = path.stat().st_size
    if size > MAX_IMAGE_SIZE:
        raise ValueError(f"图片大小超过限制: {size / 1024 / 1024:.2f}MB > 10MB")

    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

def call_n8n_webhook(
    endpoint: str,
    payload: Dict[str, Any],
    timeout: Optional[int] = None
) -> Dict[str, Any]:
    """调用 n8n Webhook 端点"""
    config = get_config()

    url = f"{config.n8n_base_url}{endpoint}"
    timeout = timeout or config.timeout

    headers = {
        "Content-Type": "application/json",
        **config.auth_headers  # 合并鉴权 Headers
    }

    retry_times = config.retry_times
    last_error = None

    for attempt in range(retry_times):
        try:
            response = requests.post(
                url,
                json=payload,
                headers=headers,
                timeout=timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            last_error = "请求超时"
        except requests.exceptions.RequestException as e:
            last_error = str(e)

        if attempt < retry_times - 1:
            import time
            time.sleep(2 ** attempt)  # 指数退避

    return {"success": False, "error": last_error}

# ============ 核心功能 ============

def upload_image(
    image_path: str,
    material_type: Optional[str] = None
) -> Dict[str, Any]:
    """上传图片到微信公众号素材库"""
    config = get_config()
    material_type = material_type or config.material_type

    try:
        image_base64 = image_to_base64(image_path)
        filename = Path(image_path).name

        payload = {
            "image": image_base64,
            "filename": filename,
            "type": material_type
        }

        return call_n8n_webhook(config.webhook_upload_image, payload)
    except Exception as e:
        return {"success": False, "error": str(e)}

def create_draft(
    title: str,
    content: str,
    author: str = "",
    digest: str = "",
    thumb_media_id: str = "",
    content_source_url: str = ""
) -> Dict[str, Any]:
    """创建微信公众号草稿"""
    config = get_config()

    # 使用默认作者（如果未指定）
    if not author:
        author = config.default_author

    payload = {
        "title": title,
        "content": content,
        "author": author,
        "digest": digest,
        "thumb_media_id": thumb_media_id,
        "content_source_url": content_source_url
    }

    return call_n8n_webhook(config.webhook_create_draft, payload, timeout=120)
```

### workspace.py - 更新使用项目根目录

```python
#!/usr/bin/env python3
"""
微信公众号文章工作区管理

工作区位于当前项目根目录的 .wechat/articles/ 下

用法:
    python -m scripts.workspace init "文章标题"
    python -m scripts.workspace status <article_name>
    python -m scripts.workspace list
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional

from .config import get_articles_dir, get_wechat_dir

# ============ 工作区类 ============

class ArticleWorkspace:
    """文章工作区管理"""

    def __init__(self, path: Path):
        self.path = Path(path)
        self.meta_file = self.path / "meta.json"
        self.source_dir = self.path / "source"
        self.images_dir = self.source_dir / "images"
        self.output_dir = self.path / "output"
        self.publish_dir = self.path / "publish"

    @classmethod
    def create(cls, title: str) -> "ArticleWorkspace":
        """创建新文章工作区"""
        articles_dir = get_articles_dir()
        articles_dir.mkdir(parents=True, exist_ok=True)

        # 生成目录名：日期_标题（sanitize）
        date_str = datetime.now().strftime("%Y-%m-%d")
        safe_title = "".join(c if c.isalnum() or c in "-_" else "_" for c in title)
        safe_title = safe_title[:50]  # 限制长度
        dir_name = f"{date_str}_{safe_title}"

        workspace_path = articles_dir / dir_name

        # 如果已存在，添加序号
        counter = 1
        original_path = workspace_path
        while workspace_path.exists():
            workspace_path = original_path.parent / f"{original_path.name}_{counter}"
            counter += 1

        ws = cls(workspace_path)
        ws._init_structure(title)
        return ws

    @classmethod
    def load(cls, name_or_path: str) -> "ArticleWorkspace":
        """加载已有文章工作区"""
        path = Path(name_or_path)

        # 如果是相对名称，在 articles 目录下查找
        if not path.is_absolute():
            articles_dir = get_articles_dir()
            # 精确匹配
            if (articles_dir / name_or_path).exists():
                path = articles_dir / name_or_path
            else:
                # 模糊匹配
                matches = list(articles_dir.glob(f"*{name_or_path}*"))
                if len(matches) == 1:
                    path = matches[0]
                elif len(matches) > 1:
                    raise ValueError(
                        f"找到多个匹配的文章目录:\n" +
                        "\n".join(f"  - {m.name}" for m in matches)
                    )
                else:
                    raise ValueError(f"未找到文章目录: {name_or_path}")

        ws = cls(path)
        if not ws.meta_file.exists():
            raise ValueError(f"无效的文章目录（缺少 meta.json）: {path}")
        return ws

    @classmethod
    def list_all(cls) -> list:
        """列出所有文章工作区"""
        articles_dir = get_articles_dir()
        if not articles_dir.exists():
            return []

        workspaces = []
        for d in sorted(articles_dir.iterdir(), reverse=True):
            if d.is_dir() and (d / "meta.json").exists():
                workspaces.append(cls(d))
        return workspaces

    def _init_structure(self, title: str):
        """初始化工作区目录结构"""
        self.source_dir.mkdir(parents=True)
        self.images_dir.mkdir()
        self.output_dir.mkdir()
        self.publish_dir.mkdir()

        meta = {
            "title": title,
            "author": "",
            "digest": "",
            "cover": "",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "status": "draft",
            "tags": []
        }
        self._save_json(self.meta_file, meta)

        # 创建空的 article.md
        (self.source_dir / "article.md").write_text(
            f"# {title}\n\n在此编写文章内容...\n",
            encoding="utf-8"
        )

    # ... 其余方法与 v3 相同 ...
```

## 交付物清单

### 阶段 1 交付物（完整列表）

| 类型 | 文件 | 说明 |
|------|------|------|
| **配置模板** | `scripts/templates/config.template.json` | n8n 配置模板 |
| **配置 Schema** | `scripts/templates/config.schema.json` | 配置验证 Schema |
| **Python 脚本** | `scripts/__init__.py` | 模块初始化 |
| **Python 脚本** | `scripts/config.py` | 配置管理 |
| **Python 脚本** | `scripts/core.py` | n8n 调用核心 |
| **Python 脚本** | `scripts/workspace.py` | 工作区管理 |
| **Python 脚本** | `scripts/upload.py` | 图片上传 CLI |
| **n8n 工作流** | `scripts/n8n-workflows/image-upload.json` | 图片上传工作流 |
| **n8n 工作流** | `scripts/n8n-workflows/README.md` | 工作流说明 |
| **参考文档** | `references/features-workspace.md` | 工作区指南 |
| **参考文档** | `references/features-n8n-integration.md` | n8n 集成指南 |
| **技能索引** | `SKILL.md` | 更新功能引用 |

### 配置模板详情

#### config.template.json

```json
{
  "$schema": "./config.schema.json",
  "version": "1.0",

  "_说明": "请复制此文件为 config.json 并填写配置",
  "_文档": "参考 references/features-n8n-integration.md",

  "n8n": {
    "base_url": "http://localhost:5678",
    "webhooks": {
      "upload_image": "/webhook/wechat-upload-image",
      "create_draft": "/webhook/wechat-create-draft"
    },
    "auth": {
      "_说明": "鉴权类型: none=无鉴权, basic=用户名密码, header=自定义Header",
      "type": "none",
      "basic": {
        "username": "",
        "password": ""
      },
      "header": {
        "name": "X-N8N-API-KEY",
        "value": ""
      }
    },
    "timeout": 60
  },

  "wechat": {
    "account_name": "填写你的公众号名称",
    "default_author": "填写默认作者名",
    "default_source_url": ""
  },

  "upload": {
    "_素材类型": "permanent=永久素材, temporary=临时素材(3天有效)",
    "material_type": "permanent",
    "max_concurrent": 3,
    "retry_times": 3
  }
}
```

#### config.schema.json

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "微信公众号 n8n 配置",
  "type": "object",
  "required": ["version", "n8n"],
  "properties": {
    "version": {
      "type": "string",
      "description": "配置版本"
    },
    "n8n": {
      "type": "object",
      "required": ["base_url", "webhooks", "auth"],
      "properties": {
        "base_url": {
          "type": "string",
          "description": "n8n 实例地址",
          "examples": ["http://localhost:5678", "https://n8n.example.com"]
        },
        "webhooks": {
          "type": "object",
          "required": ["upload_image", "create_draft"],
          "properties": {
            "upload_image": {"type": "string"},
            "create_draft": {"type": "string"}
          }
        },
        "auth": {
          "type": "object",
          "required": ["type"],
          "properties": {
            "type": {
              "type": "string",
              "enum": ["none", "basic", "header"]
            },
            "basic": {
              "type": "object",
              "properties": {
                "username": {"type": "string"},
                "password": {"type": "string"}
              }
            },
            "header": {
              "type": "object",
              "properties": {
                "name": {"type": "string"},
                "value": {"type": "string"}
              }
            }
          }
        },
        "timeout": {
          "type": "integer",
          "default": 60
        }
      }
    },
    "wechat": {
      "type": "object",
      "properties": {
        "account_name": {"type": "string"},
        "default_author": {"type": "string"},
        "default_source_url": {"type": "string"}
      }
    },
    "upload": {
      "type": "object",
      "properties": {
        "material_type": {
          "type": "string",
          "enum": ["permanent", "temporary"],
          "default": "permanent"
        },
        "max_concurrent": {"type": "integer", "default": 3},
        "retry_times": {"type": "integer", "default": 3}
      }
    }
  }
}
```

## 使用示例

### 初始化配置

```bash
# 在项目根目录执行
python -m scripts.config init
```

输出：
```
✅ 配置模板已创建: .wechat/config.template.json
✅ 配置文件已创建: .wechat/config.json
   ⚠️ 请编辑配置文件，填写 n8n 连接信息

⚠️ 建议将以下内容添加到 .gitignore:
   .wechat/config.json

📁 工作区结构:
   .wechat/
   ├── config.json          ← 编辑此文件
   ├── config.template.json
   └── articles/            ← 文章目录
```

### 完整工作流

```bash
# 1. 初始化配置（首次）
python -m scripts.config init
# 编辑 .wechat/config.json 填写 n8n 地址

# 2. 创建文章工作区
python -m scripts.workspace init "Claude Code 使用指南"

# 3. 准备素材
# - 编辑 .wechat/articles/2026-01-29_Claude_Code_使用指南/source/article.md
# - 添加图片到 source/images/

# 4. Claude 排版 → 生成 output/article.html

# 5. 上传图片
python -m scripts.upload --workspace "Claude_Code"

# 6. 创建草稿
python -m scripts.publish --workspace "Claude_Code"
```

## 验收标准

### 配置管理验收

- [ ] `config init` 正确创建 .wechat 目录结构
- [ ] 配置模板包含完整字段和说明
- [ ] 配置 Schema 可用于 IDE 验证
- [ ] 无鉴权/Basic Auth/Header 三种鉴权方式都能正确工作
- [ ] 配置缺失时给出明确错误提示

### 工作区验收

- [ ] 工作区创建在项目根目录的 .wechat/articles/ 下
- [ ] 文章名称支持中文（转换为拼音/安全字符）
- [ ] 同名文章自动添加序号

### 功能验收

- [ ] 图片上传使用配置中的 n8n 地址和鉴权
- [ ] 失败自动重试（根据 retry_times 配置）
- [ ] 超时使用配置中的 timeout 值

---

## 下一步

规划已更新：

1. ✅ 工作区位置：当前项目根目录 `.wechat/`
2. ✅ 配置管理：`config.json` + `config.template.json`
3. ✅ 鉴权支持：none / basic / header 三种方式
4. ✅ 交付物清单：完整定义

**确认后，我将开始执行阶段 1 的实施任务。**

---

*请确认更新后的规划内容，或提出进一步修改意见。*

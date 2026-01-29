---
name: n8n 集成
description: 使用 config.json 管理 n8n Webhook 与鉴权配置
---

# n8n 集成

通过统一的 `config.json` 管理 n8n 实例、Webhook 路径与鉴权方式，脚本会自动读取并带上鉴权 Header。

## Usage

### 初始化配置

```bash
python -m scripts.config init
```

会在项目根目录生成 `.wechat/config.json` 与 `.wechat/config.template.json`。

### 配置示例

```json
{
  "n8n": {
    "base_url": "http://localhost:5678",
    "webhooks": {
      "upload_image": "/webhook/wechat-upload-image",
      "create_draft": "/webhook/wechat-create-draft"
    },
    "auth": {
      "type": "header",
      "header": {
        "name": "X-N8N-API-KEY",
        "value": "your-secret"
      }
    }
  }
}
```

### 鉴权类型

- `none`：本地或内网无需鉴权
- `basic`：n8n Basic Auth
- `header`：自定义 Header 鉴权（推荐生产环境）

## Key Points

- 配置文件位置固定为 `.wechat/config.json`，建议加入 `.gitignore`。
- `config.schema.json` 可用于 IDE 提示与校验。
- 脚本自动合并鉴权 Header 并统一超时与重试策略。

<!--
Source references:
- scripts/wechat-n8n-integration-3.md
-->

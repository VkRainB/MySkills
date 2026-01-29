---
name: n8n 配置步骤
description: 配置 n8n Webhook 与鉴权的完整中文流程
---

# n8n 配置步骤

本节说明如何在 n8n 中创建 Webhook 工作流，并将参数写入 `.wechat/config.json`。

## 前置条件

- 已有可访问的 n8n 实例（本地或服务器）
- 你有权限创建/启用 Workflow

## 步骤 1：创建 Webhook 工作流

### 1.1 图片上传工作流

1. 新建 Workflow，添加 **Webhook** 节点
2. 配置：
   - HTTP Method：`POST`
   - Path：`wechat-upload-image`
   - Response：`Respond immediately`
3. 在后续节点调用你的“图片上传”服务（公众号素材上传接口或自研服务）
4. 末尾添加 **Respond to Webhook** 节点，返回 JSON

**推荐返回结构：**

```json
{
  "success": true,
  "media_id": "MEDIA_ID",
  "url": "https://..."
}
```

### 1.2 草稿创建工作流

1. 新建 Workflow，添加 **Webhook** 节点
2. 配置：
   - HTTP Method：`POST`
   - Path：`wechat-create-draft`
   - Response：`Respond immediately`
3. 调用草稿创建接口（公众号草稿箱 API 或中间服务）
4. 末尾添加 **Respond to Webhook** 节点返回 JSON

**推荐返回结构：**

```json
{
  "success": true,
  "draft_id": "DRAFT_ID"
}
```

## 步骤 2：配置鉴权方式

### 2.1 无鉴权（本地/内网）

- 不配置鉴权即可访问 Webhook
- `config.json` 设置：

```json
{
  "n8n": { "auth": { "type": "none" } }
}
```

### 2.2 Basic Auth

- n8n 服务开启 Basic Auth
- `config.json` 设置：

```json
{
  "n8n": {
    "auth": {
      "type": "basic",
      "basic": { "username": "admin", "password": "your-password" }
    }
  }
}
```

### 2.3 Header 鉴权（推荐生产环境）

- 在 Webhook 后添加 IF 节点，校验 Header
- 示例条件：`{{$json.headers['x-n8n-api-key'] === 'your-secret'}}`
- `config.json` 设置：

```json
{
  "n8n": {
    "auth": {
      "type": "header",
      "header": { "name": "X-N8N-API-KEY", "value": "your-secret" }
    }
  }
}
```

## 步骤 3：更新本地配置

执行初始化：

```bash
python -m scripts.config init
```

编辑 `.wechat/config.json`：

- `n8n.base_url`：你的 n8n 地址，例如 `http://localhost:5678`
- `n8n.webhooks.upload_image`：`/webhook/wechat-upload-image`
- `n8n.webhooks.create_draft`：`/webhook/wechat-create-draft`
- `n8n.auth`：根据实际鉴权填写

## 步骤 4：联调验证

```bash
# 上传图片
python -m scripts.upload --workspace "文章标题"

# 创建草稿
python -m scripts.publish --workspace "文章标题"
```

验证 `publish/images.json` 与 `publish/draft.json` 返回内容。

## Key Points

- Webhook Path 必须与 `config.json` 完全一致。
- Workflow 必须启用（Active），否则 Webhook 不可用。
- 建议使用 Header 鉴权，并在 n8n 中添加校验节点。

<!--
Source references:
- scripts/wechat-n8n-integration-3.md
-->

# Skills 格式指南

本文档详细解读 Agent Skills 的文件格式和结构设计。

## 概述

Skills 采用**三层结构设计**：

```
skills/{project}/
├── SKILL.md              # 索引文件（必需）
├── GENERATION.md         # Type 1 追踪元数据
├── SYNC.md               # Type 2 追踪元数据
└── references/           # 具体技能文件
    ├── core-*.md
    ├── features-*.md
    ├── best-practices-*.md
    └── advanced-*.md
```

**设计理念：**
- 面向 AI Agent 优化，不是文档的简单复制
- 为 LLM 消费重新组织的结构化知识
- 使用 YAML Frontmatter 标准化元数据

---

## 1. 索引文件：SKILL.md

这是技能的**入口文件**，定义了整个技能的目录结构。

### 格式模板

```markdown
---
name: nuxt                           # 技能标识符（kebab-case）
description: Nuxt is a Vue.js...     # 简短描述
metadata:
  author: Anthony Fu                 # 作者
  version: "2026.1.28"              # 版本号（日期格式）
  source: Generated from ...         # 来源说明
---

Nuxt is a full-stack Vue framework...  # 概述段落

## Core                                 # 分类标题
| Topic | Description | Reference |    # 表格格式的技能索引
|-------|-------------|-----------|
| Routing | File-based routing... | [core-routing](references/core-routing.md) |

## Features                             # 另一个分类
| Topic | Description | Reference |
|-------|-------------|-----------|
| Composables | Vue APIs, utilities... | [features-composables](references/features-composables.md) |

## Best Practices                       # 最佳实践分类
| Topic | Description | Reference |
|-------|-------------|-----------|
| SSR | Avoiding hydration issues... | [best-practices-ssr](references/best-practices-ssr.md) |
```

### 实际示例（Nuxt）

```markdown
---
name: nuxt
description: Nuxt is a Vue.js framework for building full-stack web applications with SSR, auto-imports, file-based routing, and hybrid rendering
metadata:
  author: Anthony Fu
  version: "2026.1.28"
  source: Generated from https://github.com/nuxt/nuxt, scripts located at https://github.com/antfu/skills
---

Nuxt is a full-stack Vue framework that provides server-side rendering, file-based routing, auto-imports, and a powerful module system. It uses Nitro as its server engine for universal deployment across Node.js, serverless, and edge platforms.

## Core

| Topic | Description | Reference |
|-------|-------------|-----------|
| Directory Structure | Project folder structure, conventions, file organization | [core-directory-structure](references/core-directory-structure.md) |
| Configuration | nuxt.config.ts, app.config.ts, runtime config, environment variables | [core-config](references/core-config.md) |
| CLI Commands | Dev server, build, generate, preview, and utility commands | [core-cli](references/core-cli.md) |
| Routing | File-based routing, dynamic routes, navigation, middleware, layouts | [core-routing](references/core-routing.md) |
| Data Fetching | useFetch, useAsyncData, $fetch, caching, refresh | [core-data-fetching](references/core-data-fetching.md) |
| Modules | Creating and using Nuxt modules, Nuxt Kit utilities | [core-modules](references/core-modules.md) |
| Deployment | Platform-agnostic deployment with Nitro, Vercel, Netlify, Cloudflare | [core-deployment](references/core-deployment.md) |

## Features

| Topic | Description | Reference |
|-------|-------------|-----------|
| Composables Auto-imports | Vue APIs, Nuxt composables, custom composables, utilities | [features-composables](references/features-composables.md) |
| Components Auto-imports | Component naming, lazy loading, hydration strategies | [features-components-autoimport](references/features-components-autoimport.md) |
| Built-in Components | NuxtLink, NuxtPage, NuxtLayout, ClientOnly, and more | [features-components](references/features-components.md) |
| State Management | useState composable, SSR-friendly state, Pinia integration | [features-state](references/features-state.md) |
| Server Routes | API routes, server middleware, Nitro server engine | [features-server](references/features-server.md) |

## Best Practices

| Topic | Description | Reference |
|-------|-------------|-----------|
| Data Fetching Patterns | Efficient fetching, caching, parallel requests, error handling | [best-practices-data-fetching](references/best-practices-data-fetching.md) |
| SSR & Hydration | Avoiding context leaks, hydration mismatches, composable patterns | [best-practices-ssr](references/best-practices-ssr.md) |

## Advanced

| Topic | Description | Reference |
|-------|-------------|-----------|
| Layers | Extending applications with reusable layers | [advanced-layers](references/advanced-layers.md) |
| Lifecycle Hooks | Build-time, runtime, and server hooks | [advanced-hooks](references/advanced-hooks.md) |
| Module Authoring | Creating publishable Nuxt modules with Nuxt Kit | [advanced-module-authoring](references/advanced-module-authoring.md) |
```

### 设计原则

- 使用**表格**组织技能列表，方便 AI 快速定位
- 按**类别分组**（Core、Features、Advanced 等）
- 每个技能有 **Topic | Description | Reference** 三列
- 表格结构让 AI Agent 可以快速扫描并定位需要的技能

---

## 2. 参考文件：references/*.md

这是具体的技能内容文件。

### 格式模板

```markdown
---
name: Routing                          # 技能名称
description: File-based routing...      # 简短描述
---

# Routing                              # 标题

简要介绍这个技能涵盖的内容。

## Usage                               # 使用方法
代码示例和实用模式。

## Key Points                          # 关键点
- 重要细节 1
- 重要细节 2

<!--
Source references:                      # 源文档引用（HTML注释）
- https://example.com/docs/...
-->
```

### 实际示例（core-routing.md）

```markdown
---
name: Routing
description: File-based routing, dynamic routes, navigation, and middleware in Nuxt
---

# Routing

Nuxt uses file-system routing based on vue-router. Files in `app/pages/` automatically create routes.

## Basic Routing

```
pages/
├── index.vue      → /
├── about.vue      → /about
└── posts/
    ├── index.vue  → /posts
    └── [id].vue   → /posts/:id
```

## Dynamic Routes

Use brackets for dynamic segments:

```
pages/
├── users/
│   └── [id].vue       → /users/:id
├── posts/
│   └── [...slug].vue  → /posts/* (catch-all)
└── [[optional]].vue   → /:optional? (optional param)
```

Access route parameters:

```vue
<script setup lang="ts">
const route = useRoute()
// /posts/123 → route.params.id = '123'
console.log(route.params.id)
</script>
```

## Navigation

### NuxtLink Component

```vue
<template>
  <nav>
    <NuxtLink to="/">Home</NuxtLink>
    <NuxtLink to="/about">About</NuxtLink>
    <NuxtLink :to="{ name: 'posts-id', params: { id: 1 } }">Post 1</NuxtLink>
  </nav>
</template>
```

NuxtLink automatically prefetches linked pages when they enter the viewport.

### Programmatic Navigation

```vue
<script setup lang="ts">
const router = useRouter()

function goToPost(id: number) {
  navigateTo(`/posts/${id}`)
  // or
  router.push({ name: 'posts-id', params: { id } })
}
</script>
```

## Route Middleware

### Named Middleware

```ts
// middleware/auth.ts
export default defineNuxtRouteMiddleware((to, from) => {
  const isAuthenticated = false // Your auth logic

  if (!isAuthenticated) {
    return navigateTo('/login')
  }
})
```

Apply to pages:

```vue
<script setup lang="ts">
definePageMeta({
  middleware: 'auth',
  // or multiple: middleware: ['auth', 'admin']
})
</script>
```

### Global Middleware

Name files with `.global` suffix:

```ts
// middleware/logging.global.ts
export default defineNuxtRouteMiddleware((to, from) => {
  console.log('Navigating to:', to.path)
})
```

## Layouts

Define layouts in `app/layouts/`:

```vue
<!-- layouts/default.vue -->
<template>
  <div>
    <header>Header</header>
    <slot />
    <footer>Footer</footer>
  </div>
</template>
```

Use in pages:

```vue
<script setup lang="ts">
definePageMeta({
  layout: 'admin',
})
</script>
```

<!--
Source references:
- https://nuxt.com/docs/getting-started/routing
- https://nuxt.com/docs/directory-structure/app/pages
- https://nuxt.com/docs/directory-structure/app/middleware
-->
```

### 设计原则

- **代码优先**：每个概念都配有可运行的代码示例
- **结构清晰**：使用 H2 标题分隔不同主题
- **源引用在注释中**：不干扰阅读，但保留溯源能力
- AI 在生成代码时会参考示例模式，好的示例 = 好的代码生成质量

---

## 3. 追踪文件

### GENERATION.md（Type 1 生成型技能）

用于追踪生成来源，便于后续更新：

```markdown
# Generation Info

- **Source:** `sources/nuxt`
- **Git SHA:** `c9fed804b9bef362276033b03ca43730c6efa7dc`
- **Generated:** 2026-01-28
```

**作用：** 可以精确知道技能基于哪个版本生成，便于检测上游更新并增量同步。

### SYNC.md（Type 2 同步型技能）

用于追踪同步来源：

```markdown
# Sync Info

- **Source:** `vendor/slidev/skills/slidev`
- **Git SHA:** `abc123...`
- **Synced:** 2026-01-28
```

---

## 4. 文件命名规范

参考文件使用**前缀分类**：

| 前缀 | 含义 | 示例 |
|------|------|------|
| `core-*` | 核心概念 | `core-routing.md`, `core-config.md` |
| `features-*` | 功能特性 | `features-composables.md`, `features-state.md` |
| `best-practices-*` | 最佳实践 | `best-practices-ssr.md`, `best-practices-data-fetching.md` |
| `advanced-*` | 高级用法 | `advanced-hooks.md`, `advanced-layers.md` |

---

## 5. 完整目录结构示例

```
skills/nuxt/
├── SKILL.md                              # 索引入口（必需）
├── GENERATION.md                         # 追踪元数据（Type 1 技能）
└── references/                           # 具体技能文件
    ├── core-routing.md                   # 核心：路由
    ├── core-config.md                    # 核心：配置
    ├── core-data-fetching.md             # 核心：数据获取
    ├── core-directory-structure.md       # 核心：目录结构
    ├── core-cli.md                       # 核心：CLI 命令
    ├── core-modules.md                   # 核心：模块系统
    ├── core-deployment.md                # 核心：部署
    ├── features-composables.md           # 功能：组合式函数
    ├── features-components.md            # 功能：内置组件
    ├── features-components-autoimport.md # 功能：组件自动导入
    ├── features-state.md                 # 功能：状态管理
    ├── features-server.md                # 功能：服务端路由
    ├── best-practices-ssr.md             # 最佳实践：SSR
    ├── best-practices-data-fetching.md   # 最佳实践：数据获取
    ├── advanced-hooks.md                 # 高级：生命周期钩子
    ├── advanced-layers.md                # 高级：层扩展
    └── advanced-module-authoring.md      # 高级：模块开发
```

---

## 6. 技能编写原则

1. **面向 Agent 重写** - 不要逐字复制文档，为 LLM 消费而综合内容
2. **实用性优先** - 聚焦使用模式和代码示例
3. **简洁明了** - 去除冗余，保留关键信息
4. **一个概念一个文件** - 将大主题拆分为独立的技能文件
5. **包含代码** - 始终提供可运行的代码示例
6. **解释原因** - 不仅说明如何使用，还说明何时和为何使用

---

## 7. 三种技能类型

| 类型 | 来源 | 输出 | 追踪文件 |
|------|------|------|----------|
| Type 1: 生成型 | `sources/{project}/docs/` | `skills/{project}/` | `GENERATION.md` |
| Type 2: 同步型 | `vendor/{project}/skills/` | `skills/{output-name}/` | `SYNC.md` |
| Type 3: 手写型 | 手动维护 | `skills/antfu/` | 无 |

---

## 参考资料

- 项目配置：[meta.ts](../meta.ts)
- 生成指南：[AGENTS.md](../AGENTS.md)
- CLI 工具：[scripts/cli.ts](../scripts/cli.ts)

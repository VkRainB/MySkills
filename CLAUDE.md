# CLAUDE.md

这个文件为 Claude Code (claude.ai/code) 在此代码库中工作时提供指导。

## 项目概述

这是一个 **Agent Skills 生成器和技能集合**，用于从开源项目文档生成 AI Agent 技能，并保持它们与上游文档同步。项目包含 Anthony Fu 精心策划的 Web 开发技能集合（Vue、Nuxt、Vite、pnpm 等）。

## 核心架构

### 三种技能类型

项目通过 `meta.ts` 配置管理三种类型的技能：

1. **Type 1: 生成型技能** (`sources/` → `skills/`)
   - 从 OSS 项目文档自动生成
   - 源码：`sources/{project}/docs/`
   - 输出：`skills/{project}/`
   - 示例：vue, nuxt, vite, unocss, pnpm, pinia, tsdown, vitest, vitepress

2. **Type 2: 同步型技能** (`vendor/` → `skills/`)
   - 从已有技能仓库同步
   - 源码：`vendor/{project}/skills/{skill-name}/`
   - 输出：`skills/{output-name}/`
   - 示例：slidev, vueuse-functions, turborepo, vue-best-practices, web-design-guidelines

3. **Type 3: 手写型技能** (`skills/antfu/`)
   - Anthony Fu 手动维护的个人偏好和最佳实践
   - 包含 ESLint 配置、工具链选择、开发规范等

### 目录结构

```
.
├── meta.ts                    # 项目配置：定义所有 submodule 和 vendor
├── scripts/cli.ts             # CLI 工具：管理 submodules 和技能同步
├── instructions/*.md          # 生成指引：针对特定项目的生成说明
│
├── sources/{project}/         # Type 1 源：OSS 项目 git submodules
│   └── docs/                  # 从这里读取文档
│
├── vendor/{project}/          # Type 2 源：已有技能的 git submodules
│   └── skills/{skill-name}/   # 要同步的技能
│
└── skills/{output-name}/      # 输出目录（所有类型的技能）
    ├── SKILL.md              # 技能索引文件
    ├── GENERATION.md         # Type 1 追踪元数据（git SHA）
    ├── SYNC.md               # Type 2 追踪元数据（git SHA）
    └── references/*.md       # 具体的技能文件
```

## 常用命令

### 依赖管理
```bash
pnpm install                   # 安装依赖
nr lint                        # 运行 ESLint 检查
nr lint --fix                  # 自动修复 lint 问题
```

### 技能管理（使用 CLI）
```bash
nr start                       # 交互式菜单
nr start init                  # 初始化新的 submodules
nr start init -y               # 跳过确认直接初始化
nr start sync                  # 同步所有 vendor 技能（Type 2）
nr start check                 # 检查 submodules 更新
nr start cleanup               # 清理未使用的 submodules 和技能
```

### Git Submodule 操作
```bash
git submodule update --init --recursive   # 初始化并更新所有 submodules
git submodule update --remote --merge     # 拉取 submodules 的最新更改
```

## 如何阅读和理解项目

### 1. 从入口开始
- **README.md**：项目介绍和使用说明
- **meta.ts**：核心配置，定义所有技能来源
- **AGENTS.md**：技能生成的完整工作流指南

### 2. 理解技能结构
查看示例技能以理解格式：
- `skills/antfu/SKILL.md` - 手写技能的索引示例
- `skills/nuxt/SKILL.md` - 生成技能的索引示例
- `skills/nuxt/references/` - 具体技能文件示例

### 3. 理解 CLI 工具
- **scripts/cli.ts**：管理 submodules 和技能同步的主要脚本
  - `initSubmodules()` - 添加新 git submodules
  - `syncSubmodules()` - 同步 vendor 技能到 skills/
  - `checkUpdates()` - 检查上游更新
  - `cleanup()` - 清理未使用的资源

## 如何编写自己的技能

### 快速流程

1. **Fork 并配置**
   ```bash
   git clone <your-fork>
   pnpm install
   ```

2. **更新 meta.ts**
   - 添加到 `submodules` 对象（Type 1）或 `vendors` 对象（Type 2）

3. **初始化源码**
   ```bash
   nr start init -y              # 克隆新的 submodules
   nr start sync                 # 同步 vendor 技能
   ```

4. **生成技能**（Type 1）
   - 阅读 `sources/{project}/docs/` 中的文档
   - 阅读 `instructions/{project}.md`（如果存在）
   - 在 `skills/{project}/references/` 中创建技能文件
   - 创建 `SKILL.md` 索引文件
   - 创建 `GENERATION.md` 追踪文件

### 技能编写原则

参考 `AGENTS.md` 中的详细指南：

1. **面向 Agent 重写** - 不要逐字复制文档，为 LLM 消费而综合内容
2. **实用性优先** - 聚焦使用模式和代码示例
3. **简洁明了** - 去除冗余，保留关键信息
4. **一个概念一个文件** - 将大主题拆分为独立的技能文件
5. **包含代码** - 始终提供可运行的代码示例
6. **解释原因** - 不仅说明如何使用，还说明何时和为何使用

### 技能文件格式

#### SKILL.md（索引文件）
```markdown
---
name: {kebab-case-name}
description: {简短描述}
metadata:
  author: Anthony Fu
  version: "2026.1.1"
  source: Generated from {source-url}
---

> 此技能基于 {project} v{version}，生成于 {date}。

## Core References
| Topic | Description | Reference |
|-------|-------------|-----------|
| ... | ... | [link](references/core-*.md) |

## Features
...
```

#### references/*.md（具体技能）
```markdown
---
name: {name}
description: {description}
---

# {概念名称}

简要描述这个技能涵盖的内容。

## Usage
代码示例和实用模式。

## Key Points
- 重要细节 1
- 重要细节 2

<!--
Source references:
- {source-url}
-->
```

### 技能分类规范

为 references 文件名添加类别前缀：
- `core-*` - 核心概念
- `features-*` - 功能特性
- `best-practices-*` - 最佳实践
- `advanced-*` - 高级用法

## 更新技能

### Type 1（生成型技能）
1. 检查自上次同步以来的 git diff：
   ```bash
   cd sources/{project}
   git diff {old-sha}..HEAD -- docs/
   ```
2. 根据变更更新受影响的技能文件
3. 更新 `SKILL.md` 中的版本和技能表
4. 更新 `GENERATION.md` 中的 SHA

### Type 2（同步型技能）
1. 检查自上次同步以来的 git diff：
   ```bash
   cd vendor/{project}
   git diff {old-sha}..HEAD -- skills/{skill-name}/
   ```
2. 运行 `nr start sync` 自动复制更改
3. `SYNC.md` 会自动更新

**注意**：不要手动修改同步的技能，应该向上游项目贡献更改。

## 技术栈

- **包管理器**：pnpm（启用 workspaces）
- **语言**：TypeScript（ESM 模式）
- **Linting**：@antfu/eslint-config（无 Prettier）
- **Git Hooks**：simple-git-hooks + lint-staged
- **CLI**：@clack/prompts（交互式提示）

## 重要约定

1. **不要直接编辑 submodules** - 它们是只读的源
2. **Type 2 技能不可修改** - 向上游贡献
3. **始终更新追踪文件** - GENERATION.md 或 SYNC.md 中的 SHA
4. **遵循 meta.ts** - 它是真相的唯一来源
5. **技能名称使用 kebab-case** - 例如 `core-routing`、`features-composables`

## 故障排除

- **Submodule 未初始化**：运行 `git submodule update --init --recursive`
- **Submodule 过时**：运行 `nr start sync` 或 `git submodule update --remote`
- **多余的技能/submodules**：运行 `nr start cleanup`
- **ESLint 错误**：运行 `nr lint --fix`

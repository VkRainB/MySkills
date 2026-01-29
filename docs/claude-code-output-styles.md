# Claude Code Output Styles 输出风格

## 概述

Output Styles（输出风格）是 Claude Code 插件系统中的一类特殊插件，用于**自定义 Claude 的响应方式**。通过安装不同的输出风格插件，可以改变 Claude 与你交互时的表达方式，使其更适合特定的使用场景。

## 官方提供的输出风格

目前 Anthropic 官方 marketplace 提供了两种输出风格插件：

| 插件名称 | 用途 |
|---------|------|
| `explanatory-output-style` | 教育性输出风格 - 提供关于实现选择的深入解释和见解 |
| `learning-output-style` | 学习模式输出风格 - 交互式学习模式，专为技能培养设计 |

### 1. Explanatory Output Style（解释性输出风格）

这个风格会让 Claude 在回答时：
- 解释**为什么**选择某种实现方式
- 提供关于技术决策的教育性见解
- 帮助你理解代码背后的设计思路

**适用场景**：
- 学习新技术或框架
- 理解最佳实践的原因
- 代码审查和重构

### 2. Learning Output Style（学习输出风格）

这个风格会让 Claude：
- 采用交互式的教学方式
- 逐步引导你理解概念
- 注重技能培养而非直接给出答案

**适用场景**：
- 学习编程基础
- 培养解决问题的能力
- 教育性编程练习

## 如何安装输出风格插件

### 方法一：通过命令行安装

```shell
# 安装解释性输出风格
/plugin install explanatory-output-style@claude-plugins-official

# 安装学习输出风格
/plugin install learning-output-style@claude-plugins-official
```

### 方法二：通过交互式界面安装

1. 在 Claude Code 中运行 `/plugin` 命令
2. 切换到 **Discover** 标签页
3. 找到想要的输出风格插件
4. 选择安装范围（User/Project/Local）

## 安装范围说明

| 范围 | 说明 |
|-----|------|
| **User** | 为你个人安装，在所有项目中生效 |
| **Project** | 为项目安装，所有协作者共享（添加到 `.claude/settings.json`）|
| **Local** | 仅为你在当前仓库中安装，不与他人共享 |

## 管理已安装的输出风格

### 查看已安装的插件

```shell
/plugin
# 然后切换到 Installed 标签页
```

### 禁用/启用插件

```shell
# 禁用（不卸载）
/plugin disable explanatory-output-style@claude-plugins-official

# 重新启用
/plugin enable explanatory-output-style@claude-plugins-official
```

### 卸载插件

```shell
/plugin uninstall explanatory-output-style@claude-plugins-official
```

## 工作原理

Output Styles 插件通过 Claude Code 的插件系统工作：

1. **Skills（技能）**：定义 Claude 应该如何响应
2. **配置注入**：修改 Claude 的系统提示词或行为模式
3. **即时生效**：安装后立即改变 Claude 的输出方式

## 注意事项

- 一次可以安装多个输出风格插件，但它们可能会相互影响
- 如果输出效果不理想，可以随时禁用或卸载
- 官方 marketplace 的插件会自动更新（默认启用 auto-update）
- 安装前请确保你信任插件来源

## 版本要求

- Claude Code 版本 **1.0.33** 或更高版本
- 如果 `/plugin` 命令无法识别，请先更新 Claude Code：
  - Homebrew: `brew upgrade claude-code`
  - npm: `npm update -g @anthropic-ai/claude-code`

## 相关链接

- [Claude Code 插件文档](https://code.claude.com/docs/en/discover-plugins)
- [创建自定义插件](https://code.claude.com/docs/en/plugins)
- [插件参考手册](https://code.claude.com/docs/en/plugins-reference)

---

> 文档基于 Claude Code 官方文档整理，更新于 2026-01-28

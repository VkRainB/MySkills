# 微信公众号排版技能安装指南

本文档介绍如何将 `wechat-article-formatting` 技能安装到 Claude Code 中。

## 技能概述

| 属性 | 值 |
|------|------|
| 名称 | `wechat-article-formatting` |
| 描述 | 微信公众号文章排版指南，涵盖字体样式、布局结构、图片处理、样式组件和移动端适配最佳实践 |
| 版本 | 2026.1.28 |
| 类型 | 手写技能 |

## 安装位置选择

Claude Code 支持两种安装位置：

| 安装类型 | 路径 | 适用范围 |
|----------|------|----------|
| **个人级**（推荐） | `~/.claude/skills/wechat-article-formatting/` | 你的所有项目都可用 |
| **项目级** | `<项目根目录>/.claude/skills/wechat-article-formatting/` | 仅当前项目可用 |

### 路径说明

- **Windows 个人级路径**：`C:\Users\<你的用户名>\.claude\skills\wechat-article-formatting\`
- **macOS/Linux 个人级路径**：`~/.claude/skills/wechat-article-formatting/`

## 安装步骤

### 方法一：手动复制（推荐）

#### Windows 用户

```powershell
# 1. 创建目标目录
mkdir -p "$env:USERPROFILE\.claude\skills\wechat-article-formatting\references"

# 2. 复制技能文件（假设当前在 skills 仓库根目录）
Copy-Item -Recurse "skills\wechat-article-formatting\*" "$env:USERPROFILE\.claude\skills\wechat-article-formatting\"
```

或使用 CMD：

```cmd
:: 1. 创建目标目录
mkdir "%USERPROFILE%\.claude\skills\wechat-article-formatting\references"

:: 2. 复制技能文件
xcopy /E /I "skills\wechat-article-formatting\*" "%USERPROFILE%\.claude\skills\wechat-article-formatting\"
```

#### macOS/Linux 用户

```bash
# 1. 创建目标目录
mkdir -p ~/.claude/skills/wechat-article-formatting/references

# 2. 复制技能文件（假设当前在 skills 仓库根目录）
cp -r skills/wechat-article-formatting/* ~/.claude/skills/wechat-article-formatting/
```

### 方法二：符号链接（适合开发者）

如果你想保持技能与仓库同步更新：

#### Windows（管理员权限）

```powershell
# 创建符号链接
New-Item -ItemType SymbolicLink `
  -Path "$env:USERPROFILE\.claude\skills\wechat-article-formatting" `
  -Target "F:\new_project_up\Skills\skills\skills\wechat-article-formatting"
```

#### macOS/Linux

```bash
# 创建符号链接
ln -s /path/to/skills/wechat-article-formatting ~/.claude/skills/wechat-article-formatting
```

## 文件结构

安装后的目录结构应如下：

```
~/.claude/skills/wechat-article-formatting/
├── SKILL.md                              # 技能入口文件（必需）
└── references/                           # 详细参考文档
    ├── core-typography.md                # 排版基础
    ├── core-structure.md                 # 文章结构
    ├── core-images.md                    # 图片处理
    ├── features-components.md            # 样式组件
    ├── features-code-blocks.md           # 代码展示
    ├── features-tools.md                 # 排版工具
    ├── best-practices-mobile.md          # 移动端适配
    ├── best-practices-readability.md     # 可读性优化
    └── best-practices-branding.md        # 品牌一致性
```

## 验证安装

安装完成后，可以通过以下方式验证：

### 1. 检查技能是否被识别

在 Claude Code 中输入：

```
What skills are available?
```

你应该能在列表中看到 `wechat-article-formatting` 技能。

### 2. 直接调用技能

```
/wechat-article-formatting
```

### 3. 自动触发

当你的问题涉及微信公众号排版时，Claude 会自动应用此技能：

```
帮我写一篇关于 Vue 3 的微信公众号文章，注意排版格式
```

## 使用示例

### 示例 1：获取排版建议

```
请按照微信公众号排版规范，帮我优化这篇文章的格式
```

### 示例 2：查看具体规范

```
/wechat-article-formatting 告诉我移动端适配的最佳实践
```

### 示例 3：生成排版模板

```
用微信公众号排版规范，帮我创建一个技术文章的排版模板
```

## 技能内容概览

此技能包含以下知识领域：

### 核心规范
- **排版基础**：字体、字号、行高、颜色、对齐方式
- **文章结构**：标题层级、段落间距、内容分块、视觉节奏
- **图片处理**：图片尺寸、格式选择、封面图设计、图文混排

### 功能组件
- **样式组件**：引用框、分隔线、高亮块、卡片样式
- **代码展示**：代码块样式、语法高亮方案
- **排版工具**：常用编辑器和工具推荐

### 最佳实践
- **移动端适配**：手机屏幕排版优化
- **可读性优化**：提升阅读体验的技巧
- **品牌一致性**：统一视觉风格

## 常见问题

### Q: 技能没有被识别？

1. 检查目录结构是否正确
2. 确保 `SKILL.md` 文件存在且格式正确
3. 重启 Claude Code

### Q: 如何更新技能？

重新执行复制命令覆盖现有文件，或者如果使用符号链接，直接拉取仓库更新即可。

### Q: 如何卸载技能？

删除技能目录即可：

```bash
# macOS/Linux
rm -rf ~/.claude/skills/wechat-article-formatting

# Windows PowerShell
Remove-Item -Recurse -Force "$env:USERPROFILE\.claude\skills\wechat-article-formatting"
```

## 相关资源

- [Claude Code 技能文档](https://docs.anthropic.com/en/docs/claude-code/skills)
- [技能格式指南](./skills-format-guide.md)

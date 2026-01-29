# UI/UX Pro Max SKILL.md 深度解读

## 📋 文档概览

这是一份为 Claude AI 助手设计的 **Skill 配置文件**,用于在 Claude Code 环境中提供 UI/UX 设计智能。文件采用 **YAML Frontmatter + Markdown** 格式,遵循 Claude Skills 规范。

---

## 🏗️ 文件结构分析

### 整体架构

```
┌─────────────────────────────────────────────────┐
│              YAML Frontmatter                    │  ← Skill 元数据
├─────────────────────────────────────────────────┤
│         核心概念 (When to Apply)                 │  ← 触发条件
├─────────────────────────────────────────────────┤
│         规则优先级表 (8个优先级)                  │  ← 系统设计
├─────────────────────────────────────────────────┤
│         快速参考 (Quick Reference)               │  ← 核心规则速查
├─────────────────────────────────────────────────┤
│         环境准备 (Prerequisites)                 │  ← Python 安装
├─────────────────────────────────────────────────┤
│         工作流程 (4步法)                         │  ← 核心使用方法
├─────────────────────────────────────────────────┤
│         搜索参考 (Domains & Stacks)              │  ← 数据库文档
├─────────────────────────────────────────────────┤
│         示例工作流 (Example Workflow)            │  ← 实战案例
├─────────────────────────────────────────────────┤
│         专业规则集 (Common Rules)                │  ← 反模式检查
├─────────────────────────────────────────────────┤
│         交付清单 (Pre-Delivery Checklist)        │  ← 质量保证
└─────────────────────────────────────────────────┘
```

---

## 🎯 第一部分: YAML Frontmatter (Skill 元数据)

### 代码分析

```yaml
---
name: ui-ux-pro-max
description: "UI/UX design intelligence. 50 styles, 21 palettes..."
---
```

### 作用解读

这是 **Claude Skills 系统的索引信息**,相当于技能的"身份证":

#### 1. `name` 字段
- **用途**: Skill 的唯一标识符
- **影响**: Claude 通过这个名字激活和引用该技能
- **命名规范**: 小写+连字符 (kebab-case)

#### 2. `description` 字段 (关键!)
这是整个 Skill 最重要的部分,包含三类信息:

**① 能力声明** (What it can do)
```
50 styles, 21 palettes, 50 font pairings, 20 charts, 9 stacks
```
→ 告诉 Claude 这个 Skill 有多少资源

**② 触发关键词** (When to activate)
```
Actions: plan, build, create, design, implement, review, fix...
Projects: website, landing page, dashboard, admin panel...
Elements: button, modal, navbar, sidebar, card...
Styles: glassmorphism, claymorphism, minimalism...
Topics: color palette, accessibility, animation...
```
→ 当用户消息包含这些词时,Claude 自动激活此 Skill

**③ 集成声明** (Integrations)
```
Integrations: shadcn/ui MCP for component search
```
→ 声明与其他工具(如 MCP)的协同能力

### 设计模式: 关键词云 (Keyword Cloud Pattern)

这种设计非常聪明:
- Claude 在处理用户消息时会扫描 description
- 匹配到关键词 → 自动激活 Skill
- 无需用户显式调用 `/ui-ux-pro-max`

**示例触发场景:**
```
用户: "帮我做一个 SaaS 产品的 landing page"
      ↓ 匹配到: "landing page", "SaaS"
Claude: ✅ 激活 ui-ux-pro-max skill
```

---

## 🎯 第二部分: When to Apply (触发条件)

```markdown
## When to Apply

Reference these guidelines when:
- Designing new UI components or pages
- Choosing color palettes and typography
- Reviewing code for UX issues
- Building landing pages or dashboards
- Implementing accessibility requirements
```

### 作用解读

这是 **人类可读的触发条件说明**,补充了 YAML 的关键词触发机制:

1. **明确使用场景**: 告诉开发者何时应该求助这个 Skill
2. **设定边界**: 暗示不适用的场景(如后端逻辑、算法设计)
3. **引导用户**: 提示用户如何更有效地提问

### 设计思路

遵循 "Show, don't tell" 原则:
- 不说"这是一个 UI 设计工具"
- 而是列举具体的使用场景
- 让用户立刻理解价值

---

## 🎯 第三部分: 规则优先级表 (Rule Categories by Priority)

```markdown
| Priority | Category | Impact | Domain |
|----------|----------|--------|--------|
| 1 | Accessibility | CRITICAL | `ux` |
| 2 | Touch & Interaction | CRITICAL | `ux` |
| 3 | Performance | HIGH | `ux` |
| 4 | Layout & Responsive | HIGH | `ux` |
| 5 | Typography & Color | MEDIUM | `typography`, `color` |
| 6 | Animation | MEDIUM | `ux` |
| 7 | Style Selection | MEDIUM | `style`, `product` |
| 8 | Charts & Data | LOW | `chart` |
```

### 核心设计思想: 分层决策系统

这张表建立了一个 **决策优先级框架**:

#### 1. Priority (优先级层次)
```
Level 1-2: CRITICAL  → 法律/道德要求(可访问性、触控体验)
Level 3-4: HIGH      → 用户体验基础(性能、响应式)
Level 5-6: MEDIUM    → 品牌表达(字体、颜色、动画)
Level 7-8: LOW       → 锦上添花(样式选择、图表美化)
```

**意义**: 当 Claude 面临冲突时,按优先级解决

**示例冲突场景:**
```
用户要求: "用淡灰色文字(好看) + 白色背景"
           ↓
Skill 检测: 违反 Priority 1 (color-contrast 对比度 < 4.5:1)
           ↓
Claude 行为: 拒绝淡灰色,建议深灰色(slate-600),并解释原因
```

#### 2. Impact (影响范围)
- **CRITICAL**: 影响法律合规、可用性
- **HIGH**: 影响核心体验、SEO
- **MEDIUM**: 影响品牌感知
- **LOW**: 影响局部细节

#### 3. Domain (数据域映射)
将优先级映射到具体的数据库表:
- `ux` → `ux_guidelines.csv`
- `typography` → `typography.csv`
- `color` → `colors.csv`
- `style` → `styles.csv`
- `chart` → `charts.csv`

**作用**: 告诉 Claude 应该查询哪个数据库

---

## 🎯 第四部分: Quick Reference (快速参考)

### 结构模式

每个优先级类别都包含:

```markdown
### 1. Accessibility (CRITICAL)

- `color-contrast` - Minimum 4.5:1 ratio for normal text
- `focus-states` - Visible focus rings on interactive elements
- `alt-text` - Descriptive alt text for meaningful images
  ↑           ↑
  规则ID      规则描述
```

### 设计模式: ID + 描述

#### 1. 规则 ID (Rule ID)
- 用反引号包裹: `color-contrast`
- 采用 kebab-case 命名
- 作用: 可被其他部分引用、搜索

#### 2. 规则描述 (Rule Description)
- 简洁明了 (一句话)
- 包含具体数值 (如 "4.5:1", "44x44px")
- 可直接执行

### 核心规则解读

让我挑选几条关键规则深度解读:

#### 🔴 Priority 1: Accessibility (可访问性)

```markdown
- `color-contrast` - Minimum 4.5:1 ratio for normal text
```

**背景**: WCAG 2.1 AA 级标准
**检测方法**: 
```javascript
// 对比度计算公式
const contrast = (L1 + 0.05) / (L2 + 0.05);
// L1 = 较亮颜色的相对亮度
// L2 = 较暗颜色的相对亮度
```

**Claude 的行为**:
1. 生成配色时自动计算对比度
2. 如果 < 4.5:1,拒绝并建议替代色

---

```markdown
- `touch-target-size` - Minimum 44x44px touch targets
```

**背景**: Apple HIG 和 Material Design 标准
**原因**: 人类手指平均触控面积 ≈ 40-48px
**Claude 的行为**:
```css
/* 不合格 */
.button { 
  padding: 4px 8px; /* ❌ 高度 < 44px */
}

/* 合格 */
.button {
  padding: 12px 24px; /* ✅ 高度 ≥ 44px */
  min-height: 44px;
}
```

#### 🟡 Priority 3: Performance (性能)

```markdown
- `image-optimization` - Use WebP, srcset, lazy loading
```

**Claude 的实现**:
```html
<img 
  src="hero.webp"
  srcset="hero-400.webp 400w, hero-800.webp 800w"
  sizes="(max-width: 768px) 100vw, 800px"
  loading="lazy"
  alt="Hero image"
/>
```

---

## 🎯 第五部分: Prerequisites (环境准备)

```markdown
## Prerequisites

Check if Python is installed:
```bash
python3 --version || python --version
```
```

### 作用解读

这个部分是 **环境检测与安装指南**:

#### 1. 为什么需要 Python?

因为核心搜索引擎是用 Python 实现的:
```
skills/ui-ux-pro-max/scripts/
├── search.py          # CLI 入口
├── core.py            # BM25 搜索引擎
└── design_system.py   # 设计系统生成器
```

#### 2. 多平台兼容

提供了 3 个主流操作系统的安装命令:

**macOS** (Homebrew)
```bash
brew install python3
```

**Ubuntu/Debian** (APT)
```bash
sudo apt update && sudo apt install python3
```

**Windows** (winget)
```powershell
winget install Python.Python.3.12
```

### Claude 的行为逻辑

```
用户请求 UI 设计
  ↓
Claude 检测 Python 环境
  ↓
如果未安装
  ↓
显示对应操作系统的安装命令
  ↓
等待用户确认安装完成
  ↓
继续执行 search.py
```

---

## 🎯 第六部分: 工作流程 (4步法)

这是整个 Skill 的**核心操作流程**,定义了 Claude 应该如何使用这个工具。

### Step 1: Analyze User Requirements (需求分析)

```markdown
Extract key information from user request:
- **Product type**: SaaS, e-commerce, portfolio...
- **Style keywords**: minimal, playful, professional...
- **Industry**: healthcare, fintech, gaming...
- **Stack**: React, Vue, Next.js, or default to `html-tailwind`
```

#### 作用: 信息提取与分类

Claude 从用户的自然语言中提取结构化信息:

**示例对话:**
```
用户: "帮我做一个医疗 SaaS 的仪表板,要简洁专业的风格"
      ↓ Claude 提取
Product type: SaaS
Product subtype: Dashboard
Industry: Healthcare
Style keywords: minimal, professional, clean
Stack: (未指定) → 默认 html-tailwind
```

#### 设计模式: 默认值策略

注意 `or default to html-tailwind`:
- 原因: Tailwind CSS 是最通用的技术栈
- 好处: 即使用户不懂技术,也能生成可用代码
- 灵活性: 用户可以随时指定其他栈

---

### Step 2: Generate Design System (设计系统生成)

```markdown
**Always start with `--design-system`** to get comprehensive recommendations

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<product_type> <industry> <keywords>" --design-system [-p "Project Name"]
```
```

#### 核心概念: Design System First

这是整个 Skill 最关键的设计决策:

**为什么强调 "Always start"?**

传统流程 (❌ 不好):
```
用户要求 → 直接写代码 → 发现颜色不统一 → 返工
                      → 发现字体不搭配 → 返工
                      → 发现缺少组件 → 返工
```

Design System First (✅ 好):
```
用户要求 → 生成完整设计系统 → 一次性获得:
                           - 配色方案
                           - 字体配对
                           - 组件样式
                           - 动效规范
         → 基于设计系统写代码 → 一致性保证
```

#### 命令结构解析

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<query>" --design-system [-p "Name"]
         ↑                                        ↑            ↑            ↑
      Python 解释器                          查询字符串    设计系统模式   项目名称
```

**参数说明:**
- `<query>`: 自然语言查询,可包含:
  - 产品类型: "SaaS", "e-commerce"
  - 行业: "healthcare", "fintech"
  - 风格词: "elegant", "playful", "minimal"
  
- `--design-system`: 触发完整设计系统生成
  - 并行搜索 5 个域: product, style, color, landing, typography
  - 应用推理规则 (从 `ui-reasoning.csv`)
  - 返回统一的设计方案

- `-p "Name"`: 项目名称 (可选)
  - 用于持久化存储
  - 影响设计系统文件命名

#### 示例解读

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "beauty spa wellness service" --design-system -p "Serenity Spa"
```

**这条命令会做什么?**

1. **并行搜索 5 个数据库**:
   ```
   products.csv    → 匹配 "beauty", "spa", "wellness", "service"
   styles.csv      → 匹配适合美容行业的风格
   colors.csv      → 匹配 "beauty" 色彩方案
   typography.csv  → 匹配 "elegant", "luxury" 字体
   landing.csv     → 匹配 "service" 类页面结构
   ```

2. **应用推理规则**:
   ```python
   # 从 ui-reasoning.csv 加载规则
   IF industry == "beauty":
       prefer_styles = ["elegant", "minimalism", "soft-gradient"]
       avoid_styles = ["brutalism", "cyberpunk", "dark-mode-primary"]
   ```

3. **生成完整设计系统**:
   ```markdown
   # Design System for Serenity Spa
   
   ## Pattern
   - Product: Beauty & Wellness Service
   - Style: Elegant Minimalism
   
   ## Colors
   - Primary: #F4E4D7 (Warm Beige)
   - Secondary: #8B7355 (Muted Brown)
   - Accent: #DDA15E (Golden)
   
   ## Typography
   - Heading: Cormorant Garamond (serif, elegant)
   - Body: Montserrat (sans-serif, readable)
   
   ## Effects
   - Glassmorphism cards with soft shadows
   - Smooth fade-in animations (300ms)
   - Hover: subtle scale + glow
   
   ## Anti-Patterns to Avoid
   - ❌ Don't use bright neon colors
   - ❌ Don't use harsh shadows
   - ❌ Don't use geometric brutalist shapes
   ```

---

### Step 2b: Persist Design System (设计系统持久化)

```markdown
To save the design system for **hierarchical retrieval across sessions**, add `--persist`:
```

#### 核心概念: Master + Overrides Pattern

这是一个非常先进的设计模式,类似于 CSS 的层叠机制:

**文件结构:**
```
project/
└── design-system/
    ├── MASTER.md              # 全局设计规则 (Source of Truth)
    └── pages/
        ├── dashboard.md       # 仪表板页面覆盖规则
        ├── checkout.md        # 结账页面覆盖规则
        └── profile.md         # 个人资料页面覆盖规则
```

**工作原理:**

1. **MASTER.md**: 全局真相源
   ```markdown
   # Global Design System
   
   ## Colors
   - Primary: #3B82F6 (Blue)
   - Background: #FFFFFF (White)
   
   ## Typography
   - Heading: Inter Bold
   - Body: Inter Regular
   ```

2. **pages/checkout.md**: 页面特定覆盖
   ```markdown
   # Checkout Page Overrides
   
   ## Colors (Override)
   - Primary: #10B981 (Green) # 结账页用绿色表示安全
   - Accent: #FBBF24 (Yellow)  # 突出优惠信息
   
   ## Typography (Inherit from Master)
   ```

3. **层叠查询逻辑**:
   ```python
   def get_design_rules(page_name):
       master = read("design-system/MASTER.md")
       override = read(f"design-system/pages/{page_name}.md")
       
       if override exists:
           return merge(master, override)  # override 优先
       else:
           return master
   ```

#### 使用场景

**场景 1: 多页面一致性**
```
问题: 电商网站有 20 个页面,每个页面都要重新生成设计系统?
解决: 生成一次 MASTER.md,所有页面继承
```

**场景 2: 特殊页面差异化**
```
问题: 首页要品牌感强,而仪表板要功能优先,如何平衡?
解决: MASTER.md 定义品牌色,dashboard.md 覆盖为功能色
```

**场景 3: 跨会话一致性**
```
问题: 今天生成了首页,明天生成仪表板,如何保持风格统一?
解决: 两次都读取同一个 MASTER.md
```

#### Claude 的检索提示

```markdown
**Context-aware retrieval prompt:**
```
I am building the [Page Name] page. Please read design-system/MASTER.md.
Also check if design-system/pages/[page-name].md exists.
If the page file exists, prioritize its rules.
```
```

这个提示词告诉 Claude:
1. 先读取 MASTER.md (建立基线)
2. 检查是否有页面特定文件
3. 如果有,页面规则优先
4. 如果没有,严格遵守 MASTER 规则

---

### Step 3: Supplement with Detailed Searches (补充详细搜索)

```markdown
After getting the design system, use domain searches to get additional details:

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<keyword>" --domain <domain> [-n <max_results>]
```
```

#### 设计思路: 两阶段搜索

**第一阶段** (Step 2): 宽搜索
- 用 `--design-system` 获取全局视图
- 快速确定大方向

**第二阶段** (Step 3): 深搜索
- 用 `--domain` 深入特定领域
- 获取更多备选方案

#### 域搜索表解读

```markdown
| Need | Domain | Example |
|------|--------|---------|
| More style options | `style` | `--domain style "glassmorphism dark"` |
| Chart recommendations | `chart` | `--domain chart "real-time dashboard"` |
| UX best practices | `ux` | `--domain ux "animation accessibility"` |
```

**每个域的用途:**

1. **`style` 域**: 
   - 数据源: `styles.csv` (67 种风格)
   - 用途: 获取更多风格变体
   - 场景: "设计系统给了 minimalism,我想看看 brutalism 是否更合适"

2. **`chart` 域**:
   - 数据源: `charts.csv` (24 种图表)
   - 用途: 数据可视化选择
   - 场景: "我有时间序列数据,应该用折线图还是面积图?"

3. **`ux` 域**:
   - 数据源: `ux_guidelines.csv` (98 条最佳实践)
   - 用途: 检查反模式、优化交互
   - 场景: "我的动画会不会太快?加载状态该怎么处理?"

4. **`typography` 域**:
   - 数据源: `typography.csv` (56 组字体配对)
   - 用途: 探索替代字体
   - 场景: "Inter + Roboto 太常见,有没有更独特的组合?"

5. **`landing` 域**:
   - 数据源: `landing.csv` (页面结构模式)
   - 用途: 页面布局策略
   - 场景: "SaaS landing page 应该包含哪些区块?"

---

### Step 4: Stack Guidelines (技术栈指南)

```markdown
Get implementation-specific best practices. If user doesn't specify a stack, **default to `html-tailwind`**.
```

#### 技术栈选择策略

**默认栈: `html-tailwind`**

**为什么选 Tailwind?**
1. **零配置**: 不需要构建工具
2. **浏览器直接运行**: 可以用 CDN
3. **最小化学习曲线**: 类名即样式
4. **广泛支持**: 可转换为任何框架

**可用栈及其特点:**

| 栈 | 适用场景 | 特点 |
|----|---------|------|
| `html-tailwind` | 静态页面、原型 | 零配置,快速迭代 |
| `react` | SPA、复杂交互 | 组件化,状态管理 |
| `nextjs` | SEO、SSR | 全栈,性能优化 |
| `vue` | 渐进式应用 | 易学,灵活 |
| `svelte` | 高性能应用 | 编译时优化 |
| `swiftui` | iOS 原生 | 声明式 UI |
| `react-native` | 跨平台移动 | 一套代码两端 |
| `flutter` | 高性能移动 | 自绘引擎 |
| `shadcn` | 企业级 Web | 组件库 + Tailwind |
| `jetpack-compose` | Android 原生 | 声明式 UI |

#### 栈特定搜索示例

```bash
# 搜索 React 性能最佳实践
python3 skills/ui-ux-pro-max/scripts/search.py "performance optimization" --stack react

# 可能返回:
# - Use React.memo for expensive components
# - Implement code splitting with lazy()
# - Avoid inline function definitions in JSX
# - Use useCallback for event handlers
```

---

## 🎯 第七部分: Search Reference (搜索参考手册)

### 可用域 (Available Domains)

这个表格是**数据库的使用说明书**:

```markdown
| Domain | Use For | Example Keywords |
|--------|---------|------------------|
| `product` | Product type recommendations | SaaS, e-commerce, portfolio |
| `style` | UI styles, colors, effects | glassmorphism, minimalism |
| `typography` | Font pairings, Google Fonts | elegant, playful, professional |
```

#### 域之间的关系

```
用户查询: "为金融科技 SaaS 设计仪表板"
           ↓
并行搜索多个域:
┌─────────────────────────────────────────┐
│ product domain: fintech + SaaS          │ → 返回: 信任感设计模式
│ style domain: professional + dashboard  │ → 返回: 简洁风格
│ color domain: fintech                   │ → 返回: 蓝色系 (信任色)
│ typography: professional                │ → 返回: Inter + Roboto Mono
│ chart domain: dashboard                 │ → 返回: 折线图、柱状图
└─────────────────────────────────────────┘
           ↓
综合生成设计系统
```

### 可用栈 (Available Stacks)

这个表格定义了**每个栈的知识范围**:

```markdown
| Stack | Focus |
|-------|-------|
| `html-tailwind` | Tailwind utilities, responsive, a11y (DEFAULT) |
| `react` | State, hooks, performance, patterns |
| `nextjs` | SSR, routing, images, API routes |
```

#### 栈知识的组织方式

每个栈对应一个文件: `data/stacks/{stack_name}.md`

**示例: `react.md` 内容结构**
```markdown
# React Best Practices

## State Management
- Use useState for simple state
- Use useReducer for complex state
- Consider Zustand for global state

## Performance
- Wrap expensive components with React.memo
- Use useCallback for functions passed to children
- Implement virtualization for long lists

## Common Pitfalls
- ❌ Don't use index as key
- ❌ Don't mutate state directly
- ❌ Don't forget cleanup in useEffect
```

---

## 🎯 第八部分: Example Workflow (示例工作流)

```markdown
**User request:** "Làm landing page cho dịch vụ chăm sóc da chuyên nghiệp"
```

### 作用: 实战演示

这个部分通过**真实案例**演示完整流程,帮助 Claude 理解如何串联各个步骤。

#### 工作流拆解

**输入**: 越南语请求 "为专业护肤服务做 landing page"

**Step 1: 分析**
```
Product type: Beauty/Spa service
Style keywords: elegant, professional, soft
Industry: Beauty/Wellness
Stack: html-tailwind (默认)
```

**Step 2: 生成设计系统**
```bash
python3 skills/ui-ux-pro-max/scripts/search.py \
  "beauty spa wellness service elegant" \
  --design-system \
  -p "Serenity Spa"
```

→ 返回完整设计系统 (颜色、字体、风格、效果)

**Step 3: 补充搜索** (可选)
```bash
# 检查 UX 最佳实践
python3 skills/ui-ux-pro-max/scripts/search.py \
  "animation accessibility" \
  --domain ux

# 探索其他字体选项
python3 skills/ui-ux-pro-max/scripts/search.py \
  "elegant luxury serif" \
  --domain typography
```

**Step 4: 技术栈指南**
```bash
python3 skills/ui-ux-pro-max/scripts/search.py \
  "layout responsive form" \
  --stack html-tailwind
```

**最终输出**: 综合所有信息,生成 HTML + Tailwind 代码

---

## 🎯 第九部分: Common Rules for Professional UI (专业规则集)

这是整个 Skill 的**质量控制核心**,列举了最容易被忽略的细节。

### 设计模式: 表格化规则

每个表格采用三列结构:

```markdown
| Rule | Do | Don't |
|------|----|----- |
| **No emoji icons** | Use SVG icons | Use emojis like 🎨 🚀 ⚙️ |
```

#### 列结构解读

1. **Rule 列**: 规则名称
   - 加粗显示 (引起注意)
   - 简短命名 (易记忆)

2. **Do 列**: 正确做法
   - 具体可执行
   - 包含工具/库名称

3. **Don't 列**: 错误做法
   - 真实案例
   - 可视化展示 (使用 emoji/代码)

### 关键规则深度解读

#### 🚫 No emoji icons

```markdown
| Rule | Do | Don't |
| **No emoji icons** | Use SVG icons (Heroicons, Lucide) | Use emojis like 🎨 🚀 ⚙️ |
```

**为什么这条规则如此重要?**

1. **跨平台渲染不一致**:
   ```
   iOS:      🚀 (3D, 有光泽)
   Android:  🚀 (2D, 扁平)
   Windows:  🚀 (卡通风格)
   ```
   → 品牌形象失控

2. **无法精确控制**:
   ```css
   /* Emoji 无法做到: */
   .icon {
     color: #3B82F6;      /* ❌ Emoji 不受 color 影响 */
     width: 20px;          /* ❌ Emoji 不受 width 影响 */
     stroke-width: 2px;    /* ❌ Emoji 没有 stroke */
   }
   ```

3. **可访问性问题**:
   ```html
   <!-- ❌ 屏幕阅读器读出: "rocket" -->
   <button>🚀 Launch</button>
   
   <!-- ✅ 屏幕阅读器读出: "Launch" -->
   <button>
     <svg aria-hidden="true">...</svg>
     Launch
   </button>
   ```

**正确做法:**
```jsx
import { Rocket } from 'lucide-react';

<button>
  <Rocket className="w-5 h-5 text-blue-500" />
  Launch
</button>
```

---

#### 🎯 Cursor pointer

```markdown
| Rule | Do | Don't |
| **Cursor pointer** | Add `cursor-pointer` to all clickable | Leave default cursor |
```

**为什么要加 `cursor-pointer`?**

这是 **可交互性暗示** (Affordance):

**不好的例子:**
```html
<div onclick="handleClick()">
  Click me
</div>
<!-- ❌ 鼠标悬停时仍然是箭头,用户不知道可以点击 -->
```

**好的例子:**
```html
<div class="cursor-pointer" onclick="handleClick()">
  Click me
</div>
<!-- ✅ 鼠标悬停变成手型,用户知道可以点击 -->
```

**Tailwind 中的最佳实践:**
```jsx
// 交互元素都应该有 cursor-pointer
<div className="cursor-pointer hover:bg-gray-100">
  Card
</div>

<button className="cursor-pointer">
  Button  {/* button 默认有 cursor-pointer */}
</button>

<a href="#" className="cursor-pointer">
  Link    {/* a 标签默认有 cursor-pointer */}
</a>
```

---

#### 🌓 Light/Dark Mode Contrast (光暗模式对比度)

这个表格解决了一个常见问题:**设计在暗色模式看起来不错,但在亮色模式下完全看不清**。

```markdown
| Rule | Do | Don't |
| **Glass card light mode** | Use `bg-white/80` | Use `bg-white/10` (too transparent) |
| **Text contrast light** | Use `#0F172A` (slate-900) | Use `#94A3B8` (slate-400) |
```

**问题场景:**

很多设计师习惯在暗色模式下设计:
```css
/* 在暗色背景下看起来不错 */
.card {
  background: rgba(255, 255, 255, 0.1); /* 10% 白色 */
  color: #94A3B8; /* Slate-400 灰色文字 */
}
```

但切换到亮色模式:
```css
/* 在亮色背景下完全看不见! */
.card {
  background: rgba(255, 255, 255, 0.1); /* ❌ 几乎透明 */
  color: #94A3B8; /* ❌ 对比度不足 */
}
```

**正确的响应式对比度:**
```css
/* Tailwind 的正确做法 */
.card {
  /* 亮色模式: 80% 不透明白色 */
  @apply bg-white/80 dark:bg-white/10;
  
  /* 亮色模式: 深色文字,暗色模式: 浅色文字 */
  @apply text-slate-900 dark:text-slate-100;
}
```

---

#### 📐 Layout & Spacing (布局与间距)

```markdown
| Rule | Do | Don't |
| **Floating navbar** | Add `top-4 left-4 right-4` | Stick to `top-0 left-0 right-0` |
```

**设计理念: 呼吸空间**

**传统设计** (❌ 拥挤):
```css
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
}
/* 导航条紧贴屏幕边缘,看起来局促 */
```

**现代设计** (✅ 有呼吸感):
```css
.navbar {
  position: fixed;
  top: 1rem;    /* 16px */
  left: 1rem;
  right: 1rem;
}
/* 导航条"浮"在页面上,四周有留白 */
```

**视觉效果对比:**
```
传统:
┌──────────────────────────────┐
│ Navbar (贴边)                 │
├──────────────────────────────┤
│ Content                       │


现代:
┌──────────────────────────────┐
│   ┌────────────────────┐      │  ← 有间距
│   │ Navbar (浮动)       │      │
│   └────────────────────┘      │
│                               │
│ Content                       │
```

---

## 🎯 第十部分: Pre-Delivery Checklist (交付前检查清单)

```markdown
## Pre-Delivery Checklist

Before delivering UI code, verify these items:
```

### 作用: 质量门禁

这是 Claude 在生成代码后的**最后一道防线**,确保不遗漏常见问题。

### 清单结构分析

清单分为 5 个类别:

#### 1. Visual Quality (视觉质量)
```markdown
- [ ] No emojis used as icons (use SVG instead)
- [ ] All icons from consistent icon set (Heroicons/Lucide)
- [ ] Brand logos are correct (verified from Simple Icons)
- [ ] Hover states don't cause layout shift
- [ ] Use theme colors directly (bg-primary) not var() wrapper
```

**最后一项解读:**
```css
/* ❌ 不好: 过度抽象 */
.button {
  background: var(--button-bg);
}

/* ✅ 好: 直接使用 Tailwind 类 */
<button class="bg-primary hover:bg-primary-dark">
```

**原因**: 
- Tailwind 本身就是设计系统
- 过度使用 CSS 变量反而增加复杂度
- 除非需要运行时主题切换,否则不推荐

---

#### 2. Interaction (交互)
```markdown
- [ ] All clickable elements have `cursor-pointer`
- [ ] Hover states provide clear visual feedback
- [ ] Transitions are smooth (150-300ms)
- [ ] Focus states visible for keyboard navigation
```

**交互反馈的三个层次:**

**层次 1: Cursor (最基础)**
```css
.card { cursor: pointer; }
```

**层次 2: Hover (视觉反馈)**
```css
.card:hover {
  background-color: rgba(0, 0, 0, 0.05);
}
```

**层次 3: Transition (流畅性)**
```css
.card {
  transition: background-color 200ms ease;
}
```

---

#### 3. Light/Dark Mode (光暗模式)
```markdown
- [ ] Light mode text has sufficient contrast (4.5:1 minimum)
- [ ] Glass/transparent elements visible in light mode
- [ ] Borders visible in both modes
- [ ] Test both modes before delivery
```

**测试策略:**
```javascript
// 快速切换测试
document.documentElement.classList.toggle('dark');

// 检查对比度
const contrast = checkContrast(textColor, bgColor);
if (contrast < 4.5) {
  console.warn('Contrast ratio too low!');
}
```

---

#### 4. Layout (布局)
```markdown
- [ ] Floating elements have proper spacing from edges
- [ ] No content hidden behind fixed navbars
- [ ] Responsive at 375px, 768px, 1024px, 1440px
- [ ] No horizontal scroll on mobile
```

**断点测试清单:**

| 断点 | 设备 | 要验证的内容 |
|------|------|-------------|
| 375px | iPhone SE | 最小字号 ≥ 16px |
| 768px | iPad | 汉堡菜单 → 完整导航 |
| 1024px | Laptop | 卡片从单列 → 多列 |
| 1440px | Desktop | 内容居中,不要太宽 |

---

#### 5. Accessibility (可访问性)
```markdown
- [ ] All images have alt text
- [ ] Form inputs have labels
- [ ] Color is not the only indicator
- [ ] `prefers-reduced-motion` respected
```

**最后一项示例:**
```css
/* 尊重用户的运动偏好设置 */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

**为什么重要?**
- 前庭障碍患者看到动画会晕眩
- 这是 WCAG 2.1 AA 级要求
- macOS/iOS/Windows 都有此设置

---

## 📊 整体设计哲学总结

### 1. 优先级驱动 (Priority-Driven)
```
Accessibility > Performance > Aesthetics
↑              ↑             ↑
法律要求        用户体验      品牌表达
```

### 2. 搜索优先 (Search-First)
```
不是直接生成 → 而是先搜索最佳实践 → 再基于规则生成
```

### 3. 持久化设计 (Persistent Design)
```
MASTER.md = 单一真相源
pages/*.md = 页面级覆盖
→ 跨会话一致性
```

### 4. 防御式设计 (Defensive Design)
```
生成代码前: 搜索反模式
生成代码后: 运行检查清单
→ 双重质量保证
```

### 5. 渐进式增强 (Progressive Enhancement)
```
基础: html-tailwind (所有浏览器可用)
增强: React/Vue/... (现代浏览器)
→ 兼容性优先
```

---

## 🎓 学习建议

如果你想深入理解这份 Skill:

1. **阅读数据库文件**:
   - `data/styles.csv` - 了解 67 种风格
   - `data/colors.csv` - 学习配色原理
   - `data/ux_guidelines.csv` - 掌握 UX 规则

2. **研究搜索引擎**:
   - `scripts/core.py` - BM25 算法实现
   - `scripts/design_system.py` - 推理规则

3. **实践工作流**:
   - 手动运行 `search.py` 命令
   - 对比 `--design-system` 和 `--domain` 的输出
   - 尝试持久化模式

4. **扩展 Skill**:
   - 添加新的风格到 `styles.csv`
   - 添加新的技术栈到 `data/stacks/`
   - 编写自定义推理规则

---

## 💡 关键洞察

这份 SKILL.md 的成功之处在于:

1. **不是规则手册,而是决策系统**
   - 不是"必须用蓝色"
   - 而是"金融科技推荐蓝色,因为信任"

2. **不是静态文档,而是可执行工具**
   - 每条规则都对应一个 Python 脚本
   - 可以自动搜索、验证、生成

3. **不是完美主义,而是实用主义**
   - 有默认栈 (html-tailwind)
   - 有默认行为 (--design-system)
   - 有防御机制 (checklist)

4. **不是孤立技能,而是生态系统**
   - 集成 MCP (shadcn/ui)
   - 支持多平台 (Cursor, Claude Code)
   - 可持久化 (MASTER + Overrides)

这就是一份**工业级 AI Skill 配置文件**的样子! 🚀

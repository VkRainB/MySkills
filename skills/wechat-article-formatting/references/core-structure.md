---
name: 文章结构
description: 微信公众号文章的标题层级、段落间距、内容分块和视觉节奏设计
---

# 文章结构

良好的文章结构让读者快速获取信息，保持阅读兴趣。本节介绍如何组织公众号文章的层级和节奏。

## 标题层级

公众号文章建议最多使用 3 级标题：

```
文章标题（由公众号后台设置）
├── 一级标题（H2）：主要章节
│   ├── 二级标题（H3）：子章节
│   │   └── 三级标题（加粗文本）：细分内容
│   └── 二级标题（H3）
└── 一级标题（H2）
```

### 标题样式示例

```html
<!-- 一级标题：醒目、有分隔感 -->
<h2 style="
  font-size: 18px;
  font-weight: bold;
  color: #1a1a1a;
  border-left: 4px solid #07c160;
  padding-left: 12px;
  margin: 2.5em 0 1em;
">
  一级标题
</h2>

<!-- 二级标题：次要但清晰 -->
<h3 style="
  font-size: 16px;
  font-weight: bold;
  color: #333;
  margin: 2em 0 0.8em;
">
  二级标题
</h3>

<!-- 三级标题：使用加粗正文 -->
<p style="
  font-size: 15px;
  font-weight: bold;
  color: #333;
  margin: 1.5em 0 0.5em;
">
  三级标题
</p>
```

## 段落间距

### 段落之间

```html
<!-- 推荐：1.5em 的段落间距 -->
<p style="margin-bottom: 1.5em;">第一段内容...</p>
<p style="margin-bottom: 1.5em;">第二段内容...</p>
```

### 标题与正文

```html
<!-- 标题上方留更多空间，下方适当紧凑 -->
<h2 style="margin: 2.5em 0 1em;">标题</h2>
<p style="margin-bottom: 1.5em;">紧跟标题的正文...</p>
```

### 间距参考表

| 元素关系 | 推荐间距 | CSS 示例 |
|----------|----------|----------|
| 段落之间 | 1.5em | `margin-bottom: 1.5em` |
| 一级标题上方 | 2.5em | `margin-top: 2.5em` |
| 一级标题下方 | 1em | `margin-bottom: 1em` |
| 二级标题上方 | 2em | `margin-top: 2em` |
| 二级标题下方 | 0.8em | `margin-bottom: 0.8em` |
| 图片上下 | 1.5-2em | `margin: 1.5em 0` |
| 列表项之间 | 0.5em | `margin-bottom: 0.5em` |

## 内容分块

### 使用分隔线

```html
<!-- 简洁分隔线 -->
<hr style="
  border: none;
  border-top: 1px solid #eee;
  margin: 2em 0;
"/>

<!-- 居中装饰分隔 -->
<p style="text-align: center; color: #ccc; margin: 2em 0;">
  · · ·
</p>

<!-- 图标分隔 -->
<p style="text-align: center; margin: 2em 0;">
  ━━━━━ ✦ ━━━━━
</p>
```

### 使用留白

大量留白让内容更易消化：

```html
<!-- 重要内容前后增加留白 -->
<div style="margin: 3em 0;">
  <p style="font-size: 18px; text-align: center; font-weight: bold;">
    核心观点或金句
  </p>
</div>
```

## 文章节奏

### 长短交替

避免连续的长段落或短句：

```
✅ 好的节奏：
短句引入。

一段较长的详细解释，包含具体的例子和数据支撑，
让读者充分理解这个概念。这种长段落不宜连续出现。

再用短句过渡。

另一段中等长度的内容...
```

```
❌ 差的节奏：
这是第一段很长的文字这是第一段很长的文字这是第一段很长的文字...

这是第二段很长的文字这是第二段很长的文字这是第二段很长的文字...

这是第三段很长的文字这是第三段很长的文字这是第三段很长的文字...
```

### 视觉元素穿插

每 3-5 段插入视觉元素：

```
文字段落 1
文字段落 2
文字段落 3
【图片】
文字段落 4
文字段落 5
【引用框/列表/代码块】
文字段落 6
...
```

## 列表排版

### 无序列表

```html
<ul style="padding-left: 1.5em; margin: 1em 0;">
  <li style="margin-bottom: 0.5em; line-height: 1.8;">列表项一</li>
  <li style="margin-bottom: 0.5em; line-height: 1.8;">列表项二</li>
  <li style="margin-bottom: 0.5em; line-height: 1.8;">列表项三</li>
</ul>
```

### 有序列表

```html
<ol style="padding-left: 1.5em; margin: 1em 0;">
  <li style="margin-bottom: 0.5em; line-height: 1.8;">第一步</li>
  <li style="margin-bottom: 0.5em; line-height: 1.8;">第二步</li>
  <li style="margin-bottom: 0.5em; line-height: 1.8;">第三步</li>
</ol>
```

### 自定义列表样式

```html
<!-- 使用 emoji 作为列表标记 -->
<p style="margin-bottom: 0.8em;">✅ 推荐做法一</p>
<p style="margin-bottom: 0.8em;">✅ 推荐做法二</p>
<p style="margin-bottom: 0.8em;">❌ 避免做法一</p>
```

## 文章开头

### 开篇模式

```html
<!-- 模式一：直接点题 -->
<p style="font-size: 15px; color: #3f3f3f;">
  今天聊一个困扰很多人的问题：如何写出高阅读量的公众号文章？
</p>

<!-- 模式二：场景引入 -->
<p style="font-size: 15px; color: #888; font-style: italic;">
  "为什么我的文章阅读量总是上不去？"
</p>
<p style="font-size: 15px; color: #3f3f3f;">
  这是后台收到最多的问题。今天我们就来解答。
</p>

<!-- 模式三：数据/事实引入 -->
<p style="font-size: 15px; color: #3f3f3f;">
  <strong>90% 的公众号文章</strong>在发布后 2 小时内决定了最终阅读量。
</p>
```

## 文章结尾

```html
<!-- 总结回顾 -->
<h2 style="...">总结</h2>
<p>本文主要介绍了以下几点：</p>
<ul>
  <li>要点一</li>
  <li>要点二</li>
  <li>要点三</li>
</ul>

<!-- 行动号召 -->
<p style="
  background: #f0f9eb;
  padding: 15px;
  border-radius: 4px;
  margin-top: 2em;
">
  💡 <strong>下一步行动</strong>：尝试用今天学到的方法优化你的下一篇文章！
</p>

<!-- 引导互动 -->
<p style="text-align: center; color: #888; margin-top: 2em;">
  觉得有用？点个「在看」支持一下 👇
</p>
```

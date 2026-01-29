---
name: 样式组件
description: 微信公众号文章常用的引用框、分隔线、高亮块、卡片等可复用样式组件
---

# 样式组件

本节提供一系列可复制使用的公众号样式组件，帮助快速搭建专业的文章排版。

## 引用框

### 基础引用

```html
<blockquote style="
  margin: 1.5em 0;
  padding: 15px 20px;
  background: #f7f7f7;
  border-left: 4px solid #ddd;
  color: #666;
  font-size: 14px;
  line-height: 1.8;
">
  这是一段引用文字，可以用来展示名人名言、
  重要概念或者需要突出的内容。
</blockquote>
```

### 带作者引用

```html
<blockquote style="
  margin: 1.5em 0;
  padding: 20px;
  background: #fafafa;
  border-left: 4px solid #07c160;
  font-style: italic;
">
  <p style="margin: 0 0 10px; font-size: 15px; color: #555; line-height: 1.8;">
    "简单是终极的复杂。"
  </p>
  <p style="margin: 0; font-size: 13px; color: #888; text-align: right;">
    —— 达·芬奇
  </p>
</blockquote>
```

### 圆角引用框

```html
<div style="
  margin: 1.5em 0;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 8px;
  color: #fff;
">
  <p style="margin: 0; font-size: 16px; line-height: 1.8; text-align: center;">
    ✨ 重要提示或金句 ✨
  </p>
</div>
```

## 提示框

### 信息提示

```html
<div style="
  margin: 1.5em 0;
  padding: 15px 20px;
  background: #e7f3ff;
  border-radius: 4px;
  border-left: 4px solid #1890ff;
">
  <p style="margin: 0; font-size: 14px; color: #333; line-height: 1.6;">
    💡 <strong>提示</strong>：这里是一些补充说明信息。
  </p>
</div>
```

### 警告提示

```html
<div style="
  margin: 1.5em 0;
  padding: 15px 20px;
  background: #fff3cd;
  border-radius: 4px;
  border-left: 4px solid #ffc107;
">
  <p style="margin: 0; font-size: 14px; color: #856404; line-height: 1.6;">
    ⚠️ <strong>注意</strong>：请务必注意这个问题。
  </p>
</div>
```

### 成功提示

```html
<div style="
  margin: 1.5em 0;
  padding: 15px 20px;
  background: #d4edda;
  border-radius: 4px;
  border-left: 4px solid #28a745;
">
  <p style="margin: 0; font-size: 14px; color: #155724; line-height: 1.6;">
    ✅ <strong>完成</strong>：恭喜你完成了这一步！
  </p>
</div>
```

### 错误/危险提示

```html
<div style="
  margin: 1.5em 0;
  padding: 15px 20px;
  background: #f8d7da;
  border-radius: 4px;
  border-left: 4px solid #dc3545;
">
  <p style="margin: 0; font-size: 14px; color: #721c24; line-height: 1.6;">
    ❌ <strong>错误</strong>：这种做法可能导致问题。
  </p>
</div>
```

## 分隔线

### 简洁分隔线

```html
<hr style="
  border: none;
  border-top: 1px solid #eee;
  margin: 2em 0;
"/>
```

### 渐变分隔线

```html
<div style="
  height: 1px;
  background: linear-gradient(to right, transparent, #ddd, transparent);
  margin: 2em 0;
"></div>
```

### 装饰分隔线

```html
<!-- 圆点分隔 -->
<p style="text-align: center; color: #ccc; margin: 2em 0; letter-spacing: 8px;">
  · · ·
</p>

<!-- 符号分隔 -->
<p style="text-align: center; color: #ddd; margin: 2em 0;">
  ━━━━━ ✦ ━━━━━
</p>

<!-- Emoji 分隔 -->
<p style="text-align: center; margin: 2em 0;">
  🔹🔹🔹
</p>

<!-- 文字分隔 -->
<p style="text-align: center; color: #999; font-size: 12px; margin: 2em 0;">
  ── 以下是正文 ──
</p>
```

## 高亮块

### 文字高亮

```html
<!-- 背景高亮 -->
<span style="background: #fffacd; padding: 2px 6px;">重点内容</span>

<!-- 下划线高亮 -->
<span style="
  border-bottom: 2px solid #07c160;
  padding-bottom: 2px;
">重点内容</span>

<!-- 标记笔效果 -->
<span style="
  background: linear-gradient(to bottom, transparent 60%, #ffeb3b 60%);
">重点内容</span>
```

### 高亮段落

```html
<div style="
  margin: 1.5em 0;
  padding: 20px;
  background: #fffbeb;
  border-radius: 8px;
  border: 1px dashed #f59e0b;
">
  <p style="margin: 0; font-size: 15px; line-height: 1.8; color: #92400e;">
    🌟 这是需要重点关注的内容，使用高亮背景和边框突出显示。
  </p>
</div>
```

## 卡片组件

### 基础卡片

```html
<div style="
  margin: 1.5em 0;
  padding: 20px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
">
  <h4 style="margin: 0 0 10px; font-size: 16px; color: #333;">卡片标题</h4>
  <p style="margin: 0; font-size: 14px; color: #666; line-height: 1.6;">
    卡片内容描述，可以包含简介、说明等信息。
  </p>
</div>
```

### 带标签的卡片

```html
<div style="
  margin: 1.5em 0;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  overflow: hidden;
">
  <div style="background: #07c160; padding: 8px 20px;">
    <span style="color: #fff; font-size: 12px; font-weight: bold;">推荐</span>
  </div>
  <div style="padding: 20px;">
    <h4 style="margin: 0 0 10px; font-size: 16px; color: #333;">产品名称</h4>
    <p style="margin: 0; font-size: 14px; color: #666; line-height: 1.6;">
      产品描述或推荐理由。
    </p>
  </div>
</div>
```

### 步骤卡片

```html
<div style="margin: 1.5em 0;">
  <!-- 步骤 1 -->
  <div style="display: flex; margin-bottom: 15px;">
    <div style="
      width: 32px;
      height: 32px;
      background: #07c160;
      color: #fff;
      border-radius: 50%;
      text-align: center;
      line-height: 32px;
      font-weight: bold;
      flex-shrink: 0;
    ">1</div>
    <div style="margin-left: 15px; flex: 1;">
      <h4 style="margin: 0 0 5px; font-size: 15px;">第一步标题</h4>
      <p style="margin: 0; font-size: 14px; color: #666;">步骤描述内容</p>
    </div>
  </div>
  <!-- 步骤 2 -->
  <div style="display: flex; margin-bottom: 15px;">
    <div style="
      width: 32px;
      height: 32px;
      background: #07c160;
      color: #fff;
      border-radius: 50%;
      text-align: center;
      line-height: 32px;
      font-weight: bold;
      flex-shrink: 0;
    ">2</div>
    <div style="margin-left: 15px; flex: 1;">
      <h4 style="margin: 0 0 5px; font-size: 15px;">第二步标题</h4>
      <p style="margin: 0; font-size: 14px; color: #666;">步骤描述内容</p>
    </div>
  </div>
</div>
```

## 按钮样式

```html
<!-- 主要按钮 -->
<p style="text-align: center; margin: 1.5em 0;">
  <span style="
    display: inline-block;
    padding: 12px 30px;
    background: #07c160;
    color: #fff;
    border-radius: 24px;
    font-size: 15px;
    font-weight: bold;
  ">立即查看</span>
</p>

<!-- 次要按钮 -->
<p style="text-align: center; margin: 1.5em 0;">
  <span style="
    display: inline-block;
    padding: 10px 25px;
    background: #fff;
    color: #07c160;
    border: 1px solid #07c160;
    border-radius: 20px;
    font-size: 14px;
  ">了解更多</span>
</p>
```

## 表格样式

```html
<table style="
  width: 100%;
  border-collapse: collapse;
  margin: 1.5em 0;
  font-size: 14px;
">
  <thead>
    <tr style="background: #f5f5f5;">
      <th style="padding: 12px; border: 1px solid #e0e0e0; text-align: left;">标题1</th>
      <th style="padding: 12px; border: 1px solid #e0e0e0; text-align: left;">标题2</th>
      <th style="padding: 12px; border: 1px solid #e0e0e0; text-align: left;">标题3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; border: 1px solid #e0e0e0;">内容1</td>
      <td style="padding: 12px; border: 1px solid #e0e0e0;">内容2</td>
      <td style="padding: 12px; border: 1px solid #e0e0e0;">内容3</td>
    </tr>
    <tr style="background: #fafafa;">
      <td style="padding: 12px; border: 1px solid #e0e0e0;">内容4</td>
      <td style="padding: 12px; border: 1px solid #e0e0e0;">内容5</td>
      <td style="padding: 12px; border: 1px solid #e0e0e0;">内容6</td>
    </tr>
  </tbody>
</table>
```

## 标签/徽章

```html
<!-- 普通标签 -->
<span style="
  display: inline-block;
  padding: 2px 8px;
  background: #e0e0e0;
  color: #666;
  border-radius: 3px;
  font-size: 12px;
">标签</span>

<!-- 彩色标签 -->
<span style="
  display: inline-block;
  padding: 2px 8px;
  background: #e6f7ff;
  color: #1890ff;
  border-radius: 3px;
  font-size: 12px;
">新功能</span>

<!-- 圆角徽章 -->
<span style="
  display: inline-block;
  padding: 4px 12px;
  background: #ff4d4f;
  color: #fff;
  border-radius: 12px;
  font-size: 12px;
">HOT</span>
```

## 作者信息卡

```html
<div style="
  margin: 2em 0;
  padding: 20px;
  background: #f9f9f9;
  border-radius: 8px;
  display: flex;
  align-items: center;
">
  <img src="avatar.jpg" style="
    width: 60px;
    height: 60px;
    border-radius: 50%;
    margin-right: 15px;
  " />
  <div>
    <h4 style="margin: 0 0 5px; font-size: 16px; color: #333;">作者名称</h4>
    <p style="margin: 0; font-size: 13px; color: #888; line-height: 1.5;">
      一句话介绍 | 公众号：xxx
    </p>
  </div>
</div>
```

## 编号列表组件

### 圆形编号列表

```html
<!-- 编号列表 -->
<div style="margin: 1.5em 0;">
  <!-- 项目 1 -->
  <div style="display: flex; margin-bottom: 15px;">
    <div style="
      width: 28px;
      height: 28px;
      background: #07c160;
      color: #fff;
      border-radius: 50%;
      text-align: center;
      line-height: 28px;
      font-size: 14px;
      font-weight: bold;
      flex-shrink: 0;
    ">1</div>
    <div style="margin-left: 12px; flex: 1;">
      <p style="margin: 0 0 4px; font-size: 15px; font-weight: bold; color: #333;">安装方便</p>
      <p style="margin: 0; font-size: 14px; color: #666; line-height: 1.6;">
        IDE 里装个插件就完事了，不用单独下载软件。
      </p>
    </div>
  </div>

  <!-- 项目 2 -->
  <div style="display: flex; margin-bottom: 15px;">
    <div style="
      width: 28px;
      height: 28px;
      background: #07c160;
      color: #fff;
      border-radius: 50%;
      text-align: center;
      line-height: 28px;
      font-size: 14px;
      font-weight: bold;
      flex-shrink: 0;
    ">2</div>
    <div style="margin-left: 12px; flex: 1;">
      <p style="margin: 0 0 4px; font-size: 15px; font-weight: bold; color: #333;">对设计师友好</p>
      <p style="margin: 0; font-size: 14px; color: #666; line-height: 1.6;">
        操作逻辑几乎和 Figma 一样，上手非常快。
      </p>
    </div>
  </div>

  <!-- 项目 3 -->
  <div style="display: flex;">
    <div style="
      width: 28px;
      height: 28px;
      background: #07c160;
      color: #fff;
      border-radius: 50%;
      text-align: center;
      line-height: 28px;
      font-size: 14px;
      font-weight: bold;
      flex-shrink: 0;
    ">3</div>
    <div style="margin-left: 12px; flex: 1;">
      <p style="margin: 0 0 4px; font-size: 15px; font-weight: bold; color: #333;">自带组件库</p>
      <p style="margin: 0; font-size: 14px; color: #666; line-height: 1.6;">
        内置 shadcn、Halo 等组件库，一句话调用。
      </p>
    </div>
  </div>
</div>
```

### 简洁编号列表

```html
<!-- 简洁版编号 -->
<div style="margin: 1.5em 0;">
  <div style="display: flex; align-items: flex-start; margin-bottom: 12px;">
    <span style="
      color: #07c160;
      font-weight: bold;
      margin-right: 10px;
    ">①</span>
    <span style="font-size: 15px; color: #333;">首先是<strong>安装方便</strong>，IDE 里装个插件就完事了</span>
  </div>
  <div style="display: flex; align-items: flex-start; margin-bottom: 12px;">
    <span style="
      color: #07c160;
      font-weight: bold;
      margin-right: 10px;
    ">②</span>
    <span style="font-size: 15px; color: #333;">然后是<strong>对设计师友好</strong>，操作逻辑和 Figma 几乎一样</span>
  </div>
  <div style="display: flex; align-items: flex-start;">
    <span style="
      color: #07c160;
      font-weight: bold;
      margin-right: 10px;
    ">③</span>
    <span style="font-size: 15px; color: #333;">还有一点很爽：<strong>自带组件库</strong></span>
  </div>
</div>
```

## 互动引导组件

### 三按钮互动引导

```html
<!-- 点赞/在看/星标 引导 -->
<div style="margin: 2.5em 0; text-align: center;">
  <p style="margin: 0 0 15px; font-size: 14px; color: #666;">
    觉得有用？点个「在看」支持一下
  </p>

  <div style="display: flex; justify-content: center; gap: 40px;">
    <!-- 点赞 -->
    <div style="text-align: center;">
      <div style="
        width: 50px;
        height: 50px;
        background: #fff5f5;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        margin: 0 auto 8px;
      ">👍</div>
      <span style="font-size: 12px; color: #888;">点赞</span>
    </div>

    <!-- 在看 -->
    <div style="text-align: center;">
      <div style="
        width: 50px;
        height: 50px;
        background: #f0fff4;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        margin: 0 auto 8px;
      ">👀</div>
      <span style="font-size: 12px; color: #888;">在看</span>
    </div>

    <!-- 星标 -->
    <div style="text-align: center;">
      <div style="
        width: 50px;
        height: 50px;
        background: #fffbeb;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        margin: 0 auto 8px;
      ">⭐</div>
      <span style="font-size: 12px; color: #888;">星标</span>
    </div>
  </div>

  <p style="margin: 15px 0 0; font-size: 12px; color: #bbb;">
    THANKS FOR READING
  </p>
</div>
```

### 简约互动引导

```html
<!-- 简约版 -->
<p style="
  text-align: center;
  color: #888;
  font-size: 13px;
  margin: 2em 0;
">
  👇 点击「在看」，让更多人看到
</p>
```

### 横向互动条

```html
<!-- 横向互动条 -->
<div style="
  margin: 2em 0;
  padding: 15px 20px;
  background: #f9f9f9;
  border-radius: 8px;
  display: flex;
  justify-content: space-around;
  align-items: center;
">
  <div style="text-align: center;">
    <span style="font-size: 18px;">👍</span>
    <span style="font-size: 13px; color: #666; margin-left: 5px;">点赞</span>
  </div>
  <div style="width: 1px; height: 20px; background: #ddd;"></div>
  <div style="text-align: center;">
    <span style="font-size: 18px;">💬</span>
    <span style="font-size: 13px; color: #666; margin-left: 5px;">留言</span>
  </div>
  <div style="width: 1px; height: 20px; background: #ddd;"></div>
  <div style="text-align: center;">
    <span style="font-size: 18px;">🔄</span>
    <span style="font-size: 13px; color: #666; margin-left: 5px;">转发</span>
  </div>
</div>
```

## 标签式标题组件

### 基础标签标题

```html
<!-- 标签 + 标题 -->
<div style="margin: 2.5em 0 1em;">
  <span style="
    display: inline-block;
    background: #f0f0f0;
    padding: 4px 12px;
    border-radius: 4px;
    font-size: 11px;
    color: #666;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 8px;
  ">Tool Review</span>
  <h2 style="
    margin: 0;
    font-size: 20px;
    font-weight: bold;
    color: #1a1a1a;
  ">Stitch vs Pencil</h2>
</div>
```

### 彩色标签标题

```html
<!-- 彩色标签 -->
<div style="margin: 2.5em 0 1em;">
  <span style="
    display: inline-block;
    background: #e6f7ff;
    color: #1890ff;
    padding: 4px 12px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: bold;
    margin-bottom: 8px;
  ">新功能</span>
  <h2 style="
    margin: 0;
    font-size: 18px;
    font-weight: bold;
    color: #333;
  ">一键导出 React 代码</h2>
</div>
```

### 带副标题的标签

```html
<!-- 完整版：标签 + 主标题 + 副标题 -->
<div style="margin: 2.5em 0 1em;">
  <span style="
    display: inline-block;
    background: #f6ffed;
    color: #52c41a;
    padding: 4px 10px;
    border-radius: 4px;
    font-size: 11px;
    margin-bottom: 10px;
  ">Workflow</span>
  <h2 style="
    margin: 0 0 6px;
    font-size: 18px;
    font-weight: bold;
    color: #1a1a1a;
  ">MCP + Skills 组合工作流</h2>
  <p style="
    margin: 0;
    font-size: 13px;
    color: #888;
  ">全程在一个对话里完成，形成可复用的工作流</p>
</div>
```

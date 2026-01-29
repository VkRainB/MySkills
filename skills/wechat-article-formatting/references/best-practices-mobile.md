---
name: 移动端适配
description: 针对手机屏幕的微信公众号文章排版优化策略
---

# 移动端适配

微信公众号文章 90%+ 的阅读发生在手机上。本节介绍如何针对移动端进行排版优化。

## 屏幕尺寸理解

### 常见手机屏幕宽度

| 设备 | 屏幕宽度 | 公众号内容区宽度 |
|------|----------|------------------|
| iPhone SE | 375px | ~320px |
| iPhone 14 | 390px | ~335px |
| iPhone 14 Pro Max | 430px | ~375px |
| 主流安卓 | 360-412px | ~305-357px |

**关键数据：**
- 公众号内容区实际宽度约为 **320-375px**
- 设计时以 **350px** 为参考宽度
- 图片最大宽度为 **100%** 自适应

## 字号适配

### 推荐字号范围

```html
<!-- 移动端友好的字号 -->
<style>
  正文：14-16px（推荐 15px）
  标题：17-20px
  小字：12-13px
  最小可读：11px（不推荐更小）
</style>
```

### 避免的问题

```html
<!-- ❌ 字号过小 -->
<p style="font-size: 12px;">这段文字在手机上很难阅读</p>

<!-- ❌ 字号过大 -->
<p style="font-size: 20px;">这段正文太大，一行显示不了几个字</p>

<!-- ✅ 合适的字号 -->
<p style="font-size: 15px;">这是移动端最佳阅读字号</p>
```

## 行宽与行高

### 每行字数

移动端最佳阅读体验：

```
每行 18-25 个汉字

计算：
- 内容区宽度：350px
- 字号：15px
- 字间距：1px
- 每行约：350 ÷ 16 ≈ 22 个字
```

### 行高设置

```html
<!-- 移动端推荐行高 -->
<p style="
  font-size: 15px;
  line-height: 2;      /* 2 倍行高 = 30px */
  letter-spacing: 1px;
">
  移动端需要更大的行高，让眼睛更容易追踪下一行。
  小屏幕上阅读更费力，充足的行间距减少疲劳。
</p>
```

## 触控友好设计

### 点击区域

手指触控需要足够的点击区域：

```html
<!-- ❌ 点击区域太小 -->
<a href="#" style="font-size: 12px;">链接</a>

<!-- ✅ 足够的点击区域 -->
<a href="#" style="
  display: inline-block;
  padding: 10px 20px;
  font-size: 15px;
">链接</a>
```

**最小触控区域：44 × 44 像素**（Apple 人机界面指南推荐）

### 按钮设计

```html
<!-- 移动端友好的按钮 -->
<p style="text-align: center;">
  <span style="
    display: inline-block;
    padding: 14px 40px;
    background: #07c160;
    color: #fff;
    border-radius: 24px;
    font-size: 16px;
  ">点击查看</span>
</p>
```

## 图片适配

### 自适应宽度

```html
<!-- 所有图片使用 100% 宽度 -->
<img src="image.jpg" style="
  max-width: 100%;
  height: auto;
" />
```

### 避免超宽

```html
<!-- ❌ 固定宽度可能超出屏幕 -->
<img src="image.jpg" style="width: 500px;" />

<!-- ✅ 限制最大宽度 -->
<img src="image.jpg" style="
  width: 100%;
  max-width: 500px;
" />
```

### 高清适配

```markdown
移动端 Retina 屏幕需要 2x/3x 图片：

- 显示 300px 宽 → 实际需要 600-900px 宽的图片
- 封面图 900×383 实际显示约 300×128
- 图片清晰度要求高于桌面端
```

## 表格优化

表格是移动端适配的难点：

### 方案一：简化表格

```html
<!-- 减少列数，只保留关键信息 -->
<table style="width: 100%; font-size: 13px;">
  <tr>
    <td style="padding: 8px;">项目</td>
    <td style="padding: 8px;">说明</td>
  </tr>
</table>
```

### 方案二：转为列表

```html
<!-- 将表格内容转为卡片列表 -->
<div style="
  background: #f7f7f7;
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 10px;
">
  <p style="margin: 0 0 5px; font-weight: bold;">项目名称</p>
  <p style="margin: 0; color: #666; font-size: 14px;">说明文字</p>
</div>
```

### 方案三：横向滚动

```html
<div style="overflow-x: auto;">
  <table style="min-width: 500px;">
    <!-- 表格内容 -->
  </table>
</div>
```

## 间距优化

### 增加留白

移动端需要更多呼吸空间：

```html
<!-- 段落间距 -->
<p style="margin-bottom: 1.5em;">段落内容</p>

<!-- 章节间距 -->
<h2 style="margin-top: 2.5em; margin-bottom: 1em;">章节标题</h2>

<!-- 组件间距 -->
<div style="margin: 2em 0;">引用框/图片/代码块</div>
```

### 避免拥挤

```html
<!-- ❌ 间距不足 -->
<h2 style="margin: 0.5em 0;">标题</h2>
<p style="margin-bottom: 0.5em;">段落</p>

<!-- ✅ 充足间距 -->
<h2 style="margin: 2em 0 1em;">标题</h2>
<p style="margin-bottom: 1.5em;">段落</p>
```

## 导航与阅读引导

### 使用目录

长文章添加目录帮助导航：

```html
<div style="
  background: #f5f5f5;
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 2em;
">
  <p style="margin: 0 0 10px; font-weight: bold;">📑 本文目录</p>
  <p style="margin: 5px 0; font-size: 14px;">1. 第一部分</p>
  <p style="margin: 5px 0; font-size: 14px;">2. 第二部分</p>
  <p style="margin: 5px 0; font-size: 14px;">3. 第三部分</p>
</div>
```

### 阅读进度提示

```html
<!-- 在长文中适时提示 -->
<p style="
  text-align: center;
  color: #999;
  font-size: 12px;
  margin: 2em 0;
">
  ── 已阅读 50% ──
</p>
```

## 加载性能

### 图片优化

```markdown
移动端网络环境复杂：

1. 压缩图片（目标 < 200KB）
2. 使用合适的格式（照片用 JPG）
3. 控制图片数量（< 15 张）
4. 首屏图片优先加载
```

### 减少复杂样式

```html
<!-- ❌ 过多阴影和渐变 -->
<div style="
  box-shadow: 0 0 10px rgba(0,0,0,0.1),
              0 5px 20px rgba(0,0,0,0.1),
              inset 0 0 5px rgba(0,0,0,0.05);
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
">

<!-- ✅ 简化样式 -->
<div style="
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  background: #667eea;
">
```

## 测试检查清单

```markdown
发布前检查：

□ 手机预览过整篇文章
□ 字号舒适可读（15-16px）
□ 图片全部正常显示
□ 没有横向滚动条
□ 点击区域足够大
□ 表格内容可见完整
□ 加载速度可接受
□ 不同机型测试（iOS/Android）
```

## 快速适配样式

```html
<!-- 移动端友好的基础样式 -->
<div style="
  font-size: 15px;
  line-height: 2;
  color: #3f3f3f;
  letter-spacing: 1px;
  word-wrap: break-word;
  overflow-wrap: break-word;
">
  <!-- 文章内容 -->
</div>

<!-- 移动端图片 -->
<img style="
  max-width: 100%;
  height: auto;
  display: block;
  margin: 1.5em auto;
" />

<!-- 移动端表格 -->
<table style="
  width: 100%;
  font-size: 13px;
  border-collapse: collapse;
">
```

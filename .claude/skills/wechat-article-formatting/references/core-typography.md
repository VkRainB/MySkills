---
name: 排版基础
description: 微信公众号文章的字体、字号、行高、颜色等基础样式规范
---

# 排版基础

微信公众号文章在移动端阅读为主，排版需要兼顾可读性和美观性。以下是经过验证的基础样式规范。

## 字体选择

微信公众号支持的字体有限，推荐使用系统默认字体栈：

```css
/* 推荐字体栈 */
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
             "Helvetica Neue", Arial, "PingFang SC", "Hiragino Sans GB",
             "Microsoft YaHei", sans-serif;
```

**要点：**
- 避免使用特殊字体，大多数用户看到的是系统默认字体
- iOS 优先显示「苹方」，Android 优先显示「思源黑体」或「微软雅黑」
- 不要在正文中混用多种字体

## 字号规范

| 元素 | 推荐字号 | 说明 |
|------|----------|------|
| 正文 | 15-16px | 移动端最佳阅读字号 |
| 主标题 | 18-20px | 文章内的一级标题 |
| 副标题 | 16-17px | 二级标题 |
| 小标题 | 15-16px | 三级标题，可用加粗区分 |
| 注释/引用 | 13-14px | 辅助信息 |
| 图片说明 | 12-13px | 图注文字 |

**示例 HTML：**

```html
<!-- 正文 -->
<p style="font-size: 15px; line-height: 2; color: #3f3f3f;">
  这是正文内容，使用 15px 字号配合 2 倍行高。
</p>

<!-- 标题 -->
<h2 style="font-size: 18px; font-weight: bold; color: #1a1a1a;">
  这是主标题
</h2>
```

## 行高设置

行高直接影响阅读舒适度：

| 场景 | 推荐行高 | line-height 值 |
|------|----------|----------------|
| 正文 | 1.8-2.0 倍 | `line-height: 2;` |
| 标题 | 1.4-1.6 倍 | `line-height: 1.5;` |
| 引用 | 1.6-1.8 倍 | `line-height: 1.75;` |

```html
<!-- 舒适的正文行高 -->
<p style="font-size: 15px; line-height: 2;">
  较大的行高让文字呼吸，减少阅读疲劳。
  特别是在手机小屏幕上，充足的行间距更重要。
</p>
```

## 颜色规范

### 文字颜色

| 用途 | 推荐色值 | 示例 |
|------|----------|------|
| 正文 | #3f3f3f 或 #333333 | 深灰，比纯黑柔和 |
| 标题 | #1a1a1a 或 #000000 | 接近纯黑，突出层级 |
| 辅助文字 | #888888 或 #999999 | 灰色，用于注释 |
| 链接/强调 | #576b95 | 微信默认链接蓝 |
| 重点强调 | #c7000b 或品牌色 | 用于关键词高亮 |

### 背景颜色

```html
<!-- 引用块背景 -->
<blockquote style="background: #f7f7f7; padding: 15px; border-left: 3px solid #ddd;">
  引用内容
</blockquote>

<!-- 重点提示背景 -->
<div style="background: #fff3cd; padding: 15px; border-radius: 4px;">
  ⚠️ 注意事项
</div>

<!-- 成功提示背景 -->
<div style="background: #d4edda; padding: 15px; border-radius: 4px;">
  ✅ 操作成功
</div>
```

## 对齐方式

- **正文**：左对齐（`text-align: left`）- 最符合中文阅读习惯
- **标题**：左对齐或居中，保持全文一致
- **图片**：居中对齐
- **图注**：居中对齐，字号略小

```html
<!-- 图片居中 -->
<p style="text-align: center;">
  <img src="image.jpg" style="max-width: 100%;" />
</p>
<p style="text-align: center; font-size: 12px; color: #888;">
  图 1：示意图说明
</p>
```

## 首行缩进

**现代排版趋势：不使用首行缩进**

传统印刷使用首行缩进 2 字符，但在移动端：
- 屏幕窄，缩进占用宝贵空间
- 段落间距已足够区分段落
- 西文排版影响，无缩进更简洁

```html
<!-- 推荐：不缩进 + 段落间距 -->
<p style="text-indent: 0; margin-bottom: 1.5em;">
  第一段内容...
</p>
<p style="text-indent: 0; margin-bottom: 1.5em;">
  第二段内容...
</p>
```

如确需首行缩进：

```html
<p style="text-indent: 2em;">
  首行缩进两个字符的段落...
</p>
```

## 字间距

适当的字间距提升阅读体验：

```html
<!-- 正文字间距 -->
<p style="letter-spacing: 1px;">
  增加 1px 字间距，文字更透气。
</p>

<!-- 标题字间距 -->
<h2 style="letter-spacing: 2px;">
  标题可以用更大的字间距
</h2>
```

## 快速参考

```html
<!-- 标准正文样式 -->
<p style="
  font-size: 15px;
  line-height: 2;
  color: #3f3f3f;
  letter-spacing: 1px;
  margin-bottom: 1.5em;
">
  正文内容...
</p>

<!-- 标准标题样式 -->
<h2 style="
  font-size: 18px;
  font-weight: bold;
  color: #1a1a1a;
  line-height: 1.5;
  margin: 2em 0 1em;
">
  标题文字
</h2>
```

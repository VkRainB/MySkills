---
name: 高级章节设计
description: 微信公众号文章的编号章节、案例展示、进阶模块等高级排版设计
---

# 高级章节设计

高级章节设计能让文章结构更加清晰、专业，帮助读者快速定位和理解内容。本节介绍编号章节、案例展示等高级排版技巧。

## 编号章节设计

### 大号数字编号（推荐）

使用醒目的数字编号创建强视觉层级，这是专业公众号常用的设计方式：

```html
<!-- 编号章节 -->
<div style="margin: 3em 0 1.5em;">
  <!-- 数字编号 -->
  <div style="
    display: inline-block;
    font-size: 32px;
    font-weight: bold;
    color: #07c160;
    font-family: 'Georgia', serif;
    line-height: 1;
    margin-bottom: 8px;
  ">01</div>

  <!-- 章节标题 -->
  <h2 style="
    margin: 0;
    font-size: 18px;
    font-weight: bold;
    color: #1a1a1a;
    display: flex;
    align-items: center;
    gap: 8px;
  ">
    <span style="color: #07c160;">STITCH</span>
    <span style="color: #999; font-weight: normal;">/</span>
    <span>3 分钟 5 个页面，速度非常快</span>
  </h2>
</div>
```

### 简化版编号

适合更简洁的文章风格：

```html
<!-- 简化编号章节 -->
<div style="margin: 2.5em 0 1em;">
  <div style="
    display: flex;
    align-items: center;
    gap: 12px;
  ">
    <!-- 数字 -->
    <span style="
      font-size: 28px;
      font-weight: bold;
      color: #1890ff;
      font-family: 'Georgia', serif;
    ">01</span>

    <!-- 标题 -->
    <h2 style="
      margin: 0;
      font-size: 18px;
      font-weight: bold;
      color: #333;
    ">快速上手指南</h2>
  </div>
</div>
```

### 圆形编号

```html
<!-- 圆形背景编号 -->
<div style="margin: 2.5em 0 1em;">
  <div style="
    display: flex;
    align-items: center;
    gap: 15px;
  ">
    <!-- 圆形数字 -->
    <div style="
      width: 40px;
      height: 40px;
      background: #07c160;
      border-radius: 50%;
      color: #fff;
      font-size: 18px;
      font-weight: bold;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    ">1</div>

    <!-- 标题 -->
    <h2 style="
      margin: 0;
      font-size: 18px;
      font-weight: bold;
      color: #333;
    ">第一步：安装配置</h2>
  </div>
</div>
```

## 标签式标题

在标题上方添加小标签，增加信息层次：

### 基础标签标题

```html
<!-- 标签 + 标题组合 -->
<div style="margin: 2.5em 0 1em;">
  <!-- 小标签 -->
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

  <!-- 主标题 -->
  <h2 style="
    margin: 0;
    font-size: 22px;
    font-weight: bold;
    color: #1a1a1a;
  ">Stitch vs Pencil</h2>

  <!-- 副标题（可选） -->
  <p style="
    margin: 8px 0 0;
    font-size: 14px;
    color: #888;
  ">两款 AI UI 设计工具对比评测</p>
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
  ">支持一键导出 React 代码</h2>
</div>
```

### 多标签组合

```html
<!-- 多标签 -->
<div style="margin: 2.5em 0 1em;">
  <div style="margin-bottom: 10px;">
    <span style="
      display: inline-block;
      background: #f6ffed;
      color: #52c41a;
      padding: 3px 8px;
      border-radius: 3px;
      font-size: 11px;
      margin-right: 6px;
    ">推荐</span>
    <span style="
      display: inline-block;
      background: #fff7e6;
      color: #fa8c16;
      padding: 3px 8px;
      border-radius: 3px;
      font-size: 11px;
    ">进阶</span>
  </div>

  <h2 style="
    margin: 0;
    font-size: 18px;
    font-weight: bold;
    color: #333;
  ">MCP + Skills 组合工作流</h2>
</div>
```

## 案例展示设计

### Case 标签模式

用于展示多个案例或示例：

```html
<!-- 案例标签 -->
<div style="margin: 1.5em 0;">
  <!-- Case 标签 -->
  <p style="
    margin: 0 0 10px;
    font-size: 13px;
    color: #888;
    font-style: italic;
  ">case1: 外卖 App 首页</p>

  <!-- 案例图片 -->
  <p style="text-align: center; margin: 0;">
    <img src="case1.jpg" style="
      max-width: 100%;
      border-radius: 8px;
      box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    " />
  </p>
</div>

<!-- 案例 2 -->
<div style="margin: 2em 0;">
  <p style="
    margin: 0 0 10px;
    font-size: 13px;
    color: #888;
    font-style: italic;
  ">case2: AI 情绪日记</p>

  <p style="text-align: center; margin: 0;">
    <img src="case2.jpg" style="
      max-width: 100%;
      border-radius: 8px;
      box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    " />
  </p>
</div>
```

### 卡片式案例

```html
<!-- 案例卡片 -->
<div style="
  margin: 1.5em 0;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.08);
  overflow: hidden;
">
  <!-- 案例标签头 -->
  <div style="
    background: #1890ff;
    padding: 8px 15px;
    color: #fff;
    font-size: 12px;
    font-weight: bold;
  ">📱 Case 1</div>

  <!-- 案例图片 -->
  <img src="case.jpg" style="width: 100%; display: block;" />

  <!-- 案例说明 -->
  <div style="padding: 15px;">
    <h4 style="margin: 0 0 8px; font-size: 15px; color: #333;">拉了么 - 外卖 App</h4>
    <p style="margin: 0; font-size: 13px; color: #666; line-height: 1.6;">
      使用 Stitch 生成的外卖应用首页，包含搜索、分类、推荐等模块。
    </p>
  </div>
</div>
```

### 对比案例

```html
<!-- 前后对比 -->
<div style="margin: 2em 0;">
  <div style="display: flex; gap: 15px;">
    <!-- Before -->
    <div style="flex: 1; text-align: center;">
      <p style="
        margin: 0 0 8px;
        font-size: 12px;
        color: #888;
      ">（原型）</p>
      <img src="before.jpg" style="
        width: 100%;
        border-radius: 8px;
        border: 1px solid #eee;
      " />
    </div>

    <!-- After -->
    <div style="flex: 1; text-align: center;">
      <p style="
        margin: 0 0 8px;
        font-size: 12px;
        color: #888;
      ">（应用）</p>
      <img src="after.jpg" style="
        width: 100%;
        border-radius: 8px;
        border: 1px solid #eee;
      " />
    </div>
  </div>
</div>
```

## 进阶玩法模块

用于展示高级用法或扩展内容：

### 进阶标题

```html
<!-- 进阶模块标题 -->
<h3 style="
  margin: 2em 0 1em;
  padding: 10px 15px;
  background: linear-gradient(90deg, #f0f0f0 0%, transparent 100%);
  font-size: 16px;
  font-weight: bold;
  color: #333;
  border-left: 4px solid #fa8c16;
">进阶实战：在同一个上下文里完成全流程</h3>
```

### 折叠提示框

```html
<!-- 进阶提示框 -->
<div style="
  margin: 1.5em 0;
  padding: 20px;
  background: #fffbe6;
  border: 1px solid #ffe58f;
  border-radius: 8px;
">
  <p style="
    margin: 0 0 10px;
    font-size: 14px;
    font-weight: bold;
    color: #d48806;
  ">🚀 进阶玩法</p>
  <p style="
    margin: 0;
    font-size: 14px;
    color: #666;
    line-height: 1.8;
  ">
    让 AI 在读取设计数据的同时，调用你自己的 Skills。
    这样生成的代码不仅符合设计稿，还会遵循你团队的代码规范。
  </p>
</div>
```

### 专家提示

```html
<!-- 专家/Pro 提示 -->
<div style="
  margin: 1.5em 0;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 8px;
  color: #fff;
">
  <p style="
    margin: 0 0 8px;
    font-size: 12px;
    opacity: 0.9;
  ">💡 PRO TIP</p>
  <p style="
    margin: 0;
    font-size: 15px;
    line-height: 1.8;
  ">
    在 IDE 里选择更强的模型（比如 Claude 4.5 Opus）做前期规划，
    再调用 Stitch 执行——这套组合打法可以把整个流程串起来。
  </p>
</div>
```

## 总结性设计

### 核心观点突出

```html
<!-- 核心观点大字展示 -->
<div style="
  margin: 2.5em 0;
  padding: 30px 20px;
  text-align: center;
">
  <p style="
    margin: 0;
    font-size: 20px;
    font-weight: bold;
    color: #1a1a1a;
    line-height: 1.6;
  ">把 80% 的重复 UI 工作交给 AI<br/>
  剩下 20% 才是人该干的——<span style="color: #07c160;">品味把控</span></p>
</div>
```

### 金句高亮

```html
<!-- 金句卡片 -->
<div style="
  margin: 2em 0;
  padding: 25px;
  background: #f9f9f9;
  border-radius: 12px;
  border-left: 5px solid #07c160;
">
  <p style="
    margin: 0 0 10px;
    font-size: 18px;
    font-weight: bold;
    color: #333;
    line-height: 1.6;
  ">"品味的本质是「知道该拒绝什么」"</p>
  <p style="
    margin: 0;
    font-size: 14px;
    color: #888;
  ">—— 当 AI 能生成一切，你要知道什么该留、什么该扔</p>
</div>
```

### 行动号召

```html
<!-- CTA 行动号召 -->
<div style="
  margin: 2em 0;
  padding: 25px;
  background: linear-gradient(135deg, #07c160 0%, #10b981 100%);
  border-radius: 12px;
  text-align: center;
  color: #fff;
">
  <p style="
    margin: 0 0 15px;
    font-size: 16px;
    font-weight: bold;
  ">💡 下一步行动</p>
  <p style="
    margin: 0;
    font-size: 14px;
    opacity: 0.95;
  ">用今天学到的方法，试试优化你的下一个项目！</p>
</div>
```

## 互动引导设计

### 三按钮引导

```html
<!-- 点赞/在看/星标 引导 -->
<div style="
  margin: 2.5em 0;
  text-align: center;
">
  <p style="
    margin: 0 0 15px;
    font-size: 14px;
    color: #666;
  ">觉得有用？点个「在看」支持一下</p>

  <div style="
    display: flex;
    justify-content: center;
    gap: 40px;
  ">
    <!-- 点赞 -->
    <div style="text-align: center; cursor: pointer;">
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
    <div style="text-align: center; cursor: pointer;">
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
    <div style="text-align: center; cursor: pointer;">
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
</div>
```

### 简约版引导

```html
<!-- 简约互动引导 -->
<p style="
  text-align: center;
  color: #888;
  font-size: 13px;
  margin: 2em 0;
">
  👇 点击「在看」，让更多人看到
</p>
```

## 使用建议

```markdown
章节设计原则：

1. 编号一致性
   - 全文使用同一种编号样式
   - 01/02/03 或 1/2/3 保持统一

2. 层级清晰
   - 大编号用于主要章节
   - 小标题用于子章节
   - 不要超过 3 级

3. 适度使用标签
   - 标签用于补充分类信息
   - 不要每个标题都加标签

4. 案例标准化
   - 统一使用 case1/case2 格式
   - 图片尺寸和样式保持一致

5. 总结要醒目
   - 核心观点用大字展示
   - 金句配合视觉效果
   - 行动号召放在文末

6. 互动要自然
   - 结尾添加互动引导
   - 不要过度营销感
```


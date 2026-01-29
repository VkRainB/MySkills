---
name: 品牌一致性
description: 建立统一的微信公众号视觉风格和排版规范
---

# 品牌一致性

统一的视觉风格让读者形成品牌认知，提升专业形象。本节介绍如何建立和维护公众号的品牌一致性。

## 为什么需要一致性

```markdown
品牌一致性带来的价值：

✅ 识别度高 — 读者一眼认出是你的文章
✅ 专业形象 — 细节体现用心程度
✅ 效率提升 — 排版有规范可循
✅ 阅读体验 — 读者形成预期，减少认知负担
✅ 品牌资产 — 长期积累形成差异化
```

## 品牌色彩系统

### 定义主色

```html
<!-- 品牌色示例 -->
<style>
  /* 主色：品牌标志色 */
  --primary: #07c160;      /* 微信绿 */

  /* 辅助色 */
  --primary-light: #e6f7ee; /* 浅绿背景 */
  --primary-dark: #059048;  /* 深绿强调 */

  /* 中性色 */
  --text-primary: #1a1a1a;  /* 标题 */
  --text-body: #3f3f3f;     /* 正文 */
  --text-secondary: #888;   /* 辅助 */
  --text-hint: #bbb;        /* 提示 */

  /* 背景色 */
  --bg-primary: #ffffff;    /* 主背景 */
  --bg-secondary: #f7f7f7;  /* 卡片背景 */
  --bg-tertiary: #f0f0f0;   /* 代码背景 */
</style>
```

### 应用示例

```html
<!-- 标题使用主色装饰 -->
<h2 style="
  color: #1a1a1a;
  border-left: 4px solid #07c160;
  padding-left: 12px;
">标题</h2>

<!-- 引用块使用主色强调 -->
<blockquote style="
  border-left: 4px solid #07c160;
  background: #e6f7ee;
">引用内容</blockquote>

<!-- 按钮使用主色 -->
<span style="
  background: #07c160;
  color: #fff;
">按钮文字</span>
```

### 色彩搭配方案

```markdown
方案一：科技蓝
- 主色：#1890ff
- 辅助：#e6f7ff
- 适合：科技、产品类

方案二：活力橙
- 主色：#fa8c16
- 辅助：#fff7e6
- 适合：营销、电商类

方案三：专业灰
- 主色：#333333
- 辅助：#f5f5f5
- 适合：商务、财经类

方案四：清新绿
- 主色：#52c41a
- 辅助：#f6ffed
- 适合：健康、环保类
```

## 字体规范

### 字体家族

```html
<!-- 统一字体栈 -->
<div style="
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI',
               'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei',
               'Helvetica Neue', Helvetica, Arial, sans-serif;
">
```

### 字号层级

```markdown
品牌字号规范：

标题层级：
- H1（文章标题）：由后台控制
- H2（一级标题）：18px
- H3（二级标题）：16px
- H4（三级标题）：15px + bold

正文层级：
- 正文：15px
- 小字：13px
- 注释：12px
- 最小：11px（仅限版权声明等）
```

## 标题样式规范

### 定义 2-3 种标题样式

```html
<!-- 样式 A：左侧色条 -->
<h2 style="
  font-size: 18px;
  font-weight: bold;
  color: #1a1a1a;
  border-left: 4px solid #07c160;
  padding-left: 12px;
  margin: 2.5em 0 1em;
">标题样式 A</h2>

<!-- 样式 B：底部色条 -->
<h2 style="
  font-size: 18px;
  font-weight: bold;
  color: #1a1a1a;
  border-bottom: 2px solid #07c160;
  padding-bottom: 8px;
  margin: 2.5em 0 1em;
">标题样式 B</h2>

<!-- 样式 C：背景色块 -->
<h2 style="
  font-size: 18px;
  font-weight: bold;
  color: #fff;
  background: #07c160;
  padding: 10px 15px;
  border-radius: 4px;
  margin: 2.5em 0 1em;
">标题样式 C</h2>
```

### 选择并坚持

```markdown
建议：
- 全文使用同一种标题样式
- 或固定组合（H2 用样式 A，H3 用简洁粗体）
- 切忌每篇文章换一种风格
```

## 组件库建设

### 常用组件规范

```html
<!-- 品牌引用框 -->
<blockquote style="
  margin: 1.5em 0;
  padding: 15px 20px;
  background: #f7f7f7;
  border-left: 4px solid #07c160;
  color: #666;
  font-size: 14px;
  line-height: 1.8;
">引用内容</blockquote>

<!-- 品牌提示框 -->
<div style="
  margin: 1.5em 0;
  padding: 15px 20px;
  background: #e6f7ee;
  border-radius: 4px;
  border-left: 4px solid #07c160;
">
  <p style="margin: 0; font-size: 14px; color: #333;">
    💡 <strong>提示</strong>：提示内容
  </p>
</div>

<!-- 品牌分隔线 -->
<div style="
  height: 1px;
  background: linear-gradient(to right, transparent, #07c160, transparent);
  margin: 2em 0;
"></div>
```

### 组件使用规则

```markdown
使用原则：

1. 引用框：用于名人名言、重要引述
2. 提示框：用于注意事项、补充说明
3. 代码框：用于代码、命令展示
4. 分隔线：用于章节分隔（每篇 2-3 处为宜）
5. 卡片：用于独立信息块、推荐内容
```

## 图片风格

### 封面图规范

```markdown
封面图统一规范：

尺寸：900 × 383 px（头条）
风格：
  □ 统一的背景颜色或渐变
  □ 统一的标题字体和位置
  □ 统一的装饰元素
  □ 品牌 logo 固定位置

模板化：
  - 创建 3-5 个封面模板
  - 每期只换文字和配图
  - 保持视觉一致性
```

### 文内配图

```markdown
配图规范：

风格统一：
  □ 同一滤镜/色调处理
  □ 统一的圆角（4px 或 8px）
  □ 统一的阴影效果
  □ 统一的图注样式

尺寸规范：
  □ 宽度：100% 或固定 80%
  □ 压缩标准：< 200KB
  □ 格式：JPG（照片）/ PNG（图标）
```

```html
<!-- 统一的图片样式 -->
<p style="text-align: center; margin: 1.5em 0;">
  <img src="image.jpg" style="
    max-width: 100%;
    border-radius: 8px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  " />
</p>
<p style="
  text-align: center;
  font-size: 12px;
  color: #888;
  margin-top: 8px;
">
  ▲ 图片说明
</p>
```

## 版头与版尾

### 固定版头

```html
<!-- 品牌版头 -->
<div style="
  text-align: center;
  margin-bottom: 2em;
  padding-bottom: 1em;
  border-bottom: 1px solid #eee;
">
  <img src="brand-header.png" style="max-width: 200px;" />
  <p style="
    margin: 10px 0 0;
    font-size: 12px;
    color: #888;
  ">专注于 xxx 领域的原创内容</p>
</div>
```

### 固定版尾

```html
<!-- 品牌版尾 -->
<div style="
  margin-top: 3em;
  padding-top: 1.5em;
  border-top: 1px solid #eee;
  text-align: center;
">
  <!-- 作者信息 -->
  <div style="margin-bottom: 1.5em;">
    <img src="avatar.jpg" style="
      width: 60px;
      height: 60px;
      border-radius: 50%;
    " />
    <p style="margin: 8px 0 0; font-size: 14px; color: #333;">
      <strong>作者名称</strong>
    </p>
    <p style="margin: 4px 0 0; font-size: 12px; color: #888;">
      一句话介绍
    </p>
  </div>

  <!-- 引导关注 -->
  <p style="font-size: 13px; color: #666;">
    👆 长按识别二维码关注
  </p>

  <!-- 往期推荐 -->
  <div style="
    margin-top: 1.5em;
    padding: 15px;
    background: #f7f7f7;
    border-radius: 8px;
    text-align: left;
  ">
    <p style="margin: 0 0 10px; font-size: 13px; font-weight: bold;">
      📚 往期精选
    </p>
    <p style="margin: 5px 0; font-size: 13px;">
      <a style="color: #576b95;">文章标题一</a>
    </p>
    <p style="margin: 5px 0; font-size: 13px;">
      <a style="color: #576b95;">文章标题二</a>
    </p>
  </div>
</div>
```

## 品牌规范文档

### 创建规范文档

```markdown
# 公众号视觉规范 V1.0

## 品牌色彩
- 主色：#07c160
- 辅色：#e6f7ee
- 文字：#3f3f3f
- 标题：#1a1a1a

## 字体规范
- 正文：15px，行高 2
- 标题：18px，加粗
- 小字：13px

## 标题样式
- 采用左侧色条样式
- 色条宽度：4px
- 色条颜色：主色

## 组件规范
- 引用框：灰底 + 主色左边框
- 提示框：浅绿底 + 主色左边框
- 分隔线：主色渐变

## 图片规范
- 圆角：8px
- 阴影：0 2px 12px rgba(0,0,0,0.08)
- 压缩：< 200KB

## 封面图
- 尺寸：900×383
- 模板：使用固定模板
- 字体：思源黑体 Bold
```

## 检查清单

```markdown
品牌一致性检查：

□ 主色调一致（全文使用相同的品牌色）
□ 标题样式统一（H2、H3 样式固定）
□ 字号规范（遵循字号层级）
□ 组件风格统一（引用框、提示框样式一致）
□ 图片处理统一（圆角、阴影一致）
□ 封面图风格统一（使用模板）
□ 版头版尾一致（固定格式）
□ 整体视觉和谐（没有突兀元素）
```

## 模板化实践

```markdown
高效运营流程：

1. 创建样式模板库
   - 存储常用组件的 HTML 代码
   - 按类别分类（标题、引用、卡片等）

2. 使用排版工具的「我的样式」功能
   - 135编辑器：收藏自定义样式
   - 秀米：保存常用模板

3. 建立封面图模板
   - Canva/稿定设计创建模板
   - 每期只改文字和配图

4. 复用版头版尾
   - 保存为固定组件
   - 每篇文章直接插入
```

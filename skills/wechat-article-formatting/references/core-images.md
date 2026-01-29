---
name: 图片处理
description: 微信公众号文章的图片尺寸、格式选择、封面图设计和图文混排技巧
---

# 图片处理

图片是公众号文章的重要组成部分，正确的图片处理能显著提升阅读体验和加载速度。

## 图片尺寸规范

### 正文配图

| 类型 | 推荐宽度 | 说明 |
|------|----------|------|
| 通栏图 | 1080px | 占满文章宽度 |
| 普通配图 | 800-1080px | 常用尺寸 |
| 缩略图 | 400-600px | 小尺寸展示 |

**高度建议：**
- 横图比例：16:9、4:3、3:2
- 方图比例：1:1
- 竖图比例：3:4、2:3（慎用，占屏幕空间大）

```html
<!-- 通栏图片 -->
<p style="text-align: center;">
  <img src="image.jpg"
       style="width: 100%; max-width: 1080px;"
       alt="图片描述" />
</p>

<!-- 固定宽度图片 -->
<p style="text-align: center;">
  <img src="image.jpg"
       style="width: 80%; max-width: 600px;"
       alt="图片描述" />
</p>
```

### 封面图

| 类型 | 尺寸 | 比例 | 用途 |
|------|------|------|------|
| 头条封面 | 900×383px | 2.35:1 | 第一条推送 |
| 次条封面 | 500×500px | 1:1 | 第二条及以后 |
| 分享封面 | 500×500px | 1:1 | 朋友圈/聊天分享 |

**封面图设计要点：**
- 主体居中，避免被裁剪
- 文字大、少、醒目
- 考虑小尺寸预览效果
- 避免使用过多细节

## 图片格式选择

| 格式 | 适用场景 | 优点 | 缺点 |
|------|----------|------|------|
| JPG | 照片、复杂配图 | 文件小，色彩丰富 | 不支持透明 |
| PNG | 图标、截图、需要透明 | 支持透明，无损 | 文件较大 |
| GIF | 动图、简单动画 | 支持动画 | 色彩有限 |
| WebP | 现代浏览器 | 体积最小 | 兼容性略差 |

### 压缩建议

```
原则：在保证清晰度的前提下，尽量压缩

推荐工具：
- TinyPNG (tinypng.com) - 在线压缩
- Squoosh (squoosh.app) - Google 出品
- ImageOptim - Mac 本地工具

目标文件大小：
- 普通配图：< 200KB
- 大尺寸图：< 500KB
- GIF 动图：< 2MB
```

## 图文混排

### 图片居中（最常用）

```html
<p style="text-align: center; margin: 1.5em 0;">
  <img src="image.jpg" style="max-width: 100%;" />
</p>
<p style="text-align: center; font-size: 12px; color: #888; margin-top: 0.5em;">
  图 1：图片说明文字
</p>
```

### 图片左/右浮动

```html
<!-- 左浮动：图片在左，文字环绕 -->
<div style="overflow: hidden; margin: 1em 0;">
  <img src="avatar.jpg" style="
    float: left;
    width: 100px;
    height: 100px;
    margin-right: 15px;
    border-radius: 50%;
  " />
  <p style="margin: 0; line-height: 1.8;">
    这是环绕图片的文字内容。适合人物介绍、
    产品展示等需要图文并排的场景。
  </p>
</div>
```

### 并排多图

```html
<!-- 两图并排 -->
<p style="text-align: center; margin: 1.5em 0;">
  <img src="img1.jpg" style="width: 48%; display: inline-block;" />
  <img src="img2.jpg" style="width: 48%; display: inline-block;" />
</p>

<!-- 三图并排 -->
<p style="text-align: center; margin: 1.5em 0;">
  <img src="img1.jpg" style="width: 32%; display: inline-block;" />
  <img src="img2.jpg" style="width: 32%; display: inline-block;" />
  <img src="img3.jpg" style="width: 32%; display: inline-block;" />
</p>
```

## 图片样式增强

### 圆角效果

```html
<img src="image.jpg" style="
  max-width: 100%;
  border-radius: 8px;
" />
```

### 阴影效果

```html
<img src="image.jpg" style="
  max-width: 100%;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
" />
```

### 边框效果

```html
<img src="image.jpg" style="
  max-width: 100%;
  border: 1px solid #eee;
  padding: 4px;
  background: #fff;
" />
```

### 图片卡片

```html
<div style="
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  overflow: hidden;
  margin: 1.5em 0;
">
  <img src="image.jpg" style="width: 100%;" />
  <p style="padding: 12px; margin: 0; font-size: 14px; color: #666;">
    图片说明或标题
  </p>
</div>
```

## 图片说明（图注）

```html
<!-- 基础图注 -->
<p style="
  text-align: center;
  font-size: 12px;
  color: #888;
  margin-top: 8px;
">
  图 1：说明文字
</p>

<!-- 带编号的图注 -->
<p style="
  text-align: center;
  font-size: 12px;
  color: #888;
  margin-top: 8px;
">
  ▲ 数据来源：xxx 报告
</p>

<!-- 图片来源声明 -->
<p style="
  text-align: center;
  font-size: 11px;
  color: #aaa;
  margin-top: 5px;
">
  图源｜Unsplash
</p>
```

## 长图处理

对于信息图、流程图等长图：

```html
<!-- 长图展示 -->
<p style="text-align: center; margin: 1.5em 0;">
  <img src="long-image.jpg" style="
    max-width: 100%;
    width: 600px;
  " />
</p>
<p style="text-align: center; font-size: 12px; color: #888;">
  👆 长按保存查看大图
</p>
```

**长图建议：**
- 宽度控制在 750-1080px
- 高度不超过 10000px（微信限制）
- 考虑拆分为多张图片

## GIF 动图

```html
<p style="text-align: center; margin: 1.5em 0;">
  <img src="demo.gif" style="
    max-width: 100%;
    border-radius: 4px;
  " />
</p>
<p style="text-align: center; font-size: 12px; color: #888;">
  ▲ 操作演示
</p>
```

**GIF 注意事项：**
- 帧数越少文件越小
- 控制时长在 5-10 秒
- 画面尺寸适当缩小
- 考虑用视频替代复杂动画

## 图片 SEO

虽然公众号内部搜索权重有限，但良好的图片描述有助于：

```html
<!-- 添加 alt 属性 -->
<img src="cover.jpg"
     alt="2024年互联网行业薪资报告封面"
     style="max-width: 100%;" />
```

- 无障碍访问
- 图片加载失败时的替代文字
- 搜索引擎理解图片内容

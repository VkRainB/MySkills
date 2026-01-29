---
name: 代码展示
description: 微信公众号技术文章的代码块样式、语法高亮方案和最佳展示实践
---

# 代码展示

技术类公众号文章经常需要展示代码，本节介绍如何在公众号中优雅地展示代码。

## 微信公众号代码限制

**重要限制：**
- 微信不支持 `<pre>` 和 `<code>` 的默认样式
- 不支持 JavaScript，无法使用前端语法高亮库
- 复制的代码可能丢失格式

**解决方案：**
- 使用内联样式模拟代码块效果
- 使用代码截图
- 使用第三方排版工具生成带样式的代码

## 行内代码

```html
<code style="
  background: #f4f4f4;
  padding: 2px 6px;
  border-radius: 3px;
  font-family: Consolas, Monaco, 'Courier New', monospace;
  font-size: 14px;
  color: #c7254e;
">npm install</code>
```

效果：在正文中使用 `npm install` 安装依赖。

## 代码块样式

### 基础代码块

```html
<div style="
  margin: 1.5em 0;
  background: #282c34;
  border-radius: 8px;
  overflow: hidden;
">
  <!-- 标题栏 -->
  <div style="
    background: #21252b;
    padding: 8px 15px;
    display: flex;
    align-items: center;
  ">
    <span style="
      width: 12px;
      height: 12px;
      background: #ff5f56;
      border-radius: 50%;
      margin-right: 8px;
    "></span>
    <span style="
      width: 12px;
      height: 12px;
      background: #ffbd2e;
      border-radius: 50%;
      margin-right: 8px;
    "></span>
    <span style="
      width: 12px;
      height: 12px;
      background: #27c93f;
      border-radius: 50%;
    "></span>
    <span style="
      margin-left: 15px;
      color: #888;
      font-size: 12px;
    ">JavaScript</span>
  </div>
  <!-- 代码内容 -->
  <pre style="
    margin: 0;
    padding: 15px;
    overflow-x: auto;
    font-family: Consolas, Monaco, 'Courier New', monospace;
    font-size: 14px;
    line-height: 1.6;
    color: #abb2bf;
  ">function hello() {
  console.log('Hello World');
}</pre>
</div>
```

### 浅色主题代码块

```html
<div style="
  margin: 1.5em 0;
  background: #f6f8fa;
  border: 1px solid #e1e4e8;
  border-radius: 6px;
  overflow: hidden;
">
  <pre style="
    margin: 0;
    padding: 16px;
    overflow-x: auto;
    font-family: Consolas, Monaco, 'Courier New', monospace;
    font-size: 14px;
    line-height: 1.5;
    color: #24292e;
  ">const name = 'World';
console.log(`Hello ${name}`);</pre>
</div>
```

### 带行号的代码块

```html
<div style="
  margin: 1.5em 0;
  background: #1e1e1e;
  border-radius: 8px;
  overflow: hidden;
  display: flex;
">
  <!-- 行号 -->
  <div style="
    padding: 15px 12px;
    background: #252526;
    color: #858585;
    font-family: Consolas, Monaco, monospace;
    font-size: 14px;
    line-height: 1.6;
    text-align: right;
    user-select: none;
  ">1<br>2<br>3<br>4</div>
  <!-- 代码 -->
  <pre style="
    margin: 0;
    padding: 15px;
    flex: 1;
    overflow-x: auto;
    font-family: Consolas, Monaco, monospace;
    font-size: 14px;
    line-height: 1.6;
    color: #d4d4d4;
  ">function add(a, b) {
  return a + b;
}
console.log(add(1, 2));</pre>
</div>
```

## 手动语法高亮

由于无法使用 JS，需要手动添加颜色：

```html
<pre style="
  margin: 1.5em 0;
  padding: 16px;
  background: #282c34;
  border-radius: 8px;
  font-family: Consolas, Monaco, monospace;
  font-size: 14px;
  line-height: 1.6;
  overflow-x: auto;
">
<span style="color: #c678dd;">const</span> <span style="color: #e06c75;">name</span> <span style="color: #56b6c2;">=</span> <span style="color: #98c379;">'World'</span>;
<span style="color: #61afef;">console</span>.<span style="color: #61afef;">log</span>(<span style="color: #98c379;">`Hello </span><span style="color: #c678dd;">${</span><span style="color: #e06c75;">name</span><span style="color: #c678dd;">}</span><span style="color: #98c379;">`</span>);
</pre>
```

### 常用颜色参考（One Dark 主题）

| 元素类型 | 颜色代码 | 用途 |
|----------|----------|------|
| 关键字 | #c678dd | const, let, function, if |
| 变量 | #e06c75 | 变量名、参数名 |
| 字符串 | #98c379 | 'string', "string" |
| 函数调用 | #61afef | console.log, Array.map |
| 数字 | #d19a66 | 123, 3.14 |
| 注释 | #5c6370 | // comment |
| 运算符 | #56b6c2 | =, +, => |

## 代码截图方案

对于复杂代码，推荐使用截图：

### 推荐工具

| 工具 | 特点 | 网址 |
|------|------|------|
| Carbon | 美观、多主题 | carbon.now.sh |
| Ray.so | Raycast 出品，渐变背景 | ray.so |
| Codesnap | VS Code 插件 | VS Code 扩展市场 |
| Chalk.ist | 支持多窗格 | chalk.ist |

### 截图最佳实践

```markdown
1. 选择合适的主题（推荐深色）
2. 字号设置 14-16px
3. 宽度控制在 600-800px
4. 开启行号（可选）
5. 使用 PNG 格式保存
6. 添加适当的内边距
```

### 截图展示模板

```html
<div style="margin: 1.5em 0; text-align: center;">
  <img src="code-screenshot.png" style="
    max-width: 100%;
    border-radius: 8px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
  " />
</div>
<p style="
  text-align: center;
  font-size: 12px;
  color: #888;
  margin-top: 8px;
">
  ▲ 示例代码
</p>
```

## 终端/命令行样式

```html
<div style="
  margin: 1.5em 0;
  background: #0d1117;
  border-radius: 8px;
  overflow: hidden;
">
  <div style="
    background: #161b22;
    padding: 10px 15px;
    color: #8b949e;
    font-size: 12px;
  ">Terminal</div>
  <pre style="
    margin: 0;
    padding: 15px;
    font-family: Consolas, Monaco, monospace;
    font-size: 14px;
    line-height: 1.6;
    color: #c9d1d9;
  "><span style="color: #7ee787;">$</span> npm install vue
<span style="color: #7ee787;">$</span> npm run dev

<span style="color: #8b949e;"># 输出</span>
<span style="color: #58a6ff;">VITE</span> v5.0.0 ready in 320 ms
➜ Local: http://localhost:5173/</pre>
</div>
```

## 代码对比

```html
<div style="margin: 1.5em 0;">
  <!-- 错误示例 -->
  <div style="
    background: #2d1b1b;
    padding: 15px;
    border-radius: 8px 8px 0 0;
    border-left: 4px solid #f44336;
  ">
    <p style="margin: 0 0 10px; color: #f44336; font-size: 12px; font-weight: bold;">
      ❌ 错误写法
    </p>
    <pre style="
      margin: 0;
      font-family: Consolas, Monaco, monospace;
      font-size: 14px;
      color: #e8e8e8;
    ">var name = "World"
console.log("Hello " + name)</pre>
  </div>
  <!-- 正确示例 -->
  <div style="
    background: #1b2d1b;
    padding: 15px;
    border-radius: 0 0 8px 8px;
    border-left: 4px solid #4caf50;
  ">
    <p style="margin: 0 0 10px; color: #4caf50; font-size: 12px; font-weight: bold;">
      ✅ 推荐写法
    </p>
    <pre style="
      margin: 0;
      font-family: Consolas, Monaco, monospace;
      font-size: 14px;
      color: #e8e8e8;
    ">const name = 'World';
console.log(`Hello ${name}`);</pre>
  </div>
</div>
```

## 代码展示最佳实践

1. **代码简短**：每段代码控制在 20 行以内
2. **添加注释**：关键行添加说明注释
3. **高亮重点**：使用颜色或标记突出关键部分
4. **提供上下文**：说明代码的用途和场景
5. **可运行**：确保示例代码可以直接运行
6. **格式统一**：全文使用相同的代码样式

### 代码说明模板

```html
<!-- 代码前的说明 -->
<p style="font-size: 15px; color: #3f3f3f; margin-bottom: 1em;">
  下面的代码展示了如何使用 <code style="...">async/await</code> 处理异步请求：
</p>

<!-- 代码块 -->
<div style="...">
  <!-- 代码内容 -->
</div>

<!-- 代码后的解释 -->
<p style="font-size: 14px; color: #666; margin-top: 1em; line-height: 1.8;">
  <strong>代码解析</strong>：第 3 行使用 <code>await</code> 等待请求完成，
  第 5 行处理可能的错误情况。
</p>
```

# New Session Prompt

> 复制以下内容发给新的 AI agent 或新的 session，即可让它无缝接手。

---

你正在接手 Trevor Huang 的个人网站项目。请按以下顺序操作：

## 1. 先读这些文件（按顺序）
1. `CLAUDE.md` — 项目总览、设计系统、规则、颜色 tokens、字体、光标规范
2. `ROADMAP.md` — 已完成/待办进度
3. `Trevor_WorkContext_ForWebsite.md` — 工作经历的 source of truth
4. `Trevor_WorkExperience_Memory_01.md` — 工作经历详细版

## 2. 项目概览

- Trevor Huang（黄拓文）的个人网站，GitHub Pages 托管
- 仓库：`thuang17/thuang17.github.io`
- 线上地址：`https://thuang17.github.io`
- 英文版 `index.html`（主），中文版 `zh.html`
- 纯静态 HTML + Tailwind CDN + Google Fonts，零构建步骤
- 主 repo 路径：`/Users/h3art/Documents/github/personal-website/`
- 当前在 `main` 分支工作
- 不要删除 `explorations/` 目录下的 demo 文件

## 3. 当前状态

**主页已部署：** 横向 5-panel continuous surface，滚动右移。结构：
- Panel 1 — Hero：Geist 5 行文字 + 淡紫大圆（#D0C4F0 / #5B4A8C，panel-height）+ 入场动画
- Panel 2 — WORK：90px Geist 全大写，左下裁切
- Panel 3 — MAKING：90px Geist，左上裁切
- Panel 4 — STORIES：90px Geist，右下裁切，深色背景
- Panel 5 — Info：超大文字（o 裁切），点击弹出浮层

**设计系统（已锁定）：**
- 字体：Geist（Hero/Panel 标题）、Montserrat、Nunito Sans、JetBrains Mono
- 页面背景：#E8E8E8，Panel 背景：#f9f9f9
- 珊瑚光标 #E07B5A（r=7/8px，CSS cursor: url()），可拖拽区用系统光标
- 入场动画在 `@media (prefers-reduced-motion: no-preference)` 内
- Scrubber 200px 轨道 B2 规格，hover 1.1x，可拖拽

**中文版：** `zh.html` 已同步所有主页改动（入场动画、圆圈、panel 等）

**子页面（未适配新设计）：** decathlon.html, mayora.html, cny-campaign.html, decathlon-ux.html, ai.html, darts.html 仍是旧布局

## 4. 下一步最优先任务

### 4.1 建 Work 索引页（work.html）
- Trevor 点 Work panel 后应该先看到一个汇总页，而不是直接跳转到具体经历
- 结构：Editorial list，Experience 4 行（Decathlon / Mayora / SynTao / Tianfeng）+ Projects 2 行（CNY campaign / Decathlon UX）
- 视觉：Geist 标题 + Nunito 正文 + mono 日期，极细分割线，大留白，同主页色板
- 顶栏：← Home 返回 + 语言/主题控件（同主页）
- 方向已 brainstorming 确认：list over cards，editorial over panel
- Trevor 想先自己找一些 reference 再继续讨论具体视觉

### 4.2 修 panel 跳转逻辑
- Work panel → work.html（当前直接跳到 decathlon.html）
- Making panel → ai.html（作为 Making 的索引/入口）
- Stories panel → darts.html（作为 Stories 的索引/入口）
- 清理 AI ↔ darts 之间的跨链接

### 4.3 统一子页面视觉
- 所有子页面改成 Geist 字体 + 珊瑚光标 + 同色板

## 5. 已知问题

- **点击涟漪效果**：测试页可行，index.html 中不生效。可能是 Tailwind CDN 或已有 JS 冲突。ROADMAP 里有记录，可后续排查，优先级低。

## 6. 关键交互细节
- 滚动：velocity+friction（WHEEL_ACCELERATION=0.16, FRICTION=0.9, MAX_VELOCITY=120）
- `data-transition="page"` 触发 page-out 过渡动画
- `cursor: url()` 自定义光标，可交互元素 r=8px，默认 r=7px
- 入场动画全在 `@media (prefers-reduced-motion: no-preference)` 内
- 移动端 <980px 纵向堆叠

## 7. Trevor 的偏好
- 设计方向：minimal, restrained, editorial, 不花哨
- 参考 [rauno.me](https://rauno.me) 的交互逻辑但不照搬视觉
- 不喜欢动画过度的东西，偏好"静下来看"的感觉
- 文案要诚实、直接、不吹，像真人在说话
- 所有改动先用 brainstorming 过方向，再动代码
- 每次修改前先确认理解，不要假设

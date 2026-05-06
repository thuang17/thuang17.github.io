# CLAUDE.md — Trevor Huang Personal Website

每次新 session 开始时先读这个文件，以及 `Trevor_WorkContext_ForWebsite.md` 和 `Trevor_WorkExperience_Memory_01.md`。

---

## 项目概述

Trevor Huang（黄拓文）的个人网站。GitHub Pages 托管，Astro v5 构建输出静态文件。
当前方向不是“求职站优先”，而是：

- **personal website first**
- **proof-bearing site second**

首页不再默认服务于 HR 扫描，而是作为一个克制的个人入口页，让访客先选择从哪条线进入 Trevor。

- **英文版**：`index.astro` → `/`（主版本，默认入口）
- **中文版**：`zh.astro` → `/zh`
- 两个版本内容和结构保持同步，语言不同

---

## 技术栈

- **Astro v5 + React 19 + TypeScript**（2026-05 从纯静态 HTML 迁移）
- 构建命令：`npm run build`，输出到 `dist/`
- 开发服务器：`npm run dev`
- GitHub Actions 自动构建部署到 GitHub Pages
- CSS：全局设计系统在 `src/styles/global.css`，页面级 CSS 在各自 `.astro` 文件的 `<style>` 块中
- 图标：内联 SVG（不要用外部图标 CDN）
- 暗色模式：`data-theme="dark"` 在 `<html>` 上，localStorage 持久化

---

## 设计系统（已定，不要随意改动）

### 颜色 tokens
```css
--bg:       #E8E8E8   /* 页面背景 */
--bg-sub:   #F0EEE8   /* hover 背景 */
--bg-foot:  #E8E6DE   /* footer 背景 */
--fg:       #1C1917   /* 主文字 */
--fg-2:     #57534E   /* 次要文字 */
--fg-3:     #A8A29E   /* 标签/日期 */
--border:   #E7E5E4
--accent:   #7C3AED   /* 紫色主色调 */
```
暗色模式已实现，通过 `data-theme="dark"` 切换，localStorage 持久化。

### 字体
- **Hero / Panel 标题 / 大字**：Geist（400, 500, 600）→ 主要的展示字体
- **标题 fallback**：Montserrat（700, 800）→ `--f-display`
- **正文**：Nunito Sans（300, 400, 500, 600）→ `--f-body`
- **标签 / 日期 / mono**：JetBrains Mono（300, 400）→ `--f-mono`
- 中文版额外加载 Noto Sans SC 作为中文 fallback

### 布局
- 横向连续 surface，5 个 panel，鼠标滚轮驱动右移
- Panel 统一宽度：`min(80vw, 1240px)`
- Topbar：Scrubber 居中 + 语言/主题切换在右
- 移动端（<980px）：panel 纵向堆叠

### 自定义光标
- **全局光标**：珊瑚色实心圆点（`#E07B5A`），r=7px（14px 直径），CSS `cursor: url()` 实现
- **可交互元素**（链接/按钮/可点击 panel）：同色放大圆点，r=8px（16px 直径）
- **可拖拽区域**（胶囊/滑块轨道）：使用系统光标（`grab` / `grabbing`），不使用自定义光标
- 此规则适用于全站所有页面，确保光标体验统一

## 内容规则

### Tone
- **Casual business**：自信、直接、有主见，像一个聪明的人在聊天，不像在背稿
- **去 AI 味**：不用"通过...实现了..."、不用过度并列排比、不用"此外"/"综上"
- **英文版**：第一人称叙述，有具体细节和决策逻辑
- **中文版**：口语化，接地气，不堆砌术语

### 首页方向（2026-05-03 后）
- 首页应该像 **personal index / entry surface**，不是 resume homepage
- 首页的任务不是“总结 Trevor”，而是让人选择先进入哪个 Trevor
- 第一屏只保留少量但刻意的内容，不再平均展示经历、项目、技能、教育、联系方式
- 高级感主要来自 **hover** 和 **click / transition**
- 不靠热闹的开场动画，不靠 chapter metaphor，不靠卡片堆砌

### 内容 source of truth
所有工作经历和数据以这两个文件为准，不要凭记忆编：
- `Trevor_WorkContext_ForWebsite.md`
- `Trevor_WorkExperience_Memory_01.md`

### 已确认的关键数据
- 迪卡侬痛点数量：**16 个**（不是 20）
- 迪卡侬时间：**2025.12–2026.02**（网站显示 2025–2026）
- 迈大食品时间：**2024.07–2025.05**（网站显示 2024–2025）
- 商道纵横时间：**2024.01–2024.04**（网站显示 2024）
- 天风证券时间：**2022.08–2022.09**（网站显示 2022）
- 礼盒 campaign ROI：**7.22**（综合全窗口）
- 新品增长：**~600%**（vs 投放前日均基线，不是同比）

### 不出现在英文版的内容
- 任何中文字符（除了 nav 里的「中文」切换链接）
- "Project Manager" 头衔（Trevor 没有正式担任过 PM，只是 PM Intern）

### 语言切换
- 英文版 nav 有「中文」链接 → `/zh`
- 中文版 nav 有「EN」链接 → `/`

---

## 网站结构（当前已实现）

```
src/pages/
├── index.astro              # EN 首页（横向 5-panel surface）
├── zh.astro                 # ZH 首页
├── work.astro               # Work 索引页
├── zh-work.astro            # ZH Work 索引页
├── stories.astro            # Stories 索引页
├── zh-stories.astro         # ZH Stories 索引页
├── ai.astro                 # AI / Making 故事页
├── zh-ai.astro              # ZH AI / Making 页
├── darts.astro              # Darts 故事页
├── zh-darts.astro           # ZH Darts 故事页
├── decathlon.astro          # Decathlon 案例页
├── mayora.astro             # Mayora 案例页
├── cny-campaign.astro       # CNY Campaign 项目深挖
├── decathlon-ux.astro       # Decathlon UX 项目深挖
├── making/
│   └── index.astro          # Making 产品列表（自动从 content 生成）
└── products/
    └── [...slug].astro      # 产品详情动态路由

src/content/products/        # ⭐ 产品 Markdown 文件放这里
├── product1.md              # 写新产品的 .md 文件，自动生成页面
├── product2.md
└── ...
```

### 产品内容系统

产品放在 `src/content/products/` 目录下，每个产品一个 `.md` 文件：

```markdown
---
title: “产品名”
description: “一句话介绍”
pubDate: 2026-05-06
tags: [“标签1”, “标签2”]
status: building    # building | live | archived
---
## 正文
markdown 格式写内容。
```

- 产品列表页：`/making/`（自动按日期排序，React 卡片网格）
- 产品详情页：`/products/product1/`（自动生成）
- status 控制徽章颜色：building（紫色）、live（绿色）、archived（灰色）

---

## 待办 / 规划

详见 `ROADMAP.md`。

### 下一阶段优先级
1. `Now` 页面 / 区块（需 Trevor 提供内容）
2. Writing 区块占位（内容后续填充）
3. 中文文案重写 — 去掉 AI 味

### 暂缓事项
- 点击涟漪效果
- 自定义域名（先用免费 github.io）
- CSS View Transitions
- 照片（待 Trevor 提供）

---

## 文件结构

```
personal-website/
├── src/
│   ├── pages/               # 所有页面 (.astro)
│   ├── components/          # React 组件
│   ├── content/products/    # 产品 Markdown 文件
│   ├── layouts/             # BaseLayout.astro
│   └── styles/              # global.css（设计系统）
├── public/                  # 静态资源
├── context/                 # AI 协作上下文
├── CLAUDE.md / AGENTS.md    # 本文件 / Codex 配置
├── ROADMAP.md               # 项目规划
├── astro.config.mjs         # Astro 配置
├── package.json             # 依赖
├── Trevor_WorkContext_ForWebsite.md
└── Trevor_WorkExperience_Memory_01.md
```

---

*最后更新：2026-05-07*

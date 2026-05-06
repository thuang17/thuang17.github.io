# New Session Prompt

> 复制以下内容发给新的 AI agent 或新的 session，即可让它无缝接手。

---

你正在接手 Trevor Huang 的个人网站项目。先不要执行任何操作，先读完所有文件，理解上下文，然后和我讨论下一步计划。

## 1. 先读这些文件（按顺序）

1. `CLAUDE.md` — 项目总览、设计系统、规则、颜色 tokens、字体、光标规范
2. `ROADMAP.md` — 已完成/待办进度
3. `worklog/Session_Handoff_2026-05-06_Subpage_Unification.md` — 上一个 Session 的完整记录（最重要的上下文文件，所有设计决策和变更都在里面）
4. `worklog/Session_Handoff_2026-05-05_Work_Index_Page.md` — 上上个 Session 记录
5. `Trevor_WorkContext_ForWebsite.md` — 工作经历的 source of truth
6. `Trevor_WorkExperience_Memory_01.md` — 工作经历详细版

## 2. 项目概览

- Trevor Huang（黄拓文）的个人网站，GitHub Pages 托管
- 仓库：`thuang17/thuang17.github.io`
- 线上：`https://thuang17.github.io`
- 英文版 `index.html`（主），中文版 `zh.html`
- 纯静态 HTML + Tailwind CDN + Google Fonts + Geist/Nunito Sans/JetBrains Mono
- **当前已经在 main 分支工作**，上一个 session 已合并
- 子页面已全部统一视觉风格（decathlon/mayora/ai/darts/work/stories + 中文镜像）

## 3. 当前项目状态

### 已完成
- **主页**：横向 5-panel continuous surface，入场动画，Scrubber，Info overlay
- **Work 索引页**：`work.html` / `zh-work.html` — editorial 列表，v9 入场动画，focus hover
- **Stories 索引页**：`stories.html` / `zh-stories.html` — 同上设计，目前只有 Darts
- **子页面视觉统一**：
  - `decathlon.html` / `zh-decathlon.html` — Editorial longform + scroll ruler + data island + nav overlay
  - `mayora.html` / `zh-mayora.html` — 同上，CNY campaign 内容合并
  - `ai.html` / `zh-ai.html` — Timeline 布局 + cursor 跟随紫色圆点
  - `darts.html` / `zh-darts.html` — 水平传送带 gallery + 飞镖刻度指示器
- **导航浮框**：所有内容页左上角三条杠 hamburger → 目录浮框（含 Info 浮层）
- **珊瑚光标** `#E07B5A`，全站统一，暗色模式，入场动画，退出过渡

### 设计系统（已锁定，不可随意改动）
```css
--bg: #E8E8E8 | --fg: #1C1917 | --accent: #7C3AED | --fg-2: #57534E | --fg-3: #A8A29E
--f-display: 'Geist', sans-serif | --f-body: 'Nunito Sans', sans-serif | --f-mono: 'JetBrains Mono', monospace
```
暗色模式 `data-theme="dark"` + localStorage，中日落图标切换。
珊瑚光标 `#E07B5A`，r=7px 默认 / r=8px 可交互。

## 4. 三档"阅读温度"

Work / Making / Stories 三个 wing 的设计已经刻意区分：

| Wing | 页面 | 温度 | 核心交互 | 访客行为 |
|------|------|------|---------|---------|
| Work | decathlon.html, mayora.html | 热 | scroll ruler + data island + pull quote | 读 |
| Making | ai.html | 温 | timeline + cursor 跟随圆点 | 看 |
| Stories | darts.html, stories.html | 冷 | 水平传送带 + 飞镖刻度 | 翻 |

**注意：** 这是一个已确认的核心设计决策。新 agent 必须维持这三种温度的差异化，不能把三个 wing 统一回同一种风格。之后添加新的子页面时，需要匹配相应的阅读温度。

## 5. 下一步优先级（待讨论）

上一个 session 后，以下方向待推进——**需要先和我讨论再做**：

### 5.1 背景质感优化（frontend-design 建议）
目前所有页面是纯色 `#E8E8E8` 背景。可以考虑：
- 极微妙的 noise 纹理 overlay
- 或 editorial 页面加很浅的 radial-gradient
- 但不能过头——要 editorial 质感，不是装饰
- 讨论点：做什么程度、是否区分三个 wing

### 5.2 Scroll-triggered 渐进动画
editorial 页面（decathlon/mayora）目前只有一次整体 400ms 入场。可以：
- 每个 section 进入视口时极轻的 opacity 0→1 + 4px 上浮（300ms）
- 必须比上一个 session 被删掉的 scroll reveal 更轻
- 讨论点：做不做、做多重

### 5.3 Hover 微交互提升
- 链接 hover + 极微 `translateX(1px)` 位移（editorial 页）
- 传送带图片 hover + `brightness(1.05)`
- 讨论点：是否值得做

### 5.4 编辑长文"读起来太累"问题（已记录，暂缓）
记录在 `MEMORY.md` 中。scroll ruler + data island + pull quote 已缓解但核心问题仍在。
**优先级低**——后续再回来处理。

### 5.5 Now 页面 / Writing 区块
需要你提供内容。当前不推进。

### 5.6 Adding 更多子页面
- Making 页面等你添加更多的 AI 产品/项目
- Stories 索引页目前只有 Darts，后面可能加 Hiking
- 添加时需要匹配各自的阅读温度

## 6. 关键技术点

### 文件结构
```
personal-website/
├── index.html / zh.html                 # 主页
├── work.html / zh-work.html             # Work 索引
├── stories.html / zh-stories.html       # Stories 索引
├── decathlon.html / zh-decathlon.html   # 迪卡侬详情 (Work·热)
├── mayora.html / zh-mayora.html         # 迈大详情 (Work·热)
├── ai.html / zh-ai.html                 # AI Making (Making·温)
├── darts.html / zh-darts.html           # 飞镖故事 (Stories·冷)
├── docs/superpowers/specs/              # 设计规格
├── docs/superpowers/plans/              # 实施计划
└── worklog/                             # Session 交接文档
```

### 重要技术决策
- 所有页面使用 `favicon.png?v=2` + `apple-touch-icon.png`（不要漏）
- `loading="lazy"` 在横向 overflow-x 容器中有 bug → 用 `loading="eager"`
- 飞镖页图片不可点击/保存：`pointer-events: none` + `-webkit-user-drag: none`
- 中文版已全部同步（EN/ZH 成对），添加新 EN 页时必须同步创建 ZH 版

### 关键交互细节
- 入场动画在 `@media (prefers-reduced-motion: no-preference)` 内
- 退出过渡：body.page-out → main opacity 0 + translateY 8px, 180ms
- 导航浮框：内容页用三条杠 hamburger，索引页用纯文字 "Home"
- Info 浮层：精确复制主页的 design（grid、font、shadow、blur）

## 7. 必读文件

1. `worklog/Session_Handoff_2026-05-06_Subpage_Unification.md` — **最详细的上下文**
2. `CLAUDE.md` — 项目总览和设计系统
3. `ROADMAP.md` — 待办和规划

**读完这些文件后，先和我讨论下一步做什么，不要自行执行。**

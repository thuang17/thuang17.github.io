---
name: Session handoff — Work Index Page (2026-05-05)
description: Comprehensive record of the session that built work.html and zh-work.html, including all design decisions, animation specs, and technical details
type: project
originSessionId: aef9eb62-bac9-437f-a9b7-904a72cf923d
---

# Session Report: Work Index Page — Trevor Huang Personal Website

**日期：** 2026-05-05
**分支：** `claude/stoic-mendel-5deeba` → 已合并至 `main`
**GitHub：** https://github.com/thuang17/thuang17.github.io
**线上：** https://thuang17.github.io

---

## 1. 本 Session 完成了什么

### 核心交付：work.html + zh-work.html — Work 索引页

这是 homepage → 详情页之间的中间层页面。用户从主页点 WORK panel 后进入这个 editorial directory，然后从列表中选择具体经历/项目跳转到详情页。

**页面定位：**
- 纯列表型目录，不是一个介绍页面
- 极简 editorial 风格，无标题、无分割线、无 footer
- 任务不是"展示 Trevor 的总结"，而是让访客选择进入哪段经历

### 英文版（work.html）

| 条目 | 名称 | 年份 | 链接 |
|------|------|------|------|
| Experience | Decathlon | 2025–2026 | decathlon.html |
| Experience | Mayora | 2024–2025 | mayora.html |
| Experience | SynTao | 2024 | 无（纯文本） |
| Experience | Tianfeng Securities | 2022 | 无（纯文本） |
| Projects | O2O CNY Promotion | 2025 | cny-campaign.html |
| Projects | WeChat Mini Program UX Optimization | 2026 | decathlon-ux.html |

### 中文版（zh-work.html）

| 条目 | 名称 | 年份 | 链接 |
|------|------|------|------|
| 经历 | 迪卡侬 | 2025–2026 | decathlon.html |
| 经历 | 迈大食品 | 2024–2025 | mayora.html |
| 经历 | 商道纵横 | 2024 | 无 |
| 经历 | 天风证券 | 2022 | 无 |
| 项目 | 即时零售CNY大促 | 2025 | cny-campaign.html |
| 项目 | 微信小程序用户体验优化 | 2026 | decathlon-ux.html |

---

## 2. 设计决策全记录

### 2.1 整体方向
- **风格**：rauno.me 子页面启发——极度克制、editorial、无装饰
- **布局**：居中窄列 max-width 680px，垂直居中于视口
- **Topbar**：fixed 定位，"← Home" 左上角，语言切换 + 主题切换右上角
- **分组**：Experience 和 Projects 之间仅用 48px 空白分隔，无 label
- **无 footer**：页面到底就是列表结束，什么都不加
- **排序**：reverse chronological（新的在上）

### 2.2 入场动画 — v9（Rise + Fade）

这是经过多个版本迭代后的最终方案：

| 版本 | 方案 | 为什么被淘汰 |
|------|------|-------------|
| v1–v3 | 纯 clip-path 中心展开 | 太简单，缺少文本层动画 |
| v4 | 逐帧字母 scramble（每 16ms 换字符，含符号） | 太夸张，过于喧闹 |
| v5 | 字母 scramble（90ms tick，仅字母） | tick 太慢，看着卡 |
| v6 | 字母 scramble（45ms tick，仅字母） | 仍然偏"技术感"，不够 editorial |
| v7 | 字符 stagger fade-in（opacity 0→1） | 太微妙，不够有存在感 |
| v8 | 纯 clip-path 整行展开 | 太简单 |
| v10 | Focus Pull（blur → 清晰） | 太戏剧化 |
| v11 | Staggered Center Clip | 和 v8 太接近 |

**v9 最终规格：**
- 每行整体：`opacity: 0 → 1` + `transform: translateY(12px) → 0`，duration 700ms，easing `cubic-bezier(.22,1,.36,1)`
- 点线（dot leader）：`clip-path: inset(0 50% 0 50%) → inset(0 0% 0 0%)`，duration 900ms，同一 easing
- 行间 stagger：100ms，自上而下波纹
- 初始延迟：200ms（等字体加载）
- 所有行同时开始动画序列，不等待前一行完成

### 2.3 Focus Hover 效果
- 入场动画完成后激活（通过 JS 添加 `.ready` class，防止动画期间被 hover 干扰）
- 列表 hover → 所有行 dim 到 `opacity: 0.35`（transition 300ms）
- 单行 hover → 该行恢复 `opacity: 1`
- 移动端触摸设备禁用（`@media (hover: none)`）

### 2.4 页面退出过渡
- 点击可链接名称 → `body.page-out` → main `opacity: 0, translateY(8px)`（180ms）
- 过渡完成后 `window.location.href` 跳转
- 仅可链接的 name 触发（SynTao / Tianfeng 无此效果）

### 2.5 主题切换
- 完整克隆主页实现
- 内联 `<script>` 在 head 中读取 localStorage 防闪烁
- 太阳/月亮 SVG icon 切换
- 暗色模式：bg #18181B, fg #FAFAFA, accent #A78BFA, dot leader 颜色为 `rgba(255,255,255,0.12)`

---

## 3. 技术实现细节

### 3.1 技术选型
- **纯手写 CSS**（未使用 Tailwind CDN，因为页面极简不需要）
- 设计 tokens 完整复制自 index.html（`:root` 和 `[data-theme="dark"]`）
- Google Fonts：Geist + Nunito Sans + JetBrains Mono（中文版加 Noto Sans SC）
- 珊瑚光标 `#E07B5A`：CSS `cursor: url(data:image/svg+xml,...)` — 默认 r=7px，可交互元素 r=8px

### 3.2 关键 CSS 结构

```css
/* 页面居中 */
main {
  max-width: 680px; margin: 0 auto; padding: 0 32px;
  min-height: 100vh;
  display: flex; flex-direction: column; justify-content: center;
}

/* Topbar — 固定在视口上方，不阻挡内容点击 */
.topbar {
  position: fixed; top: 0; left: 0; right: 0; z-index: 50;
  display: flex; align-items: center; justify-content: space-between;
  padding: 24px 32px;
  pointer-events: none;  /* 整个 bar 不阻挡下方内容 */
}
.topbar > * { pointer-events: auto; }  /* 子元素可点击 */

/* 行布局 — flex 三点式：名称 + 点线 + 年份 */
.entry-row { overflow: hidden; padding: 14px 0; }
.row-unit { display: flex; justify-content: space-between; align-items: center; }
.name { flex-shrink: 0; white-space: nowrap; }  /* 名称不换行不收缩 */
.dot-leader { flex: 1; min-width: 24px; }       /* 点线自动填充剩余空间 */
.year { flex-shrink: 0; white-space: nowrap; }   /* 年份不换行不收缩 */

/* Focus 效果 — 通过 .ready class 激活，避免入场动画期间误触发 */
.entry-list.ready .row-unit { transition: opacity 300ms ease; }
.entry-list.ready:hover .row-unit { opacity: 0.35; }
.entry-list.ready .row-unit:hover { opacity: 1; }
```

### 3.3 关键 JS 结构

```javascript
// 入场动画
const ROW_STAGGER = 100;  // 行间延迟
function playEntry() {
  units.forEach((unit, i) => {
    setTimeout(() => {
      unit.classList.add('revealed');           // opacity + transform
      unit.querySelector('.dot-leader').classList.add('revealed');  // clip-path
    }, i * ROW_STAGGER);
  });
}
setTimeout(playEntry, 200);  // 等待字体加载

// Focus 效果延迟激活
const animEnd = 200 + (totalRows - 1) * ROW_STAGGER + 700;
setTimeout(() => {
  document.querySelector('.entry-list').classList.add('ready');
}, animEnd);
```

### 3.4 主页 Panel 跳转修复

Work panel 原来直接跳到 `decathlon.html`（旧行为）。修改为：
- `index.html` WORK → `work.html`
- `zh.html` WORK → `zh-work.html`

两个主页文件在**主 worktree** 和**本 worktree** 中均做了修改。

---

## 4. 文件变更清单

### 新建文件
| 文件 | 用途 |
|------|------|
| `work.html` | Work 索引页（EN） |
| `zh-work.html` | Work 索引页（ZH） |

### 修改文件
| 文件 | 变更 |
|------|------|
| `index.html` | WORK panel `href` 从 `decathlon.html` → `work.html` |
| `zh.html` | WORK panel `href` 从 `decathlon.html` → `zh-work.html` |
| `CLAUDE.md` | 新增 work 索引页描述、更新文件结构、更新优先级 |
| `ROADMAP.md` | work index page 和 panel navigation 标记为完成、新增 decision log |

### Git 提交记录
```
b32e34d fix: update Chinese work index entry names
c71138d docs: update CLAUDE.md and ROADMAP.md for work.html completion
59d2daf fix: update work index entry names for clarity and accuracy
83ba119 fix: route WORK panel to work index page instead of decathlon detail
8e6f2ec feat: add work index page with editorial entry animation
```

---

## 5. 当前项目状态

### 已完成
- [x] 横向 5-panel 首页（index.html / zh.html）— 完整部署
- [x] Work 索引页（work.html / zh-work.html）— 本次完成
- [x] Panel 跳转逻辑修复（WORK → work 索引页）
- [x] 入场动画（Hero frame + circle + text reveal + panel fade-in）
- [x] 珊瑚自定义光标全站统一
- [x] 暗色模式（localStorage 持久化）
- [x] 所有详情页（decathlon / mayora / cny-campaign / decathlon-ux）
- [x] 故事页（darts / ai + 中文镜像）
- [x] Compact floating nav（B3-lite pill）

### 尚未完成（优先级排序）
1. **子页面统一新设计** — decathlon / mayora / cny-campaign / decathlon-ux / ai / darts 这些子页面视觉上和主页不一致（旧字体、无双色板、无珊瑚光标）
2. **中文版 detail pages** — zh-decathlon.html, zh-mayora.html 等尚未创建
3. **Now 页面 / 区块** — 需 Trevor 提供内容
4. **Writing 区块** — 占位结构

### 已知 Bug
- 点击涟漪效果：独立 test 页可行，index.html 中不生效（Tailwind 或 JS 冲突）
- 部分子页面跨链接混乱

---

## 6. 给新 Agent 的上下文

### 必读文件（按顺序）
1. `CLAUDE.md` — 项目总览、设计系统、规则
2. `ROADMAP.md` — 已完成/待办/规划
3. `Trevor_WorkContext_ForWebsite.md` — 工作经历 data source
4. `Trevor_WorkExperience_Memory_01.md` — 工作经历详细版
5. 本文件 — Session 上下文

### 设计系统（不可随意改动）
- 颜色 tokens：bg #E8E8E8, fg #1C1917, accent #7C3AED, fg-2 #57534E, fg-3 #A8A29E
- 字体：Geist（标题/大字）→ Nunito Sans（正文）→ JetBrains Mono（标签/日期）
- 中文加 Noto Sans SC
- 珊瑚光标 #E07B5A，r=7px 默认 / r=8px 可交互 / 拖拽区用系统光标
- 暗色模式 `data-theme="dark"` + localStorage

### 工作环境
- 仓库：`thuang17/thuang17.github.io`
- 主 repo 路径：`/Users/h3art/Documents/github/personal-website/`
- 零构建步骤，单 HTML + Google Fonts
- 子页面用 inline SVG 做图标（Lucide CDN 曾经加载失败）

### Trevor 的内容偏好
- Tone：casual business — 自信直接有主见，像聪明人在聊天
- 去 AI 味：不用"通过...实现了..."、不用过度排比、不用"此外"/"综上"
- 英文版第一人称叙述，有具体细节和决策逻辑
- 中文版口语化接地气，不堆砌术语
- 不出 "Project Manager" 头衔

### Brainstorming 记录
存放在 `.superpowers/brainstorm/34756-1777958132/content/`，包含 page-entry-v1 到 v11 的动画迭代 HTML。仅作参考，不要删。临时 Playwright 脚本（rauno-*.js）在 worktree 根目录，也仅作参考。

---

*撰写：2026-05-05 · Session ID: aef9eb62-bac9-437f-a9b7-904a72cf923d*

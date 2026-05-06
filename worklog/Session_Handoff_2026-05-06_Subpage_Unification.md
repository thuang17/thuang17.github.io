---
name: Session handoff — Sub-page Visual Unification (2026-05-06)
description: Comprehensive record of the session that unified all sub-page designs, built nav overlay, created Stories index, and synced Chinese versions
type: project
originSessionId: aef9eb62-bac9-437f-a9b7-904a72cf923d
---

# Session Report: Sub-page Visual Unification — Trevor Huang Personal Website

**日期：** 2026-05-05 → 2026-05-06
**分支：** `claude/bold-mahavira-f48b76` → 已合并至 `main`
**GitHub：** https://github.com/thuang17/thuang17.github.io
**线上：** https://thuang17.github.io

---

## 1. 本 Session 完成了什么

### 核心交付：6 个子页面视觉统一 + 导航浮框 + Stories 索引页 + 中文版同步

从 Work 索引页完成后，下一步是统一所有子页面的视觉风格。经过 brainstorming 确认了三个方向的差异化：

- **Work（热）**：editorial longform，文字为主，数据+叙事
- **Making（温）**：timeline，竖线+光标圆点，轻量阅读
- **Stories（冷）**：水平照片传送带，图片驱动

### 页面变更总览

| 页面 | 变更 | 新设计 |
|------|------|--------|
| decathlon.html | 重写 | Editorial longform + scroll ruler + data island + nav overlay |
| mayora.html | 重写 | 同模板，CNY campaign 内容合并 |
| ai.html | 重写 | Timeline 布局 + 跟随 cursor 紫色圆点 |
| darts.html | 重写 | 水平传送带 gallery + 16:9 裁剪 + 飞镖刻度指示器 |
| stories.html | 新建 | Work.html 风格索引页，Darts · 2021–Now |
| work.html | 修改 | 删 Projects 两行，删 ← 箭头 |
| zh-work.html | 修改 | 同上，中文版 |
| zh-stories.html | 新建 | 中文 Stories 索引（飞镖 · 2021–至今） |
| zh-decathlon.html | 新建 | 中文 editorial longform |
| zh-mayora.html | 新建 | 中文 editorial longform，CNY 内容 |
| zh-ai.html | 更新 | 同步 timeline + cursor dot |
| zh-darts.html | 更新 | 同步传送带 gallery |
| index.html | 修改 | Stories panel → stories.html |
| zh.html | 修改 | Stories panel → zh-stories.html |

---

## 2. 设计决策全记录

### 2.1 内容架构（Option A）

**决策：** 取消 Projects 分类，将项目内容合并到工作经历页面。

- `work.html` 删除 Projects 两行（CNY Campaign + WeChat UX / 即时零售CNY大促 + 微信小程序UX优化）
- `decathlon-ux.html` 和 `cny-campaign.html` 保留文件但不再从 work.html 入口
- 项目内容融入了 decathlon.html 和 mayora.html

**理由：** 经历不够厚，强行拆分导致两处内容都薄弱。

### 2.2 子页面统一设计系统

所有子页面共享的设计 tokens，与 index.html 和 work.html 一致：

```css
--bg:      #E8E8E8;
--bg-sub:  #F0EEE8;
--fg:      #1C1917;
--fg-2:    #57534E;
--fg-3:    #A8A29E;
--border:  #E7E5E4;
--accent:  #7C3AED;
```

暗色模式：`#18181B` / `#FAFAFA` / `#A78BFA`
字体：Geist（标题）+ Nunito Sans（正文）+ JetBrains Mono（标签）
珊瑚光标：`#E07B5A`，r=7px 默认 / r=8px 可交互

### 2.3 入场动画

- 所有详情页：400ms opacity 0→1 + translateY 6px→0，ease-out
- 菜单列表页（work/stories）：v9 Rise+Fade 逐行 700ms + dot leader 中心展开 900ms + 100ms stagger
- 有 `prefers-reduced-motion` 保护

### 2.4 退出过渡

- 链接点击触发 `body.page-out` → main `opacity:0, translateY:8px`, 180ms
- 过渡完成后 `window.location.href` 跳转

### 2.5 导航浮框（Nav Overlay）

所有内容页（decathlon/mayora/ai/darts）左上角改为三条杠 hamburger，点击展开目录浮框：

```
Homepage
Work
  Decathlon (当前页高亮)
  Mayora
  SynTao
  Tianfeng Securities
───────
Making
Stories
Info → 触发 Info 浮层（同主页设计）
```

- Index / 首页 保持 "Home" 纯文字
- work.html／stories.html 保持 "Home" 纯文字（导航页不需要 nav overlay）

### 2.6 Info 浮层

精确复制主页的 Info overlay 设计：
- 两列布局：Education + Contact & Social，底部 Toolkit 全宽
- 背景 `color-mix(in srgb, var(--bg) 50%, transparent)` + `blur(12px)`
- 圆角 20px，阴影 `0 24px 72px`
- 字号、字体、间距与主页完全一致

---

## 3. 各页面详细设计

### 3.1 decathlon.html — Editorial Longform

**布局：** 单列居中 680px，无 TOC、无 footer、无 next link

**topbar：** fixed，三条杠 + 语言/主题切换

**标题架构：**
- Decathlon（Geist 48px, weight 400）
- E-commerce Technology PM Intern · 2025–2026（Nunito Sans 16px）

**段落：** body-lg 18px（开场）/ body-text 16px（正文），line-height 1.8，section 间距 80px

**数据岛：** 2 列，上下 border 框住，40px 数字 + mono 标签
- 16 pain points identified via competitive benchmarking
- 2 scoring dimensions

**Pull quote：** 左边框 1px accent + italic，上下 margin 52px

**Scroll ruler + reading line：**
- 左侧竖线 48px，范围 25vh–75vh
- 40 个刻度（wave 效果：附近放大，远离恢复）
- 紫色横线 1.5px，opacity 0.55，随 scroll 平滑移动（transform: translateY）

**段落结构：**
1. Opening（untitled）
2. WeChat Mini Program UX（含数据岛 + pull quote）
3. UAT Coordination（含 pull quote）
4. PM Tool Optimization
5. Reflection

### 3.2 mayora.html — Editorial Longform + CNY Merged

同 decathlon 设计。CNY 数据岛：
- 7.22 gift box overall campaign ROI
- ~600% new product growth vs baseline

**段落结构：**
1. Opening
2. CNY Campaign（合并原 cny-campaign.html 的预算、人群策略、两轮优化、ROI）
3. Daily O2O Operations
4. Reflection

### 3.3 ai.html — Timeline 布局

**格式：** 左竖线 + 右文字，5 个阶段

**时间线条：** 1.5px，fg-3，opacity 0.5

**阶段节点：** 空心圆点 border，transparent 背景（竖线贯穿不中断）

**Cursor 跟随圆点：**
- 紫色实心圆点，始终可见
- 跟随鼠标 Y 轴在竖线范围内移动（clamped 0–timeline.height）
- 使用 requestAnimationFrame 60fps 平滑追踪
- 鼠标在页面任意位置生效

**5 个阶段：**
1. ChatGPT as a workaround
2. NotebookLM made the system visible
3. Prompts as thinking tools
4. Claude moved it to execution
5. First product in a weekend

### 3.4 darts.html — 水平传送带 Gallery

**容器：** 暖灰色背景 #E8E8E8，无白色卡片

**标题：** "Darts" Geist 36px，无副标题

**刻度条 + 飞镖指示器（标题下方）：**
- 200px 宽，9 个刻度（24px 高，像从侧面看的板子）
- 飞镖图标（自定义 SVG：直杆 + 左尾翼 + 右箭头 → 后来换成用户提供的 PNG）
- 飞镖水平向右，跟随 scroll 进度移动
- **最终版本：** 用户提供的 PNG，背景透明化（PIL 处理），10 倍放大

**画廊：**
- 原 7 张 → 8 张 → 最终 9 张图片（16:9 裁剪，object-fit: cover）
- 76vw 宽，max 960px，圆角 24px，阴影 0 2px 24px
- 非活跃图：opacity 0.4 + scale 0.88
- 原生横向滚动（overflow-x: auto），隐藏 scrollbar
- 底部索引：01 / 09
- 图片不可点击、不可保存（pointer-events: none, user-select: none, draggable: false）
- loading="lazy" → eager（修了横滚加载 bug）

**交互探索（未采用）：**
- 首字下沉（drop cap）→ 去掉
- 阅读聚光灯（段落左边框高亮）→ 和 pull quote 冲突，去掉
- 垂直传送带 → 不满足，回滚

---

## 4. 技术实现细节

### 4.1 核心交互

**Scroll ruler + wave：** transform: translateY + requestAnimationFrame 实现平滑追踪。40 个动态生成的 tick，按 scroll 进度计算波峰位置。

**水平传送带：** `overflow-x: auto` 原生滚动，JS 监听 scroll 事件计算每张图到视口中心的距离，应用 scale/filter/opacity。GPS 加速通过 `will-change: transform, filter, opacity`。

**Timeline cursor dot：** 绝对定位在 timeline 容器内，mouse mousemove → requestAnimationFrame → 计算相对 Y → clamp 到容器高度 → 设置 `style.top`。

### 4.2 Key CSS 模式

```
/* Nav overlay */
.nav-overlay {
  position: fixed; inset: 0; z-index: 60;
  background: rgba(0,0,0,0.2);
  display: none; align-items: flex-start;
  padding: 80px 32px;
}
.nav-overlay.open { display: flex; }

/* Gallery dim effect */
.slot img.dim {
  opacity: 0.4; transform: scale(0.88);
  transition: transform .4s ease, opacity .4s ease;
}
```

### 4.3 性能优化

- `loading="lazy"` → `loading="eager"` 修复横滚图加载
- `will-change: transform` 为动画元素启用 GPU 层
- `prefers-reduced-motion: reduce` 禁用所有动效
- `pointer-events: none` 禁用图片交互 + `-webkit-user-drag: none` 防拖拽

### 4.4 光标统一

所有交互元素使用 `cursor: inherit` 从父级继承珊瑚光标。修复 `.info-close` 的 `cursor: pointer` 覆盖 bug。`.nav-panel a, .nav-panel button` 显式设置珊瑚光标 URL。

---

## 5. 文件变更清单

### 新建文件
| 文件 | 用途 |
|------|------|
| `stories.html` | Stories 索引页（EN） |
| `zh-stories.html` | Stories 索引页（ZH） |
| `zh-decathlon.html` | Decathlon 中文详情页 |
| `zh-mayora.html` | Mayora 中文详情页 |
| `docs/superpowers/specs/2026-05-05-subpage-visual-unification-design.md` | 设计规格 |
| `docs/superpowers/plans/2026-05-05-subpage-visual-unification.md` | 实施计划 |
| `darts/挑选/2/*.jpg/*.png` | 9 张新飞镖照片 |

### 修改文件
| 文件 | 变更 |
|------|------|
| `decathlon.html` | Editorial longform + scroll ruler + nav overlay |
| `mayora.html` | Editorial longform + CNY 合并 + nav overlay |
| `ai.html` | Timeline + cursor dot + nav overlay |
| `darts.html` | 横向传送带 + 飞镖刻度 + nav overlay |
| `work.html` | 删 Projects 两行，删 ← |
| `zh-work.html` | 同上，中文版 |
| `index.html` | Stories panel → stories.html |
| `zh.html` | Stories panel → zh-stories.html |
| `zh-ai.html` | 同步 timeline 设计 |
| `zh-darts.html` | 同步传送带设计 |

### 删除内容
- Projects 2 行从 work.html/zh-work.html 移除
- 飞镖页原有 7 章流水账文字（改为纯图片 gallery）
- 各页旧版 Montserrat 字体 → Geist
- 各页旧版 `#FAFAF8` 背景 → `#E8E8E8`
- 旧版 breadcrumb nav → hamburger nav overlay
- 各页 footer 和 next link

---

## 6. 已知问题 / 待解决

1. **编辑长文页面"读起来太累"** — 已记入 memory。Dropdown、pull quote、data island、ruler+line 已缓解但核心问题仍在。后续考虑内容层面的减法，而非交互层增加元素。**优先级：低**
2. **Making 页面当前内容偏薄** — Timeline 只有 5 个阶段，后续添加产品和项目后更充实
3. **Stories 索引页目前只有飞镖** — 添加 hiking 等内容后自然丰富

---

## 7. Git 提交记录（按时间顺序）

```
7388746 fix: add favicon cache-busting and apple-touch-icon to new pages
c80ce99 feat: add zh-decathlon, zh-mayora, update zh Stories link
fbe22f6 feat: add zh-stories, zh-darts, zh-ai Chinese pages
ad56644 feat: add Stories index page, route all Stories links to stories.html
26e4c27 revert: restore left-line right-text timeline layout
d18bd69 feat: center timeline line with alternating left/right text blocks
0b6c878 fix: smooth cursor dot with rAF + transform, constrained to line X
7e3eb32 feat: thicker timeline line + cursor-following purple dot
fd6f2d2 feat: redesign Making page as vertical timeline
0be00fa fix: add work.html link to Work in nav panel
6b644ed fix: explicit coral cursor on nav-panel instead of inherit
ecf2df5 fix: info-close cursor: pointer → inherit for coral consistency
...（共 81 个 commit）
```

---

## 8. 给新 Agent 的上下文

### 页面"阅读温度"差异
- **Work（decathlon/mayora）**：Editorial longform，scroll ruler，数据岛 — 访客在"读"
- **Making（ai）**：Timeline + cursor dot — 访客在"看"时间线
- **Stories（darts）**：水平传送带 gallery，无文字 — 访客在"翻"

### Nav Overlay 规则
- 内容页（decathlon/mayora/ai/darts）：左上角三条杠 hamburger
- 索引页（work/stories）：保留 "Home" 纯文字
- 主页（index/zh）：不做改动

### 重要技术决策
- 所有页面使用 `favicon.png?v=2` + `apple-touch-icon.png`
- `loading="lazy"` 在横向 overflow 容器中有 bug，改为 `loading="eager"`
- 飞镖页图片不可点击/保存：`pointer-events: none` + `-webkit-user-drag: none`
- 中文版同步完成，所有 EN/ZH 成对

### 文件结构说明
```
docs/superpowers/specs/2026-05-05-subpage-visual-unification-design.md   — 设计规格
docs/superpowers/plans/2026-05-05-subpage-visual-unification.md           — 实施计划
darts/挑选/2/                                                             — 9 张 16:9 飞镖照片
```

---

*撰写：2026-05-06 · Session merged to main · 81 commits, 29 files changed*

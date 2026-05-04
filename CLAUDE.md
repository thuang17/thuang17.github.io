# CLAUDE.md — Trevor Huang Personal Website

每次新 session 开始时先读这个文件，以及 `Trevor_WorkContext_ForWebsite.md` 和 `Trevor_WorkExperience_Memory_01.md`。

---

## 项目概述

Trevor Huang（黄拓文）的个人网站。GitHub Pages 托管，静态页面，无构建步骤。
当前方向不是“求职站优先”，而是：

- **personal website first**
- **proof-bearing site second**

首页不再默认服务于 HR 扫描，而是作为一个克制的个人入口页，让访客先选择从哪条线进入 Trevor。

- **英文版**：`index.html`（主版本，默认入口）
- **中文版**：`zh.html`
- 两个版本内容和结构保持同步，语言不同

---

## 技术栈

- 单 HTML 文件 + Tailwind CDN + Google Fonts
- 零构建步骤，直接 GitHub Pages 部署
- 当前阶段不引入框架（React / Vue 等）——保持部署简单。如后期需要复杂功能可以引入，届时需要同步调整部署方式
- 图标目前用内联 SVG（曾遇到 Lucide CDN 加载失败的 bug）。如需使用外部图标库，确保加载方式可靠即可

---

## 设计系统（已定，不要随意改动）

### 颜色 tokens
```css
--bg:       #FAFAF8   /* 页面背景 */
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
- **标题 / 大字**：Montserrat（700, 800）→ `--f-display`
- **正文**：Nunito Sans（300, 400, 500, 600）→ `--f-body`
- **标签 / 日期 / mono**：JetBrains Mono（300, 400）→ `--f-mono`
- 中文版额外加载 Noto Sans SC 作为中文 fallback

### 布局
- 统一容器宽度：`max-width: 1080px`，`padding: 0 48px`
- 类名：`.wrap` 和 `.wrap-w`（两个都是同一宽度，历史遗留，不用区分）
- Nav inner 同样 1080px / 48px

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
- 英文版 nav 有「中文」链接 → `zh.html`
- 中文版 nav 有「EN」链接 → `index.html`

---

## 网站结构（当前已实现）

```
Homepage first fold   → personal index
Primary entries       → Work / AI-Making / Stories
Work                  → 迪卡侬 / 迈大食品 / 商道纵横 / 天风证券
Selected proof        → CNY O2O 大促 / 迪卡侬 UX 研究
Skills                → 4列 grid（后续可能降权或并入 info）
Stories bridge        → 飞镖 + AI 探索的过渡说明（后续继续调整）
Education             → 悉尼大学 + 上外
Contact               → 邮件 + LinkedIn
Footer                → 社交图标（Email / LinkedIn / Instagram / X / 小红书）
```

### Primary entries 的含义
- **Work**：最能说明判断力的真实工作内容，不是完整履历档案
- **AI / Making**：工具、实验、搭东西、自主把想法变成产物的那一面
- **Stories**：用来解释 Trevor 为什么会这样做事的个人材料

内容边界：
- `darts` 属于 `Stories`
- `AI` 不应再主要属于 `Stories`
- `ai.html / zh-ai.html` 后续应逐步向 `AI / Making` 重构

---

## 待办 / 规划

详见 `ROADMAP.md`。

### 下一阶段优先级
1. 收掉首页下半部分仍然偏 resume-scan 的结构
2. 把 `ai.html / zh-ai.html` 从“AI 故事页”重构成更像 `AI / Making`
3. 再决定 `Skills / Education / Contact` 应该怎样继续降权或迁移
4. `Now` 页面 / 区块（需 Trevor 提供内容）
5. Writing 区块占位（内容后续填充）

### 暂缓事项
- 自定义域名（先用免费 github.io）
- CSS View Transitions 项目详情页
- 照片（待 Trevor 提供）
- 中英文内容深度对齐（仍需持续收口）

---

## 文件结构

```
personal-website/
├── index.html                          # 英文版（主）
├── zh.html                             # 中文版
├── avatar.png                          # 卡通头像（透明背景）
├── Anime Image Avatar.png              # 原始头像（不使用）
├── CLAUDE.md                           # 本文件
├── ROADMAP.md                          # 项目规划
├── docs/superpowers/specs/2026-05-03-personal-index-direction-design.md
│                                       # 首页方向 spec（重要）
├── Trevor_WorkContext_ForWebsite.md    # 工作经历 source of truth (v1)
└── Trevor_WorkExperience_Memory_01.md  # 工作经历 source of truth (v2，更详细)
```

---

*最后更新：2026-05-03*

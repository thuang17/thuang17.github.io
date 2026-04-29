# CLAUDE.md — Trevor Huang Personal Website

每次新 session 开始时先读这个文件，以及 `Trevor_WorkContext_ForWebsite.md` 和 `Trevor_WorkExperience_Memory_01.md`。

---

## 项目概述

Trevor Huang（黄拓文）的个人网站。GitHub Pages 托管，静态单页，无构建步骤。
目标受众：中国国内公司 + 在华外企的 HR 和招聘方。

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

### 卡通头像
- 文件：`avatar.png`（AI 抠图，透明背景，1254×1254 RGBA）
- 原始文件：`Anime Image Avatar.png`（有白色背景，不使用）
- 显示在 hero 区右侧，宽 248px

---

## 内容规则

### Tone
- **Casual business**：自信、直接、有主见，像一个聪明的人在聊天，不像在背稿
- **去 AI 味**：不用"通过...实现了..."、不用过度并列排比、不用"此外"/"综上"
- **英文版**：第一人称叙述，有具体细节和决策逻辑
- **中文版**：口语化，接地气，不堆砌术语

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
Hero          → 姓名 + bio + chips + 卡通头像
Work          → 迪卡侬 / 迈大食品 / 商道纵横 / 天风证券
Projects      → CNY O2O 大促 / 迪卡侬 UX 研究
Skills        → 4列 grid（PM / 数据 / 工具 / AI）
About         → 飞镖 + AI 探索（待丰富）
Education     → 悉尼大学 + 上外
Contact       → 邮件 + LinkedIn
Footer        → 社交图标（Email / LinkedIn / Instagram / X / 小红书）
```

---

## 待办 / 规划

详见 `ROADMAP.md`（待建）。

### 下一阶段优先级
1. 建 `ROADMAP.md` 作为项目管理文件
2. About 区块内容丰富化（飞镖故事 + AI 探索故事，需 Trevor 提供素材）
3. Now 页面 / 区块（需 Trevor 提供内容）
4. Writing 区块占位（内容后续填充）
5. GitHub 建仓 + GitHub Pages 部署

### 暂缓事项
- 自定义域名（先用免费 github.io）
- CSS View Transitions 项目详情页
- 照片（待 Trevor 提供）
- 中英文内容深度对齐（目前英文版更完整）

---

## 文件结构

```
personal-website/
├── index.html                          # 英文版（主）
├── zh.html                             # 中文版
├── avatar.png                          # 卡通头像（透明背景）
├── Anime Image Avatar.png              # 原始头像（不使用）
├── CLAUDE.md                           # 本文件
├── ROADMAP.md                          # 项目规划（待建）
├── Trevor_WorkContext_ForWebsite.md    # 工作经历 source of truth (v1)
└── Trevor_WorkExperience_Memory_01.md  # 工作经历 source of truth (v2，更详细)
```

---

*最后更新：2026-04-28*

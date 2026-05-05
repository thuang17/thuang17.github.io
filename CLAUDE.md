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
- 英文版 nav 有「中文」链接 → `zh.html`
- 中文版 nav 有「EN」链接 → `index.html`

---

## 网站结构（当前已实现）

```
首页 → 横向 5-panel surface（Hero / Work / Making / Stories / Info）
- Hero：Geist 5行文字 + 淡紫大圆 + 入场缩放动画
- Work / Making / Stories：90px Geist 全大写标题 + 左对齐副标题 + 不对称裁切布局
- Stories panel：深色背景作为明暗对比
- Info panel：超大 “Info” 文字（o 被裁切）→ 点击弹出浮层
- Info overlay：Education / Toolkit / Contact 宽幅布局
- Scrubber：200px 轨道 + 胶囊（hover 放大 + 可拖拽）
- Nav：中文/EN + 太阳/月亮主题切换（无边框），与 Scrubber 同行
- 入场动画：Hero frame 1200ms 缩放 → 圆延迟缩放 → 文字逐行 clip reveal → 其余 panel 淡入
```

### Work 索引页（work.html / zh-work.html）
- 纯 editorial directory：Experience 4 行 + Projects 2 行，reverse chrono
- v9 入场动画：每行 12px 上浮 + 淡入（700ms），点线中心展开（900ms），自上而下 100ms 波纹
- Focus hover：列表 hover 后其余行 dim 到 0.35，hover 单行恢复
- Fixed topbar：`← Home` 左上 / 语言+主题切换右上
- 无标题、无分割线、无 footer，48px gap 分隔 Experience 和 Projects
- 名称更新：Tianfeng Securities / O2O CNY Promotion / WeChat Mini Program UX Optimization
- 中文镜像使用中文公司/项目名称

### 子页面
- **Work 索引页**：`work.html` / `zh-work.html` — editorial directory，v9 入场动画，已适配新设计
- **详情页（尚未适配新设计）**：`decathlon.html` / `mayora.html` / `cny-campaign.html` / `decathlon-ux.html`
- **故事页**：`darts.html` / `ai.html` + 中文镜像
- `zh-*` 中文镜像（部分尚未创建）

---

## 待办 / 规划

详见 `ROADMAP.md`。

### 下一阶段优先级
1. 子页面（decathlon / mayora / ai / darts 等）适配新设计的风格和布局
2. `Now` 页面 / 区块（需 Trevor 提供内容）
3. Writing 区块占位（内容后续填充）
4. 中文版 detail pages（zh-decathlon.html, zh-mayora.html 等）

### 暂缓事项
- 点击涟漪效果（已尝试多次未成功，记录在 ROADMAP.md 待排查）
- `ai.html / zh-ai.html` 重构为 `AI / Making`
- 自定义域名（先用免费 github.io）
- CSS View Transitions 项目详情页
- 照片（待 Trevor 提供）

---

## 文件结构

```
personal-website/
├── index.html                          # 英文版（主）
├── zh.html                             # 中文版
├── work.html                           # Work 索引页（EN）
├── zh-work.html                        # Work 索引页（ZH）
├── CLAUDE.md                           # 本文件
├── ROADMAP.md                          # 项目规划
├── explorations/                       # 横向 homepage demo（交互验证用，保留）
├── docs/superpowers/specs/             # 设计 spec
├── docs/superpowers/plans/             # 实现 plan
├── Trevor_WorkContext_ForWebsite.md    # 工作经历 source of truth (v1)
└── Trevor_WorkExperience_Memory_01.md  # 工作经历 source of truth (v2，更详细)
```

---

*最后更新：2026-05-05*

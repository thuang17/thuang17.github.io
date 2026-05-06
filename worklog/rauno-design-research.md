# Rauno.me 设计研究 & 项目推进记录

## 一、插件安装

### UI/UX Pro Max

- **方式一（CLI）成功**
  - `npm install -g uipro-cli` → 23 packages installed
  - `uipro init --ai claude` → 安装到 `.claude/skills/ui-ux-pro-max/`
  - `search.py` 验证通过（fintech crypto 设计系统搜索正常）

### Superpowers

- `/plugin install superpowers@claude-plugins-official` → 已安装（scope: user）
- 核心 skills 验证通过：
  - brainstorming ✓
  - test-driven-development ✓
  - writing-plans ✓
  - executing-plans ✓
  - verification-before-completion ✓
- 共 20 个 skill 可用

---

## 二、参考网站：Rauno.me

> 我们的主页风格和 rauno.me 基本一致，已确定主基调。后续页面需要视觉统一，但**不能照搬**——内容完全不同。

---

### Rauno.me 设计分析

#### 主页

- **极端文字驱动**：名字拆成碎片逐行排列（"Rauno / Freiberg / is an Estonian / interaction / designer..."），读者在阅读中拼凑出身份
- **类 concrete poem**：每一行文字都是刻意放置的视觉单元，靠断行和留白建立层级
- **单色/近无色**：黑白灰，让排版和间距承担全部视觉重量
- **底部三个极简 icon** 作为次级导航入口

#### /craft 页面（作品/项目列表）

- 网格卡片系统，responsive tiled card，按时间倒序
- 每张卡片结构：日期（大写，极灰，极小）+ 标题（medium weight，14-16px）+ CTA（"Read Essay" / "View Production" / "View Prototype" 三种意图区分）
- 间距克制：卡片之间 32-48px，padding 24-32px
- 底部导航：(/) /craft /projects 三个链接，11px 灰色，极度不显眼
- 没有分类、没有筛选：强制线性浏览，靠时间顺序制造偶遇感

#### /projects 页面

- 更极端：只有项目名 + 年份，连描述、缩略图、分割线都没有
- 纯文字列表，信任读者凭名字判断是否点进去

#### 共同特点

- 极端克制 — 相信留白和排版就足够，不要任何多余元素
- 去装饰化 — 没有 emoji、没有彩色标签、没有阴影卡片
- 内容即结构 — 不靠 UI 组件组织信息，靠文字本身
- 时间倒序 — 用时间线而非分类作为默认组织方式
- 底部极简 nav — 三个裸链接，几乎隐身

---

### 与我们的主页对比

| 维度 | Rauno | 我们 |
|------|-------|------|
| 滚动方向 | 垂直 | 横向 5-panel |
| 色彩 | 几乎单色 | 灰白底 + 紫色 accent + 珊瑚光标 |
| 字体 | Geist 为主 | Geist + Montserrat + Nunito Sans |
| 动效 | 几乎无 | 入场动画 + panel 过渡 |
| 导航 | 底部裸链接 | Scrubber + Topbar |
| 气质 | brutalist-minimalist | editorial-minimal（稍微暖一点） |

**结论**：我们的主基调（Geist 大字、大留白、文字优先、克制配色）已经和 rauno 在同一频道，但我们更暖（珊瑚光标、灰白底而非纯白），且横向滚动是独有的交互差异点。

---

## 三、Rauno.me 深度交互分析（Playwright 实测）

### 核心技术发现

- **首页是交互式的**，不是静态页面
- **Camera/Pan 系统**：整个首页是一个可拖拽/滚动的画布，`main[data-sheet="index"]` 高达 6108px
- 通过 `.pan-camera`、`.cursor-resizing-ew`、`.cursor-moving`、`.cursor-grabbing` 这些 class 控制交互模式
- Scrollbar 隐藏：`::-webkit-scrollbar { display: none }`
- `overscroll-behavior: none`，桌面端 `touch-action: pan-x pan-y`
- 文字碎片在一个可探索的二维空间中，用户拖拽时文字和元素以不同速度移动

### 10 个交互/设计细节

| # | 细节 | 具体表现 |
|---|------|----------|
| 1 | 导航链接几乎不可见 | 顶部 nav link (DD, Craft, Projects 等) opacity 仅 0.018 |
| 2 | 年份链接 85px 大号字 | "Twitter" "2023" "2022" "GitHub" 作为页面视觉锚点 |
| 3 | 底部导航有延迟淡入 | footer link transition 有 0.2s delay |
| 4 | 全然没有自定义光标 | cursor: auto，唯一例外是 email 复制按钮 cursor: copy |
| 5 | Craft 卡片没有 hover 效果 | bg/border/transform/shadow/opacity/filter 完全不变 |
| 6 | 三种 CTA 类型区分内容意图 | "View Production" / "Read Essay" / "View Prototype" |
| 7 | 卡片明暗交替 | 部分深色底（文字 #EDEDED），其余白底，是内容层级 |
| 8 | 自定义字体 "X" | 从 /dd.woff2 加载，只有 400 和 500 weight |
| 9 | 背景色是 #EDEDED | 不是纯白，是微暖的灰 |
| 10 | Switchboard 呼吸灯 | 1px 圆点 + box-shadow 蓝色辉光 + 透明度动画 |

### 与我们的关键差异总结

| 维度 | Rauno | 我们 |
|------|-------|------|
| 首页交互 | Camera pan + 拖拽探索 | 横向滚轮滚动（velocity+friction） |
| 光标 | 系统默认（auto） | 珊瑚圆点自定义光标 |
| 字体 | 自定制 "X"（仅 400/500） | Geist（400/500/600） |
| 背景 | #EDEDED | #E8E8E8 |
| 子页卡片 hover | 无 hover 效果 | 待定 |
| 子页组织 | 时间倒序，无分类 | 需要 Experience vs Projects 两类 |
| 色彩 | 黄/橙/红 accents + Radix 灰度 | 紫色 accent + 自定义灰度 tokens |
| 底部 nav | (/) /craft /projects 三个裸链接 | Scrubber + 语言/主题切换 |

### 借鉴 vs 不抄

**可以借鉴的：**

- Craft 页面的 card grid 结构（日期-标题-CTA 三行，极简无 hover）
- 三种内容类型的区分逻辑（对我们：Experience 行 vs Project 行）
- Transition easing `cubic-bezier(.2, .8, .2, 1)` — 比 linear 高级，比 ease 干净
- 卡片明暗交替来区分内容层级
- /projects 页面的极致简单列表

**不能抄的：**

- Custom font（我们有 Geist，已经足够）
- 全站无 cursor（我们有珊瑚光标，是特色不是 bug）
- Pan/camera 首页（我们横向滚动已经是差异化）
- 导航几乎隐形（Trevor 的内容需要清晰导航，因为不是设计师个人品牌）

---

## 四、额外 Reference（匹配非技术背景）

搜索标准：**非技术背景 + 极简编辑风 + 策略/运营/咨询类**

### 强相关

| Reference | 背景 | 风格特点 |
|-----------|------|----------|
| **Gaurav Kapadia** | Operator / curator，非设计师 | 极简编辑布局，安静自信，让内容说话 |
| **Andy Raskin** | 战略叙事顾问 | 绝对极简单页，直接对目标人群说话 |
| **Wells Collins** | 品牌策略师 | 克制优雅，FK Roman + Messina Sans，石墨+珊瑚配色 |
| **ThomasBL** | 学术+咨询+创意 | 极简现代，Framer 搭建，平衡咨询可信度与个人表达 |
| **Founder Personal Website** | 职业策略师/创业者 | 大胆排版+极简美学，分受众导航 |

### 风格参考（背景不同但设计语言可借鉴）

| Reference | 背景 | 值得看的地方 |
|-----------|------|-------------|
| **Lou Stoppard** | 作家/策展人 | 严格网格 + 内容索引式组织 |
| **Richard Prescott** | 创意人 | 极简 + 流畅动效的结合方式 |
| **Digitalista.io** | 产品策略师（非设计师） | 用产品思维架构个人站 |

### 共同原则（来自对 15 个个人品牌站的分析）

1. **清晰 > 好看**：大部分站过度投资设计，低估了清晰度
2. **策展而非穷举**：3-6 个案例优于 30 个
3. **先定位，后设计**：先写一句话定位，再搭建
4. **单页往往胜出**：独立顾问/小众创作者的单页站持续优于复杂多页站

---

## 五、下一步计划

### 第一步：修改 index.html / 索引页

在动手前：
1. 调用相关 skills（brainstorming、test-driven-development、writing-plans）
2. 深入研究 rauno.me 的设计（已完成以上分析）
3. 寻找匹配 Trevor 背景的 reference（已完成以上搜集）

### 对 work.html 的影响

基于以上研究，work.html 应该：

- 继续 Geist + 大留白 + 克制配色
- 采用**垂直滚动**（子页面不需要横向 panel）
- 采用**时间倒序 editorial list**（rauno 子页面的核心组织方式）
- 不照搬 rauno：我们有紫色 accent、珊瑚光标、不同内容结构（Experience vs Projects 两类）

---

## 六、技术记录

### Playwright 安装

```bash
npm install playwright
npx playwright install chromium
```

- 用于研究网站上无法通过静态抓取获取的交互细节
- 可执行：截图、点击、hover、滚动、读取 DOM、执行 JS
- 比 Chrome 扩展方案简单（无需额外开发）

### Chrome 扩展方案（备用）

架构：

```
AI (终端) ←→ localhost:9222 (Chrome DevTools Protocol) ←→ Chrome
```

启动命令：

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/chrome-debug
```

如需完整扩展，结构：

```
Extension/
├── manifest.json     # 权限：tabs, activeTab, debugger, scripting, storage
├── background.js     # Service worker，接收命令、管理状态
├── content.js        # 注入页面，执行 DOM 操作
└── popup.html/popup.js  # 可选 UI，显示连接状态
```

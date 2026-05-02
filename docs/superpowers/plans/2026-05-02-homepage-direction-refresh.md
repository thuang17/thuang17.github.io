# Homepage Direction Refresh Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refresh `index.html` and `zh.html` so the homepage presents Trevor as an operator with strong judgment and a maker edge.

**Architecture:** Keep the current pure static HTML structure and inline CSS/JS pattern. Add focused homepage sections and classes inside `index.html` and `zh.html`; do not introduce shared build tooling, frameworks, or external icon libraries. Preserve existing design tokens, dark mode, reduced-motion behavior, and footer/social icon work.

**Tech Stack:** Static HTML, inline CSS, vanilla JavaScript, Tailwind CDN only on homepage files, existing Google Fonts.

---

## File Structure

- Modify: `index.html`
  - Update English hero positioning.
  - Add proof strip under hero.
  - Reframe Work and Projects into clearer "selected proof" cards.
  - Add a compact "maker edge" bridge before About.
  - Keep existing animations and reduced-motion support.

- Modify: `zh.html`
  - Apply equivalent structure with natural Chinese copy.
  - Do not translate English sentence-by-sentence.
  - Keep links aligned with English homepage.

- Modify: `ROADMAP.md`
  - Mark homepage direction refresh as complete after implementation.
  - Add decision log entry if the homepage structure materially changes.

No new runtime files. No framework migration. No changes to verified career facts.

---

## Task 1: Hero Positioning And Proof Strip

**Files:**
- Modify: `index.html`
- Modify: `zh.html`

- [ ] **Step 1: Add hero CSS for positioning line, action row, and proof strip**

In both `index.html` and `zh.html`, add the following CSS after `.hero-chips`:

```css
    .hero-position{
      font-family:var(--f-display);font-size:clamp(22px,4vw,34px);
      font-weight:700;line-height:1.18;letter-spacing:-.025em;
      color:var(--fg);max-width:680px;margin:0 0 18px;
    }
    .hero-actions{display:flex;flex-wrap:wrap;gap:10px;margin-top:24px}
    .btn-primary,.btn-secondary{
      display:inline-flex;align-items:center;gap:7px;
      min-height:38px;padding:8px 13px;border-radius:8px;
      font-size:13px;font-weight:650;line-height:1;
      transition:background var(--t),border-color var(--t),color var(--t),transform var(--t);
    }
    .btn-primary{background:var(--fg);color:var(--bg);border:1px solid var(--fg)}
    .btn-primary:hover{transform:translateY(-1px);background:var(--accent);border-color:var(--accent);color:#fff}
    .btn-secondary{color:var(--fg);border:1px solid var(--border);background:transparent}
    .btn-secondary:hover{background:var(--bg-sub);border-color:var(--border-2);transform:translateY(-1px)}
    .proof-strip{
      display:grid;grid-template-columns:repeat(3,1fr);gap:1px;
      margin-top:42px;border:1px solid var(--border);border-radius:10px;
      overflow:hidden;background:var(--border);
    }
    .proof-item{background:var(--bg);padding:16px 18px;min-height:92px}
    .proof-value{
      font-family:var(--f-display);font-size:clamp(22px,4vw,32px);
      font-weight:800;line-height:1;letter-spacing:-.035em;color:var(--accent);
    }
    .proof-label{
      font-family:var(--f-mono);font-size:10px;letter-spacing:.08em;
      text-transform:uppercase;color:var(--fg-3);margin-top:7px;
    }
    .proof-note{font-size:13px;line-height:1.45;color:var(--fg-2);margin-top:6px}
    @media(max-width:720px){
      .proof-strip{grid-template-columns:1fr;margin-top:32px}
      .proof-item{min-height:auto}
    }
```

- [ ] **Step 2: Replace English hero copy**

In `index.html`, replace the current hero text block from `<p class="hero-eyebrow reveal">Hello</p>` through the closing `.hero-chips` div with:

```html
        <p class="hero-eyebrow reveal">Operator / PM-minded / Builder</p>

        <div>
          <h1 class="hero-name">Trevor Huang</h1>
        </div>

        <p class="hero-position reveal" style="transition-delay:70ms">
          I turn ambiguous business and product problems into structured action.
        </p>

        <div class="hero-bio reveal" style="transition-delay:120ms">
          <p>MPM student at the University of Sydney with hands-on FMCG O2O, instant retail, and e-commerce tech experience in China. My strongest work sits between operations, data, user experience, and cross-functional execution.</p>
          <p>I use AI tools the same way I approach work: start with a messy problem, build a working system, and keep improving it until it becomes useful.</p>
        </div>

        <div class="hero-chips reveal" style="transition-delay:170ms">
          <span class="tag">FMCG O2O</span>
          <span class="tag">E-commerce Tech</span>
          <span class="tag">UX Prioritization</span>
          <span class="tag">AI-assisted Builder</span>
        </div>

        <div class="hero-actions reveal" style="transition-delay:220ms">
          <a class="btn-primary" href="#projects">View selected proof →</a>
          <a class="btn-secondary" href="#about">See maker edge</a>
        </div>
```

- [ ] **Step 3: Add English proof strip under hero grid**

In `index.html`, immediately after the closing `</div>` for `.hero-grid` and before `</div></section>`, add:

```html
    <div class="proof-strip reveal" style="transition-delay:260ms" aria-label="Selected proof points">
      <div class="proof-item">
        <div class="proof-value">7.2×</div>
        <div class="proof-label">Campaign ROI</div>
        <p class="proof-note">Built Mayora's first instant retail CNY campaign from zero.</p>
      </div>
      <div class="proof-item">
        <div class="proof-value">16</div>
        <div class="proof-label">UX pain points</div>
        <p class="proof-note">Self-initiated Decathlon WeChat Mini Program benchmarking.</p>
      </div>
      <div class="proof-item">
        <div class="proof-value">8</div>
        <div class="proof-label">Parallel UAT projects</div>
        <p class="proof-note">Coordinated releases across Douyin, Tmall, and Taobao Flash Sale.</p>
      </div>
    </div>
```

- [ ] **Step 4: Replace Chinese hero copy**

In `zh.html`, replace the current hero text block from `<p class="hero-eyebrow reveal">你好</p>` through the closing `.hero-chips` div with:

```html
        <p class="hero-eyebrow reveal">运营 / 项目协作 / AI Builder</p>

        <div class="reveal" style="transition-delay:55ms">
          <h1 class="hero-name">黄拓文</h1>
          <p class="hero-name-en">Trevor Huang</p>
        </div>

        <p class="hero-position reveal" style="transition-delay:70ms">
          我擅长把模糊的业务和产品问题，拆成可以推进的行动。
        </p>

        <div class="hero-bio reveal" style="transition-delay:120ms">
          <p>悉尼大学项目管理硕士在读，有 FMCG O2O、即时零售和电商技术相关经历。我的优势在运营、数据、用户体验和跨部门协作的交界处。</p>
          <p>我使用 AI 工具的方式也类似：先面对一个混乱的问题，再把它做成一个能跑、能用、还能继续迭代的系统。</p>
        </div>

        <div class="hero-chips reveal" style="transition-delay:170ms">
          <span class="tag">FMCG O2O</span>
          <span class="tag">电商技术</span>
          <span class="tag">UX 优先级判断</span>
          <span class="tag">AI 辅助构建</span>
        </div>

        <div class="hero-actions reveal" style="transition-delay:220ms">
          <a class="btn-primary" href="#projects">查看代表案例 →</a>
          <a class="btn-secondary" href="#about">了解个人侧面</a>
        </div>
```

- [ ] **Step 5: Add Chinese proof strip under hero grid**

In `zh.html`, immediately after the closing `</div>` for `.hero-grid` and before `</div></section>`, add:

```html
    <div class="proof-strip reveal" style="transition-delay:260ms" aria-label="代表性证明点">
      <div class="proof-item">
        <div class="proof-value">7.2×</div>
        <div class="proof-label">Campaign ROI</div>
        <p class="proof-note">从零搭建迈大食品首个即时零售 CNY 大促。</p>
      </div>
      <div class="proof-item">
        <div class="proof-value">16</div>
        <div class="proof-label">UX pain points</div>
        <p class="proof-note">自发完成迪卡侬微信小程序全链路竞品分析。</p>
      </div>
      <div class="proof-item">
        <div class="proof-value">8</div>
        <div class="proof-label">Parallel UAT projects</div>
        <p class="proof-note">协调抖音、天猫、淘宝闪购等多个并行项目测试。</p>
      </div>
    </div>
```

- [ ] **Step 6: Browser check hero**

Run a local static server:

```bash
python3 -m http.server 4173
```

Open:

- `http://localhost:4173/index.html`
- `http://localhost:4173/zh.html`

Expected:

- Hero still fits first viewport on desktop without feeling crowded.
- Avatar remains visible and does not collide with text.
- Proof strip is visible immediately after hero content.
- Mobile stacks proof items cleanly.
- Dark mode preserves contrast.

- [ ] **Step 7: Commit Task 1**

```bash
git add index.html zh.html
git commit -m "Refresh homepage hero positioning"
```

---

## Task 2: Selected Proof Project Cards

**Files:**
- Modify: `index.html`
- Modify: `zh.html`

- [ ] **Step 1: Add selected proof card CSS**

In both homepage files, add after `.card-desc`:

```css
    .proof-card{
      position:relative;border:1px solid var(--border);background:var(--bg);
      padding:22px;border-radius:10px;margin:0 0 14px;
      transition:background var(--t),border-color var(--t),transform var(--t),box-shadow var(--t);
    }
    .proof-card:hover{
      background:var(--bg-sub);border-color:var(--border-2);
      transform:translateY(-2px);box-shadow:0 10px 30px rgba(0,0,0,.06);
    }
    [data-theme="dark"] .proof-card:hover{box-shadow:0 10px 30px rgba(0,0,0,.26)}
    .proof-card-kicker{
      font-family:var(--f-mono);font-size:10px;letter-spacing:.09em;
      text-transform:uppercase;color:var(--fg-3);margin-bottom:8px;
    }
    .proof-card-grid{
      display:grid;grid-template-columns:minmax(0,1fr) minmax(220px,280px);
      gap:28px;align-items:end;
    }
    .proof-card-question{
      font-size:14px;line-height:1.65;color:var(--fg-2);
      border-left:2px solid var(--accent);padding-left:12px;margin-top:12px;
    }
    .proof-metrics{
      display:grid;grid-template-columns:repeat(2,1fr);gap:12px;
    }
    .proof-metric{
      border-top:1px solid var(--border);padding-top:10px;
    }
    @media(max-width:760px){
      .proof-card-grid{grid-template-columns:1fr;gap:18px}
      .proof-metrics{grid-template-columns:repeat(3,1fr)}
    }
    @media(max-width:480px){
      .proof-metrics{grid-template-columns:1fr}
    }
```

- [ ] **Step 2: Change Projects section heading**

In `index.html`, replace:

```html
<div class="reveal"><p class="label">Case Studies</p><h2 class="h2">Projects</h2></div>
```

with:

```html
<div class="reveal"><p class="label">Selected proof</p><h2 class="h2">Where judgment shows up</h2></div>
```

In `zh.html`, replace:

```html
<div class="reveal"><p class="label">项目案例</p><h2 class="h2">项目</h2></div>
```

with:

```html
<div class="reveal"><p class="label">代表案例</p><h2 class="h2">判断力体现在哪里</h2></div>
```

- [ ] **Step 3: Replace English project cards with proof cards**

In `index.html`, replace the two `<a href="... class="card reveal"...>` project cards with:

```html
      <a href="cny-campaign.html" class="proof-card reveal" style="display:block">
        <div class="proof-card-grid">
          <div>
            <p class="proof-card-kicker">Business ambiguity → operating system</p>
            <div class="card-head">
              <span>CNY FMCG O2O Growth Campaign</span>
              <svg class="card-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 7h10v10"/><path d="M7 17 17 7"/></svg>
            </div>
            <p class="card-desc">Mayora's first instant retail campaign had no SOP, no historical data, and no proven audience playbook. I built the campaign structure, tracked audience-level ROI weekly, and reallocated budget when returning customers and gifting-intent segments clearly outperformed broad targeting.</p>
            <p class="proof-card-question">Key judgment: when signal appeared, shift budget toward the highest-converting audience instead of keeping spend evenly distributed.</p>
            <div class="tags" style="margin-top:14px"><span class="tag">FMCG</span><span class="tag">O2O</span><span class="tag">RTB</span><span class="tag">Budget reallocation</span></div>
          </div>
          <div class="proof-metrics">
            <div class="proof-metric"><div class="stat-v">7.2×</div><div class="stat-l">Gift box ROI</div></div>
            <div class="proof-metric"><div class="stat-v">600%</div><div class="stat-l">New product growth</div></div>
            <div class="proof-metric"><div class="stat-v">1.38M</div><div class="stat-l">Impressions</div></div>
          </div>
        </div>
      </a>

      <a href="decathlon-ux.html" class="proof-card reveal" style="display:block">
        <div class="proof-card-grid">
          <div>
            <p class="proof-card-kicker">Blank canvas → prioritized roadmap</p>
            <div class="card-head">
              <span>Decathlon WeChat Mini Program UX Study</span>
              <svg class="card-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 7h10v10"/><path d="M7 17 17 7"/></svg>
            </div>
            <p class="card-desc">No one assigned the project. I benchmarked Decathlon's WeChat Mini Program against JD 1P/3P across purchase and returns flows, surfaced 16 pain points, and built a dual-weighted Value-Effort Matrix to help the team prioritize what should move first.</p>
            <p class="proof-card-question">Key judgment: push back on courier return pickup because the short-term return-rate risk outweighed the UX upside before logistics was ready.</p>
            <div class="tags" style="margin-top:14px"><span class="tag">UX research</span><span class="tag">Prioritization</span><span class="tag">Competitive analysis</span></div>
          </div>
          <div class="proof-metrics">
            <div class="proof-metric"><div class="stat-v">16</div><div class="stat-l">Pain points</div></div>
            <div class="proof-metric"><div class="stat-v">4</div><div class="stat-l">Platforms</div></div>
            <div class="proof-metric"><div class="stat-v">¥6M+</div><div class="stat-l">Projected GMV</div></div>
          </div>
        </div>
      </a>
```

- [ ] **Step 4: Replace Chinese project cards with proof cards**

In `zh.html`, replace the two project cards with:

```html
      <a href="cny-campaign.html" class="proof-card reveal" style="display:block">
        <div class="proof-card-grid">
          <div>
            <p class="proof-card-kicker">业务空白 → 可执行系统</p>
            <div class="card-head">
              <span>美团闪购 CNY 促销增长项目</span>
              <svg class="card-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 7h10v10"/><path d="M7 17 17 7"/></svg>
            </div>
            <p class="card-desc">公司第一次做即时零售大促，没有 SOP，也没有历史数据。我从活动结构、投放节奏、受众拆分到 ROI 追踪搭起一套可执行方法，并在老客和礼赠人群表现明显更好后，及时调整预算方向。</p>
            <p class="proof-card-question">关键判断：不是平均分配预算，而是在信号出现后，把资源转向转化效率最高的人群。</p>
            <div class="tags" style="margin-top:14px"><span class="tag">快消</span><span class="tag">O2O</span><span class="tag">RTB</span><span class="tag">预算调整</span></div>
          </div>
          <div class="proof-metrics">
            <div class="proof-metric"><div class="stat-v">7.2×</div><div class="stat-l">礼盒 ROI</div></div>
            <div class="proof-metric"><div class="stat-v">600%</div><div class="stat-l">新品增长</div></div>
            <div class="proof-metric"><div class="stat-v">1.38M</div><div class="stat-l">曝光量</div></div>
          </div>
        </div>
      </a>

      <a href="decathlon-ux.html" class="proof-card reveal" style="display:block">
        <div class="proof-card-grid">
          <div>
            <p class="proof-card-kicker">空白任务 → 优先级路线图</p>
            <div class="card-head">
              <span>迪卡侬微信小程序 UX 研究</span>
              <svg class="card-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 7h10v10"/><path d="M7 17 17 7"/></svg>
            </div>
            <p class="card-desc">没人要求我做这件事。我自发对标京东 1P/3P 的下单、物流和售后链路，整理出 16 个用户痛点，再用双维度 Value-Effort 矩阵帮助团队判断哪些需求值得先推进。</p>
            <p class="proof-card-question">关键判断：快递上门取件短期可能拉高退货率，在物流基础还没准备好前，先暂缓比快速上线更合理。</p>
            <div class="tags" style="margin-top:14px"><span class="tag">UX 研究</span><span class="tag">需求优先级</span><span class="tag">竞品分析</span></div>
          </div>
          <div class="proof-metrics">
            <div class="proof-metric"><div class="stat-v">16</div><div class="stat-l">痛点数</div></div>
            <div class="proof-metric"><div class="stat-v">4</div><div class="stat-l">对标平台</div></div>
            <div class="proof-metric"><div class="stat-v">¥6M+</div><div class="stat-l">预测 GMV</div></div>
          </div>
        </div>
      </a>
```

- [ ] **Step 5: Browser check project cards**

Expected:

- Project cards read as structured case evidence, not generic cards.
- Metrics remain scan-friendly.
- The "key judgment" line is visible without dominating the card.
- Mobile card order is title, story, key judgment, metrics.

- [ ] **Step 6: Commit Task 2**

```bash
git add index.html zh.html
git commit -m "Reframe homepage projects as selected proof"
```

---

## Task 3: Work Section Scanability

**Files:**
- Modify: `index.html`
- Modify: `zh.html`

- [ ] **Step 1: Add work intro and outcome-list CSS**

In both homepage files, add after `.row-desc`:

```css
    .section-intro{
      font-size:14px;line-height:1.72;color:var(--fg-2);
      max-width:620px;margin:-18px 0 24px;
    }
    .outcome-list{
      display:grid;gap:6px;margin-top:10px;
      font-size:13.5px;line-height:1.55;color:var(--fg-2);
    }
    .outcome-list span{display:flex;gap:8px;align-items:flex-start}
    .outcome-list span::before{
      content:"";width:5px;height:5px;border-radius:50%;
      background:var(--accent);margin-top:.72em;flex:0 0 auto;
    }
```

- [ ] **Step 2: Add English Work intro**

In `index.html`, immediately after the Work heading div:

```html
    <p class="section-intro reveal">The pattern across my work: enter a messy operating environment, identify the real constraint, then turn it into a trackable system or decision.</p>
```

- [ ] **Step 3: Add Chinese Work intro**

In `zh.html`, immediately after the Work heading div:

```html
    <p class="section-intro reveal">几段经历里反复出现的一点是：先进入一个不够清晰的业务现场，找到真正的约束，再把它变成可追踪、可推进的系统或决策。</p>
```

- [ ] **Step 4: Add outcome bullets to Decathlon row**

In `index.html`, after the Decathlon `.row-desc`, add:

```html
          <div class="outcome-list">
            <span>Turned a blank intern brief into a prioritized UX improvement roadmap.</span>
            <span>Separated user pain points from logistics risks before recommending what to build.</span>
          </div>
```

In `zh.html`, after the Decathlon `.row-desc`, add:

```html
          <div class="outcome-list">
            <span>把一个很空的实习任务，推进成有优先级的 UX 改进路线图。</span>
            <span>在建议上线前，先区分用户体验收益和物流承接风险。</span>
          </div>
```

- [ ] **Step 5: Add outcome bullets to Mayora row**

In `index.html`, after the Mayora `.row-desc`, add:

```html
          <div class="outcome-list">
            <span>Built a campaign operating loop where audience ROI informed weekly budget shifts.</span>
            <span>Moved from campaign execution to repeatable instant-retail decision logic.</span>
          </div>
```

In `zh.html`, after the Mayora `.row-desc`, add:

```html
          <div class="outcome-list">
            <span>建立受众 ROI 到预算调整的周度运营闭环。</span>
            <span>从单次大促执行，沉淀出可复用的即时零售判断逻辑。</span>
          </div>
```

- [ ] **Step 6: Browser check Work section**

Expected:

- Work section is easier to skim before reading full paragraphs.
- Outcome bullets do not make rows too visually heavy.
- English and Chinese row heights remain acceptable on mobile.

- [ ] **Step 7: Commit Task 3**

```bash
git add index.html zh.html
git commit -m "Improve homepage work scanability"
```

---

## Task 4: Maker Edge Bridge

**Files:**
- Modify: `index.html`
- Modify: `zh.html`

- [ ] **Step 1: Add maker bridge CSS**

In both homepage files, add after `.ablock-body p+p`:

```css
    .maker-bridge{
      display:grid;grid-template-columns:minmax(0,0.9fr) minmax(0,1.1fr);
      gap:34px;align-items:start;padding:34px 0;
    }
    .maker-line{
      font-family:var(--f-display);font-size:clamp(22px,4vw,34px);
      font-weight:750;line-height:1.18;letter-spacing:-.025em;color:var(--fg);
    }
    .maker-copy{font-size:15px;line-height:1.82;color:var(--fg-2)}
    .maker-links{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px}
    @media(max-width:760px){
      .maker-bridge{grid-template-columns:1fr;gap:18px;padding:24px 0}
    }
```

- [ ] **Step 2: Insert English maker bridge before About section**

In `index.html`, insert this block between `</section>` for Skills and `<!-- ═══════════ ABOUT ═══════════ -->`:

```html
<!-- ═══════════ MAKER EDGE ═══════════ -->
<section id="maker-edge">
  <div class="wrap">
    <div class="maker-bridge reveal">
      <p class="maker-line">The personal edge is not separate from the work.</p>
      <div>
        <p class="maker-copy">Darts taught me structure, repetition, and pressure. AI tools taught me to move from idea to prototype faster. Both show the same underlying habit: I like turning vague intent into something observable, testable, and better than it was yesterday.</p>
        <div class="maker-links">
          <a class="btn-secondary" href="darts.html">Read darts story</a>
          <a class="btn-secondary" href="ai.html">Read AI story</a>
        </div>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 3: Insert Chinese maker bridge before About section**

In `zh.html`, insert this block between `</section>` for Skills and `<!-- ═══════════ ABOUT ═══════════ -->`:

```html
<!-- ═══════════ MAKER EDGE ═══════════ -->
<section id="maker-edge">
  <div class="wrap">
    <div class="maker-bridge reveal">
      <p class="maker-line">这些个人兴趣，不是和工作割裂的另一面。</p>
      <div>
        <p class="maker-copy">飞镖让我习惯结构、重复和压力下的稳定发挥。AI 工具让我更快把想法变成原型。它们背后其实是同一种习惯：把模糊的意图，变成可观察、可测试、还能继续改进的东西。</p>
        <div class="maker-links">
          <a class="btn-secondary" href="zh-darts.html">阅读飞镖故事</a>
          <a class="btn-secondary" href="zh-ai.html">阅读 AI 故事</a>
        </div>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 4: Browser check maker bridge**

Expected:

- Bridge makes About feel intentional, not appended.
- Copy is concise enough to scan.
- Buttons align with hero button style.
- Section does not create excessive whitespace on mobile.

- [ ] **Step 5: Commit Task 4**

```bash
git add index.html zh.html
git commit -m "Connect homepage personal stories to positioning"
```

---

## Task 5: Final Verification, Roadmap, Push

**Files:**
- Modify: `ROADMAP.md`

- [ ] **Step 1: Visual verification**

Run:

```bash
python3 -m http.server 4173
```

Check:

- `http://localhost:4173/index.html`
- `http://localhost:4173/zh.html`

Required viewports:

- Desktop: 1440 x 1000
- Mobile: 390 x 844

Required themes:

- Light
- Dark

Expected:

- No horizontal overflow.
- Hero CTA buttons do not wrap awkwardly.
- Proof strip and proof cards remain legible.
- Chinese text does not feel machine-translated.
- Existing footer icons still align.
- Reduced motion CSS still exists and disables reveal/name animation.

- [ ] **Step 2: Link verification**

Click or inspect these links:

```text
index.html -> #projects
index.html -> #about
index.html -> cny-campaign.html
index.html -> decathlon-ux.html
index.html -> darts.html
index.html -> ai.html
zh.html -> #projects
zh.html -> #about
zh.html -> cny-campaign.html
zh.html -> decathlon-ux.html
zh.html -> zh-darts.html
zh.html -> zh-ai.html
```

Expected:

- Anchor links scroll to the right sections.
- Detail page links do not 404.

- [ ] **Step 3: Update ROADMAP**

In `ROADMAP.md`, under `Phase 3 · Main Narrative`, add:

```markdown
- [x] Homepage direction refresh — reframe hero, selected proof, work scanability, and personal maker bridge around operator judgment
```

Add this decision row:

```markdown
| 2026-05 | Homepage structured around selected proof | First impression should show business judgment before personal texture |
```

- [ ] **Step 4: Commit roadmap and final polish**

```bash
git add ROADMAP.md index.html zh.html
git commit -m "Complete homepage direction refresh"
```

- [ ] **Step 5: Push**

```bash
git push
```

Expected:

- Push succeeds to `main`.
- GitHub Pages deploys automatically.

---

## Self-Review

Spec coverage:

- PRD positioning is covered by hero positioning, selected proof cards, and maker bridge.
- Target audience scanning behavior is covered by proof strip, work intro, outcome bullets, and metrics.
- Chinese naturalness is addressed with non-literal Chinese copy.
- Non-goals are respected: no framework, no build step, no new external icon system, no verified data changes.

Placeholder scan:

- No placeholder markers or unspecified implementation steps remain.
- Every code-editing step includes concrete snippets.

Risk notes:

- `index.html` and `zh.html` duplicate CSS. This plan follows the current codebase instead of introducing a shared stylesheet.
- The homepage currently uses Tailwind CDN, but the planned changes use custom CSS only and keep that existing setup unchanged.
- Some verified metrics are reused from existing page content; do not invent new numbers.

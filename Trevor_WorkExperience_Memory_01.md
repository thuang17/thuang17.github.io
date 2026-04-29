# Trevor Huang (黄拓文) - Work Experience Deep Dive
> This document contains detailed memory of Trevor's work experience, extracted from an extended interview prep + resume optimization session. Intended for use by Claude Code when building Trevor's personal website.

---

## Basic Info
- **Name:** 黄拓文 (Trevor Huang)
- **Email:** trevor.tw.huang@outlook.com
- **Phone:** +86 15183781017
- **Current:** Master of Project Management, University of Sydney (2025.08–2027.01), GPA 3.8/4.0, WAM 79.6, TOP 15%
- **Undergraduate:** International Economics and Trade (Full English Program), Shanghai University of International Business and Economics (2020.09–2024.06), GPA 3.1/4.0

---

## Work Experience

### 1. Decathlon | E-commerce Tech PM Intern | 2025.12–2026.02
**Location:** Shanghai HQ, E-commerce Department

#### Role Context
- Reported to a mentor who gave Trevor open-ended space to discover problems independently
- Managed a portfolio of ~8 projects across WeChat Mini Program, Douyin, Tmall, and Taobao Flash Sale channels
- Acted as bridge between business teams and IT

#### Project A: WeChat Mini Program UX Improvement (Trevor's own initiative)
**Role:** Project Initiator

**How it started:**
- Mentor gave Trevor freedom to identify problems independently
- Trevor proactively observed UX pain points in the Mini Program without being assigned the task

**Research method:**
- Full-funnel competitive benchmarking: JD 1P, JD 3P, Tmall, and other sports/outdoor brand Mini Programs
- Covered: PDP page, logistics, after-sales
- Documented with screenshots and written analysis
- No internal user behavior data was available; Trevor flagged this to mentor but mentor judged the pain points were obvious enough to proceed
- Trevor's reflection: ideally should have pushed harder to get heatmap or conversion funnel data to validate priority objectively

**Pain points identified:** 16 total
- Key examples:
  - SKU naming inconsistency (hurts off-platform seeding and on-platform conversion)
  - Missing logistics ETA display (low dev cost, high UX impact, fast to implement)
  - No self-service return with courier pickup (high priority long-term, deprioritized short-term -- see below)

**Priority framework:**
- Built a customized Value-Effort Matrix with dual-dimension weighted scoring:
  - Dimension 1: Consumer need intensity (0–5)
  - Dimension 2: Business value (0–5)
  - Weighted total score determines quadrant placement
- Held 2 alignment meetings with the team's Project Manager to validate quadrant placement
- Output: requirements mapped into 4 quadrants; high-priority items pushed into sprint, others into backlog

**Key decision: Courier pickup deprioritized**
- Mentor initially wanted to prioritize self-service return with courier pickup
- Trevor argued against it with two reasons:
  1. Cost: requires reverse logistics API integration + courier partnership agreements -- short-term ROI poor
  2. Business impact: would reduce friction for returns, likely spike return rate short-term, increasing reverse logistics cost
- Both agreed the feature is necessary long-term; disagreement was only on timing
- Result: feature entered backlog at low priority
- This is Trevor's best example of "using data/logic to persuade others" (P&G Q4 behavior)

**BRD output:**
- Wrote BRD for delivery radius expansion to 10km
- Projected annual GMV uplift: 6M+ RMB

#### Project B: DTC Manual Refund Optimization
**Role:** PM coordinating business, IT, and customer service teams

**Background:**
- DTC channels (WeChat Mini Program + official website) frequently required manual refunds for price differences, compensation, etc.
- No automated refund-only feature existed; manual process had compliance violations
- Project formed to standardize the process

**Key challenge (cross-department friction):**
- After Round 1 UAT, IT completed fixes
- Customer service team responsible for re-testing went past due date with no response to WeChat messages
- Trevor's resolution:
  1. Judged async communication was failing
  2. Scheduled a short in-person meeting
  3. Did NOT open with "you're overdue" -- instead asked about their status first
  4. Explained project value to CS team: standardization would reduce their compliance risk and workload
  5. CS team understood and completed re-testing promptly
- This is Trevor's best example of "working effectively with people to accomplish results" (P&G Q5 behavior)

#### Project C: Internal PM Tool Optimization + Trello Introduction
**Role:** Assigned by mentor based on Trevor's PM academic background

**How it started:**
- Mentor knew Trevor was studying PM; proactively assigned this task (NOT Trevor's own initiative -- important distinction)
- Decathlon was building an internal PM software (chose not to buy commercial tools)

**Research method:**
- Benchmarked: Jira, Trello, Monday, DingTalk, Feishu
- Constraint: Decathlon needed highest-value features shipped quickly, not a full commercial tool clone
- Held 2 meetings with the team's dedicated Project Manager to validate pain points

**Pain points identified:** 13 total
- Key examples:
  - No project progress visibility (had to click into Jira link to see which stage a project was in)
  - No clear owner mapping (couldn't tell who was responsible for a project without asking around)

**Trello introduction:**
- Mentor mentioned team was using Notion but found it insufficient (free tier limits)
- Trevor proactively proposed Trello as lightweight team-level kanban supplement
- Held a meeting to walk through advantages; mentor approved
- Trello serves team-level task management; the internal software serves company-wide PM -- no conflict
- Team adopted Trello and continued using it

---

### 2. Mayora Food (迈大食品) | Management Trainee | 2024.07–2025.05
**Full name:** Mayora Food (Shanghai) -- part of PT Mayora Indah Tbk, Indonesian FMCG multinational
**Brands:** Kopiko, Danisa, Roma, Energen, Torabika

#### Role Context
- Responsible for all brand operations across Meituan Flash Sale, JD Daojia, Taobao Flash Sale (O2O platforms)
- Reported to a line manager (LM) who set macro direction; Trevor handled daily operations, data monitoring, and campaign execution

#### Project: Meituan Flash Sale CNY Campaign | 2024.12–2025.02
**Role:** Project execution lead (NOT initiator -- LM proposed the project)

**Background:**
- Company's FIRST instant retail project -- no SOP, no historical data
- Two product lines: gift boxes (礼盒) and new products (新品)
- Trevor was one of two team members; LM handled macro decisions, Trevor handled day-to-day execution

**RTB Advertising structure:**
- Two campaign types ran simultaneously:
  1. RTB (Real-Time Bidding) placements -- automated auction for ad impressions
  2. Vouchers (e.g., 满59减15, brand vouchers 20-4) -- promotional mechanics to drive conversion
- RTB = "find the right people to see you"; vouchers = "give them a reason to buy"

**Audience targeting strategy and hypotheses:**
- Cookie/biscuit audience (饼干人群): Direct match -- highest frequency buyers of the category, lowest conversion barrier, core base
- Gift-giving & care audience (礼赠关怀人群): CNY gifting occasion + gift box product = high-intent match for send-as-gift use case
- Existing customers (老客): Brand familiarity drives repurchase during CNY; low re-engagement cost
- Dairy transaction audience (乳品交易人群): Hypothesis = biscuits + milk is a common consumption pairing; treated as TEST investment from the start, with expectation of mid-campaign data validation and adjustment if underperforming
- This approach (hypothesis-driven targeting + data validation + dynamic adjustment) is Trevor's strongest consumer insight example

**Budget management:**
- City allocation based on resource availability
- Gift box: started conservatively in Beijing, Shanghai, Hangzhou (3 cities)
- New products: launched nationally from the start (more aggressive)

**Round 1 optimization (Week 1):**
- Expanded gift box cities from 3 to 5 (added Nanjing, Guangzhou)
- Switched audience targeting from broad (all-users) to precision insight plans
- CPM bidding mode adopted for insight plans
- Eliminated dairy transaction audience (incremental ROI insufficient)
- Increased gift-giving & care audience budget separately

**Round 2 optimization (Sprint phase, Jan 13–17):**
- Significantly increased budget: gift box GMV plans from 500 RMB to 800 → 1000 → 3000 RMB
- New products from 1000 to 1500 → 2000 RMB
- Extended ad hours from afternoon-only to full day (07:00–24:00)
- Continued eliminating low-performing audience segments

**Post-campaign wind-down:**
- Gift box: all plans paused (budget fully utilized)
- New products: reduced frequency, narrowed hours back to 14:00–22:00, budget reduced to 250 RMB
- Retained only top-performing audiences: biscuit and home-living segments
- Cracker series (脆乐脆) split out with CPC (cost-per-click) objective

**ROI metrics:**
- New product sales: ~600% growth vs. January pre-campaign daily average baseline
  - Denominator: daily average sales in January before campaign launch
  - Numerator: sales during CNY window (D-16 to D+20)
  - Additional validation: compared against 2024 same-period data AND isolated campaign-attributed sales (total minus non-campaign sales) to control for seasonality
- Gift box daily direct ROI: stable 4–5
- Gift box comprehensive ROI (full window): peaked at 7.2
  - Calculated as: total gift box sales / total ad spend for the entire CNY window

**Key decision: Why not increase budget for high-performing audiences?**
- Early stage: conservatively held back due to concern about spending too fast (judgment call, not a hard threshold)
- Late stage: discovered total budget was underspent; tried to ramp up aggressively to test ROI ceiling
- Result: campaign window ended before ROI ceiling was identified
- Trevor's reflection: this was a learning rather than a failure -- initial decision criteria should have been predefined thresholds (e.g., daily spend rate vs. plan), not intuitive judgment

**Incremental ROI logic (how underperforming cities were identified):**
- Compared each city's sales performance against its own historical baseline (January pre-campaign daily average)
- Cities where post-campaign sales showed little lift vs. their own baseline = low incremental ROI
- NOT a cross-city comparison (Shanghai vs. Chengdu would be invalid due to different market sizes)

**SOP output:**
- Documented a replicable framework: 节奏制定 → 资源确认 → 投放执行 → 数据复盘

**Reporting cadence:**
- Daily: key metrics dashboard (ROI, GMV, conversion rate, impression rate) exported from Meituan backend
- Weekly: written data analysis report to LM
- TP partner contact: Trevor handled day-to-day TP liaison; LM involved for major decisions

---

### 3. SynTao Green Finance (商道纵横) | ESG Consulting Intern | 2024.01–2024.04

- Applied GRI, CDP, SASB, MSCI, CSA frameworks
- Drafted ESG reports for listed companies: baseline analysis, policy research, materiality analysis, document QC
- Collected and edited data from 20+ ESG reports across healthcare, industrial, nuclear energy, and renewable energy sectors
- Wrote 10+ chapters
- Conducted internal roadshow on materiality issues in the healthcare sector

---

### 4. Tianfeng Securities (天风证券) | Equity Research Intern | 2022.08–2022.09

- Independently wrote deep-dive research reports on smart wearables and men's jewelry
- Projected CAGR and investment potential for niche markets
- Collected and verified macro market data; identified structural opportunities in "silver economy" non-medical discretionary spending
- Managed expert database and meeting records

---

## Key Behavioral Examples (P&G 8 Questions Mapping)

| Question | Core Competency | Best Case |
|----------|----------------|-----------|
| Q1 | High goal + execution | CNY campaign: first-ever instant retail project, no SOP, no historical data, delivered 600% growth |
| Q2 | Leadership + initiative | UX project: self-initiated, built analysis framework from zero, drove prioritization and project approval |
| Q3 | Analytical judgment | UX Value-Effort Matrix: dual-dimension weighted scoring, 16 pain points into 4 quadrants, cross-dept alignment |
| Q4 | Persuading with data | Courier pickup deprioritization: two-angle argument (API cost + return rate spike), mentor convinced |
| Q5 | Teamwork | DTC refund UAT: CS team unresponsive, escalated to in-person meeting, led with project value not deadline pressure |
| Q6 | Innovation | PM tool optimization + Trello: benchmarked 5 tools, 13 pain points documented, Trello adopted to replace Notion |
| Q7 | Adaptability | CNY two-round optimization: switched from broad to precision targeting, reallocated budget based on incremental ROI |
| Q8 | Information gathering | UX competitive benchmarking: full-funnel analysis across JD/Tmall, industry-validated pain points as proxy for user data |

---

## Personality / Reflection Notes (useful for About section)
- Tends to be data-driven but pragmatic when data is unavailable (uses competitive benchmarking as proxy)
- Comfortable operating in ambiguity (first-ever projects with no SOP)
- Self-aware about gaps: knows his background is PM-heavy, not brand/marketing -- actively working to bridge
- Communication style: prefers leading with value/interest alignment rather than authority when influencing peers
- Bilingual: Chinese (native), English (IELTS 6.5, worked in full-English environments)

---

## Tools & Skills
- **Data:** MS Excel, SQL, Power BI, Tableau
- **PM:** Jira, MS Project, MS Office, Miro, Figma, Trello; Agile methodology
- **Advertising platforms:** Meituan Flash Sale backend, RTB bidding (GMV optimization plans, CPM insight plans, CPC)
- **ESG frameworks:** GRI, CDP, SASB, MSCI, CSA
- **Languages:** Chinese (native), English (IELTS 6.5)

# Project Context

## What This Is

Personal website for Trevor Huang (黄拓文).
The site should feel like a personal website first, and only secondarily function as a professional asset.

This is NOT a generic portfolio site.
This is a structured narrative showing how Trevor thinks, decides, executes, and is still becoming.

Current homepage direction:

- personal index first
- proof-bearing site second
- depth by invitation, not by homepage density

---

## Target Roles

- FMCG: Marketing / Brand / E-commerce Operations
- Internet companies: Operations / BI / Product-related roles
- Project Management / Coordination roles

Primary audience:

- curious visitors who want to understand Trevor's way of thinking
- hiring managers and recruiters as a secondary audience

The site should not optimize the homepage primarily for recruiter scanning.
Role-fit language and resume facts can still exist deeper in the site.

---

## Trevor's Background (Summary)

- Master of Project Management, University of Sydney (GPA 3.8/4.0, top 15%), 2025–2027
- Bachelor's, International Economics & Trade, SUIBE Shanghai, 2020–2024
- Work experience:
  - Decathlon China — E-commerce Tech PM Intern (2025–2026)
  - Mayora Food — Management Trainee, FMCG O2O (2024–2025)
  - SynTao — ESG Consulting Intern (2024)
  - Tianfeng Securities — Equity Research Intern (2022)
- Non-work identity: darts club president, Shanghai university league champion, AI tools explorer

Full data source: `Trevor_WorkContext_ForWebsite.md` and `Trevor_WorkExperience_Memory_01.md`

---

## Tech Stack (updated 2026-05-06)

- **Astro v5 + React 19 + TypeScript** — build step required (`npm run build`)
- **GitHub Actions** — auto-builds and deploys to Pages on push to `main`
- **CSS:** `src/styles/global.css` (design system) + scoped `<style>` blocks per page
- **Icons:** inline SVGs only
- **No Tailwind CDN** — all CSS is locally bundled

## Site Structure

```
src/pages/
├── index.astro          — EN homepage (primary)
├── zh.astro             — ZH homepage
├── work.astro           — Work index
├── zh-work.astro        — ZH Work index
├── stories.astro        — Stories index
├── zh-stories.astro     — ZH Stories index
├── ai.astro             — AI / Making story
├── zh-ai.astro          — ZH AI / Making story
├── darts.astro          — Darts story
├── zh-darts.astro       — ZH Darts story
├── decathlon.astro      — Decathlon case study
├── zh-decathlon.astro   — ZH Decathlon case study
├── mayora.astro         — Mayora case study
├── zh-mayora.astro      — ZH Mayora case study
├── cny-campaign.astro   — CNY campaign deep-dive
├── decathlon-ux.astro   — Decathlon UX research deep-dive
├── making/              — Product listing (auto-generated)
└── products/            — Product detail pages (auto-generated)

src/content/products/    — Product Markdown files
├── product1.md
└── ...
```

All URLs use clean paths: `work.astro` → `/work`, `zh.astro` → `/zh`, etc.

Homepage information architecture:

- `Work` → `/work` — strongest evidence of judgment in real operating environments
- `AI / Making` → `/ai` — experiments, tools, building instinct, and self-directed making
- `Stories` → `/stories` — personal material that explains discipline, pressure, repetition, and systems

Important content boundary:

- `darts` belongs in `Stories`
- `AI` should no longer primarily live in `Stories`
- `ai.astro` direction should gradually evolve toward `AI / Making`

---

## Content Principles

- Show decision-making process, not just outcomes
- Every claim needs a specific number or concrete detail behind it
- 2–3 strong case studies only; do not treat all experiences equally
- Mayora CNY campaign and Decathlon UX research are the two flagship projects
- Homepage should not try to summarize everything
- Resume-style sections should be lower-priority than the chosen entry points

---

## Tone

**English:** First-person, direct, confident. Specific details and decision logic. No corporate jargon.
**Chinese:** Conversational, grounded, no buzzword stacking.

Anti-patterns to avoid:
- "通过...实现了..." constructions
- Excessive parallel lists
- "此外" / "综上" / "不仅...而且..."
- Anything that reads like it was written by an AI

Homepage tone and UX direction:

- sparse
- deliberate
- visually restrained
- calm at rest
- premium mainly through hover and click / transition
- no noisy intro animation

---

## Key Data (Verified — Do Not Change Without Checking Source Files)

| Item | Value |
|------|-------|
| Decathlon pain points | 16 (not 20) |
| Decathlon delivery radius (current) | 3km (target: 10km) |
| Decathlon dates | 2025.12–2026.02 |
| Mayora dates | 2024.07–2025.05 |
| Gift box campaign ROI | 7.22 (full CNY window) |
| New product growth | ~600% vs pre-campaign daily baseline (NOT YoY) |
| Gift box impressions | 1.38M |
| BRD projected GMV uplift | ¥6M+ |

---

*Last updated: 2026-05-07*

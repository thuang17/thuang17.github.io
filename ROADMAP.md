# ROADMAP — Trevor Huang Personal Website

Lightweight project management file. Update after each meaningful change.

---

## Completed

**Phase 0 · Foundation**

- [x] Design system (colors, typography, dark mode)
- [x] Bilingual setup (index.html EN / zh.html ZH)
- [x] All work experience content (Decathlon / Mayora / SynTao / Tianfeng)
- [x] Project cards (CNY campaign / Decathlon UX)
- [x] Skills section
- [x] Cartoon avatar (AI-cutout, transparent background)
- [x] Social icons (Email / LinkedIn / Instagram / X / Xiaohongshu)
- [x] GitHub repo + GitHub Pages deployment → https://thuang17.github.io

**Phase 1 · Case Study Pages**

- [x] decathlon.html — Full Decathlon work experience case study (two-column + sticky TOC)
- [x] mayora.html — Full Mayora work experience case study (two-column + sticky TOC)
- [x] cny-campaign.html — CNY campaign project deep-dive (audience table, phase blocks, data cards)
- [x] decathlon-ux.html — Decathlon UX research project deep-dive (quadrant grid, pain point list)
- [x] darts.html / zh-darts.html — Darts story detail pages (photo strips, lightbox)
- [x] ai.html / zh-ai.html — AI Explorer story detail pages (timeline layout)
- [x] Main page Work rows linked to case study pages
- [x] Main page Project cards linked to project detail pages
- [x] /context folder — shared reference files for multi-AI collaboration

---

## In Progress

**Phase 2 · Content & Story Quality**

- [x] Redesign darts.html and ai.html — both story pages now use stronger editorial / immersive layouts instead of single-column article layouts.
- [ ] Chinese text rewrite — current Chinese copy has AI-generated patterns, feels unnatural. Trevor writes key sentences, Claude structures around them.
- [ ] Create Chinese versions of work case study pages (zh-decathlon.html, zh-mayora.html) — optional, lower priority

---

## Next

**Phase 3 · Main Narrative**

- [x] Website direction PRD — define "operator with a maker edge" as the next design/narrative direction
- [x] Homepage direction refresh — reframe hero, selected proof, work scanability, and personal maker bridge around operator judgment
- [x] Remove duplicated Beyond Work block — maker edge bridge now carries the personal-story entry points
- [x] Homepage first fold rebuilt as a personal index — the landing surface now foregrounds Work / AI-Making / Stories instead of leading with a resume-style hero
- [x] Context files synced to personal-index direction — `AGENTS.md`, `CLAUDE.md`, and `context/project-context.md` now reflect the new homepage role and IA
- [x] Homepage contact anchors repaired after info-strip merge — both locales now point `Contact / 联系` to the contact column, and the Instagram profile link is restored
- [x] Homepage education strip refined — school names are now standalone links and degree details live on the muted year line in both locales
- [x] Homepage info strip rebalanced for long education labels — desktop now gives the education column more room while preserving responsive fallback
- [x] Homepage migrated to horizontal single-surface model — 5 panels (Hero/Work/Making/Stories/Info), Rauno-style hero with Geist typography, velocity+friction scroll, Minimal Scrubber, Info overlay, mobile fallback. Both locales (EN/ZH) migrated.
- [ ] "Now" section / page — what Trevor is currently doing, thinking, building (Trevor provides content)
- [ ] Writing section placeholder — no content yet, just structure
- [ ] Hero bio refinement — after "Now" content is ready

---

## Someday

**Phase 4 · Interaction & Polish**
- [x] Homepage compact floating nav — desktop scroll turns the top bar into a restrained B3-lite floating pill; mobile keeps the stable navigation layout.
- CSS View Transitions: project card click → detail page animation
- Subtle scroll-triggered animations on case study pages
- Custom cursor or other personality touches (evaluate later)

**Phase 5 · Content Expansion**
- Writing: actual articles (China O2O market / AI tools / PM thinking)
- Now page: update every quarter
- 1–2 English articles

**Phase 6 · Deployment & SEO**
- Custom domain (once content is mature)
- SEO meta tags optimization
- Performance optimization (images / font loading)

**Phase 7 · Framework Migration (on-demand, not urgent)**
- Consider migrating to Next.js or Astro
- Trigger conditions — evaluate only when one of these becomes true:
  - Need a CMS (blog posts without editing HTML manually)
  - Need backend logic (comments, forms, user data)
  - HTML file count becomes unmanageable
- Current state: pure static HTML meets all needs, no migration needed

---

## Decisions Log

| Date | Decision | Reason |
|------|----------|--------|
| 2026-04 | English as primary, Chinese as secondary | Target audience includes foreign-invested companies; English version built first |
| 2026-04 | Fonts: Montserrat + Nunito Sans | Close to Gotham aesthetic, free via Google Fonts |
| 2026-04 | No framework, single HTML files | Zero-config GitHub Pages deployment, easy to maintain |
| 2026-04 | Container width: 1080px unified | Eliminates hero/body misalignment |
| 2026-04 | github.io for now, no custom domain yet | Wait for content to mature before investing |
| 2026-04 | No "Project Manager" title | Trevor has not held a formal PM role; avoid misleading |
| 2026-04 | Pain points count: 16 | Verified against source files across both work context documents |
| 2026-04 | No Next.js migration for now | Static HTML sufficient; migration only when backend/CMS needs arise |
| 2026-04 | Multi-AI collaboration via /context folder | Claude Code reads repo directly; ChatGPT/Codex require context files to be pasted manually |
| 2026-05 | Website direction: operator with a maker edge | Prioritize hiring credibility and decision quality, with personal texture as differentiation |
| 2026-05 | Homepage structured around selected proof | First impression should show business judgment before personal texture |
| 2026-05 | Homepage nav uses B3-lite compact floating behavior | Keep the playful/product-like reference effect, but preserve full nav clarity and mobile usability |
| 2026-05 | Homepage becomes a personal index first | The site should feel like Trevor's entry surface first, with detail moved one layer deeper |
| 2026-05 | Context files now follow the personal-index direction | Prevent future sessions from drifting back to a recruiter-first homepage interpretation |

---

*Last updated: 2026-05-03*

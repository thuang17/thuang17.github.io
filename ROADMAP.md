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

- [ ] "Now" section / page — what Trevor is currently doing, thinking, building (Trevor provides content)
- [ ] Writing section placeholder — no content yet, just structure
- [ ] Hero bio refinement — after "Now" content is ready
- [ ] About section: add photo(s) once Trevor provides them

---

## Someday

**Phase 4 · Interaction & Polish**
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

---

*Last updated: 2026-05-02*

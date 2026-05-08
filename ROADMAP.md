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

**Phase 7 · Framework Migration (completed 2026-05-06)**

- [x] Migrate from pure static HTML to **Astro v5 + React 19 + TypeScript**
- [x] Initialize Astro project with `@astrojs/react` integration
- [x] Create shared `BaseLayout.astro` — removes duplicate head/fonts/tokens across all 18 pages
- [x] Create global CSS design system (`src/styles/global.css`) — design tokens, reset, typography, cursor
- [x] Migrate homepage (EN/ZH) — preserve horizontal surface, scrubber, entry animation, dark mode
- [x] Migrate all 14 sub-pages (work, stories, ai, darts, 4 case studies + Chinese mirrors)
- [x] Migrate 2 remaining Chinese case study pages (zh-decathlon, zh-mayora)
- [x] Set up products content system — `src/content/products/*.md` → auto-generated listing + detail pages
- [x] Create React components — `ProductCard.tsx`, `ProductGrid.tsx`
- [x] Configure GitHub Actions deploy workflow — builds Astro, deploys `dist/` to Pages
- [x] Remove Tailwind CDN dependency — CSS is now locally bundled
- [x] Clean up root `.html` files (all deleted, git history preserved)

---

## In Progress

**Phase 2 · Content & Story Quality**

- [x] Redesign darts.html and ai.html — both story pages now use stronger editorial / immersive layouts instead of single-column article layouts.
- [ ] Chinese text rewrite — current Chinese copy has AI-generated patterns, feels unnatural. Trevor writes key sentences, Claude structures around them.
- [x] Create Chinese versions of work case study pages (zh-decathlon.astro, zh-mayora.astro) — migrated together with all pages

---

## Next

**Phase 3 · Main Narrative** *(all complete)*

- [x] Website direction PRD — define "operator with a maker edge" as the next design/narrative direction
- [x] Homepage direction refresh, context files synced, horizontal surface migration
- [x] Hero entry animation, accent circle, Chinese version sync
- [ ] Click ripple effect — deferred, low priority
- [ ] "Now" section / page — needs Trevor content
- [ ] Writing section placeholder — needs content

**Phase 3.5 · Sub-page Structure** *(all complete)*

- [x] Work index page (work.astro + zh-work.astro) — editorial directory with v9 entry animation
- [x] All pages migrated to Astro: work, stories, ai, darts, decathlon, mayora, cny-campaign, decathlon-ux + Chinese mirrors
- [x] Panel navigation uses clean Astro URLs (/work, /ai, /stories, etc.)
- [x] Info overlay copy synced across homepage and index-linked sub-pages; removed language line from the modal

---

## Someday

**Phase 4 · Interaction & Polish**
- [x] Homepage compact floating nav, custom cursor, entry animation, scrubber
- CSS View Transitions, scroll-triggered animations (deferred)

**Phase 5 · Content Expansion**
- Writing, Now page, English articles (deferred, needs content)

**Phase 6 · Deployment & SEO**
- Custom domain, SEO meta tags, perf optimization (deferred)

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
| 2026-05-05 | Work index page: editorial directory over cards | Rauno-inspired restrained list with v9 entry animation, focus hover, no titles/footer. Better matches the personal-index direction and feels more editorial than panel-card layout |
| 2026-05-06 | Migrate to Astro v5 + React 19 + TypeScript | Pure static HTML no longer sufficient: 18 pages unmanageable, need shared layout + product content system. Astro chosen over Next.js for zero-JS output and gradual migration path |
| 2026-05-06 | CSS bundling: Astro import instead of `<link>` | `<link rel="stylesheet" href="/src/styles/global.css">` doesn't resolve in production. Must use `import '../styles/global.css'` in Astro frontmatter |
| 2026-05-06 | Script scoping: `is:inline` for global functions | Astro bundles `<script>` as ES module by default; functions not accessible from `onclick` handlers. Use `is:inline` or convert to `addEventListener` |
| 2026-05-06 | Dynamic elements need `:global()` CSS | `.ruler-tick` created via JS `createElement` lacks Astro scope attribute. Must use `:global(.ruler-tick)` in scoped `<style>` blocks |
| 2026-05-07 | Products content system docs in CLAUDE.md + AGENTS.md | Multiple AI tools (Claude Code, Codex) need to know about `src/content/products/*.md` convention. Documented in both project-level context files + memory |

---

*Last updated: 2026-05-08*

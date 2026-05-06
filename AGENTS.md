# AGENTS.md — For OpenAI Codex

This file is read automatically by OpenAI Codex CLI at session start.
For Claude Code, see CLAUDE.md instead.

---

## Quick Start

Read these files before doing anything:

1. `/context/project-context.md` — goals, target audience, tone rules, verified data
2. `/context/design-system.md` — color tokens, fonts, layout specs, component patterns
3. `/context/rules.md` — what to do and what NOT to do
4. `ROADMAP.md` — current state, what's done, what's pending

---

## Project Summary

Personal website for Trevor Huang (黄拓文), hosted on GitHub Pages.
The current direction is `personal website first, proof-bearing site second`.
Do not default to treating the homepage as a recruiter-first resume surface.

Live URL: https://thuang17.github.io

Current homepage role:

- a restrained personal index
- three primary entry points: `Work`, `AI / Making`, `Stories`
- depth moves to second-layer pages instead of being front-loaded on the homepage

---

## Tech Stack

- **Astro v5 + React 19 + TypeScript** (migrated from pure HTML in May 2026)
- Build: `npm run build` → output to `dist/`
- Dev server: `npm run dev`
- Deploy: GitHub Actions auto-builds and pushes to GitHub Pages
- CSS: `src/styles/global.css` for design system tokens, per-page `<style>` blocks for page-specific CSS
- Icons: inline SVGs only (no icon CDN)
- Dark mode: `data-theme="dark"` on `<html>`, persisted via localStorage

---

## File Structure

```
src/
├── pages/                  # All website pages (.astro files)
│   ├── index.astro         # EN homepage
│   ├── zh.astro            # ZH homepage
│   ├── work.astro          # Work index
│   ├── zh-work.astro       # ZH Work index
│   ├── stories.astro       # Stories index
│   ├── zh-stories.astro    # ZH Stories index
│   ├── ai.astro            # AI / Making story
│   ├── zh-ai.astro         # ZH AI / Making story
│   ├── darts.astro         # Darts story
│   ├── zh-darts.astro      # ZH Darts story
│   ├── decathlon.astro     # Decathlon case study
│   ├── mayora.astro        # Mayora case study
│   ├── cny-campaign.astro  # CNY campaign deep-dive
│   ├── decathlon-ux.astro  # Decathlon UX deep-dive
│   ├── making/             # Product listing (auto-generated)
│   └── products/           # Product detail pages (auto-generated)
├── components/             # React/TSX components
│   ├── ProductCard.tsx
│   └── ProductGrid.tsx
├── content/
│   └── products/           # ⭐ Product markdown files go here
│       └── product1.md     # Add product2.md, product3.md, etc.
├── layouts/
│   └── BaseLayout.astro    # Shared layout (head, theme, nav, footer)
└── styles/
    └── global.css          # Design system tokens and global styles
public/                     # Static assets (images, favicon, etc.)
context/                    # Shared context files
CLAUDE.md                   # Context for Claude Code
AGENTS.md                   # This file (for Codex)
ROADMAP.md                  # Project roadmap
```

### ⭐ Product Content System

To add a new product/project, create a `.md` file in `src/content/products/`:

```markdown
---
title: "Product Name"
description: "One-line description"
pubDate: 2026-05-06
tags: ["tag1", "tag2"]
status: building          # building | live | archived
---
## Body content (markdown)
```

The product automatically appears on the `/making/` listing page and gets its own detail page at `/products/product-name/`.

---

## Critical Rules

- **Build before deploying:** Run `npm run build` before pushing — Astro errors will surface at build time
- Never change verified data without checking source files (`Trevor_WorkContext_ForWebsite.md`)
- All icons must be inline SVGs
- Do NOT use Tailwind CDN — removed in migration, all CSS is local
- Only modify files explicitly mentioned in the task
- After any change, update `ROADMAP.md` (mark completed items, update date)

### Astro-specific rules

- **CSS import:** Always use `import` in frontmatter, never `<link rel="stylesheet">`
- **Script scoping:** Use `<script is:inline>` if functions need global access (e.g. `onclick` handlers)
- **Dynamic elements:** CSS classes added via JS `createElement` need `:global()` wrapper in `<style>` blocks
- **Dark mode selectors:** Always wrap `[data-theme="dark"]` with `:global()` in scoped `<style>`

Direction rules:

- Do not re-expand the homepage into a long-scroll resume by default
- Do not treat `Stories` as a generic misc bucket
- `darts` belongs under `Stories`
- `AI` should increasingly be framed as `AI / Making`, not primarily as a personal story page
- Premium feel should come mainly from restrained hover and click / transition behavior, not decorative animation

Full rules in `/context/rules.md`.

---

*Last updated: 2026-05-03*

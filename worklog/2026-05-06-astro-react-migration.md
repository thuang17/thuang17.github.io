# Astro + React Migration — 2026-05-06

## Summary

Migrated the personal website from pure static HTML to **Astro v5 + React 19 + TypeScript**.
All 18 pages now share a single layout template and design system. Added a products content system for the Making section.

## What Changed

### Before (pure HTML)
- 18 standalone `.html` files, each duplicating `<head>`, fonts, CSS tokens, theme script
- Tailwind CSS loaded via CDN (external dependency)
- No build step — push raw files to GitHub Pages
- No component system — every page's CSS/JS was independent
- Adding a product required hand-writing a full HTML page

### After (Astro + React)
- Shared `BaseLayout.astro` — head, theme, fonts, footer in one place
- Global CSS (`src/styles/global.css`) — design tokens, reset, typography, cursor
- Page-specific CSS auto-scoped by Astro
- All CSS bundled locally, no CDN dependency
- Build step: `npm run build` → optimized static output to `dist/`
- GitHub Actions auto-builds on push to `main`
- Products: write `.md` → auto-generated listing + detail pages
- React components ready for interactive product pages

## Files Migrated (18 pages)

| Page | File | Route |
|------|------|-------|
| EN Homepage | `src/pages/index.astro` | `/` |
| ZH Homepage | `src/pages/zh.astro` | `/zh` |
| Work Index | `src/pages/work.astro` | `/work` |
| ZH Work Index | `src/pages/zh-work.astro` | `/zh-work` |
| Stories Index | `src/pages/stories.astro` | `/stories` |
| ZH Stories Index | `src/pages/zh-stories.astro` | `/zh-stories` |
| AI/Making Story | `src/pages/ai.astro` | `/ai` |
| ZH AI/Making Story | `src/pages/zh-ai.astro` | `/zh-ai` |
| Darts Story | `src/pages/darts.astro` | `/darts` |
| ZH Darts Story | `src/pages/zh-darts.astro` | `/zh-darts` |
| Decathlon Case Study | `src/pages/decathlon.astro` | `/decathlon` |
| Mayora Case Study | `src/pages/mayora.astro` | `/mayora` |
| CNY Campaign | `src/pages/cny-campaign.astro` | `/cny-campaign` |
| Decathlon UX | `src/pages/decathlon-ux.astro` | `/decathlon-ux` |
| ZH Decathlon | `src/pages/zh-decathlon.astro` | `/zh-decathlon` |
| ZH Mayora | `src/pages/zh-mayora.astro` | `/zh-mayora` |
| Making Listing | `src/pages/making/index.astro` | `/making/` |
| Products (dynamic) | `src/pages/products/[...slug].astro` | `/products/*` |

## New Files Created

| File | Purpose |
|------|---------|
| `package.json` | Dependencies (Astro, React, TypeScript) |
| `astro.config.mjs` | Astro config with React integration |
| `tsconfig.json` | TypeScript config |
| `src/layouts/BaseLayout.astro` | Shared layout (head, theme, fonts) |
| `src/styles/global.css` | Design system, reset, typography |
| `src/styles/global.css` | Custom cursor, dark mode, utility classes |
| `src/components/ProductCard.tsx` | React product card |
| `src/components/ProductGrid.tsx` | React product grid |
| `src/content/config.ts` | Content collection schema |
| `src/content/products/product1.md` | Product placeholder |
| `.github/workflows/deploy.yml` | GitHub Actions → Pages |

## Bug Fixes (found during migration)

| Bug | Root Cause | Fix |
|-----|------------|-----|
| White background, missing cursor | BaseLayout used `<link rel="stylesheet">` (not resolve in prod) | `import` in Astro frontmatter |
| Info panel unresponsive | `<script>` bundled as ES module, `onclick` couldn't find functions | Added `is:inline` |
| Darts ruler ticks invisible | `.ruler-tick` created by JS, Astro scoped CSS didn't apply | `:global(.ruler-tick)` |
| Same bug in 5 more pages | Same pattern in decathlon, mayora, zh-* | `:global()` fix applied everywhere |
| zh-decathlon / zh-mayora 404 | Pages existed at root but not migrated to Astro | Created `.astro` versions |

## Key Lessons for Future Sessions

1. **CSS import**: `import '../styles/global.css'` in frontmatter, NOT `<link>`
2. **Script scoping**: `<script is:inline>` for global functions, `addEventListener` otherwise
3. **Dynamic elements**: Any `createElement` class needs `:global()` in CSS
4. **Dark mode**: Always wrap `[data-theme="dark"]` with `:global()` in scoped `<style>`
5. **Build required**: Always run `npm run build` before pushing

## Product Content System

To add a new product:

```markdown
# src/content/products/product-name.md
---
title: "Product Name"
description: "One-line description"
pubDate: 2026-05-06
tags: ["tag1", "tag2"]
status: building    # building | live | archived
---
Write product content in markdown...
```

The product auto-appears on `/making/` and gets its own page at `/products/product-name/`.

## Commits

```
b99cdee cleanup: remove old index.html and zh.html (migrated to Astro)
2fbc20e cleanup: remove deprecated HTML files (migrated to Astro)
f28cb2d fix: ruler-tick CSS scoping on decathlon, mayora, zh-*
3fee39e fix: zh-decathlon/zh-mayora 404, darts ruler, cross-links
088037a fix: global CSS loading, Info panel JS scope, cursor; update docs
efff38f feat: migrate to Astro + React with product content system
```

# Horizontal Homepage Integration Design

Date: 2026-05-04
Project: Trevor Huang personal website
Status: Approved via visual brainstorming

## Goal

Migrate the horizontal demo's interaction model (continuous surface, velocity/friction scroll, Minimal Scrubber) into the production homepage, replacing the current `index.html` and `zh.html` entirely.

## Architecture

The homepage is a single continuous horizontal surface with 5 panels. A top bar holds the Minimal Scrubber (centered) and language + theme controls (right-aligned). No traditional nav links, no footer.

## Top Bar

- One row: Scrubber centered, 「中文」+ sun/moon SVG (no border) on the right
- Scrubber: B2 spec — 3px track, `#e8e5e0` (dark: `#3f3f46`), 48×14px pill, `#c4c0bb` (dark: `#71717a`), 200px max-width, continuous position update
- Theme icons: existing SVG sun (rays + circle) / moon (crescent) from current `index.html`, no button frame

## Panel System

5 panels, all same width `min(80vw, 1240px)` and same height. Ordered left to right:

### Panel 1 — Hero
- Background `#f9f9f9`
- Text: Geist, 28px (reference; real page uses `clamp(56px, 8vw, 96px)`), weight 500, line-height 1.1
- Circle: `#d9d4d0`, ~55vw / max 700px, right side, partially overflowing, behind text
- Content (6 lines):
  1. Trevor Huang — left-align, margin-left: same as lines 3/5
  2. is a student — left-align, margin-left: same as lines 4
  3. at USyd — left-align, margin-left: same as line 1
  4. working on — left-align, margin-left: same as line 2
  5. figuring things out — left-align, margin-left: same as line 1
- Lines 1,3,5 share one left alignment; lines 2,4 share a different left alignment
- No kicker, no meta pills, no Info button
- Animation (reduced-motion aware): text lines stagger fade-up (0.08s apart), circle scales 0.85→1 (0.6s ease-out)

### Panel 2 — Work
- Title: "WORK", 90px, Geist, weight 600, centered
- Subtitle: "Selected proof from real operating environments.", left-aligned, 15px, Geist
- Click → navigates to `decathlon.html` with page-out transition

### Panel 3 — Making
- Title: "MAKING", 90px, Geist, weight 600, centered
- Subtitle: "Experiments, tools, and self-directed building.", left-aligned, 15px, Geist
- Click → navigates to `ai.html` with page-out transition

### Panel 4 — Stories
- Title: "STORIES", 90px, Geist, weight 600, centered
- Subtitle: "Personal material around repetition, pressure, and recovering from failure.", left-aligned, 15px, Geist
- Click → navigates to `darts.html` with page-out transition

### Panel 5 — Info
- Content: "Info" in huge Geist font, right-aligned, the "o" partially clipped by the right panel edge
- Click → opens centered overlay (not navigates)
- Overlay content:
  - Education: University of Sydney (2025–2027, MPM) / SUIBE (2020–2024, Bachelor's) — school names and degrees on same line
  - Toolkit: Python · SQL · Tableau · Excel · Jira · Feishu · MS Project · Agile Methodologies
  - Contact: Email, LinkedIn, Instagram, X, Xiaohongshu
  - Languages: Chinese — Native · English — Professional
- Overlay: full screen backdrop blur, close on background click or Escape

## Motion Model

- Input: wheel + trackpad, mapped to dominant delta
- Physics: velocity accumulation (acceleration 0.16), friction decay (0.9), max velocity 120, stop threshold 0.08
- No snap, continuous movement
- All panels shrink together via `surface-scaler` (scale 1→40/72, origin left center)
- Scrubber pill follows `state.x / state.maxX` proportionally

## Mobile (<980px)

- Panels stack vertically, horizontal scroll disabled
- Scrubber hidden
- `body { overflow: auto }`

## Preserved from Current Site

- Design tokens (`:root` / `[data-theme="dark"]`)
- Theme toggle JS (localStorage persistence)
- Page exit transition (`body.page-out main`)
- Scroll reveal (`IntersectionObserver` for `.reveal`)
- Reduced-motion awareness
- Subpages: `decathlon.html`, `mayora.html`, `cny-campaign.html`, `decathlon-ux.html`, `darts.html`, `ai.html` and `zh-*` variants

## Removed from Current Site

- Old nav links (Work, AI/Making, Stories, Contact)
- Stacked section layout
- Avatar and side-avatar
- Footer with social icons (absorbed into Info overlay)
- Proof cards, work rows, info strip

## Bilingual

- `index.html`: English, nav shows 「中文」→ `zh.html`
- `zh.html`: Chinese, nav shows 「EN」→ `index.html`
- Content mirroring TBD in implementation plan (Chinese copy to be written)

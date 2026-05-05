# Sub-page Visual Unification — Design Spec

**Date:** 2026-05-05
**Status:** Approved
**Branch:** `claude/bold-mahavira-f48b76`

---

## 1. Overview

Unify all 6 child pages (decathlon, mayora, cny-campaign, decathlon-ux, ai, darts) to match the new design language established by index.html and work.html. This is a deep unification: fonts, colors, cursor, nav chrome, content structure, and editorial tone all get updated.

---

## 2. Content Architecture Change (Option A)

**Decision:** Merge project detail pages into experience pages. Remove standalone project entries from work.html.

### work.html / zh-work.html changes
- Remove Projects section (2 rows: CNY Campaign + Decathlon UX / 即时零售CNY大促 + 微信小程序用户体验优化)
- Keep only Experience 4 rows
- cny-campaign.html and decathlon-ux.html remain on disk but lose their entry points from work.html

### Content merge mapping
| Old project page | Merged into |
|-----------------|-------------|
| decathlon-ux.html → WeChat UX content | decathlon.html |
| cny-campaign.html → CNY campaign content | mayora.html |

---

## 3. Shared Design Tokens (all sub-pages)

### Colors
```css
--bg:      #E8E8E8;
--bg-sub:  #F0EEE8;
--bg-foot: #E8E6DE;
--fg:      #1C1917;
--fg-2:    #57534E;
--fg-3:    #A8A29E;
--border:  #E7E5E4;
--accent:  #7C3AED;
```
Dark mode:
```css
[data-theme="dark"] {
  --bg:      #18181B;
  --bg-sub:  #292524;
  --bg-foot: #292524;
  --fg:      #FAFAFA;
  --fg-2:    #A8A29E;
  --fg-3:    #57534E;
  --border:  #44403C;
  --accent:  #A78BFA;
}
```

### Typography
- **Display / Headings:** Geist (400, 500, 600) via Google Fonts
- **Body:** Nunito Sans (300, 400, 500, 600) via Google Fonts
- **Mono / Labels:** JetBrains Mono (300, 400) via Google Fonts
- Chinese pages add Noto Sans SC

### Cursor
- Global: coral dot `#E07B5A`, r=7px, CSS `cursor: url(data:image/svg+xml,...)`
- Interactive (links, buttons): same color, r=8px
- Draggable areas: system cursor (`grab`/`grabbing`)

---

## 4. decathlon.html — Page Spec

### 4.1 Layout
- Single column, `max-width: 680px`, `margin: 0 auto`, `padding: 0 32px`
- No sticky TOC, no sidebar, no footer

### 4.2 Topbar
- `position: fixed`, `pointer-events: none` (children `pointer-events: auto`)
- Left: `← Work` in JetBrains Mono 12px (links to `work.html`)
- Right: language toggle (`中文` → zh-decathlon.html, mono 12px) + theme toggle (sun/moon SVG)
- Exact positioning matches work.html

### 4.3 Page Header
- 80px top padding (clearing fixed topbar)
- Title: "Decathlon" in Geist 48px, weight 400, letter-spacing -0.02em, color fg
- Subtitle: "E-commerce Technology PM Intern · 2025–2026" in Nunito Sans 16px, color fg-2
- No meta-row (Period/Location/Team/Type removed)

### 4.4 Body Text
- Opening paragraphs: Nunito Sans 18px, color fg, line-height 1.8
- Content paragraphs: Nunito Sans 16px, color fg-2, line-height 1.8
- Paragraph spacing: 16px

### 4.5 Section Headings
- Geist 28px, weight 400, letter-spacing -0.01em, color fg
- 80px gap between sections, 24px gap between heading and first paragraph

### 4.6 Pull Quotes (key decisions / insights)
- `border-left: 1px solid var(--accent)`, `padding-left: 20px`
- Nunito Sans 15px, italic, color fg
- 32px vertical margin

### 4.7 Content Sections (in order)
1. **Opening** (untitled) — 2 paragraphs of context
2. **WeChat Mini Program UX** — main body: how it started, research, 16 pain points, Value-Effort matrix, courier pickup decision (pull quote), BRD output
3. **UAT Coordination** — 8 projects, CS team story
4. **PM Tool Optimization** — 13 pain points, Trello introduction
5. **Reflection** — what I'd do differently

### 4.8 No elements
- No TOC sidebar
- No bordered h2/h3
- No callout boxes
- No data cards / data rows
- No next link
- No footer
- No scroll reveal animations (replaced by single page-load entrance)

### 4.9 Entrance Animation
- 400ms opacity 0→1 + translateY 6px→0 on the main content wrapper
- `ease-out` timing
- Triggered on DOMContentLoaded (no row stagger, no dot leader)
- Wrapped in `@media (prefers-reduced-motion: no-preference)`

### 4.10 Exit Transition
- Link clicks (that navigate away) trigger `body.page-out` → main `opacity: 0, translateY: 8px`, 180ms
- After transition, `window.location.href` navigates

### 4.11 Dark Mode
- Inline `<script>` in `<head>` reads localStorage to set `data-theme` before paint
- Toggle button swaps sun/moon SVG icons
- All color tokens respond to `[data-theme="dark"]`

### 4.12 Responsive
- `<680px`: reduce padding to 20px, Geist 48px→36px heading, Geist 28px→24px section heads
- `<480px`: Geist 48px→32px, body 18px→16px

---

## 5. Implementation Order

| # | Page | Type |
|---|------|------|
| 1 | decathlon.html | Work experience (primary, most content) |
| 2 | mayora.html | Work experience (similar structure to decathlon) |
| 3 | cny-campaign.html | Project detail → merged into mayora |
| 4 | decathlon-ux.html | Project detail → merged into decathlon |
| 5 | ai.html | Story page |
| 6 | darts.html | Story page |
| 7 | work.html + zh-work.html | Update: remove Projects rows |

---

## 6. Decisions Log

| Decision | Reason |
|----------|--------|
| Merge projects into experiences (Option A) | Trevor's experience is still thin; splitting core projects out of experiences creates duplicate content and weakens both pages |
| No entrance animation stagger | Detail pages are for reading, not discovery. A single quiet fade is enough |
| No footer / no next link | work.html is the navigation hub; duplicating nav at page bottom is visual noise |
| Pull quote replaces callout box | More editorial, less corporate wiki. Same emphasis, lighter touch |
| Geist + Nunito Sans kept | Search results confirmed no better alternatives for this editorial style |
| Content preserved, presentation changed | The existing copy is good — tone is right, details are specific. The problem was the report-style framing |

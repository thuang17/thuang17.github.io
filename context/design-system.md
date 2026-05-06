# Design System

## Color Tokens

```css
--bg:       #E8E8E8   /* page background */
--bg-sub:   #F0EEE8   /* hover / card background */
--bg-foot:  #E8E6DE   /* footer background */
--fg:       #1C1917   /* primary text */
--fg-2:     #57534E   /* secondary text */
--fg-3:     #A8A29E   /* labels / dates / muted */
--border:   #E7E5E4
--border-2: #C9C8C4
--accent:   #7C3AED   /* purple — primary accent */
--accent-2: #6D28D9
```

Dark mode via `data-theme="dark"` on `<html>`, persisted to localStorage.

---

## Typography

| Role | Font | Weight |
|------|------|--------|
| Hero / display | Geist | 400, 500, 600 |
| Display / headings fallback | Montserrat | 700, 800 |
| Body text | Nunito Sans | 300, 400, 500, 600 |
| Labels / dates / mono | JetBrains Mono | 300, 400 |
| Chinese fallback | Noto Sans SC | added on ZH pages only |

Base font size: 16px. Line height: 1.75 (body), 1.1 (large headings).
Fonts loaded via `@import` in `src/styles/global.css`.

## CSS Source

Updated 2026-05-06: All design tokens moved to `src/styles/global.css`.
Page-specific CSS lives in each `.astro` file's `<style>` block (auto-scoped by Astro).
**Do NOT add `<link rel="stylesheet">` tags** — import CSS in Astro frontmatter instead.

---

## Layout

- Main container: `max-width: 1080px`, `padding: 0 48px`
- Case study pages: `max-width: 1160px`, `padding: 0 48px`
- Case study two-column: `grid-template-columns: 1fr 220px`, `gap: 0 60px`
- Article reading column: `max-width: 680px`
- Mobile breakpoint: 860px (sidebar hidden), 480px (data cards stack)

---

## Component Patterns

### Navigation (main pages)
- Sticky, frosted glass on scroll (`backdrop-filter: blur(14px)`)
- Height: 52px
- Links: 13px, font-weight 500

### Navigation (detail pages)
- Sticky, solid background
- Height: 56px
- Breadcrumb style: `Trevor Huang / Page Name`

### Section headers (detail pages)
```css
h2 {
  font-family: Montserrat; font-size: 18px; font-weight: 700;
  padding-bottom: 10px; border-bottom: 1px solid var(--border);
}
```

### Callout boxes
```css
.callout {
  background: var(--bg-sub);
  border-left: 3px solid var(--accent);
  border-radius: 0 8px 8px 0;
  padding: 14px 18px;
}
```

### Data cards
```css
.data-card {
  background: var(--bg-sub); border: 1px solid var(--border);
  border-radius: 8px; padding: 14px 16px;
}
.data-card .num { font-family: Montserrat; font-size: 22px; font-weight: 800; color: var(--accent); }
```

### Tags / chips
```css
.tag {
  font-family: JetBrains Mono; font-size: 11px;
  color: var(--accent); background: rgba(124,58,237,0.07);
  border: 1px solid rgba(124,58,237,0.20);
  padding: 2px 10px; border-radius: 20px;
}
```

### Sticky TOC sidebar (detail pages)
```css
.toc-wrap { position: sticky; top: 72px; padding-top: 48px; }
.toc-list a { font-family: JetBrains Mono; font-size: 12px; border-left: 2px solid transparent; }
.toc-list a.active { color: var(--accent); border-left-color: var(--accent); }
```

Active TOC highlighting via IntersectionObserver with `rootMargin: '-20% 0px -70% 0px'`.

---

## Scroll Reveal

```css
.reveal { opacity: 0; transform: translateY(14px); transition: opacity .5s ease, transform .5s ease; }
.vis    { opacity: 1; transform: none; }
```

Applied via IntersectionObserver at `threshold: 0.08`.

---

## Icons

All icons are inline SVGs (Lucide-style, stroke-based). No icon CDN — CDN loading was unreliable.

---

## What to Avoid

- No emojis as UI elements
- No gradients on backgrounds (accent purple only on text/borders/data numbers)
- No heavy animations (max 300ms transitions)
- No horizontal scroll on mobile
- No Tailwind CDN (removed in migration, all styles are local)

---

*Last updated: 2026-05-07*

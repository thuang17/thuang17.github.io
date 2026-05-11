# Hero Text Redesign — 2026-05-11

## Overview

Replace the 5-line hero statement on the homepage (EN + ZH) with a shorter, larger greeting. The purple circle accent and entry animation remain unchanged.

---

## English (`src/pages/index.astro`)

### Text content (2 lines, no punctuation)
```
Hi I'm
Trevor
```

### CSS changes to `.hero-text`
- `font-size`: `clamp(56px, 8vw, 96px)` → `clamp(72px, 11.7vw, 168px)`
- Add `margin-left: 34px` to shift the whole text block rightward into the circle

### HTML `entry-line` inline margin-left (unchanged from current)
- Line 1: `style="margin-left:-0.3em"`
- Line 2: `style="margin-left:0.1em"`

---

## Chinese (`src/pages/zh.astro`)

### Text content (2 lines, no punctuation)
```
你好
我是黄拓文
```

### CSS changes to `.hero-text`
- `font-size`: `clamp(56px, 8vw, 96px)` → `clamp(64px, 9.3vw, 134px)`
- No block-level margin-left (each line has its own offset)

### HTML `entry-line` inline margin-left (per-line offsets)
- Line 1 「你好」: `style="margin-left:calc(-0.3em + 99px)"`
- Line 2 「我是黄拓文」: `style="margin-left:calc(0.1em - 22px)"`

---

## Animation

No changes to animation CSS. The existing delays on `entry-line:nth-child(1)` (200ms) and `nth-child(2)` (290ms) work correctly. Selectors for lines 3–5 match nothing and are harmless.

---

## Files to edit

1. `src/pages/index.astro` — `.hero-text` CSS + hero panel HTML (2 lines)
2. `src/pages/zh.astro` — `.hero-text` CSS + hero panel HTML (2 lines, per-line offsets)

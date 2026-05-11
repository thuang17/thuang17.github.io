# Hero Text Redesign — 2026-05-11

## Overview

Replace the 5-line hero statement on the homepage (EN + ZH) with a shorter, larger greeting. The purple circle accent and entry animation remain unchanged.

## Changes

### Text content

| File | Before | After |
|------|--------|-------|
| `src/pages/index.astro` | "Trevor Huang / is a student / at USyd / working on / figuring things out" (5 lines) | "Hi, I'm" / "Trevor." (2 lines) |
| `src/pages/zh.astro` | "黄拓文 / 在悉尼大学 / 读项目管理 / 边学边试 / 在探索中成长" (5 lines) | "你好，我是" / "黄拓文" (2 lines) |

Both lines keep the existing alternating `margin-left` offsets (`-0.3em` on line 1, `0.1em` on line 2).

### Font size

`.hero-text` font-size: `clamp(56px, 8vw, 96px)` → `clamp(80px, 11.7vw, 168px)`

### Text position (rightward offset)

Add `margin-left: 34px` to `.hero-text` to shift the text block 34px right of center, so the text overlaps the purple circle.

### Animation

No changes. The existing `entry-line:nth-child(1)` (200ms) and `nth-child(2)` (290ms) delays work correctly with 2 lines. Selectors for lines 3–5 simply match nothing.

## Files to edit

- `src/pages/index.astro` — `.hero-text` CSS + hero panel HTML
- `src/pages/zh.astro` — same CSS + hero panel HTML

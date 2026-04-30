# Collaboration Rules

Rules for any AI working on this project.

---

## Before Starting Any Task

1. Read `project-context.md` — understand goals, tone, key data
2. Read `design-system.md` — if the task touches UI or styling
3. Read `case-studies.md` — if the task touches case study content
4. Check `ROADMAP.md` — understand current state and what's pending

---

## Data Integrity

- Never change verified numbers without checking source files:
  - `Trevor_WorkContext_ForWebsite.md`
  - `Trevor_WorkExperience_Memory_01.md`
- If a number seems wrong, flag it — don't silently "fix" it
- Key data table is in `project-context.md`

---

## Content Rules

- No resume-style bullet points — use narrative paragraphs
- No AI-sounding Chinese patterns: 通过...实现了 / 此外 / 综上 / 不仅...而且
- Every claim needs a specific number or concrete example
- Do not invent details — only use what Trevor has explicitly provided
- Trevor has not held a formal "Project Manager" title — do not use that label

---

## Code Rules

- Do not use Tailwind CDN on detail pages (decathlon.html, mayora.html, etc.)
- index.html and zh.html use Tailwind CDN — that's intentional, do not remove
- All icons must be inline SVGs — no external icon CDN
- Dark mode via `data-theme="dark"` on `<html>` — always test both modes
- All pages must be mobile-responsive — test at 860px and 480px breakpoints
- No horizontal scroll on mobile

---

## Scope Control

- Only modify files explicitly mentioned in the task
- Do not "improve" other files while working on the assigned one
- Do not add new sections without explicit instruction
- Do not change the design system tokens without explicit instruction

---

## File Maintenance

- Update `ROADMAP.md` after each meaningful change (mark tasks complete, update date)
- Update relevant `/context` files if project direction, design system, or case study data changes
- These files are version-controlled — treat them as the source of truth

---

## How Claude Code Uses This

Claude Code (the primary AI for this project) reads the repo directly and does not need files pasted manually. It maintains project memory via CLAUDE.md and session summaries.

## How ChatGPT / Codex Should Use This

Paste the relevant context files at the start of each conversation:
- Content task → paste `project-context.md` + `case-studies.md`
- Design/UI task → paste `project-context.md` + `design-system.md`
- New page task → paste all three + the most relevant existing HTML page as reference

Always end your prompt with explicit constraints:
> "Do not modify any other files. Only do X. Do not change the design system."

---

*Last updated: 2026-04-30*

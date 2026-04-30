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
Built for job hunting targeting Chinese domestic and foreign-invested companies.

Live URL: https://thuang17.github.io

---

## Tech Stack

- Pure HTML + CSS + vanilla JS (no framework, no build step)
- index.html uses Tailwind CDN — detail pages use pure CSS only
- All icons are inline SVGs — no external icon CDN
- Dark mode via `data-theme="dark"` on `<html>`, persisted to localStorage
- Zero build steps — deploy by pushing to GitHub

---

## File Structure

```
index.html           — English main page (primary)
zh.html              — Chinese main page

decathlon.html       — Decathlon full work case study
mayora.html          — Mayora full work case study
cny-campaign.html    — CNY campaign project deep-dive
decathlon-ux.html    — Decathlon UX project deep-dive
darts.html           — Darts story (About section)
ai.html              — AI Explorer story (About section)
zh-darts.html        — Chinese darts story
zh-ai.html           — Chinese AI story

context/             — Shared context files (read before any task)
darts/               — Photo assets for darts story page
CLAUDE.md            — Context file for Claude Code
AGENTS.md            — This file (for Codex)
ROADMAP.md           — Project roadmap and decisions log
```

---

## Critical Rules

- Never change verified data without checking source files (`Trevor_WorkContext_ForWebsite.md`)
- Do not use Tailwind CDN on detail pages
- All icons must be inline SVGs
- Only modify files explicitly mentioned in the task
- After any change, update `ROADMAP.md` (mark completed items, update date)

Full rules in `/context/rules.md`.

---

*Last updated: 2026-04-30*

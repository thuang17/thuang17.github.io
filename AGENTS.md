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

Direction rules:

- Do not re-expand the homepage into a long-scroll resume by default
- Do not treat `Stories` as a generic misc bucket
- `darts` belongs under `Stories`
- `AI` should increasingly be framed as `AI / Making`, not primarily as a personal story page
- Premium feel should come mainly from restrained hover and click / transition behavior, not decorative animation

Full rules in `/context/rules.md`.

---

*Last updated: 2026-05-03*

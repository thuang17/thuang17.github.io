# CLAUDE.md — Trevor Huang Personal Website

Trevor Huang's personal site, live at https://thuang17.github.io. Since 2026-11-17 the whole site is the pixel-art town (V2): the old Astro site, the Chinese pages and the old components were deleted. Do not bring them back.

## What is live
- `/` and `/town/`: the town, a single-file canvas game. Walk to a building, press E to open a board (Projects/ChamberUp, Favorites, Guestbook, About Me). Narrow screens (under 900px) get a card with four buttons instead of the game.
- `/#projects`, `/#favorites`, `/#guestbook`, `/#about` open a board directly.
- `/chamberup`, `/work`, `/darts`, `/stories`, `/guestbook`: tiny redirect pages so old links still land in the right board.
- `/guestbook-admin`: moderation page (Bearer admin token). Uses `BaseLayout` and `public/fonts`.
- `404.astro`: the not-found page.

## Source of truth for the town
- Edit `docs/v2/town/index.html` (and assets under `docs/v2/`). Never edit `public/town/` by hand; it is generated.
- Export and build:
  ```bash
  python3 docs/v2/tools/export_town.py "$PWD" town --home
  npm run build
  ```
  `--home` also writes `public/index.html` (uses `<base href="/town/">`). The export injects the public guestbook API URL and Turnstile site key from `.env.production`.
- Character art: `docs/v2/tools/make_char_hi.py` (walk sheet), `make_avatar.py`, `make_demo_video.py`. Characters are drawn 1:1 with hard alpha, never resampled.
- Dev-only build mode (`?build`, `?open=`, `?design`) only works on localhost.

## Guestbook backend
- `guestbook-api/`: Cloudflare Worker + D1 (`wrangler dev --local` for testing). Public endpoints under `/api/posts`; admin under `/api/admin/*`.
- Notes are hidden until approved. Limits: nickname 30, body 1000, 5 posts per hour per IP.
- Never write to the live database without Trevor's permission.

## Deploy and rollback
- Pushing to `main` builds and deploys to GitHub Pages (`.github/workflows/deploy.yml`). Local work is usually on branch `v2`; publish with `git push origin v2:main`.
- Old site, if ever needed: commit `32ff95c` (before the town became the homepage).
- Commit or push only when Trevor says so. Stage only the files you changed; the working tree has unrelated untracked files (LOGO-*, darts/ originals).

## Content rules
- `Trevor_WorkContext_ForWebsite.md` and `Trevor_WorkExperience_Memory_01.md` are the source for any work history or numbers. Do not invent anything.
- Tone: casual, direct, specific; no AI-sounding filler. English site only for now.
- Title rule: only the ChamberUp board may say "Project Manager & Product Owner" (confirmed 2026-10-23). Work-experience entries stay "PM Intern".

## Files
```
src/pages/        404, redirect pages, guestbook-admin
src/layouts/      BaseLayout.astro
src/styles/       global.css (used by the admin page)
public/           generated town, index.html, fonts, favicons
docs/v2/          town source, tools, assets
guestbook-api/    Worker + D1
```
Stack: Astro 5 static output, no React. `ROADMAP.md` is from the old site and is out of date.

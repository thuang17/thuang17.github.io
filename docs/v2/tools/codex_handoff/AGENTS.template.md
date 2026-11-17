# Task: design the Guestbook board for a pixel-art town website

You are helping design ONE screen. Read this whole file first.

## What this project is
A personal website whose homepage is a top-down pixel-art town (like a cosy farming game). The visitor walks a small character around. Walking up to a building or the **notice board in the town square** and pressing E opens a **wooden board** in the middle of the screen, with that entrance's content on it. This task is the **Guestbook**, which opens from the notice board.

## What to design
Inside the open wooden board, design how a visitor sees and writes guestbook notes:
1. The **list of notes** (nickname, message, how long ago, optional replies from the owner).
2. The **form to leave a note** (nickname field, message field with a 0 to 1000 character counter, a Send button, a small line saying "I read every note before it goes up").
3. Empty, sending, success ("thanks, it will appear after review"), and error states.

Creative direction (this is the part you decide): present notes as **small paper notes pinned to the wooden board** (like a real notice board: cream, soft teal and warm yellow papers, slightly different sizes, a round pin or nail on each, tiny tilts of one or two degrees at most). The form can be a blank paper note the visitor writes on. It must still be easy to read and use. Do not make it messy.

## Hard rules (the owner will reject work that breaks these)
- **Pixel-art look only**: hard pixel edges, flat colour, no gradients, no blur, no rounded soft shadows, no photos, no emoji. Draw with CSS (borders, box-shadow with zero blur, `image-rendering: pixelated`), not with generated images. If you need an image, make it as a tiny pixel image in code (CSS or inline SVG with `shape-rendering="crispEdges"`).
- **Font**: only **Jersey 15** (already loaded in index.html). One weight. Never use fake bold.
- **Colours**: use only the palette already on the board and the town: wood browns `#4B3025` (outline), `#9E5F2C`, `#C26A2B`; cream `#FBE9C4`, `#F4E9D2`; warm yellow `#FFD36E`, `#FBC24B`; soft teal `#7FB5A8`; sage `#8DB580`. No pink, no red, no magenta, no pure black, no pure white.
- **Outline**: every paper note and button has a 1-art-pixel dark brown outline. In this page one art pixel is 2 CSS pixels at the default zoom, so use 2px or 4px, not 1px or 3px.
- **Real HTML text** (selectable, readable by screen readers), never text drawn on a canvas. Keyboard usable. Visible focus state. Respect `prefers-reduced-motion`.
- All user text must be inserted with `textContent` (never `innerHTML`), because it comes from strangers.
- **Do not call any network API.** Use `mock-notes.json` (it is sample data, clearly NOT real messages) so the design can be tested. The real backend is connected later by someone else; `mock-notes.json` includes the API shape only as a reference.
- **Do not change anything outside the Guestbook**: not the town, the character, the other boards, the scrollbar, the X button, `ui_layout.json`, `layout.json`, `a/`, `ui/`, `media/`. Only edit `index.html`, and only: the `Guestbook:` entry in the `CONTENT` object, plus a CSS block you add that starts with the comment `/* guestbook */` and only uses selectors that begin with `.board .gb-`.
- Do not add libraries or fonts. No build tools. Plain HTML, CSS and a little JavaScript.
- Do not add real personal data. Do not invent testimonials.

## How to run and check your work
```
cd <this folder>
python3 -m http.server 8190
```
Open http://127.0.0.1:8190/?open=Guestbook  (the `open` parameter opens the board straight away). Check at a wide window (1400 wide) and a narrow one (400 wide, phone). Check with all three notes in `mock-notes.json`, with zero notes, and with 30 notes (generate extra ones in code). The board scrolls with its own pixel scrollbar when the content is long.

## When you finish
Reply with: what you designed, what the visitor sees in each state, anything you were unsure about, and the list of things you changed. Keep the changes small and easy to review. Do not delete anything.

## Housekeeping (the owner wants no leftovers)
- Work only inside this folder. Put every temporary file (previews, test pages, scripts, screenshots) inside it too, never in /tmp or anywhere else.
- Start at most one preview server, on one port. Stop it when you finish.
- In your final reply, list: the files you changed, any extra files you created, and any server still running. The owner will have the folder deleted after the work is merged, so do not leave anything you want to keep outside the files you report as changed.


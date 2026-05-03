# Single-Surface Homepage Design

Date: 2026-05-03
Project: Trevor Huang personal website
Status: Draft approved in conversation, pending written spec review

## Goal

Redesign the homepage so it no longer reads like a vertically expanded resume.

The new homepage should function as a single, unified surface:

- calm at rest
- highly controlled in motion
- low in content density
- strong in visual identity
- details pushed into second-layer pages

This direction keeps the current first-fold large-card feeling that Trevor already likes, then extends that same interaction and layout language across the whole homepage instead of dropping into traditional stacked sections.

## Problem With Current Homepage

The current homepage already has a stronger first fold, but the rest of the page still falls back to a conventional structure:

- `Work` expands into detailed role summaries
- `Selected proof` expands into detailed case summaries
- `Info strip` behaves like a compressed resume footer

As a result, the homepage still feels like a resume page with a better opening card, rather than a fully designed personal website.

There is also a repetition problem:

- the first fold already provides entry points
- lower sections then repeat those entry functions with more content

The redesign should remove that duplication.

## Core Direction

The homepage becomes a **single-surface panel system**.

This means:

- the homepage is one designed environment, not a stack of unrelated sections
- the homepage exposes only one set of primary entry points
- case details no longer expand on the homepage
- details live in destination pages

The intent is to get closer to the feeling Trevor likes in references such as `rauno.me`, without mechanically copying the exact layout or interaction model.

## Surface Model

The homepage should be treated as one large primary surface.

Inside that surface:

- one panel is dominant at a time
- the next panel is partially visible
- panel transitions use controlled scale and slide
- the user gets a sense of tension, pull, and hand-feel before a full switch occurs

The system should feel intentional and physical, not decorative.

## Information Architecture

### Main panels

The homepage contains four main panels:

1. `Trevor / index`
2. `Work`
3. `AI / Making`
4. `Stories`

### Secondary state

`Info` is not a main panel.

It is a **secondary utility state** entered from the `Trevor / index` panel.

Reason:

- `Work`, `AI / Making`, and `Stories` are the main narrative tracks
- `Info` contains supporting metadata, not primary story content
- making `Info` equal in hierarchy would weaken the homepage focus

## Panel Roles

### 1. Trevor / index

Purpose:

- serve as the neutral homepage entry state
- set tone and identity
- introduce the site as Trevor's personal index, not a recruiter-first summary

Content shape:

- Trevor name
- one thesis-level statement
- a few light metadata chips if still useful
- auxiliary `Info` link

What it should not contain:

- a full navigation list for `Work / AI / Making / Stories`
- repeated summary blocks that duplicate the later panel system

### 2. Work

Purpose:

- represent real-world judgment and operating proof

Content shape:

- title
- one short framing statement
- possibly one or two compact signals
- entry into deeper work pages

What it should not contain:

- Decathlon and Mayora expanded into homepage paragraphs
- case-study-level bulleting or detailed proof blocks

### 3. AI / Making

Purpose:

- represent experiments, tool use, and builder instinct

Content shape:

- title
- one short framing statement
- minimal support signals
- entry into the deeper `AI / Making` page

What it should not contain:

- process breakdowns or long summaries on the homepage

### 4. Stories

Purpose:

- represent the more personal material that explains Trevor's discipline, repetition, and systems thinking

Content shape:

- title
- one short framing statement
- entry into deeper story pages

What it should not contain:

- long homepage narrative blocks

### Info

Purpose:

- hold supporting profile information
- absorb the homepage footer role

Likely contents:

- education
- language
- contact
- social links
- possibly a very light current-status note later

This state should feel quieter and more utility-like than the main panels.

## Navigation Model

### Top navigation

The top navigation should be reduced to functional controls only:

- language switch
- theme switch

Remove:

- `Trevor Huang`
- `Work`
- `AI / Making`
- `Stories`
- `Contact`

Reason:

If the panel system is the homepage's main entry mechanism, keeping a duplicate full navigation at the top would reintroduce the same redundancy the redesign is trying to remove.

### Panel entry model

The panel system itself becomes the homepage navigation.

Users should enter the site's primary areas through the panels, not through a duplicated list elsewhere on the same screen.

## Motion Direction

The chosen interaction direction is:

**Push-pull focus**

This means:

- hover creates pull or tension between the current panel and the next one
- scroll completes panel switching
- the current panel recedes slightly as the next panel becomes dominant
- the next panel grows into focus rather than simply appearing

The motion should feel:

- restrained
- premium
- tactile
- physically coherent

It should not feel:

- flashy
- elastic in a playful way
- like a product demo
- overloaded with constant movement

## Interaction Principles

### Hover behavior

Hover should:

- create anticipation
- reveal panel adjacency
- introduce slight scaling, offset, or tension

Hover should not:

- complete full navigation state changes on its own
- produce large or abrupt motion

### Scroll behavior

Scroll is the primary switching action.

The design may end up using vertical or horizontal progression internally, but the user requirement is not "must be horizontal."

The actual priority is:

- unified surface
- panel-based structure
- controlled motion
- low homepage content density

If a vertical implementation produces a better result than a forced horizontal one, that is acceptable.

### Click behavior

Click should move the user into second-layer detail pages.

The homepage should not try to partially become the detail page itself.

## Elements To Remove Or Absorb

### Remove from homepage

- current expanded `Work` section
- current expanded `Selected proof` section
- current `Info strip` as a standalone stacked section
- current left-side cartoon avatar
- current standalone footer block

### Absorb into new system

- footer information moves into `Info`
- homepage identity and entry logic move into the panel surface

## Elements To Preserve In Spirit

The redesign should preserve the qualities Trevor already likes in the current first fold:

- large-card feeling
- calm spaciousness
- low detail density
- strong framing through typography and whitespace

The redesign should not discard that language and replace it with something noisier or more product-marketing-like.

## Mobile Principle

Desktop interaction is the main reference for this design.

Mobile does not need to replicate the full tactile panel behavior exactly.

Mobile should preserve:

- single-surface logic
- reduced content density
- clear panel entry points

Mobile may simplify:

- motion intensity
- simultaneous peek states
- advanced hover-dependent behavior

## Open Implementation Questions

These are intentionally deferred to planning and prototype validation:

1. Whether the main panel progression is technically best implemented as:
   - horizontal transform system
   - vertical progression with lateral panel choreography
   - hybrid pinned section with panel switching
2. How much of the current first-fold copy survives unchanged
3. Whether the `Trevor / index` panel keeps all current metadata chips
4. Whether `Info` appears as:
   - an overlay-like state
   - an in-surface replacement state
   - a lighter panel nested inside the first state

These are implementation and prototyping questions, not direction questions.

## Out of Scope

This spec does not redesign:

- `ai.html`
- `zh-ai.html`
- work detail pages
- story detail pages
- global design tokens

This spec is only for homepage structure, hierarchy, and interaction language.

## Success Criteria

The redesign is successful if:

1. The homepage no longer reads like a resume with better styling
2. The homepage has one clear entry system instead of repeated entry points
3. The current first-fold taste level is preserved or improved
4. Motion feels controlled and tactile rather than decorative
5. Details are clearly pushed into second-layer pages
6. The site feels like a personal website first, proof-bearing second

## Supersession Notes

This spec narrows and partially supersedes parts of:

- `docs/superpowers/specs/2026-05-03-personal-index-direction-design.md`
- `docs/superpowers/specs/2026-05-03-homepage-bottom-half-restructure-design.md`

Specifically:

- the homepage should no longer be treated as a stacked `personal index + lower sections` page
- the lower-section restructuring direction is replaced by a unified single-surface homepage direction

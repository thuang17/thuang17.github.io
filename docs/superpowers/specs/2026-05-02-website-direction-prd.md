# Website Direction PRD - Trevor Huang Personal Website

Date: 2026-05-02
Status: Draft for design direction

## 1. Positioning

The site should present Trevor as an operator with strong judgment.

Primary impression:

- Clear business thinking
- Practical execution ability
- Evidence-based decision making
- Enough personal texture to be memorable

The site should not feel like a generic resume, a pure designer portfolio, or a creator playground. The correct balance is:

> Professional case-study site first, personal builder site second.

## 2. Target Audience

Primary audience:

- HR and hiring managers at Chinese domestic companies
- HR and hiring managers at foreign-invested companies in China
- Teams hiring for marketing, brand, e-commerce operations, business operations, product-adjacent, or project coordination roles

Their likely scanning behavior:

- First 10 seconds: Is this person credible?
- First 1 minute: What roles does he fit?
- First 3 minutes: Can I see how he thinks and works?
- Longer read: Is there a memorable personal edge?

## 3. Direction

Recommended direction:

### Operator With A Maker Edge

The main site experience should be structured, editorial, and easy to scan. The personality should appear through interaction details, page composition, specific writing, and selected immersive moments rather than through heavy illustration or decorative effects.

Reference interpretation:

- Rauno: use restraint, motion discipline, and a strong point of view; do not copy the abstract designer-portfolio feel.
- Tania Rascia: use clear information architecture, readable writing, and a digital-garden sense of organization.
- Sam Dickie: borrow warmth and personality, but reduce cartoon energy for a job-search context.
- Josh Comeau: borrow delight and depth, but avoid making the site feel like a productized creator platform.

## 4. Current Diagnosis

The current site is competent, but the pages do not yet share one clear visual thesis.

- Home page: professional and clean, but still close to a polished resume.
- Work case pages: clear and useful, but can feel document-like above the fold.
- Darts page: stronger editorial personality.
- AI page: strongest immersive direction and currently the clearest signal of "personal builder."

The next optimization should not be random polish. It should unify the site around one narrative:

> Trevor turns ambiguous business and product situations into structured action.

## 5. Page Roles

### Home Page

Role: fast credibility and navigation.

The home page should answer:

- Who is Trevor?
- What kind of work does he do?
- What proof should I inspect first?
- What personal edge makes him different?

Design implication:

- Keep it highly scannable.
- Make case studies feel like business artifacts, not just rows of text.
- Add stronger hierarchy around "selected proof."
- Use restrained interaction to make the site feel alive.

### Work Case Studies

Role: demonstrate judgment.

Each case should make the problem, decision logic, and outcome legible within the first fold.

Design implication:

- Add stronger "case brief" treatment near the top.
- Surface the key business question early.
- Use data cards and structured artifacts as visual anchors.
- Keep typography editorial and dense enough for serious reading.

### About Stories

Role: show memorable personal edge.

The Darts and AI pages can be more visually expressive than the work pages. They should still connect back to the main positioning: discipline, experimentation, self-directed learning, and systems thinking.

Design implication:

- Keep AI page immersive.
- Keep Darts page editorial.
- Make both feel like intentional side chapters, not unrelated microsites.

### Chinese Version

Role: make the site feel locally credible.

Chinese copy should not sound translated or AI-generated. It should be shorter, more direct, and closer to how a bilingual business candidate would actually write.

Design implication:

- Do not over-explain.
- Avoid stiff phrases and slogan-like wording.
- Prioritize natural rhythm over literal English parity.

## 6. Visual Principles

Use the existing design system. Do not change the foundation unless there is a clear reason.

Fixed foundation:

- Background: `#FAFAF8`
- Accent: `#7C3AED`
- Typography: Montserrat, Nunito Sans, JetBrains Mono
- Pure static HTML/CSS/JS
- No framework
- No build step

Design principles:

- Structure before decoration.
- One strong visual idea per page.
- Case-study pages should feel like decision documents, not blog posts.
- Personal pages can be more immersive, but must stay connected to the site identity.
- Animation should clarify attention, not become the main content.
- Avoid heavy gradients, generic glassmorphism, and one-note purple styling.

## 7. Near-Term Priorities

Priority 1: Home page narrative pass

- Reframe hero copy around operator judgment.
- Make "selected work" more visually deliberate.
- Add a stronger bridge from work proof to personal edge.

Priority 2: Work case study first-fold polish

- Improve the above-the-fold information hierarchy.
- Add concise case briefs and key-question framing.
- Make business outcomes easier to scan.

Priority 3: Chinese copy rewrite

- Rewrite Chinese pages for naturalness.
- Keep meaning aligned, but do not translate sentence-by-sentence.

Priority 4: Motion system cleanup

- Keep the existing letter animation and magnetic hover if they support the narrative.
- Add motion only where it helps scanning, page transition, or affordance.

## 8. Non-Goals

- Do not redesign the whole site into a playful creator platform.
- Do not introduce React, Next.js, Astro, or any build system.
- Do not add decorative illustrations just to make pages feel "designed."
- Do not change verified career data without checking source documents.
- Do not make the Chinese site a literal mirror of English wording.

## 9. Success Criteria

The redesign direction is successful if:

- A recruiter can understand Trevor's role fit within 10 seconds.
- A hiring manager can see decision quality within 1-3 minutes.
- The site feels more distinctive without becoming less professional.
- Work pages and personal pages feel like parts of the same person.
- The Chinese version feels written by a real bilingual candidate, not translated by a model.

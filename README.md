# Vektor10 — Site

Marketing site for **Vektor10, Inc.** — the first full-suite ChatGPT™ commerce agency. A VantaFive portfolio company. Public launch: June 15, 2026.

## Stack

- [Astro](https://astro.build) (MPA, content collections for the blog)
- Tailwind CSS v4 (design tokens in `src/styles/global.css` via `@theme`)
- Vercel (staging on `*.vercel.app`; production cutover to `vektor10.com` at launch)

## Source of truth

| File | What |
| --- | --- |
| `DESIGN.md` | Full visual system — tokens, type, components, rules. Mirrors the Paper.design canvas ("Vektor10 — Site"). |
| `PRODUCT.md` | Positioning, audience, voice, anti-references. |
| `ANIMATIONS.md` | Motion spec draft. **Canonical edited version lives in Notion ("Landing Page Animation Spec").** |
| `assets/` | Design-stage assets (hero render, marks, grain tile). |

Design changes happen in Paper first; code follows the canvas, not the other way around.

## Develop

```sh
npm install
npm run dev      # localhost:4321
npm run build    # production build to dist/
```

## Conventions

- Every color is a token — no stray hex values (see DESIGN.md "No-Stray-Values Rule").
- `10px` mono is functional-button text only; `18px` display is blockquotes only.
- Hard offset shadows + 2px ink strokes on raised surfaces; counter-light pairs on light grounds only.
- Motion: exponential ease-out only, 120–500ms, `prefers-reduced-motion` respected everywhere.

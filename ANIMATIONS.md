# Vektor10 — Animation Spec (RESOLVED 2026-06-10 — Trey's verdicts from Notion "Landing Page Animation Spec")

Each row: **what** moves · **when** (trigger) · **how** (motion) · **how fast**.
All rows below reflect Trey's verdicts. Changed rows:

- **#1 Cycling word → TYPEWRITER.** Word gets backspaced letter-by-letter, then the next word is typed in. The rectangle beside it is a blinking block caret (solid while typing). Chip width still fixed to the longest word.
- **#2 Button press → FULL COUNTERACT.** On click the button moves exactly the shadow vector (−2px x, +4px y) and the drop shadow is deleted — the 3D press. (Hover keeps the half-press.)
- **#3 Pillars → arrows ALWAYS BOB** up and down (gentle infinite loop) and fade out on scroll.
- **#4 Hero card → NOTHING on page load.** On scroll, the card holds its position on screen while the hero scrolls, then fades out before it reaches the section seam (never gets cropped).
- **NEW: Nav bar is STICKY** — locks to the top of the screen and follows the scroll.

Rows 5–12 kept as drafted.

## Motion principles (the register)

- **Instrument, not atmosphere.** Motion is quick, precise, mechanical — like the hard shadows. No floaty 1s fades, no parallax soup.
- **Two speeds only.** Interactions: 120–250ms. Section reveals: 400–500ms. Both ease-out.
- **Scroll reveals are subtle and run ONCE** (rise 12px + fade). Not every section earns one.
- **`prefers-reduced-motion` kills everything** except instant state changes. Non-negotiable.
- **No layout shift:** every media slot has a fixed aspect ratio before its asset loads (also a Core-Web-Vitals/AEO guard).

## The signature three (worth the most effort)

| # | What | When | How | Speed |
|---|------|------|-----|-------|
| 1 | **Cycling word** (hero chip) | Timer, every ~2.6s | Current word slides up+out, next slides up+in; caret blinks at 1s steps; chip width FIXED to longest word (no reflow) | 350ms ease-out |
| 2 | **Button press** (all shadow-box buttons) | Hover / click | Hover: button translates 1px toward its shadow, shadow shrinks to −1px 2px ("half-pressed"). Click: full press — translate −2px 4px, shadow 0, then release | 120ms |
| 3 | **Scroll-pinned pillars** (Plan-In-Action) | Scroll progress | Section pins; the 4 pillar boxes swap in sequence (out: fade+rise, in: fade+rise) as you scroll; arrows fade between states. Mobile: NO pin — plain stacked scroll | tied to scroll |

## Everything else

| # | What | When | How | Speed |
|---|------|------|-----|-------|
| 4 | Hero card | Page load | Card rises 16px + fades in; children stagger 80ms after | 500ms |
| 5 | Nav links / footer links | Hover | Underline appears (links already underlined in footer: offset nudges 1px) + color to teal on light surfaces | 150ms |
| 6 | Email input | Focus | 2px ink stroke → teal | 150ms |
| 7 | Section reveals (Stakes cards, bento cards, How-It-Works rows, blog grid) | First scroll into view | Rise 12px + fade, items stagger 90ms | 400ms |
| 8 | Offer-card document mock | First scroll into view | Tilts 0°→2° while impact bars grow from 0 to full width, staggered 120ms (needle-sweep feel) | 450ms |
| 9 | FAQ accordion | Click | Height expand/collapse; `+` ↔ `−` crossfade | 250ms |
| 10 | Tech-page media slots (Todd's micro-animations / Looms) | In viewport | Autoplay muted + loop; **pause when off-screen** (performance) | n/a |
| 11 | Price-gap panel ($54.99 → $28.23) | First scroll into view | Strikethrough draws across the wrong price; teal price ticks up from $0 | 300ms / 600ms |
| 12 | Page transitions | Navigation | Simple instant loads (Astro MPA). OPTIONAL: View Transitions fade, 150ms — try late, cut if flaky | 150ms |

## Deliberately static (decided, not forgotten)

- **Dither bands** — static. Animated dithering is a perf/battery trap; revisit post-launch as a WebGL experiment if craved.
- **Glass grain, tech grid, giant footer logo** — static. They're texture, not actors.
- **Blog post page** — no scroll reveals; reading pages shouldn't perform.

## Open slots for Trey's ideas
Anything you imagined that isn't above — add a row, same four columns.

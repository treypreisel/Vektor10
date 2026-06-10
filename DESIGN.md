---
name: Vektor10
description: "The first ChatGPT commerce agency: warm, instrument-grade, a little dreamlike."
colors:
  teal: "#2E926C"
  cta-green: "#237B57"
  cherry: "#E5294B"
  sky: "#6BB0D6"
  inky: "#141413"
  ink-muted: "#141413A6"
  ink-faint: "#9A968E"
  ink-panel: "#1E1E1E"
  dark-hairline: "#302F2C"
  dark-grid: "#403D38"
  bone: "#F0EEE5"
  bone-deep: "#E6DBCB"
  bone-muted: "#B5B2AB"
  white: "#FFFFFF"
typography:
  display:
    fontFamily: "Cal Sans, ui-rounded, system-ui, sans-serif"
    fontSize: "38px"
    fontWeight: 400
    lineHeight: "1.12"
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Cal Sans, system-ui, sans-serif"
    fontSize: "46px"
    fontWeight: 400
    lineHeight: "1.08"
    letterSpacing: "-0.02em"
  title:
    fontFamily: "Cal Sans, system-ui, sans-serif"
    fontSize: "30px"
    fontWeight: 400
    lineHeight: "1.1"
    letterSpacing: "-0.015em"
  body:
    fontFamily: "Geist Mono, ui-monospace, SFMono-Regular, monospace"
    fontSize: "15px"
    fontWeight: 500
    lineHeight: "1.6"
    letterSpacing: "normal"
  label:
    fontFamily: "Geist Mono, ui-monospace, monospace"
    fontSize: "15px"
    fontWeight: 500
    lineHeight: "1.2"
    letterSpacing: "normal"
rounded:
  sm: "8px"
  md: "14px"
  lg: "16px"
  glass: "15px"
  pill: "999px"
spacing:
  xs: "8px"
  sm: "12px"
  md: "20px"
  lg: "32px"
  xl: "56px"
  xxl: "96px"
components:
  button-primary:
    backgroundColor: "{colors.teal}"
    textColor: "{colors.white}"
    rounded: "{rounded.sm}"
    padding: "14px 22px"
    typography: "{typography.label}"
  button-secondary:
    backgroundColor: "{colors.white}"
    textColor: "{colors.inky}"
    rounded: "{rounded.sm}"
    padding: "11px 18px"
    typography: "{typography.label}"
  callout:
    backgroundColor: "{colors.bone-deep}"
    textColor: "{colors.inky}"
    rounded: "{rounded.lg}"
    padding: "34px 44px"
  ink-header-bar:
    backgroundColor: "{colors.ink-panel}"
    textColor: "{colors.white}"
    rounded: "{rounded.md}"
    padding: "30px 50px"
---

# Design System: Vektor10

> **Canvas is canon.** This file was reconciled against the live Paper file ("Vektor10 — Site") on 2026-06-09. Before designing or building any new section, sample computed styles from an adjacent existing section; do not work from memory.

## 1. Overview

**Creative North Star: "Warm Instrumentation"**

Artisan × technical × approachable, with a required dreamlike charge carried by imagery. The page is a color journey, not one ground: photo-led light hero → warm bone-deep → dark instrument panel → drenched brand green → bone — with **organic dither-shader bands** dissolving one ground into the next (the signature nostalgic-digital move). Decoration is the instrument (grids, hairlines, mono labels); subject matter is retro-analog consumer products rendered dreamily. Copy is direct, commerce-native; ChatGPT is always written **ChatGPT™**.

**Key Characteristics:**
- Vintage hard-offset shadows + 2px ink strokes on nearly every raised surface, including glass.
- Frosted glass with film grain in the hero; flat border-only cards in dark sections.
- Cal Sans (single weight) display against earned 15px Geist Mono body.
- Eyebrows in angle brackets: `< WHAT'S AT STAKE >` — mono, 15px, untracked.
- One playful register: emoji icons in stamped (inset-shadow) circles.

## 2. Colors

Teal anchor on warm grounds, ink everywhere as stroke-and-text, with grounds doing the section-level storytelling.

### Primary
- **Patina Teal** (`#2E926C`): brand anchor — accents, eyebrows, the cycling word, primary button fill, and the drenched Plan-section ground.
- **CTA Green** (`#237B57`): reserve AA-safe button shade (current canvas buttons use raw teal + white at 3.8:1 — open decision).

### Secondary (reserved)
- **Cherry** (`#E5294B`) and **Sky** (`#6BB0D6`): in the palette, **not yet deployed on canvas**. Cherry stays off bone and is never the CTA.

### Neutral
- **Inky** (`#141413`): text on light, ALL 2px strokes, hard shadows, the dark section ground.
- **Ink-muted** (`#141413` @ 65%): secondary text, step numbers, muted eyebrows. Alpha form is canon; legacy `#57544E` is its fixed-hex equivalent.
- **Ink-faint** (`#9A968E`): placeholders only.
- **Ink-panel** (`#1E1E1E`): dark callout bars; matches the icon-set fill.
- **Dark hairline** (`#302F2C`) / **Dark grid** (`#403D38`): borders and grid lines on dark.
- **Green hairline** (`#141413` @ 25%, i.e. `#14141340`): hairlines on the green ground (footer legal bar); kin of the green tech grid's ink @ 15%.
- **Light hairline** (`#B5B2AB` at 1px): dividers on bone (FAQ rows, plan-document internals) — bone-muted doing double duty.
- **Bone** (`#F0EEE5`): light ground, icon circles, cards on bone-deep.
- **Bone-deep** (`#E6DBCB`): Stakes ground, feature boxes on bone.
- **Bone-muted** (`#B5B2AB`): body + eyebrows on dark/green.
- **White**: glass fills (60–65%), cycling-word chip, headings on green.

### Named Rules
**The No-Stray-Values Rule.** Every color is a token — and strays must be KILLED ON SIGHT, not just noted. Why (Trey, 2026-06-10): he designs with the Paper eyedropper, so any stray that exists anywhere on canvas gets resampled and spreads. `#2E926C` is confirmed the one true teal. Full sweep folded 2026-06-10: `#2F926C` (offer eyebrow, blockquote), `#F0EDE4` (offer ground, footer column headers ×6 footers), `#E5DBCB` (footer links ×6 footers). ⚠️ One stray remains out of MCP reach: the dither shaders' bone endpoint is `#F0EDE4` — Trey must retune in-app or the eyedropper will catch it again. (The 10px email text is NOT drift; it's the functional-button size.)

**The Ground-Journey Rule.** Sections change ground color (light → warm → dark → green → bone); adjacent grounds either hue-match seamlessly (hero floor → bone-deep) or transition through a dither band. Text recolors per ground: ink on light, bone/bone-muted on dark, ink on green (headings may go white in ink panels).

## 3. Typography

**Display Font:** Cal Sans (single weight 400; fallback `ui-rounded, system-ui`)
**Body / Label Font:** Geist Mono (500; 600 only on small button labels). Geist (sans) reserved for long-form prose pages.

### Hierarchy (canvas-true)
- **Hero headline** (38px, lh 112%, ls −0.02em): hero only; cycling word matches at 38px teal.
- **Section heading** (46px, lh 105–112%, ls −0.02em): every section, light or dark.
- **Feature-box title** (30px) · **Bento title** (22px) · **Content-card title** (19px).
- **Tagline** (Cal Sans 15px, +0.02em): the small Cal Sans line under the hero form.
- **Eyebrow / label** (Geist Mono 500, 15px, **no tracking**): format `< LABEL >`.
- **Body** (Geist Mono 500, **15px**, lh 155–165%): ink on light, bone-muted on dark. 13px body is dead. Long-form (articles, legal, bios) runs lh 26px.
- **Blockquote** (Cal Sans 400, **18px**, +0.04em, lh 26px, teal): article pull quotes only, paired with a 3px ink-panel left rule. 18px exists for no other role.
- **Figure caption** (Geist Mono 500, 15px, ink-muted, **center-aligned** under the image): credit/caption slot on every article image.
- **Nav links** 14px mono · **button labels** 13–14px mono 600.
- **Functional-button text** (Geist Mono 500, **10px**): the size for in-page functional controls (currently only the hero email form). Intentional — do not "fix" to body size.

### Named Rules
**The Bracket-Label Rule.** Section eyebrows are literal `< NAME >` strings — mono, 15px, untracked. Color by ground: teal on bone/dark, ink-muted on bone-deep, bone-muted on green.

**The Earned Mono Rule.** Mono carries meaning (labels, body-as-readout); never costume.

## 4. Elevation

Flat at rest; lift is graphic, not atmospheric.

### Shadow Vocabulary
- **Hard Offset** (`box-shadow: -2px 4px 0 0 #141413` + 2px ink stroke): the vintage signature — callout boxes, buttons, glass surfaces, ink panels.
- **Counter-Light** (same `-2px 4px` vector, **3px blur**, light color): the 3D embossing pass, paired against the dark offset on light/green grounds — NOT on true dark sections. Light color = bone `#F0EEE5` on light grounds; `#FFFFFF` @ 20% (`#FFFFFF33`) on ink panels.
  - **Raised surface** = light inset + dark outset: `box-shadow: inset -2px 4px 3px #F0EEE5, -2px 4px 0 #141413` (feature boxes; ink header bar uses the `#FFFFFF33` variant).
  - **Punched hole** = dark inset + light outset: `box-shadow: inset -2px 4px 0 #141413, -2px 4px 3px #F0EEE5` (emoji icon circles — reads as a hole punched through the 3D card).
- **Glass** (white @ 60–65%, blur 8px + saturate 120%, 15px radius, hard offset, grain overlay at soft-light ~50%): hero card + nav only.

### Named Rules
**The Hard-Offset Rule.** All raised surfaces use the blur-0 offset. Never `overflow: clip` on a hard-shadow rounded box (1px corner sliver); clip inner layers (grain) via their own radius.

**The Reserve-the-Shadow's-Box Rule.** Small shadowed buttons sit absolutely at `left:2; top:-4` inside a wrapper sized to button+shadow, so the visual mass aligns with neighbors.

## 5. Components

### Buttons
- **Primary:** teal fill, white mono label (600), 8px radius, 2px stroke + hard offset, in a shadow-box wrapper.
- **Secondary ("Current Clients"):** white fill, ink 13px 600 label, same chrome.

### Glass surfaces (hero card, nav)
White 60–65% fill, 2px ink stroke, 15px radius, hard offset, backdrop blur 8 / saturate 120, noise-grain overlay (200px tile, soft-light, ~50%, self-clipped). Paper-native Glass effect for refraction.

### Feature box (light grounds)
Bone-deep fill, 2px stroke, 16px radius, **raised counter-light shadow pair**, 34/44 padding, 32px gap. Left: **108px emoji icon circle** (bone fill, 2px stroke, **punched-hole shadow pair**, 50px emoji). Right: eyebrow (teal) + 30px title + 15px body.

### Ink header bar
`#1E1E1E` fill, 2px stroke, 14px radius, **raised pair with `#FFFFFF33` counter-light**, 30/50 padding — holds a section eyebrow + white 46px heading on the green ground.

### Content cards (light)
Bone on bone-deep, 14px radius, **no stroke or shadow**, 30/40 padding, equal-width (`flexGrow:1 + flexBasis:0 + minWidth:0`).

### Bento cards (dark)
320×320 (header 660×320), section-color fill + 1px `#302F2C` stroke, 14px radius, flat. 50px padding, 20px gaps, over the dark tech grid.

### The Cycling Word (signature)
White chip, 8px inline padding, Cal Sans 38px teal word + 2px ink caret, always **line-final**. Rotation (sofa → shoe → luggage → …) is code-stage; give the chip a fixed width sized to the longest word at build.

### Dither bands (signature)
Paper ShaderDithering nodes (1440×392) dissolving one section ground into the next — always white↔green (that's the pair, both directions). **THE FOOTER RULE (Trey, 2026-06-09): every page ends with a dither band directly above the green footer**, blending the last section's ground into the footer green. Clone the About page's tuned band; Trey adjusts shader colors in-app if the preceding ground differs.

### Tech grid
20px cells, crisp 1px (`M0.5 0 V20 M0 0.5 H20`, `crispEdges`): `#403D38` on dark, ink @ 15% on green.

### Plan rows
50px block padding, no hairlines. Left: `01` mono ink-muted + 46px Cal Sans title; right: 480px mono body.

### Scroll-pinned pillar sequence
Bone ground, stacked centered states (200px gaps) with 96px down-arrows; pins and swaps on scroll at code stage.

### Offer card (lead gen — pricing merged in, no dollar figures)
One oversized ink card on a light bone ground (the section IS the card — no heading on the ground). `#1E1E1E` fill, 2px stroke, 16px radius, **raised pair with `#FFFFFF33` counter-light**, 56px padding, 1080px wide. Inside (canvas-true after Trey's 2026-06-09 tightening pass): teal eyebrow `< SAY NO MORE >` + 46px bone heading ("Your free AI commerce plan shows you…") + teal-`+` checklist (15px mono bone) + **cloned hero email form** ("Get Your Free Audit!"). Trey cut the footer expectation strip and the friction-killer microcopy — fewer elements, the card is leaner than first built.

### FAQ accordion (AEO asset)
Light bone ground, 1000px column, left-aligned: teal eyebrow `< FAIR QUESTIONS >` + 46px "Straight answers." **Seven** rows divided by 1px `#B5B2AB` hairlines, 32px block padding: question in **30px Cal Sans ink** + teal mono `−`/`+` affordance right (`flexShrink:0`). Answers at 15px mono ink-muted, 760px max-width. **All rows sit OPEN on canvas** — the copy is recorded for code stage; expand/collapse behavior (and which rows default open) is a code-stage decision. Questions are the literal queries buyers ask ChatGPT — that's the AEO play. Q1–Q5 from brief §8; Q6 "What does it cost?" (engagement shape, no dollar figures — carries old Section 7's job) and Q7 "What do we have to do on our side?" (lift objection, done-for-you reinforcement) added 2026-06-09.

### Plan document mock (signature artifact)
The free plan rendered as a physical object inside the offer card: bone fill, 2px stroke, **8px radius** (paper, not UI), plain hard offset (no counter-light — light surface), 30/28 padding, ~350px wide, **`rotate(2deg)`** — the page's only tilted element. Contents: Cal Sans 24px doc title, `PREPARED FOR:` + redaction pill, `#B5B2AB` 1px dividers, ranked `FIX 01–04` rows (10px mono labels; only FIX 01 readable, rest redacted with `#B5B2AB` pills) over **descending teal impact bars** (10px tall pills — the curiosity gap), footer `DELIVERED IN WRITING` + teal `48 HRS` stamp chip. Redacted text = solid `#B5B2AB` pills; impact bars = solid teal pills.

### Footer (green ground — shared across pages via clone)
Section ground `#2E926C` (matches the logo's teal so the "10" can blend when Trey recolors). After Trey's canvas pass the footer is **footer-only — he CUT the final-CTA block** (no closing headline/email form):
1. **Footer body** (1320px, space-between): **oversized V10 shorthand logo** left (inline SVG, 363×174 after Trey's resize; he recolors the "10" in-app) · three link columns right, order **NETWORK · PAGES · CONNECT** (VantaFive/Influent/Sohva/Recho · Technology/About/Cases/Blog · Todd@Vektor10.com/LinkedIn). Column headers: **30px Cal Sans bone `#F0EEE5`** (not bracketed mono); links **15px mono bone-deep `#E6DBCB`, underlined** (1px, 3px offset).
2. **Legal bar** (1320px): 1px `#14141340` hairline top, 28px padding — "© 2026 Vektor10, Inc. · A VantaFive Agency" (`#B5B2AB`) left; Privacy · Terms (bone, placeholder links) right.

### About page (artboard "V10 About — Desktop")
Cloned nav + footer bookend it — **edit those once on Home, re-clone everywhere**. Body after Trey's breathing pass: **manifesto column** (760px, centered, on bone, 150/100 padding): eyebrow+heading in a tight **5px lockup** (matches Plan Header) + body grafs 15px mono ink-muted 26px lh + 30px Cal Sans pull line. Then the **Leadership panel — Trey upgraded it to an inset INK PANEL**: full-width wrapper, `#1E1E1E` rounded-14 card (2px stroke + raised `#FFFFFF33` counter-light pair) floated inside the bone ground; inside it the section label is a full **46px Cal Sans bone heading** (not a mono eyebrow), founder rows 35px gaps — 380×380 headshot slots + name 30px bone / role teal mono caps / **bio 15px mono `#E6DBCBA6`** (bone-deep @ 65% = the muted-body role on ink panels). Then dither → footer.

### Inset ink panel (Trey's pattern)
A full-width content band rendered as a floating dark card: `#1E1E1E`, 14px radius, 2px stroke, raised counter-light pair, inset ~70px from artboard edges with the section ground showing around it. Text inside: 46px Cal Sans bone headings, teal accents, body `#E6DBCBA6`. Used for Leadership (About) and the featured blog post card (smaller, 1180px). This is the de-facto "emphasis band" — prefer it over inventing new dark sections on subpages.

### Eyebrow judgment (Trey, 2026-06-10 — case-by-case, NOT a hard rule)
Eyebrows are a taste call per placement: they belong on home sections, the About manifesto, and the featured blog card — but read as noise on legal pages, blog post headers, blog grid cards, and as a blog index page label. When in doubt, try the heading without one first; add the eyebrow only if the block loses its anchor.

### Blog index (artboard "V10 Blog — Desktop")
Bone ground, 1180px lane, **NO page heading** — nav drops straight into content (110px spacer): **featured post** as an ink panel card (image slot 520×300 `#141413` radius 8, teal `< FEATURED >` eyebrow, 30px bone title, excerpt `#E6DBCBA6`, **teal byline** `TODD PIECHOWSKI · JUN 09, 2026 · 9 MIN READ`, underlined bone "Read the post") → 3×2 **post-card grid** (20px gaps): flat bone-deep cards (radius 14, 24px padding) with `#1E1E1E` image slots (170px, radius 8), 30px title, mono meta ink-muted — image/title/meta only, no tags. Dither → footer.

### Blog post (artboard "V10 Blog Post — Desktop")
Bone ground: article header 760px (underlined "← All posts" ink-muted, **46px title**, **byline in TEAL** — author · date · read length) → **hero figure**: 1180×480 image slot (ink panel chrome) + **center-aligned caption/credit** below (15px mono ink-muted, 14px gap) — main image intentionally WIDER than the text column → article body 760px, 28px graf gaps: grafs 15px mono ink-muted 26px lh, **H2s = 30px Cal Sans ink**, closing CTA graf → author row (hairline top, 64px circular ink headshot slot + mono name + teal role) → dither → footer. Inline links (teal underlined) are CODE-STAGE — Paper can't color spans mid-paragraph.

### Article figure components
- **Hero figure** (top of post): image WIDER than text column (1180×480, ink-panel chrome: 2px stroke, radius 14, hard offset) + center-aligned caption/credit beneath (15px mono ink-muted, 14px gap).
- **In-body figure**: image exactly the TEXT-COLUMN width (760, height ~420, same ink-panel chrome) + center-aligned caption/credit beneath. Sits in the graf flow.
- **Blockquote (Trey's restyle)**: flex row — 3px `#1E1E1E` vertical rule (full height) + quote text in **18px Cal Sans, teal, +0.04em tracking, 26px line-height**. 18px exists ONLY for blockquotes (new type role).

### Contact page (artboard "V10 Contact — Desktop") + THE CTA MODEL
**The site's conversion flow (Trey, 2026-06-10):** every email-capture form on the site (hero, offer card) submits to **/contact with the email passed through as a query param and PREFILLED** — breaking the form into two small steps instead of one chore. The contact page: bone ground, single 546px column (hero-form width), "Let's talk." 46px, then a bare stacked form — Name / Email (canvas shows the prefilled state: value in ink, not placeholder gray) / Company / Optional Message (150px textarea) — all in hero-input chrome (white, 2px stroke, radius 8, 10px mono placeholders `#9A968E`), full-width shadow-box teal submit ("Get Your Free Audit!"), centered one-line microcopy ("Goes straight to Todd. Audit in writing within 48 hours."). Almost no decoration — deliberately. Submissions write to the **"Web Inquiries" Notion database** in the Vektor10 workspace (ID TBD — needs sharing with the connector) at code stage.

### Tech page (artboard "V10 Tech — Desktop") — the Trace showcase
Todd's copy ~verbatim; structure/styling re-mapped to system conventions (his "Heading" markers ≠ our 46px — feature rows get 30px titles; 46px reserved for hero, Lost Shelf band, How-You-Use-It, closing). **Largely visual: every [SCREENSHOT] marker became a labeled MEDIA SLOT** (ink panel chrome w/ raised pair) sized for Trey's dashboard micro-animations / Looms. Arc: hero (eyebrow `< POWERED BY TRACE >` + 46px + sub + email form + 1180×620 hero media) → 3 alternating split rows (620×400 media ↔ 30px-title copy, 1180 lane) → **price-gap inset ink panel** (the $54.99-struck vs teal $28.23 pair at 46px Cal Sans — the page's emphasis moment, line-through works in Paper) → Competitive split row → **Lost Shelf conversion band** (bone-deep, centered 46px + 980×460 calculator media + email form — Todd's mid-page CTA) → Alerts split row → How-You-Use-It (46px + 3 flat bone-deep cadence cards: Weekly/Monthly/Real-time) → closing 46px + email form → dither → footer. All CTAs = the cloned email form (→ /contact prefill model).

### Nav (launch state)
Links: Home · Tech · About · Blog. **"Cases" is HIDDEN for launch** (removed from all navs + footer PAGES columns 2026-06-10; restore when case studies exist).

### Legal pages (artboards "V10 Terms / V10 Privacy — Desktop")
Bone ground, 760px column: header (46px title + mono `EFFECTIVE — FEB 01, 2026` meta, no eyebrow) → intro graf → **ALL 13 numbered sections VERBATIM** from vektor10.com/terms & /privacy (30px Cal Sans headings, 15/26 mono ink-muted bodies, 36px section gaps; bullet lists as `•`-prefixed rows, 8px indent; contact blocks with ink company line) → dither → footer. **Entity corrected on canvas to "Vektor10, Inc."** everywhere (incl. the all-caps liability section). ⚠️ The LIVE site still says "Vektor10 Corp" — the deployed legal text needs the same fix at code stage.

## 6. Do's and Don'ts

### Do:
- **Do** sample computed styles from the canvas before building anything new — canvas is canon.
- **Do** use 15px mono body, 46px section headings, `< BRACKET >` eyebrows, and the hard-offset chrome on raised surfaces.
- **Do** write ChatGPT™ with the ™ in site copy.
- **Do** keep grounds flowing: hue-match adjacent sections or dissolve through a dither band.
- **Do** use emoji icons in stamped circles for the playful register (this overrides the generic no-emoji-icon default — Trey's call).

### Don't:
- **Don't** ship the drift values (`#2F926C`, `#F0EDE4/#F0ECE3`, `#000000`, 10px placeholders) — fold them to tokens.
- **Don't** put cherry on bone, use it as the CTA, or deploy it/sky without a deliberate decision.
- **Don't** use soft/blurred drop shadows, gradient text, side-stripe borders, or `overflow:clip` on hard-shadow boxes.
- **Don't** sound like the GEO pack, AI-futurist consultancies, or dashboards (Profound/Peec); never "score" or "GEO" in copy — commerce language, ChatGPT-only. **"Audit" UNLOCKED 2026-06-09** (Todd meeting): OK to lead with audit terminology; the old never-audit rule is dead.
- **Don't** recreate Trey's reference imagery — references inform layout and proportion only.

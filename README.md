# Vektor10 — Site

Marketing site for **Vektor10, Inc.** — the 1st full-suite ChatGPT commerce agency. A VantaFive portfolio company.

- **Staging:** https://vektor10-site.vercel.app (noindex until launch)
- **Production (after cutover):** https://vektor10.com — launch June 15, 2026
- **Status:** all pages live on staging (Tech page scaffolded but unlinked, awaiting Trace assets)

## Stack

- [Astro 5](https://astro.build) — static pages + one on-demand endpoint (`/api/inquiry`) via `@astrojs/vercel@9`
- Tailwind CSS v4 — design tokens in `src/styles/global.css` (`@theme`); **every color is a token, no stray hex values**
- Vercel — pushes to `main` auto-deploy (webhook occasionally skips; `npx vercel deploy --prod --yes` forces it)

## Source of truth

| File | What |
| --- | --- |
| `DESIGN.md` | Full visual system — tokens, type roles, components, rules. Mirrors the Paper.design canvas. |
| `PRODUCT.md` | Positioning, audience, voice, anti-references. |
| `ANIMATIONS.md` | Motion spec (resolved with Trey's verdicts). |
| `src/content/blog/*.md` | **Blog posts are markdown files.** Add a post = add a file (frontmatter: title, description, date, readTime, heroImage). The index and post pages render automatically. |

## Develop

```sh
npm install
npm run dev        # localhost:4321 (endpoint works in dev; needs .env)
npm run build      # production build
npx astro preview  # serve the build locally
```

`.env` (gitignored, never commit): `NOTION_TOKEN`, `NOTION_DATABASE_ID` — same values live in Vercel env.

## Contact form

`/contact` → POST `/api/inquiry` → row in the Notion **Web Inquiries** database (Slack notification fires via a Notion-side automation). Honeypot field `website` silently drops bots. Astro's CSRF origin check is off (misfires behind Vercel's proxy; the form is public and sessionless).

## Conventions

- 10px mono = functional-button text only; 18px = blockquotes only. Don't "fix" either.
- Hard offset shadows (`-2px 4px 0 #141413`) + 2px ink strokes on raised surfaces; counter-light pairs are the only blurred shadows.
- Motion: exponential ease-out, 120–500ms, `prefers-reduced-motion` respected; scroll reveals have a 3s failsafe so crawlers never see hidden content.
- Copy: commerce language (never "GEO" or "score"), ChatGPT™ with ™, FAQ answers are Todd's words verbatim.

## Launch-day runbook (June 15)

1. Add `PUBLIC_GA4_ID` to Vercel env (GA4 Measurement ID) and redeploy — analytics activates.
2. In `src/layouts/Base.astro`: **remove the `noindex` meta line.**
3. Replace `public/robots.txt` with allow-all (keep the Sitemap line).
4. Vercel dashboard → vektor10-site → Domains → add `vektor10.com` (+ `www`), update DNS at the registrar as instructed.
5. Deploy, then verify: `curl https://vektor10.com` serves the new site; legal pages say "Vektor10, Inc."; submit a test inquiry end to end.
6. Post-launch: watch GA4's traffic acquisition for `chatgpt.com` referrals (knowing they undercount).

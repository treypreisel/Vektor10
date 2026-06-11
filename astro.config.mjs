// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import vercel from '@astrojs/vercel';

export default defineConfig({
  site: 'https://vektor10.com',
  devToolbar: { enabled: false },
  // Pages stay prerendered; the adapter exists for the on-demand form
  // endpoint (/api/inquiry) only.
  adapter: vercel(),
  // Astro's CSRF origin check misreads the origin behind Vercel's proxy and
  // 403s every real form post. The form is public + sessionless (no CSRF
  // surface); bots are handled by the honeypot.
  security: { checkOrigin: false },
  vite: {
    plugins: [tailwindcss()],
  },
});

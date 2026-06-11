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
  vite: {
    plugins: [tailwindcss()],
  },
});

// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  site: 'https://vektor10.com',
  devToolbar: { enabled: false },
  vite: {
    plugins: [tailwindcss()],
  },
});

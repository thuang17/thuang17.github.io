import { defineConfig } from 'astro/config';

export default defineConfig({
  output: 'static',
  site: 'https://thuang17.github.io',
  devToolbar: { enabled: false },
  build: { assets: 'assets' },
});

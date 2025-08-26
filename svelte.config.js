import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
  preprocess: vitePreprocess(),
  kit: {
    adapter: adapter({
      pages: 'build',
      assets: 'build',
      fallback: '200.html' // good for SPA-style routing
    }),
      paths: {
	  relative: true,   // ensure SvelteKit outputs relative paths
	  base: ''
    }
  }
};

export default config;

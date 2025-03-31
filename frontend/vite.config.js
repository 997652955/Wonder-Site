import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  root: './',
  publicDir: 'public',
  build: {
    outDir: 'dist'
  }
}) 
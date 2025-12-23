import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    host: '0.0.0.0', // Necessário para o Docker mapear a porta corretamente
    port: 5173,
    watch: {
      usePolling: true // Melhora o Hot Reload dentro de volumes Docker no Windows/Mac
    }
  }
})
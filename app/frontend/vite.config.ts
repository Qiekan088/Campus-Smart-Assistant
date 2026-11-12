import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
export default defineConfig({plugins:[vue()],server:{watch:{usePolling:true},proxy:{'/api':{target:process.env.API_PROXY_TARGET || 'http://backend:8000',changeOrigin:true,timeout:15000,proxyTimeout:15000}}}})

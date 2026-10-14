import { readFileSync } from 'node:fs'
import { createRequire } from 'node:module'
import { dirname, join } from 'node:path'
import react from '@vitejs/plugin-react'
import { defineConfig, type Plugin } from 'vite'

const require = createRequire(import.meta.url)
const onnxRuntimeDist = dirname(require.resolve('onnxruntime-web/ort-wasm-simd-threaded.mjs'))
const onnxRuntimeFiles = ['ort-wasm-simd-threaded.mjs', 'ort-wasm-simd-threaded.wasm']

function onnxRuntimeAssets(): Plugin {
  return {
    name: 'onnx-runtime-assets',
    configureServer(server) {
      server.middlewares.use((request, response, next) => {
        const path = request.url?.split('?')[0]
        const file = path?.replace(/^\/onnx-runtime\//, '')
        if (!path?.startsWith('/onnx-runtime/') || !file || !onnxRuntimeFiles.includes(file)) return next()
        response.setHeader('Content-Type', file.endsWith('.mjs') ? 'text/javascript' : 'application/wasm')
        response.end(readFileSync(join(onnxRuntimeDist, file)))
      })
    },
    generateBundle() {
      for (const file of onnxRuntimeFiles) {
        this.emitFile({ type: 'asset', fileName: `onnx-runtime/${file}`, source: readFileSync(join(onnxRuntimeDist, file)) })
      }
    },
  }
}

export default defineConfig({
  plugins: [react(), onnxRuntimeAssets()],
  publicDir: 'images',
})

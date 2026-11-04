import { deflateSync } from 'node:zlib'
import { mkdirSync, writeFileSync } from 'node:fs'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'

const androidResDir = join(dirname(fileURLToPath(import.meta.url)), '..', 'android', 'app', 'src', 'main', 'res')
const densities = {
  'mipmap-mdpi': 1,
  'mipmap-hdpi': 1.5,
  'mipmap-xhdpi': 2,
  'mipmap-xxhdpi': 3,
  'mipmap-xxxhdpi': 4,
}
const legacyBase = 48
const foregroundBase = 108

function crc32(buffer) {
  let crc = 0xffffffff
  for (const byte of buffer) {
    crc ^= byte
    for (let bit = 0; bit < 8; bit += 1) {
      crc = (crc >>> 1) ^ (crc & 1 ? 0xedb88320 : 0)
    }
  }
  return (crc ^ 0xffffffff) >>> 0
}

function chunk(type, data) {
  const length = Buffer.alloc(4)
  length.writeUInt32BE(data.length)
  const typeBuffer = Buffer.from(type, 'ascii')
  const crcBuffer = Buffer.alloc(4)
  crcBuffer.writeUInt32BE(crc32(Buffer.concat([typeBuffer, data])))
  return Buffer.concat([length, typeBuffer, data, crcBuffer])
}

function encodePng(size, pixels) {
  const signature = Buffer.from([137, 80, 78, 71, 13, 10, 26, 10])
  const ihdr = Buffer.alloc(13)
  ihdr.writeUInt32BE(size, 0)
  ihdr.writeUInt32BE(size, 4)
  ihdr[8] = 8
  ihdr[9] = 6
  const raw = Buffer.alloc(size * (size * 4 + 1))
  for (let y = 0; y < size; y += 1) {
    raw[y * (size * 4 + 1)] = 0
    pixels[y].copy(raw, y * (size * 4 + 1) + 1)
  }
  return Buffer.concat([signature, chunk('IHDR', ihdr), chunk('IDAT', deflateSync(raw)), chunk('IEND', Buffer.alloc(0))])
}

function pointInStar(x, y, size) {
  const cx = size / 2
  const cy = size / 2
  const outer = size * 0.32
  const inner = size * 0.135
  const points = []
  for (let i = 0; i < 10; i += 1) {
    const radius = i % 2 === 0 ? outer : inner
    const angle = -Math.PI / 2 + (i * Math.PI) / 5
    points.push([cx + Math.cos(angle) * radius, cy + Math.sin(angle) * radius])
  }
  let inside = false
  for (let i = 0, j = points.length - 1; i < points.length; j = i, i += 1) {
    const [xi, yi] = points[i]
    const [xj, yj] = points[j]
    if (yi > y !== yj > y && x < ((xj - xi) * (y - yi)) / (yj - yi) + xi) inside = !inside
  }
  return inside
}

function pointInRoundedRect(x, y, size) {
  const margin = size * 0.12
  const radius = size * 0.2
  if (x < margin || x > size - margin || y < margin || y > size - margin) return false
  const minX = margin + radius
  const maxX = size - margin - radius
  const minY = margin + radius
  const maxY = size - margin - radius
  if (x < minX && y < minY) return (x - minX) ** 2 + (y - minY) ** 2 <= radius ** 2
  if (x > maxX && y < minY) return (x - maxX) ** 2 + (y - minY) ** 2 <= radius ** 2
  if (x < minX && y > maxY) return (x - minX) ** 2 + (y - maxY) ** 2 <= radius ** 2
  if (x > maxX && y > maxY) return (x - maxX) ** 2 + (y - maxY) ** 2 <= radius ** 2
  return true
}

function inSparkleDot(x, y, size, dx, dy) {
  const cx = size * dx
  const cy = size * dy
  return (x - cx) ** 2 + (y - cy) ** 2 <= (size * 0.07) ** 2
}

function lerp(a, b, t) {
  return a + (b - a) * t
}

function designColor(size, x, y) {
  if (!pointInRoundedRect(x, y, size)) return null
  const inStar = pointInStar(x, y, size)
  const inDot1 = inSparkleDot(x, y, size, 0.72, 0.26)
  const inDot2 = inSparkleDot(x, y, size, 0.26, 0.74)
  if (inStar) return [255, 214, 107]
  if (inDot1 || inDot2) return [255, 107, 157]
  const t = y / size
  return [lerp(45, 107, t), lerp(27, 63, t), lerp(105, 160, t)]
}

function renderPng(size, variant) {
  const pixels = []
  const samples = 4
  const circleRadius = size / 2
  const stickerScale = 0.62
  const stickerSize = size * stickerScale
  const stickerOffset = (size - stickerSize) / 2
  for (let y = 0; y < size; y += 1) {
    const row = Buffer.alloc(size * 4)
    for (let x = 0; x < size; x += 1) {
      let r = 0
      let g = 0
      let b = 0
      let a = 0
      let covered = 0
      for (let sy = 0; sy < samples; sy += 1) {
        for (let sx = 0; sx < samples; sx += 1) {
          const px = x + (sx + 0.5) / samples
          const py = y + (sy + 0.5) / samples
          let color = null
          if (variant === 'round') {
            const dx = px - size / 2
            const dy = py - size / 2
            if (dx * dx + dy * dy <= circleRadius * circleRadius) {
              color = designColor(size, px, py)
            }
          } else if (variant === 'foreground') {
            if (px >= stickerOffset && px < stickerOffset + stickerSize && py >= stickerOffset && py < stickerOffset + stickerSize) {
              const designX = (px - stickerOffset) / stickerScale
              const designY = (py - stickerOffset) / stickerScale
              color = designColor(stickerSize, designX, designY)
            }
          } else {
            color = designColor(size, px, py)
          }
          if (color) {
            r += color[0]
            g += color[1]
            b += color[2]
            a += 255
            covered += 1
          }
        }
      }
      const count = samples * samples
      const offset = x * 4
      row[offset] = covered > 0 ? Math.round(r / covered) : 0
      row[offset + 1] = covered > 0 ? Math.round(g / covered) : 0
      row[offset + 2] = covered > 0 ? Math.round(b / covered) : 0
      row[offset + 3] = Math.round((a / count) * 255) / 255
    }
    pixels.push(row)
  }
  return encodePng(size, pixels)
}

for (const [folder, scale] of Object.entries(densities)) {
  const dir = join(androidResDir, folder)
  mkdirSync(dir, { recursive: true })
  const legacySize = Math.round(legacyBase * scale)
  const foregroundSize = Math.round(foregroundBase * scale)
  writeFileSync(join(dir, 'ic_launcher.png'), renderPng(legacySize, 'legacy'))
  writeFileSync(join(dir, 'ic_launcher_round.png'), renderPng(legacySize, 'round'))
  writeFileSync(join(dir, 'ic_launcher_foreground.png'), renderPng(foregroundSize, 'foreground'))
  console.log('Wrote icons to', dir)
}
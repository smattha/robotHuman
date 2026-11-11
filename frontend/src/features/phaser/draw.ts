import Phaser from 'phaser'
import { palette } from './palette'

function lerpColor(a: number, b: number, t: number): number {
  const ar = (a >> 16) & 0xff
  const ag = (a >> 8) & 0xff
  const ab = a & 0xff
  const br = (b >> 16) & 0xff
  const bg = (b >> 8) & 0xff
  const bb = b & 0xff
  const r = Math.round(ar + (br - ar) * t)
  const g = Math.round(ag + (bg - ag) * t)
  const bl = Math.round(ab + (bb - ab) * t)
  return (r << 16) | (g << 8) | bl
}

function verticalGradient(scene: Phaser.Scene, top: number, bottom: number, steps = 24): void {
  const g = scene.add.graphics()
  g.setDepth(-100)
  const height = scene.scale.height
  const width = scene.scale.width
  const band = height / steps
  for (let i = 0; i < steps; i += 1) {
    const t = i / (steps - 1)
    g.fillStyle(lerpColor(top, bottom, t), 1)
    g.fillRect(0, i * band, width, band + 1)
  }
}

export function drawForestBackground(scene: Phaser.Scene): void {
  verticalGradient(scene, palette.forestTop, palette.forestBottom)
  const g = scene.add.graphics()
  g.setDepth(-90)
  const w = scene.scale.width
  const h = scene.scale.height
  g.fillStyle(0x3f8f5a, 1)
  g.fillEllipse(w * 0.2, h * 0.8, w * 0.95, h * 0.26)
  g.fillEllipse(w * 0.85, h * 0.84, w * 0.95, h * 0.28)
  g.fillStyle(0x2f6b4f, 1)
  g.fillRect(0, h * 0.86, w, h * 0.14)
  for (const [tx, th] of [
    [0.12, 0.16],
    [0.32, 0.12],
    [0.7, 0.14],
    [0.9, 0.1],
  ] as const) {
    const cx = w * tx
    const top = h * 0.52
    g.fillStyle(0x4a3520, 1)
    g.fillRect(cx - 4, top + h * th * 0.5, 8, h * th * 0.5)
    g.fillStyle(0x2f7d4a, 1)
    g.fillTriangle(cx - w * 0.06, top + h * th * 0.55, cx + w * 0.06, top + h * th * 0.55, cx, top - h * th * 0.45)
  }
  for (let i = 0; i < 14; i += 1) {
    g.fillStyle(0xfff0b3, Phaser.Math.FloatBetween(0.2, 0.6))
    g.fillCircle(Phaser.Math.Between(0, w), Phaser.Math.Between(h * 0.4, h * 0.85), Phaser.Math.Between(1, 2))
  }
}

export function drawNightBackground(scene: Phaser.Scene): void {
  verticalGradient(scene, palette.nightTop, palette.nightBottom)
  const g = scene.add.graphics()
  g.setDepth(-90)
  const w = scene.scale.width
  const h = scene.scale.height
  g.fillStyle(0xfff2c2, 1)
  g.fillCircle(w * 0.8, h * 0.16, 26)
  g.fillStyle(palette.nightTop, 1)
  g.fillCircle(w * 0.85, h * 0.13, 22)
  for (let i = 0; i < 44; i += 1) {
    g.fillStyle(0xffffff, Phaser.Math.FloatBetween(0.4, 1))
    g.fillCircle(Phaser.Math.Between(0, w), Phaser.Math.Between(0, h * 0.6), Phaser.Math.Between(1, 2))
  }
  g.fillStyle(0x241a4a, 1)
  g.fillEllipse(w * 0.5, h * 0.96, w * 1.2, h * 0.2)
}

export function drawWorkshopBackground(scene: Phaser.Scene): void {
  verticalGradient(scene, palette.workshopTop, palette.workshopBottom)
  const g = scene.add.graphics()
  g.setDepth(-90)
  const w = scene.scale.width
  const h = scene.scale.height
  g.fillStyle(0x4a3568, 1)
  g.fillRect(0, h * 0.7, w, h * 0.3)
  g.fillStyle(0x5a4278, 1)
  g.fillRect(w * 0.05, h * 0.2, w * 0.2, h * 0.45)
  g.fillRect(w * 0.75, h * 0.25, w * 0.2, h * 0.4)
  g.fillStyle(0x8a6bb0, 1)
  g.fillRect(w * 0.05, h * 0.3, w * 0.2, 6)
  g.fillRect(w * 0.75, h * 0.35, w * 0.2, 6)
  g.fillStyle(0x2a1f3a, 1)
  g.fillEllipse(w * 0.5, h * 0.82, w * 0.5, h * 0.16)
}

export function drawMushroom(g: Phaser.GameObjects.Graphics, color: number): void {
  g.fillStyle(palette.mushroomCream, 1)
  g.fillRoundedRect(-9, -2, 18, 26, 6)
  g.fillStyle(color, 1)
  g.fillEllipse(0, -6, 40, 28)
  g.fillStyle(0xffffff, 0.85)
  g.fillCircle(-10, -10, 4)
  g.fillCircle(8, -6, 3)
  g.fillCircle(2, -14, 3)
}

export function drawStar(g: Phaser.GameObjects.Graphics, color: number): void {
  g.fillStyle(color, 1)
  const spikes = 5
  const outer = 22
  const inner = 9
  g.beginPath()
  for (let i = 0; i < spikes * 2; i += 1) {
    const radius = i % 2 === 0 ? outer : inner
    const angle = (i * Math.PI) / spikes - Math.PI / 2
    const x = Math.cos(angle) * radius
    const y = Math.sin(angle) * radius
    if (i === 0) g.moveTo(x, y)
    else g.lineTo(x, y)
  }
  g.closePath()
  g.fillPath()
}

export function drawButterfly(g: Phaser.GameObjects.Graphics): void {
  g.fillStyle(palette.butterfly, 1)
  g.fillEllipse(-12, -6, 22, 26)
  g.fillEllipse(12, -6, 22, 26)
  g.fillEllipse(-10, 12, 18, 20)
  g.fillEllipse(10, 12, 18, 20)
  g.fillStyle(palette.butterflyWing, 0.8)
  g.fillCircle(-12, -8, 5)
  g.fillCircle(12, -8, 5)
  g.fillStyle(0x4a3520, 1)
  g.fillRoundedRect(-3, -16, 6, 32, 3)
  g.fillCircle(0, -18, 5)
}

export function drawBee(g: Phaser.GameObjects.Graphics): void {
  g.fillStyle(palette.bee, 1)
  g.fillEllipse(0, 0, 30, 24)
  g.fillStyle(palette.beeStripe, 1)
  g.fillRect(-12, -12, 6, 24)
  g.fillRect(2, -12, 6, 24)
  g.fillStyle(0xbfe8ff, 0.7)
  g.fillEllipse(-8, -16, 16, 12)
  g.fillEllipse(8, -16, 16, 12)
  g.fillStyle(0x2a2a2a, 1)
  g.fillCircle(12, -4, 3)
  g.fillTriangle(14, -2, 20, 0, 14, 2)
}

export function drawCauldron(g: Phaser.GameObjects.Graphics): void {
  g.fillStyle(0x2b2b3a, 1)
  g.fillEllipse(0, 6, 64, 48)
  g.fillStyle(palette.cauldron, 1)
  g.fillEllipse(0, -8, 56, 18)
  g.fillStyle(palette.cauldronGlow, 1)
  g.fillEllipse(0, -10, 48, 14)
  g.fillStyle(0x2b2b3a, 1)
  g.fillRoundedRect(-30, 26, 10, 12, 3)
  g.fillRoundedRect(20, 26, 10, 12, 3)
}

export function drawBasket(g: Phaser.GameObjects.Graphics): void {
  g.fillStyle(palette.basketWood, 1)
  g.fillEllipse(0, 0, 70, 44)
  g.fillStyle(palette.basketWeave, 1)
  g.fillEllipse(0, -8, 64, 20)
  g.fillStyle(0x6b4423, 1)
  g.fillRoundedRect(-34, -14, 68, 8, 4)
}

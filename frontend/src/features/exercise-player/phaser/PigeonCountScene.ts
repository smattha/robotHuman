import { ExerciseGameScene, type ExerciseSceneProps } from './ExerciseGameScene'
import { palette } from '../../phaser/palette'

const GREY_INDEX = [0, 2, 4]

export class PigeonCountScene extends ExerciseGameScene {
  private pigeons: { x: number; y: number; isGrey: boolean }[] = []

  protected drawBackground(): void {
    const w = this.scale.width
    const h = this.scale.height
    const g = this.add.graphics()
    g.setDepth(-100)
    g.fillStyle(0x2d2160, 1)
    g.fillRect(0, 0, w, h * 0.7)
    g.fillStyle(0x1a1442, 1)
    for (const [bx, bw, bh] of [
      [0.05, 0.2, 0.4],
      [0.3, 0.18, 0.55],
      [0.55, 0.22, 0.35],
      [0.8, 0.18, 0.5],
    ] as const) {
      g.fillRect(w * bx, h * (0.7 - bh), w * bw, h * bh)
    }
    g.fillStyle(0xfff2c2, 1)
    g.fillCircle(w * 0.15, h * 0.14, 22)
    g.fillStyle(0x4a4a5a, 1)
    g.fillRect(0, h * 0.7, w, h * 0.3)
    g.fillStyle(0x5a5a6a, 1)
    g.fillRect(0, h * 0.7, w, 10)
  }

  protected buildGameArea(): void {
    const props = this.currentProps
    if (!props) return
    const w = this.scale.width
    const h = this.scale.height
    const xs = [0.16, 0.34, 0.5, 0.66, 0.84]
    const y = h * 0.55
    const colors = [0x8a8a9a, 0xf0f0f0, 0x8a8a9a, 0x9a6a3a, 0x8a8a9a]
    xs.forEach((fx, index) => {
      const x = w * fx
      const isGrey = GREY_INDEX.includes(index)
      this.drawPigeon(x, y, colors[index])
      this.pigeons.push({ x, y, isGrey })
    })
    this.drawNumberButtons(props.options, w, h)
  }

  private drawPigeon(x: number, y: number, color: number): void {
    const g = this.add.graphics()
    g.setDepth(5)
    g.fillStyle(color, 1)
    g.fillEllipse(x, y, 34, 24)
    g.fillCircle(x + 14, y - 12, 10)
    g.fillTriangle(x - 16, y - 4, x - 30, y - 10, x - 16, y + 4)
    g.fillStyle(0xff9a3c, 1)
    g.fillTriangle(x + 22, y - 13, x + 30, y - 11, x + 22, y - 9)
    g.fillStyle(0x2a1a10, 1)
    g.fillCircle(x + 16, y - 14, 1.8)
    g.fillStyle(0x3a3a4a, 1)
    g.fillTriangle(x - 4, y + 8, x + 4, y + 8, x, y + 18)
  }

  protected revealResult(props: ExerciseSceneProps): void {
    const w = this.scale.width
    const h = this.scale.height
    this.pigeons.forEach((pigeon) => {
      if (!pigeon.isGrey) return
      const ring = this.add.circle(pigeon.x, pigeon.y - 4, 28, palette.correct, 0)
      ring.setStrokeStyle(4, palette.correct)
      ring.setDepth(20)
      this.tweens.add({ targets: ring, alpha: 1, duration: 400 })
      this.tweens.add({ targets: ring, scale: { from: 0.8, to: 1.15 }, duration: 700, yoyo: true, repeat: -1 })
    })
    if (props.isCorrect) {
      this.celebrateAt(w / 2, h * 0.55)
    } else {
      this.highlightButton(props.correctOptionId, palette.correct)
    }
  }
}

import { ExerciseGameScene, type ExerciseSceneProps } from './ExerciseGameScene'
import { palette } from '../../phaser/palette'

const HAT_WEARER_INDEX = [1, 3]

export class HatCountScene extends ExerciseGameScene {
  private people: { x: number; y: number; hasHat: boolean }[] = []

  protected drawBackground(): void {
    const w = this.scale.width
    const h = this.scale.height
    const g = this.add.graphics()
    g.setDepth(-100)
    g.fillStyle(0x8fd3ff, 1)
    g.fillRect(0, 0, w, h * 0.6)
    g.fillStyle(0x9be7a0, 1)
    g.fillRect(0, h * 0.6, w, h * 0.4)
    g.fillStyle(0xfff2c2, 1)
    g.fillCircle(w * 0.82, h * 0.14, 26)
    for (const hx of [0.16, 0.5, 0.84]) {
      const hxpx = w * hx
      const hy = h * 0.42
      g.fillStyle(0xe0a06a, 1)
      g.fillRect(hxpx - 26, hy, 52, 40)
      g.fillStyle(0xc0564a, 1)
      g.fillTriangle(hxpx - 32, hy, hxpx + 32, hy, hxpx, hy - 26)
      g.fillStyle(0x6b4423, 1)
      g.fillRect(hxpx - 8, hy + 18, 16, 22)
    }
  }

  protected buildGameArea(): void {
    const props = this.currentProps
    if (!props) return
    const w = this.scale.width
    const h = this.scale.height
    const xs = [0.14, 0.32, 0.5, 0.68, 0.86]
    const y = h * 0.52
    xs.forEach((fx, index) => {
      const x = w * fx
      const hasHat = HAT_WEARER_INDEX.includes(index)
      this.drawPerson(x, y, hasHat)
      this.people.push({ x, y, hasHat })
    })
    this.drawNumberButtons(props.options, w, h)
  }

  private drawPerson(x: number, y: number, hasHat: boolean): void {
    const g = this.add.graphics()
    g.setDepth(5)
    g.fillStyle(0x5a7ab0, 1)
    g.fillRoundedRect(x - 16, y - 6, 32, 44, 10)
    g.fillStyle(0xf0c0a0, 1)
    g.fillCircle(x, y - 18, 14)
    g.fillStyle(0x2a1a10, 1)
    g.fillCircle(x - 5, y - 20, 2)
    g.fillCircle(x + 5, y - 20, 2)
    if (hasHat) {
      g.fillStyle(0xe0564a, 1)
      g.fillEllipse(x, y - 30, 34, 10)
      g.fillRoundedRect(x - 12, y - 44, 24, 16, 5)
    }
  }

  protected revealResult(props: ExerciseSceneProps): void {
    const w = this.scale.width
    const h = this.scale.height
    this.people.forEach((person) => {
      if (!person.hasHat) return
      const ring = this.add.circle(person.x, person.y - 18, 26, palette.correct, 0)
      ring.setStrokeStyle(4, palette.correct)
      ring.setDepth(20)
      this.tweens.add({ targets: ring, alpha: 1, duration: 400 })
      this.tweens.add({ targets: ring, scale: { from: 0.8, to: 1.15 }, duration: 700, yoyo: true, repeat: -1 })
    })
    if (props.isCorrect) {
      this.celebrateAt(w / 2, h * 0.5)
    } else {
      this.highlightButton(props.correctOptionId, palette.correct)
    }
  }
}

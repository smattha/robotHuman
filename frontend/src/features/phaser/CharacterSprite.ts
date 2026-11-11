import Phaser from 'phaser'
import { characterColors, type CharacterKind } from './palette'

export type CharacterState = 'idle' | 'talking' | 'happy'

export class CharacterSprite {
  readonly container: Phaser.GameObjects.Container
  private readonly scene: Phaser.Scene
  private readonly kind: CharacterKind
  private state: CharacterState = 'idle'
  private tweens: Phaser.Tweens.Tween[] = []
  private baseY: number

  constructor(scene: Phaser.Scene, kind: CharacterKind, x: number, y: number, scale = 1) {
    this.scene = scene
    this.kind = kind
    this.baseY = y
    this.container = scene.add.container(x, y)
    this.container.setScale(scale)
    this.draw()
    this.applyState()
  }

  private graphics(): Phaser.GameObjects.Graphics {
    const g = this.scene.add.graphics()
    this.container.add(g)
    return g
  }

  private draw(): void {
    const { main, belly, accent } = characterColors[this.kind]
    const g = this.graphics()

    // Body
    g.fillStyle(belly, 1)
    g.fillEllipse(0, 26, 46, 38)
    g.fillStyle(main, 1)
    g.fillEllipse(0, 14, 52, 40)

    // Head
    g.fillStyle(main, 1)
    g.fillCircle(0, -20, 30)

    if (this.kind === 'fox') {
      g.fillStyle(main, 1)
      g.fillTriangle(-22, -34, -6, -44, -8, -24)
      g.fillTriangle(22, -34, 6, -44, 8, -24)
      g.fillStyle(accent, 1)
      g.fillTriangle(-18, -34, -8, -40, -9, -27)
      g.fillTriangle(18, -34, 8, -40, 9, -27)
      g.fillStyle(belly, 1)
      g.fillEllipse(0, -12, 26, 18)
    } else if (this.kind === 'owl') {
      g.fillStyle(main, 1)
      g.fillTriangle(-20, -42, -8, -50, -6, -34)
      g.fillTriangle(20, -42, 8, -50, 6, -34)
      g.fillStyle(0xffffff, 1)
      g.fillCircle(-11, -22, 11)
      g.fillCircle(11, -22, 11)
      g.fillStyle(0x2a1a10, 1)
      g.fillCircle(-11, -22, 5)
      g.fillCircle(11, -22, 5)
      g.fillStyle(accent, 1)
      g.fillTriangle(-5, -14, 5, -14, 0, -6)
    } else if (this.kind === 'unicorn') {
      g.fillStyle(0xffd76a, 1)
      g.fillTriangle(-4, -46, 4, -46, 0, -66)
      g.fillStyle(accent, 1)
      g.fillEllipse(-16, -30, 14, 26)
      g.fillEllipse(16, -30, 14, 26)
      g.fillEllipse(0, -34, 18, 20)
    } else {
      g.fillStyle(accent, 1)
      g.fillRect(-2, -52, 4, 14)
      g.fillCircle(0, -54, 5)
    }

    // Eyes (for non-owl)
    if (this.kind !== 'owl') {
      g.fillStyle(0x2a1a10, 1)
      g.fillCircle(-11, -24, 4)
      g.fillCircle(11, -24, 4)
    }

    // Smile
    g.lineStyle(2, 0x2a1a10, 1)
    g.beginPath()
    g.arc(0, -10, 8, 0.15 * Math.PI, 0.85 * Math.PI)
    g.strokePath()
  }

  setState(state: CharacterState): void {
    if (this.state === state) return
    this.state = state
    this.applyState()
  }

  private applyState(): void {
    this.tweens.forEach((tween) => tween.stop())
    this.tweens = []
    const { container } = this
    if (this.state === 'idle') {
      this.tweens.push(this.scene.tweens.add({ targets: container, y: this.baseY + 4, duration: 1600, yoyo: true, repeat: -1, ease: 'Sine.easeInOut' }))
    } else if (this.state === 'talking') {
      this.tweens.push(this.scene.tweens.add({ targets: container, y: this.baseY - 5, duration: 260, yoyo: true, repeat: -1, ease: 'Sine.easeInOut' }))
      this.tweens.push(this.scene.tweens.add({ targets: container, scale: container.scale * 1.06, duration: 260, yoyo: true, repeat: -1, ease: 'Sine.easeInOut' }))
    } else {
      this.tweens.push(this.scene.tweens.add({ targets: container, y: this.baseY - 14, duration: 320, yoyo: true, repeat: -1, ease: 'Bounce.easeOut' }))
    }
  }

  destroy(): void {
    this.tweens.forEach((tween) => tween.stop())
    this.tweens = []
    this.container.destroy()
  }
}

import Phaser from 'phaser'
import { ExerciseGameScene, type ExerciseSceneProps } from './ExerciseGameScene'
import { palette } from '../../phaser/palette'

const PAPER = 0xfff5e0
const PAPER_EDGE = 0xd9b87a

export class PaperMatchScene extends ExerciseGameScene {
  private candidates: { id: string; container: Phaser.GameObjects.Container; joinY: number }[] = []
  private topBottomY = 0

  protected drawBackground(): void {
    const w = this.scale.width
    const h = this.scale.height
    const g = this.add.graphics()
    g.setDepth(-100)
    g.fillStyle(0x3a2a5a, 1)
    g.fillRect(0, 0, w, h)
    g.fillStyle(0x5a4278, 1)
    g.fillRect(0, h * 0.72, w, h * 0.28)
    g.fillStyle(0x8a6bb0, 1)
    g.fillRect(0, h * 0.72, w, 6)
  }

  protected buildGameArea(): void {
    const props = this.currentProps
    if (!props) return
    const w = this.scale.width
    const h = this.scale.height
    const topY = h * 0.24
    const paperW = w * 0.46
    const paperH = h * 0.11
    this.topBottomY = topY + paperH
    this.drawPaperHalf(w / 2, topY, paperW, paperH, 3, true)

    const bumps = [0, 1, 2, 4, 3]
    const rowY = h * 0.56
    const gap = w / (bumps.length + 1)
    props.options.forEach((option, index) => {
      const x = gap * (index + 1)
      const container = this.drawPaperHalf(x, rowY, w * 0.16, h * 0.07, bumps[index], false)
      const label = this.add.text(x, rowY + h * 0.07 + 18, option.label, {
        fontFamily: 'system-ui, sans-serif',
        fontSize: '18px',
        fontStyle: 'bold',
        color: '#ffffff',
      }).setOrigin(0.5)
      label.setDepth(6)
      const zone = this.add.zone(x, rowY + h * 0.035, w * 0.16, h * 0.09).setInteractive({ useHandCursor: true })
      zone.on('pointerdown', () => this.handleTap(option.id))
      this.candidates.push({ id: option.id, container, joinY: this.topBottomY - h * 0.035 })
    })
  }

  private drawPaperHalf(x: number, y: number, wd: number, ht: number, bumps: number, isTop: boolean): Phaser.GameObjects.Container {
    const container = this.add.container(x, y)
    container.setDepth(5)
    const g = this.add.graphics()
    g.fillStyle(PAPER, 1)
    g.lineStyle(2, PAPER_EDGE, 1)
    const rectY = isTop ? 0 : 0
    g.fillRoundedRect(-wd / 2, rectY, wd, ht, 4)
    g.strokeRoundedRect(-wd / 2, rectY, wd, ht, 4)
    if (bumps > 0) {
      const r = wd / (2 * bumps)
      const edgeY = isTop ? ht : 0
      for (let i = 0; i < bumps; i += 1) {
        const bx = -wd / 2 + r + i * (2 * r)
        g.fillStyle(PAPER, 1)
        g.fillCircle(bx, edgeY, r)
        g.lineStyle(2, PAPER_EDGE, 1)
        g.strokeCircle(bx, edgeY, r)
      }
    }
    container.add(g)
    return container
  }

  private handleTap(optionId: string): void {
    const props = this.currentProps
    if (!props || props.isSubmitted) return
    props.onAnswer(optionId)
  }

  protected revealResult(props: ExerciseSceneProps): void {
    const w = this.scale.width
    const h = this.scale.height
    const correct = this.candidates.find((c) => c.id === props.correctOptionId)
    if (correct) {
      this.tweens.add({ targets: correct.container, y: correct.joinY, duration: 600, ease: 'Bounce.easeOut' })
    }
    if (props.isCorrect) {
      this.celebrateAt(w / 2, this.topBottomY)
    } else {
      const ring = this.add.circle(
        this.candidates.find((c) => c.id === props.correctOptionId)?.container.x ?? w / 2,
        this.candidates.find((c) => c.id === props.correctOptionId)?.container.y ?? h * 0.56,
        40,
        palette.correct,
        0,
      )
      ring.setStrokeStyle(4, palette.correct)
      ring.setDepth(20)
      this.tweens.add({ targets: ring, alpha: 1, duration: 400 })
    }
  }
}

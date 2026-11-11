import { ExerciseGameScene, type ExerciseSceneProps } from './ExerciseGameScene'
import { drawForestBackground } from '../../phaser/draw'
import { palette } from '../../phaser/palette'

export class KangarooScaleScene extends ExerciseGameScene {
  protected drawBackground(): void {
    drawForestBackground(this)
  }

  protected buildGameArea(): void {
    const props = this.currentProps
    if (!props) return
    const w = this.scale.width
    const h = this.scale.height
    const cx = w / 2
    const cy = h * 0.4

    this.drawKangaroo(cx, cy)
    this.drawReadingCard(cx - w * 0.26, h * 0.62, 'μαμά + μωρό', '60')
    this.drawReadingCard(cx + w * 0.26, h * 0.62, 'μαμά', '52')

    this.drawNumberButtons(props.options, w, h)
  }

  private drawKangaroo(x: number, y: number): void {
    const g = this.add.graphics()
    g.setDepth(5)
    g.fillStyle(0x9a6a3a, 1)
    g.fillEllipse(x, y + 10, 70, 80)
    g.fillEllipse(x - 30, y + 50, 30, 20)
    g.fillEllipse(x + 30, y + 50, 30, 20)
    g.fillStyle(0x8a5a2a, 1)
    g.fillEllipse(x - 38, y - 30, 40, 70)
    g.fillStyle(0xf0e0c0, 1)
    g.fillEllipse(x, y + 20, 40, 44)
    g.fillStyle(0x9a6a3a, 1)
    g.fillCircle(x, y - 50, 26)
    g.fillTriangle(x - 14, y - 70, x - 6, y - 92, x - 2, y - 68)
    g.fillTriangle(x + 14, y - 70, x + 6, y - 92, x + 2, y - 68)
    g.fillStyle(0x2a1a10, 1)
    g.fillCircle(x - 8, y - 52, 3)
    g.fillCircle(x + 8, y - 52, 3)
    g.fillEllipse(x, y - 44, 10, 6)
    g.fillStyle(0xc98a4a, 1)
    g.fillCircle(x, y + 14, 14)
    g.fillStyle(0x2a1a10, 1)
    g.fillCircle(x - 5, y + 12, 2)
    g.fillCircle(x + 5, y + 12, 2)
  }

  private drawReadingCard(x: number, y: number, label: string, value: string): void {
    const card = this.add.rectangle(x, y, 130, 70, 0x2a1f3a, 0.85).setStrokeStyle(2, 0xffd76a)
    const top = this.add.text(x, y - 14, label, {
      fontFamily: 'system-ui, sans-serif',
      fontSize: '14px',
      color: '#d9d2ff',
      align: 'center',
    }).setOrigin(0.5)
    const bottom = this.add.text(x, y + 14, value, {
      fontFamily: 'system-ui, sans-serif',
      fontSize: '30px',
      fontStyle: 'bold',
      color: '#ffd76a',
    }).setOrigin(0.5)
    card.setDepth(5)
    top.setDepth(6)
    bottom.setDepth(6)
  }

  protected revealResult(props: ExerciseSceneProps): void {
    const w = this.scale.width
    const h = this.scale.height
    const correct = props.options.find((o) => o.id === props.correctOptionId)
    const value = correct ? correct.label : '8'
    const badge = this.add.rectangle(w / 2, h * 0.3, 90, 90, palette.correct, 0.95).setStrokeStyle(4, 0xffffff)
    const num = this.add.text(w / 2, h * 0.3, value, {
      fontFamily: 'system-ui, sans-serif',
      fontSize: '48px',
      fontStyle: 'bold',
      color: '#ffffff',
    }).setOrigin(0.5)
    badge.setDepth(20)
    num.setDepth(21)
    badge.setScale(0)
    this.tweens.add({ targets: badge, scale: 1, duration: 500, ease: 'Back.easeOut' })
    this.tweens.add({ targets: num, scale: 1, duration: 500, ease: 'Back.easeOut' })
    if (props.isCorrect) {
      this.celebrateAt(w / 2, h * 0.3)
    } else {
      this.highlightButton(props.correctOptionId, palette.correct)
    }
  }
}

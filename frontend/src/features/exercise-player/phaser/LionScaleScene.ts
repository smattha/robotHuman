import { ExerciseGameScene, type ExerciseSceneProps } from './ExerciseGameScene'
import { drawForestBackground } from '../../phaser/draw'
import { palette } from '../../phaser/palette'

export class LionScaleScene extends ExerciseGameScene {
  private rightPanX = 0
  private rightPanY = 0

  protected drawBackground(): void {
    drawForestBackground(this)
  }

  protected buildGameArea(): void {
    const props = this.currentProps
    if (!props) return
    const w = this.scale.width
    const h = this.scale.height
    const midY = h * 0.44
    const cx = w / 2
    const panOffset = w * 0.28
    const panY = midY + 16

    const g = this.add.graphics()
    g.fillStyle(0x6b4423, 1)
    g.fillTriangle(cx - 36, midY + 128, cx + 36, midY + 128, cx, midY + 100)
    g.fillStyle(0x8a5a2a, 1)
    g.fillRect(cx - 6, midY - 14, 12, 116)
    g.fillStyle(0xffd76a, 1)
    g.fillCircle(cx, midY - 16, 11)
    g.fillStyle(0x8a5a2a, 1)
    g.fillRect(cx - panOffset - 34, midY - 16, panOffset * 2 + 68, 10)
    g.fillStyle(0xb5824a, 1)
    g.fillEllipse(cx - panOffset, panY, 74, 24)
    g.fillEllipse(cx + panOffset, panY, 74, 24)
    g.lineStyle(3, 0x6b4423, 1)
    g.beginPath()
    g.moveTo(cx - panOffset, midY - 6)
    g.lineTo(cx - panOffset, panY - 10)
    g.moveTo(cx + panOffset, midY - 6)
    g.lineTo(cx + panOffset, panY - 10)
    g.strokePath()

    this.drawLion(cx - panOffset, panY - 12)
    this.rightPanX = cx + panOffset
    this.rightPanY = panY - 6

    this.drawNumberButtons(props.options, w, h)
  }

  private drawLion(x: number, y: number): void {
    const g = this.add.graphics()
    g.setDepth(5)
    g.fillStyle(0xd96a1a, 1)
    g.fillCircle(x, y - 8, 27)
    g.fillStyle(0xf08a3c, 1)
    g.fillCircle(x, y - 8, 19)
    g.fillEllipse(x, y + 16, 36, 26)
    g.fillStyle(0xd96a1a, 1)
    g.fillCircle(x - 17, y - 24, 8)
    g.fillCircle(x + 17, y - 24, 8)
    g.fillStyle(0xfff0d6, 1)
    g.fillEllipse(x, y - 2, 16, 11)
    g.fillStyle(0x2a1a10, 1)
    g.fillCircle(x - 7, y - 11, 2.6)
    g.fillCircle(x + 7, y - 11, 2.6)
    g.fillEllipse(x, y - 3, 7, 4)
  }

  private drawDuckling(x: number, y: number): void {
    const g = this.add.graphics()
    g.setDepth(6)
    g.fillStyle(0xffe066, 1)
    g.fillEllipse(x, y, 22, 16)
    g.fillCircle(x + 10, y - 9, 9)
    g.fillStyle(0xff9a3c, 1)
    g.fillTriangle(x + 17, y - 10, x + 27, y - 8, x + 17, y - 6)
    g.fillStyle(0x2a1a10, 1)
    g.fillCircle(x + 11, y - 11, 1.6)
  }

  protected revealResult(props: ExerciseSceneProps): void {
    const w = this.scale.width
    const h = this.scale.height
    const correct = props.options.find((o) => o.id === props.correctOptionId)
    const count = correct ? parseInt(correct.label, 10) : 4
    for (let i = 0; i < count; i += 1) {
      const x = this.rightPanX - ((count - 1) * 15) / 2 + i * 15
      this.drawDuckling(x, this.rightPanY)
    }
    if (props.isCorrect) {
      this.celebrateAt(w / 2, h * 0.42)
    } else {
      this.highlightButton(props.correctOptionId, palette.correct)
    }
  }
}

import Phaser from 'phaser'
import { ExerciseGameScene, type ExerciseSceneProps } from './ExerciseGameScene'
import { drawButterfly, drawBee, drawCauldron, drawMushroom, drawStar } from '../../phaser/draw'
import { palette } from '../../phaser/palette'

type Candidate = { id: string; label: string; draw: (g: Phaser.GameObjects.Graphics) => void }

export class ObjectSpotlightScene extends ExerciseGameScene {
  private candidates: { id: string; x: number; y: number; ring: Phaser.GameObjects.Arc }[] = []

  protected drawBackground(): void {
    const w = this.scale.width
    const h = this.scale.height
    const g = this.add.graphics()
    g.setDepth(-100)
    g.fillStyle(0x14102e, 1)
    g.fillRect(0, 0, w, h)
    for (let i = 0; i < 30; i += 1) {
      g.fillStyle(0xffffff, Phaser.Math.FloatBetween(0.3, 0.9))
      g.fillCircle(Phaser.Math.Between(0, w), Phaser.Math.Between(0, h), Phaser.Math.Between(1, 2))
    }
  }

  protected buildGameArea(): void {
    const props = this.currentProps
    if (!props) return
    const w = this.scale.width
    const h = this.scale.height
    const targetY = h * 0.3

    const cone = this.add.graphics()
    cone.setDepth(-50)
    cone.fillStyle(0xfff2c2, 0.12)
    cone.fillTriangle(w / 2 - 14, h * 0.12, w / 2 + 14, h * 0.12, w / 2 + 70, targetY + 40)
    const glow = this.add.circle(w / 2, targetY, 56, 0xfff2c2, 0.18)
    glow.setDepth(-40)
    const targetG = this.add.graphics()
    targetG.setDepth(5)
    drawStar(targetG, palette.starGold)
    targetG.setPosition(w / 2, targetY)

    const candidates: Candidate[] = [
      { id: 'alpha', label: 'Α', draw: (g) => drawStar(g, palette.starGold) },
      { id: 'beta', label: 'Β', draw: (g) => drawMushroom(g, palette.mushroomRed) },
      { id: 'gamma', label: 'Γ', draw: (g) => drawButterfly(g) },
      { id: 'delta', label: 'Δ', draw: (g) => drawBee(g) },
      { id: 'epsilon', label: 'Ε', draw: (g) => drawCauldron(g) },
    ]
    const rowY = h * 0.62
    const gap = w / (candidates.length + 1)
    candidates.forEach((candidate, index) => {
      const x = gap * (index + 1)
      const circle = this.add.circle(x, rowY, 34, 0x2a2150, 1).setStrokeStyle(3, 0x8a6bb0)
      circle.setDepth(5)
      const obj = this.add.graphics()
      obj.setDepth(6)
      obj.setScale(0.7)
      candidate.draw(obj)
      obj.setPosition(x, rowY - 2)
      const label = this.add.text(x, rowY + 44, candidate.label, {
        fontFamily: 'system-ui, sans-serif',
        fontSize: '18px',
        fontStyle: 'bold',
        color: '#ffffff',
      }).setOrigin(0.5)
      label.setDepth(6)
      const ring = this.add.circle(x, rowY, 40, palette.correct, 0).setStrokeStyle(4, palette.correct)
      ring.setDepth(20)
      const zone = this.add.zone(x, rowY, 70, 70).setInteractive({ useHandCursor: true })
      zone.on('pointerdown', () => this.handleTap(candidate.id))
      this.candidates.push({ id: candidate.id, x, y: rowY, ring })
    })
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
      this.tweens.add({ targets: correct.ring, alpha: 1, duration: 400 })
      this.tweens.add({ targets: correct.ring, scale: { from: 0.85, to: 1.2 }, duration: 700, yoyo: true, repeat: -1 })
    }
    if (props.isCorrect) {
      this.celebrateAt(w / 2, h * 0.62)
    }
  }
}

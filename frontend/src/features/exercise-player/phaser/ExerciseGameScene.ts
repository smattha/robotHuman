import Phaser from 'phaser'
import { BaseGameScene } from '../../phaser/BaseGameScene'
import { CharacterSprite } from '../../phaser/CharacterSprite'
import { celebrate } from '../../phaser/celebration'
import { palette, type CharacterKind } from '../../phaser/palette'

export type ExerciseSceneProps = {
  helper: CharacterKind
  question: string
  options: { id: string; label: string }[]
  correctOptionId: string
  isSubmitted: boolean
  isCorrect: boolean
  selectedOptionId: string | null
  onAnswer: (optionId: string) => void
}

export abstract class ExerciseGameScene extends BaseGameScene<ExerciseSceneProps> {
  protected character: CharacterSprite | null = null
  protected optionButtons: { id: string; bg: Phaser.GameObjects.Rectangle }[] = []
  private submitted = false

  protected buildScene(): void {
    const props = this.currentProps
    if (!props) return
    const w = this.scale.width
    const h = this.scale.height
    this.drawBackground()
    this.drawQuestionBanner(props.question, w, h)
    this.buildGameArea()
    this.character = new CharacterSprite(this, props.helper, w * 0.88, h * 0.13, 0.5)
  }

  protected sync(props: ExerciseSceneProps): void {
    if (this.character) {
      this.character.setState(props.isSubmitted ? (props.isCorrect ? 'happy' : 'idle') : 'idle')
    }
    if (props.isSubmitted && !this.submitted) {
      this.submitted = true
      this.revealResult(props)
    }
  }

  protected drawQuestionBanner(question: string, w: number, h: number): void {
    const text = this.add.text(w / 2, h * 0.035, question, {
      fontFamily: 'system-ui, sans-serif',
      fontSize: '16px',
      fontStyle: 'bold',
      color: '#ffffff',
      align: 'center',
      wordWrap: { width: w * 0.9 },
      backgroundColor: 'rgba(20,14,40,0.55)',
      padding: { x: 12, y: 8 },
    })
    text.setOrigin(0.5, 0)
    text.setDepth(50)
  }

  protected drawNumberButtons(options: { id: string; label: string }[], w: number, h: number): void {
    const count = options.length
    const rowY = h * 0.85
    const gap = w / (count + 1)
    options.forEach((option, index) => {
      const x = gap * (index + 1)
      const bg = this.add.rectangle(x, rowY, gap * 0.82, 58, palette.accent, 0.92).setStrokeStyle(3, 0xffffff)
      this.add.text(x, rowY, option.label, {
        fontFamily: 'system-ui, sans-serif',
        fontSize: '24px',
        fontStyle: 'bold',
        color: '#ffffff',
      }).setOrigin(0.5)
      const zone = this.add.zone(x, rowY, gap * 0.82, 58).setInteractive({ useHandCursor: true })
      zone.on('pointerdown', () => this.handleOptionTap(option.id))
      this.optionButtons.push({ id: option.id, bg })
    })
  }

  protected makeTappable(target: Phaser.GameObjects.Container | Phaser.GameObjects.Zone, optionId: string): void {
    const interactive = target as Phaser.GameObjects.Zone
    interactive.setInteractive({ useHandCursor: true })
    interactive.on('pointerdown', () => this.handleOptionTap(optionId))
  }

  protected highlightButton(optionId: string, color: number): void {
    const btn = this.optionButtons.find((b) => b.id === optionId)
    if (btn) btn.bg.setFillStyle(color)
  }

  protected celebrateAt(x: number, y: number): void {
    celebrate(this, x, y)
  }

  private handleOptionTap(optionId: string): void {
    const props = this.currentProps
    if (!props || props.isSubmitted) return
    props.onAnswer(optionId)
  }

  protected abstract drawBackground(): void
  protected abstract buildGameArea(): void
  protected abstract revealResult(props: ExerciseSceneProps): void
}

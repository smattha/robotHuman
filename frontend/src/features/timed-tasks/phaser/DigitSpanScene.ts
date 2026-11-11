import Phaser from 'phaser'
import { BaseGameScene } from '../../phaser/BaseGameScene'
import { CharacterSprite } from '../../phaser/CharacterSprite'
import { celebrate } from '../../phaser/celebration'
import { drawNightBackground, drawStar } from '../../phaser/draw'
import { palette, type CharacterKind } from '../../phaser/palette'

export type DigitSpanSceneProps = {
  phase: 'showing' | 'answering' | 'finished'
  sequence: string[]
  sequenceIndex: number
  level: number
  answer: string
  helper: CharacterKind
  onEnterDigit: (digit: string) => void
  onClear: () => void
  onSubmit: () => void
}

const W = 390
const H = 700
const KEYS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'clear', '0', 'submit'] as const

export class DigitSpanScene extends BaseGameScene<DigitSpanSceneProps> {
  private character: CharacterSprite | null = null
  private statusText: Phaser.GameObjects.Text | null = null
  private star: Phaser.GameObjects.Container | null = null
  private starDigit: Phaser.GameObjects.Text | null = null
  private answerText: Phaser.GameObjects.Text | null = null
  private keypad: Phaser.GameObjects.Container | null = null
  private lastShowingIndex = -1

  protected buildScene(): void {
    drawNightBackground(this)
    this.character = new CharacterSprite(this, this.currentProps?.helper ?? 'unicorn', W / 2, 78, 0.62)
    this.statusText = this.add
      .text(W / 2, 150, '', { fontFamily: 'Fredoka, sans-serif', fontSize: '22px', color: '#ffffff', align: 'center' })
      .setOrigin(0.5)

    this.star = this.add.container(W / 2, 300)
    const starGfx = this.add.graphics()
    drawStar(starGfx, palette.starGold)
    this.starDigit = this.add
      .text(0, 0, '', { fontFamily: 'Fredoka, sans-serif', fontSize: '48px', fontStyle: 'bold', color: '#3a2a10' })
      .setOrigin(0.5)
    this.star.add([starGfx, this.starDigit])
    this.star.setScale(2)

    this.answerText = this.add
      .text(W / 2, 250, '', { fontFamily: 'Fredoka, sans-serif', fontSize: '44px', color: '#ffffff' })
      .setOrigin(0.5)

    this.keypad = this.add.container()
    this.buildKeypad()
    this.star.setVisible(true)
    this.answerText.setVisible(false)
    this.keypad.setVisible(false)
  }

  private buildKeypad(): void {
    const keyW = 100
    const keyH = 64
    const gap = 12
    const startY = 330
    KEYS.forEach((key, index) => {
      const col = index % 3
      const row = Math.floor(index / 3)
      const x = W / 2 + (col - 1) * (keyW + gap)
      const y = startY + row * (keyH + gap)
      const container = this.add.container(x, y)
      const bg = this.add.graphics()
      const isSubmit = key === 'submit'
      const isClear = key === 'clear'
      bg.fillStyle(isSubmit ? palette.correct : isClear ? palette.wrong : 0x3a2f6b, 1)
      bg.fillRoundedRect(-keyW / 2, -keyH / 2, keyW, keyH, 16)
      const label = isSubmit ? 'Συνέχεια' : isClear ? 'Διόρθωση' : key
      const text = this.add
        .text(0, 0, label, { fontFamily: 'Fredoka, sans-serif', fontSize: isSubmit || isClear ? '18px' : '30px', color: isSubmit ? '#08331f' : '#ffffff' })
        .setOrigin(0.5)
      container.add([bg, text])
      container.setInteractive(new Phaser.Geom.Rectangle(-keyW / 2, -keyH / 2, keyW, keyH), Phaser.Geom.Rectangle.Contains)
      container.on(Phaser.Input.Events.GAMEOBJECT_POINTER_DOWN, () => {
        const props = this.currentProps
        if (!props || props.phase !== 'answering') return
        if (key === 'clear') props.onClear()
        else if (key === 'submit') props.onSubmit()
        else props.onEnterDigit(key)
      })
      this.keypad!.add(container)
    })
  }

  protected sync(props: DigitSpanSceneProps): void {
    const showing = props.phase === 'showing'
    const answering = props.phase === 'answering'
    if (this.star) this.star.setVisible(showing)
    if (this.answerText) this.answerText.setVisible(answering)
    if (this.keypad) this.keypad.setVisible(answering)

    if (showing) {
      if (this.starDigit) this.starDigit.setText(props.sequence[props.sequenceIndex - 1] ?? '')
      if (props.sequenceIndex > 0 && props.sequenceIndex !== this.lastShowingIndex) {
        this.star!.setAlpha(0).setScale(1.2)
        this.tweens.add({ targets: this.star, alpha: 1, scale: 2, duration: 200, ease: 'Back.easeOut' })
      }
    }
    this.lastShowingIndex = showing ? props.sequenceIndex : -1

    if (this.answerText) this.answerText.setText(props.answer || ' ')
    if (this.character) this.character.setState(props.phase === 'finished' ? 'happy' : showing ? 'talking' : 'idle')
    if (this.statusText) {
      const label = props.phase === 'showing' ? 'Θυμήσου τα ψηφία' : props.phase === 'answering' ? 'Πληκτρολόγησε τη σειρά' : 'Τέλος!'
      this.statusText.setText(`${label} · επίπεδο ${props.level}`)
    }
    if (props.phase === 'finished') celebrate(this, W / 2, H * 0.4)
  }
}

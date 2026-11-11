import Phaser from 'phaser'
import { BaseGameScene } from '../../phaser/BaseGameScene'
import { CharacterSprite } from '../../phaser/CharacterSprite'
import { celebrate } from '../../phaser/celebration'
import { drawCauldron, drawWorkshopBackground } from '../../phaser/draw'
import { palette, type CharacterKind } from '../../phaser/palette'
import { COLOR_WORDS, type StroopColor } from '../stroop-logic'

export type StroopSceneProps = {
  phase: 'running' | 'finished'
  word: StroopColor
  ink: StroopColor
  trialStartedAt: number
  helper: CharacterKind
  onRespond: () => void
}

const W = 390
const H = 700
const INK_COLORS: Record<StroopColor, string> = {
  red: '#d64545',
  green: '#3f9d5a',
  blue: '#3a6fd8',
  yellow: '#d9a400',
}

export class StroopScene extends BaseGameScene<StroopSceneProps> {
  private character: CharacterSprite | null = null
  private word: Phaser.GameObjects.Text | null = null
  private lastTrialAt = -1

  protected buildScene(): void {
    drawWorkshopBackground(this)
    this.character = new CharacterSprite(this, this.currentProps?.helper ?? 'fox', W / 2, 92, 0.7)
    const panel = this.add.graphics()
    panel.fillStyle(0xfff8ec, 0.96)
    panel.fillRoundedRect(-150, -58, 300, 116, 22)
    panel.setPosition(W / 2, 280)
    this.word = this.add
      .text(W / 2, 280, '', { fontFamily: 'Fredoka, sans-serif', fontSize: '60px', fontStyle: 'bold', color: '#ffffff' })
      .setOrigin(0.5)
    const cauldron = this.add.graphics()
    drawCauldron(cauldron)
    cauldron.setPosition(W / 2, 440)
    this.addResponseButton()
  }

  private addResponseButton(): void {
    const y = 590
    const container = this.add.container(W / 2, y)
    const bg = this.add.graphics()
    bg.fillStyle(palette.correct, 1)
    bg.fillRoundedRect(-120, -38, 240, 76, 22)
    const label = this.add.text(0, 0, 'Απόκριση', { fontFamily: 'Fredoka, sans-serif', fontSize: '30px', color: '#08331f' }).setOrigin(0.5)
    container.add([bg, label])
    container.setInteractive(new Phaser.Geom.Rectangle(-120, -38, 240, 76), Phaser.Geom.Rectangle.Contains)
    container.on(Phaser.Input.Events.GAMEOBJECT_POINTER_DOWN, () => {
      const props = this.currentProps
      if (props && props.phase === 'running') props.onRespond()
    })
  }

  protected sync(props: StroopSceneProps): void {
    if (this.word) {
      this.word.setText(COLOR_WORDS[props.word]).setColor(INK_COLORS[props.ink])
      if (props.trialStartedAt !== this.lastTrialAt) {
        this.word.setAlpha(0).setScale(0.7)
        this.tweens.add({ targets: this.word, alpha: 1, scale: 1, duration: 200, ease: 'Back.easeOut' })
      }
    }
    this.lastTrialAt = props.trialStartedAt
    if (this.character) this.character.setState(props.phase === 'finished' ? 'happy' : 'idle')
    if (props.phase === 'finished') celebrate(this, W / 2, H * 0.4)
  }
}

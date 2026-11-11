import Phaser from 'phaser'
import { BaseGameScene } from '../../phaser/BaseGameScene'
import { CharacterSprite } from '../../phaser/CharacterSprite'
import { celebrate } from '../../phaser/celebration'
import { drawBasket, drawForestBackground } from '../../phaser/draw'
import { palette, type CharacterKind } from '../../phaser/palette'

export type SartSceneProps = {
  phase: 'running' | 'finished'
  stimulus: string
  trialStartedAt: number
  helper: CharacterKind
  onRespond: () => void
}

const W = 390
const H = 700

export class SartScene extends BaseGameScene<SartSceneProps> {
  private character: CharacterSprite | null = null
  private stimulus: Phaser.GameObjects.Text | null = null
  private lastTrialAt = -1

  protected buildScene(): void {
    drawForestBackground(this)
    this.character = new CharacterSprite(this, this.currentProps?.helper ?? 'unicorn', W / 2, 92, 0.7)
    const basket = this.add.graphics()
    drawBasket(basket)
    basket.setPosition(W / 2, 340)
    this.stimulus = this.add.text(W / 2, 250, '', { fontFamily: 'sans-serif', fontSize: '104px' }).setOrigin(0.5)
    this.addResponseButton()
  }

  private addResponseButton(): void {
    const y = 560
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

  protected sync(props: SartSceneProps): void {
    if (this.stimulus) {
      this.stimulus.setText(props.stimulus)
      if (props.trialStartedAt !== this.lastTrialAt) {
        this.stimulus.setAlpha(0).setScale(0.4)
        this.tweens.add({ targets: this.stimulus, alpha: 1, scale: 1, duration: 200, ease: 'Back.easeOut' })
      }
    }
    this.lastTrialAt = props.trialStartedAt
    if (this.character) this.character.setState(props.phase === 'finished' ? 'happy' : 'idle')
    if (props.phase === 'finished') celebrate(this, W / 2, H * 0.4)
  }
}

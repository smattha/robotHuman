import Phaser from 'phaser'
import { BaseGameScene } from '../../phaser/BaseGameScene'
import { CharacterSprite } from '../../phaser/CharacterSprite'
import { celebrate } from '../../phaser/celebration'
import { drawForestBackground } from '../../phaser/draw'
import { palette, type CharacterKind } from '../../phaser/palette'

export type GoNoGoSceneProps = {
  phase: 'running' | 'finished'
  isGo: boolean
  trialStartedAt: number
  helper: CharacterKind
  onRespond: () => void
}

const W = 390
const H = 700

export class GoNoGoScene extends BaseGameScene<GoNoGoSceneProps> {
  private character: CharacterSprite | null = null
  private word: Phaser.GameObjects.Text | null = null
  private lastTrialAt = -1

  protected buildScene(): void {
    drawForestBackground(this)
    this.character = new CharacterSprite(this, this.currentProps?.helper ?? 'owl', W / 2, 92, 0.7)
    this.word = this.add
      .text(W / 2, 300, '', { fontFamily: 'Fredoka, sans-serif', fontSize: '76px', fontStyle: 'bold', color: '#ffffff' })
      .setOrigin(0.5)
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

  protected sync(props: GoNoGoSceneProps): void {
    if (this.word) {
      this.word.setText(props.isGo ? 'Ξεκίνα' : 'Στοπ').setColor(props.isGo ? '#4dd4a0' : '#ff8a7a')
      if (props.trialStartedAt !== this.lastTrialAt) {
        this.word.setAlpha(0).setScale(0.6)
        this.tweens.add({ targets: this.word, alpha: 1, scale: 1, duration: 220, ease: 'Back.easeOut' })
      }
    }
    this.lastTrialAt = props.trialStartedAt
    if (this.character) this.character.setState(props.phase === 'finished' ? 'happy' : 'idle')
    if (props.phase === 'finished') celebrate(this, W / 2, H * 0.4)
  }
}

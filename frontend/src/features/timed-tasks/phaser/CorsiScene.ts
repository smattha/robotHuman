import Phaser from 'phaser'
import { BaseGameScene } from '../../phaser/BaseGameScene'
import { CharacterSprite } from '../../phaser/CharacterSprite'
import { celebrate } from '../../phaser/celebration'
import { drawForestBackground, drawMushroom } from '../../phaser/draw'
import { palette, type CharacterKind } from '../../phaser/palette'

export type CorsiSceneProps = {
  phase: 'showing' | 'answering' | 'finished'
  sequence: number[]
  sequenceIndex: number
  level: number
  answerLength: number
  helper: CharacterKind
  onTapTile: (tile: number) => void
}

const W = 390
const H = 700
const GRID_CENTER_X = W / 2
const GRID_CENTER_Y = 432
const CELL = 108

export class CorsiScene extends BaseGameScene<CorsiSceneProps> {
  private mushrooms: Phaser.GameObjects.Container[] = []
  private glows: Phaser.GameObjects.Graphics[] = []
  private character: CharacterSprite | null = null
  private statusText: Phaser.GameObjects.Text | null = null

  protected buildScene(): void {
    drawForestBackground(this)
    this.character = new CharacterSprite(this, this.currentProps?.helper ?? 'fox', W / 2, 92, 0.7)
    this.statusText = this.add
      .text(W / 2, 168, '', { fontFamily: 'Fredoka, sans-serif', fontSize: '24px', color: '#ffffff', align: 'center' })
      .setOrigin(0.5)
    for (let tile = 0; tile < 9; tile += 1) {
      const row = Math.floor(tile / 3)
      const col = tile % 3
      const x = GRID_CENTER_X + (col - 1) * CELL
      const y = GRID_CENTER_Y + (row - 1) * CELL
      const container = this.add.container(x, y)
      const glow = this.add.graphics()
      const cap = this.add.graphics()
      drawMushroom(cap, palette.mushroomRed)
      container.add([glow, cap])
      container.setScale(1.1)
      container.setInteractive(new Phaser.Geom.Rectangle(-44, -44, 88, 88), Phaser.Geom.Rectangle.Contains)
      container.on(Phaser.Input.Events.GAMEOBJECT_POINTER_DOWN, () => {
        const props = this.currentProps
        if (props && props.phase === 'answering') props.onTapTile(tile)
      })
      this.mushrooms.push(container)
      this.glows.push(glow)
    }
  }

  protected sync(props: CorsiSceneProps): void {
    const lit = props.phase === 'showing' && props.sequenceIndex > 0 ? props.sequence[props.sequenceIndex - 1] : -1
    for (let tile = 0; tile < 9; tile += 1) {
      const isLit = tile === lit
      const glow = this.glows[tile]
      glow.clear()
      glow.fillStyle(palette.mushroomGlow, isLit ? 0.9 : 0)
      glow.fillEllipse(0, 4, 84, 84)
      this.tweens.add({ targets: this.mushrooms[tile], scale: isLit ? 1.35 : 1.1, duration: 180, ease: 'Quad.easeOut' })
    }
    if (this.character) this.character.setState(props.phase === 'showing' ? 'talking' : props.phase === 'answering' ? 'idle' : 'happy')
    if (this.statusText) {
      const label =
        props.phase === 'showing'
          ? 'Παρακολούθησε τη σειρά'
          : props.phase === 'answering'
            ? `Επανάλαβε · ${props.answerLength}/${props.sequence.length}`
            : 'Τέλος!'
      this.statusText.setText(`${label} · επίπεδο ${props.level}`)
    }
    if (props.phase === 'finished') celebrate(this, W / 2, H * 0.5)
  }
}

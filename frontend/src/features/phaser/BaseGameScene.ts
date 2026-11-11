import Phaser from 'phaser'
import type { GameStore } from './game-store'

export abstract class BaseGameScene<T> extends Phaser.Scene {
  protected store: GameStore<T> | null = null
  private lastVersion = -1
  private built = false

  create(): void {
    this.store = this.readStore()
    if (this.store) this.build()
  }

  update(): void {
    if (!this.store) {
      this.store = this.readStore()
      if (!this.store) return
      this.build()
      this.lastVersion = -1
    }
    if (this.store.version !== this.lastVersion) {
      this.lastVersion = this.store.version
      this.sync(this.store.props)
    }
  }

  private build(): void {
    if (this.built) return
    this.built = true
    this.buildScene()
  }

  private readStore(): GameStore<T> | null {
    return this.game.registry.get('gameStore') as GameStore<T> | null
  }

  protected get currentProps(): T | null {
    return this.store?.props ?? null
  }

  protected abstract buildScene(): void
  protected abstract sync(props: T): void
}

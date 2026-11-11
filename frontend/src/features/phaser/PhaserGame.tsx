import { useEffect, useRef } from 'react'
import Phaser from 'phaser'
import type { GameStore } from './game-store'

type PhaserGameProps<T> = {
  scene: typeof Phaser.Scene
  sceneProps: T
  testId?: string
  ariaLabel?: string
}

const DESIGN_WIDTH = 390
const DESIGN_HEIGHT = 700

function isHeadlessEnvironment(): boolean {
  return typeof navigator !== 'undefined' && /jsdom|headless/i.test(navigator.userAgent)
}

export function PhaserGame<T>({ scene, sceneProps, testId, ariaLabel }: PhaserGameProps<T>) {
  const containerRef = useRef<HTMLDivElement>(null)
  const storeRef = useRef<GameStore<T>>({ props: sceneProps, version: 0 })
  storeRef.current.props = sceneProps
  storeRef.current.version += 1

  useEffect(() => {
    const parent = containerRef.current
    if (!parent) return
    let game: Phaser.Game | null = null
    try {
      game = new Phaser.Game({
        type: isHeadlessEnvironment() ? Phaser.HEADLESS : Phaser.AUTO,
        parent,
        width: DESIGN_WIDTH,
        height: DESIGN_HEIGHT,
        backgroundColor: '#1a1442',
        scale: {
          mode: Phaser.Scale.FIT,
          autoCenter: Phaser.Scale.CENTER_BOTH,
        },
        scene: [scene],
      })
      game.registry.set('gameStore', storeRef.current)
    } catch {
      game = null
    }
    return () => {
      if (game) game.destroy(true)
    }
  }, [scene])

  return <div className="phaser-game" data-testid={testId} aria-label={ariaLabel} ref={containerRef} />
}

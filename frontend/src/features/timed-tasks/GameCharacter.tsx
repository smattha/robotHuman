import { useEffect, useRef } from 'react'
import { helperCharacters } from '../../components/child-helper/helper-characters'
import type { ChildHelper } from '../../domain/preferences'

type GameCharacterProps = {
  helper: ChildHelper
  playing?: boolean
}

export function GameCharacter({ helper, playing = false }: GameCharacterProps) {
  const character = helperCharacters[helper]
  const videoRef = useRef<HTMLVideoElement>(null)

  useEffect(() => {
    const video = videoRef.current
    if (!video) return
    if (playing) {
      void video.play().catch(() => {})
    } else {
      video.pause()
      video.currentTime = 0
    }
    return () => video.pause()
  }, [playing, helper])

  return (
    <span className={`game-character${playing ? ' is-playing' : ''} helper-${character.color}`} aria-hidden="true">
      <span className="game-character-icon">{character.icon}</span>
      <video className="game-character-video" ref={videoRef} src={character.video} muted loop playsInline preload="none" />
    </span>
  )
}

import { useEffect, useRef } from 'react'
import type { ChildHelper as ChildHelperType } from '../../domain/preferences'
import { helperCharacters } from './helper-characters'

type ChildHelperProps = {
  helper: ChildHelperType
  message: string
  compact?: boolean
  playing?: boolean
}

export function ChildHelper({ helper, message, compact = false, playing = false }: ChildHelperProps) {
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
    <aside className={`child-helper-card${compact ? ' compact' : ''} helper-${character.color}`} aria-label={`${character.name}, ο βοηθός σου`}>
      <span className={`child-helper-art${playing ? ' is-playing' : ''}`} aria-hidden="true">
        {character.icon}
        <video className="child-helper-video" ref={videoRef} src={character.video} muted loop playsInline preload="none" />
      </span>
      <span className="child-helper-copy">
        <strong>{character.name}, ο βοηθός σου</strong>
        <span>{message}</span>
      </span>
    </aside>
  )
}

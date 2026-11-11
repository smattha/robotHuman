import { useCallback, useEffect, useRef, useState } from 'react'
import type { StoryFrame } from '../domain/exercise-model'
import type { NarrationMode, StorySpeed } from '../domain/preferences'
import { getStoryFrameDuration } from '../domain/preferences'
import { useNarration } from './use-narration'

type UseStoryPlaybackOptions = {
  frames: StoryFrame[]
  questionText: string
  storySpeed: StorySpeed
  narrationMode: NarrationMode
  speechEnabled: boolean
  enabled: boolean
}

type UseStoryPlaybackResult = {
  phase: 'playing' | 'question'
  frameIndex: number
  currentFrame: StoryFrame | null
  isNarrating: boolean
  isPreparing: boolean
  replay: () => void
  nextFrame: () => void
}

export function useStoryPlayback({ frames, questionText, storySpeed, narrationMode, speechEnabled, enabled }: UseStoryPlaybackOptions): UseStoryPlaybackResult {
  const [phase, setPhase] = useState<'playing' | 'question'>(frames.length > 0 && enabled ? 'playing' : 'question')
  const [frameIndex, setFrameIndex] = useState(0)
  const timerRef = useRef<ReturnType<typeof setTimeout> | null>(null)
  const currentFrame = phase === 'playing' ? frames[frameIndex] ?? null : null
  const narrationText = phase === 'playing' ? currentFrame?.text ?? '' : questionText
  const { isNarrating, isPreparing, replay } = useNarration({
    text: narrationText,
    narrationMode,
    speechEnabled,
    autoPlay: narrationMode === 'auto' && enabled && narrationText !== '',
  })

  const advance = useCallback(() => {
    if (timerRef.current) {
      clearTimeout(timerRef.current)
      timerRef.current = null
    }
    if (phase !== 'playing') return
    if (frameIndex < frames.length - 1) setFrameIndex((index) => index + 1)
    else setPhase('question')
  }, [phase, frameIndex, frames.length])

  useEffect(() => {
    if (phase !== 'playing' || !enabled) return
    timerRef.current = setTimeout(advance, getStoryFrameDuration(storySpeed))
    return () => {
      if (timerRef.current) {
        clearTimeout(timerRef.current)
        timerRef.current = null
      }
    }
  }, [phase, frameIndex, enabled, storySpeed, advance])

  return { phase, frameIndex, currentFrame, isNarrating, isPreparing, replay, nextFrame: advance }
}

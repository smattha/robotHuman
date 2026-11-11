import { useCallback, useEffect, useRef, useState } from 'react'
import { useSpeak, useVoices } from 'react-text-to-speech'
import { getGreekVoiceAudio, isGreekVoiceStored } from '../domain/greek-voice'
import type { NarrationMode } from '../domain/preferences'

type UseNarrationOptions = {
  text: string
  narrationMode: NarrationMode
  speechEnabled: boolean
  autoPlay: boolean
}

type NarrationState = {
  isNarrating: boolean
  isPreparing: boolean
  replay: () => void
  stop: () => void
}

export function useNarration({ text, narrationMode, speechEnabled, autoPlay }: UseNarrationOptions): NarrationState {
  const [isNarrating, setIsNarrating] = useState(false)
  const [isPreparing, setIsPreparing] = useState(false)
  const audioRef = useRef<HTMLAudioElement | null>(null)
  const audioUrlRef = useRef<string | null>(null)
  const requestRef = useRef(0)
  const { speak, stop } = useSpeak({ onStart: () => setIsNarrating(true), onStop: () => setIsNarrating(false) })
  const { voices } = useVoices()
  const greekVoice = voices.find((voice) => voice.lang.toLowerCase().startsWith('el'))

  const stopNarration = useCallback(() => {
    requestRef.current += 1
    audioRef.current?.pause()
    audioRef.current = null
    if (audioUrlRef.current) URL.revokeObjectURL(audioUrlRef.current)
    audioUrlRef.current = null
    stop()
    setIsNarrating(false)
    setIsPreparing(false)
  }, [stop])

  const narrate = useCallback(async () => {
    if (!speechEnabled || narrationMode === 'muted') return
    const request = ++requestRef.current
    audioRef.current?.pause()
    audioRef.current = null
    if (audioUrlRef.current) URL.revokeObjectURL(audioUrlRef.current)
    audioUrlRef.current = null
    stop()
    setIsNarrating(false)
    setIsPreparing(true)
    try {
      const piperStored = await isGreekVoiceStored()
      if (request !== requestRef.current) return
      if (piperStored) {
        const wav = await getGreekVoiceAudio(text, true)
        if (request !== requestRef.current) return
        const url = URL.createObjectURL(wav)
        audioUrlRef.current = url
        const audio = new Audio(url)
        audioRef.current = audio
        audio.onended = () => {
          if (request === requestRef.current) {
            setIsNarrating(false)
            setIsPreparing(false)
          }
        }
        await audio.play()
        if (request === requestRef.current) {
          setIsNarrating(true)
          setIsPreparing(false)
        }
        return
      }
      if (greekVoice) {
        speak(text, { lang: 'el-GR', rate: 0.9, voiceURI: greekVoice.voiceURI })
        setIsPreparing(false)
        return
      }
      setIsPreparing(false)
    } catch {
      if (request === requestRef.current) {
        setIsNarrating(false)
        setIsPreparing(false)
      }
    }
  }, [greekVoice, narrationMode, speechEnabled, speak, stop, text])

  useEffect(() => {
    if (autoPlay) void narrate()
    return stopNarration
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [autoPlay, text])

  useEffect(() => {
    return () => {
      requestRef.current += 1
      audioRef.current?.pause()
      audioRef.current = null
      if (audioUrlRef.current) URL.revokeObjectURL(audioUrlRef.current)
      audioUrlRef.current = null
    }
  }, [])

  useEffect(() => {
    function pauseWhenHidden() {
      if (document.visibilityState !== 'hidden') return
      stopNarration()
    }
    document.addEventListener('visibilitychange', pauseWhenHidden)
    return () => document.removeEventListener('visibilitychange', pauseWhenHidden)
  }, [stopNarration])

  return { isNarrating, isPreparing, replay: narrate, stop: stopNarration }
}

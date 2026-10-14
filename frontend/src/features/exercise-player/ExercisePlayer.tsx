import { useEffect, useRef, useState } from 'react'
import { useSpeak, useVoices } from 'react-text-to-speech'
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition'
import type { Exercise } from '../../domain/exercise'
import type { ChildHelper as ChildHelperType } from '../../domain/preferences'
import { ChildHelper } from '../../components/child-helper/ChildHelper'
import { getExerciseSpokenText, getGreekVoiceAudio, isGreekVoiceStored } from '../../domain/greek-voice'
import { matchSpokenOption } from '../../domain/speech'
import { fetchVoiceRssAudio, isVoiceRssConfigured } from '../../domain/voicerss-tts'

type ExercisePlayerProps = {
  exercise: Exercise
  progress: { current: number; total: number } | null
  selectedOptionId: string | null
  isSubmitted: boolean
  feedback: string | null
  isCorrect: boolean | null
  storyFrameDurationMs: number
  speechEnabled: boolean
  helper: ChildHelperType
  onSelect: (optionId: string) => void
  onSubmit: () => void
  onComplete: () => void
}

export function ExercisePlayer({ exercise, progress, selectedOptionId, isSubmitted, feedback, isCorrect, storyFrameDurationMs, speechEnabled, helper, onSelect, onSubmit, onComplete }: ExercisePlayerProps) {
  const [showHint, setShowHint] = useState(false)
  const [frameIndex, setFrameIndex] = useState(0)
  const [voiceMessage, setVoiceMessage] = useState('')
  const [waitingForVoiceAnswer, setWaitingForVoiceAnswer] = useState(false)
  const [isLoadingAudio, setIsLoadingAudio] = useState(false)
  const [isSpeaking, setIsSpeaking] = useState(false)
  const { speak, stop } = useSpeak()
  const { voices } = useVoices()
  const { browserSupportsSpeechRecognition, finalTranscript, isMicrophoneAvailable, listening, resetTranscript } = useSpeechRecognition()

  const onlineAudioRef = useRef<HTMLAudioElement | null>(null)
  const audioUrlRef = useRef<string | null>(null)
  const audioRequestRef = useRef(0)
  const frames = exercise.storyFrames ?? []
  const storyComplete = frames.length === 0 || frameIndex >= frames.length
  const currentFrame = frames.length > 0 ? frames[Math.min(frameIndex, frames.length - 1)] : undefined
  const greekVoice = voices.find((voice) => voice.lang.toLowerCase().startsWith('el'))

  useEffect(() => {
    return () => {
      audioRequestRef.current += 1
      onlineAudioRef.current?.pause()
      if (audioUrlRef.current) URL.revokeObjectURL(audioUrlRef.current)
    }
  }, [])

  const stopRef = useRef(stop)
  stopRef.current = stop

  useEffect(() => {
    return () => {
      stopRef.current()
    }
  }, [])

  useEffect(() => {
    return () => {
      audioRequestRef.current += 1
      onlineAudioRef.current?.pause()
      onlineAudioRef.current = null
      if (audioUrlRef.current) URL.revokeObjectURL(audioUrlRef.current)
      audioUrlRef.current = null
    }
  }, [exercise.id, frameIndex])

  useEffect(() => {
    setIsLoadingAudio(false)
    setVoiceMessage('')
  }, [exercise.id, frameIndex])

  useEffect(() => {
    if (speechEnabled) void speakText()
  }, [exercise.id])

  useEffect(() => {
    if (!speechEnabled || !currentFrame || storyComplete) return
    void speakText()
  }, [frameIndex])

  useEffect(() => {
    if (!currentFrame || storyComplete) return
    if (speechEnabled && isSpeaking) return
    const timer = setTimeout(() => setFrameIndex((index) => index + 1), storyFrameDurationMs)
    return () => clearTimeout(timer)
  }, [currentFrame, storyComplete, frameIndex, storyFrameDurationMs, isSpeaking, speechEnabled])

  useEffect(() => {
    if (!waitingForVoiceAnswer || !finalTranscript) return
    SpeechRecognition.stopListening()
    const optionId = matchSpokenOption(finalTranscript, exercise.options)
    if (optionId) {
      onSelect(optionId)
      setVoiceMessage(`Άκουσα: ${finalTranscript}. Πάτησε «Έλεγξε την απάντηση» για επιβεβαίωση.`)
    } else {
      setVoiceMessage(`Δεν κατάλαβα την απάντηση «${finalTranscript}». Δοκίμασε ξανά ή πάτησε μία επιλογή.`)
    }
    setWaitingForVoiceAnswer(false)
  }, [exercise.options, finalTranscript, onSelect, waitingForVoiceAnswer])

  function listenForAnswer() {
    if (!browserSupportsSpeechRecognition) {
      setVoiceMessage('Η αναγνώριση φωνής δεν υποστηρίζεται εδώ. Διάλεξε απάντηση με το χέρι.')
      return
    }
    if (!isMicrophoneAvailable) {
      setVoiceMessage('Το μικρόφωνο δεν είναι διαθέσιμο. Διάλεξε απάντηση με το χέρι.')
      return
    }
    resetTranscript()
    setWaitingForVoiceAnswer(true)
    setVoiceMessage('Σε ακούω...')
    setTimeout(() => {
      SpeechRecognition.startListening({ language: 'el-GR', interimResults: true }).catch((error) => {
        console.log('error', error)
        setWaitingForVoiceAnswer(false)
        setVoiceMessage('Δεν ήταν δυνατή η αναγνώριση φωνής. Μπορείς να πατήσεις μία επιλογή.')
      })
    }, 150)
  }

  async function speakText() {
    if (!speechEnabled) return
    const request = ++audioRequestRef.current
    setIsSpeaking(Boolean(speechEnabled && currentFrame))
    onlineAudioRef.current?.pause()
    if (audioUrlRef.current) URL.revokeObjectURL(audioUrlRef.current)
    audioUrlRef.current = null
    onlineAudioRef.current = null
    stop()
    setVoiceMessage('')
    if (greekVoice) {
      speak(spokenText, { lang: 'el-GR', rate: 0.9, voiceURI: greekVoice.voiceURI })
      setIsSpeaking(false)
      return
    }

    setIsLoadingAudio(true)
    setVoiceMessage('Ετοιμάζω την ελληνική φωνή...')
    try {
      if (!await isGreekVoiceStored() && request === audioRequestRef.current) {
        setVoiceMessage('Η πρώτη χρήση χρειάζεται λήψη περίπου 63 MB. Ετοιμάζω την ελληνική φωνή...')
      }
      const wav = await getGreekVoiceAudio(spokenText, true)

      if (request !== audioRequestRef.current) return
      const url = URL.createObjectURL(wav)
      audioUrlRef.current = url
      const audio = new Audio(url)
      onlineAudioRef.current = audio
      await audio.play()
      if (request === audioRequestRef.current) setVoiceMessage('')
      if (request === audioRequestRef.current) setIsSpeaking(false)
    } catch {
      if (request !== audioRequestRef.current) return
      if (isVoiceRssConfigured()) {
        const result = await fetchVoiceRssAudio(spokenText)
        if (request !== audioRequestRef.current) return
        if (result.ok) {
          const audio = new Audio(result.audioDataUrl)
          onlineAudioRef.current = audio
          try {
            await audio.play()
            setVoiceMessage('')
            setIsSpeaking(false)
            return
          } catch {
            // Keep the readable text available when playback is blocked.
          }
        }
      }
      setVoiceMessage('Δεν ήταν δυνατή η αναπαραγωγή ήχου αυτή τη στιγμή. Μπορείς να διαβάσεις το κείμενο.')
      setIsSpeaking(false)
    } finally {
      if (request === audioRequestRef.current) setIsLoadingAudio(false)
    }
  }

  function stopAudio() {
    audioRequestRef.current += 1
    setIsLoadingAudio(false)
    setIsSpeaking(false)
    stop()
    SpeechRecognition.abortListening()
    onlineAudioRef.current?.pause()
    onlineAudioRef.current = null
    if (audioUrlRef.current) URL.revokeObjectURL(audioUrlRef.current)
    audioUrlRef.current = null
    setVoiceMessage('')
    setWaitingForVoiceAnswer(false)
  }

  const spokenText = currentFrame?.text ?? getExerciseSpokenText(exercise)

  return (
    <section className="page-section player-section" aria-labelledby="exercise-title">
      <div className="player-topline">
        <span className="step-label">Αποστολή {progress?.current ?? 1} / {progress?.total ?? 1}</span>
        <span className="category-pill">{exercise.category}</span>
      </div>
      <div className="progress-track" aria-label="Πρόοδος αποστολών"><span style={{ width: `${((progress?.current ?? 1) / (progress?.total ?? 1)) * 100}%` }} /></div>
      <ChildHelper helper={helper} message={isSubmitted
        ? isCorrect ? 'Το σκέφτηκες πολύ καλά! Ετοιμάσου για την επόμενη αποστολή.' : 'Δεν πειράζει! Κάθε δοκιμή μάς βοηθά να μάθουμε.'
        : storyComplete ? 'Κοίτα προσεκτικά και διάλεξε ό,τι σου φαίνεται σωστό.' : 'Ας δούμε μαζί την ιστορία. Δεν χρειάζεται να βιαστείς!'} />
      <div className="player-layout">
        <div className="story-panel">
          <div className="story-badge" aria-hidden="true">✦</div>
          <p className="eyebrow">{frames.length ? 'Η ιστορία' : 'Η αποστολή'}</p>
          <h1 id="exercise-title">{exercise.title}</h1>
          {currentFrame ? (
            <div className="story-frame">
              <p className="frame-count">Εικόνα {Math.min(frameIndex + 1, frames.length)} από {frames.length}</p>
              <img src={currentFrame.imagePath} alt={currentFrame.text} />
              <p>{currentFrame.text}</p>
              {!storyComplete && <div className="frame-auto-advance" aria-hidden="true"><span key={frameIndex} style={{ animationDuration: `${storyFrameDurationMs}ms` }} /></div>}
                {!storyComplete && <button className="secondary-button" type="button" disabled={speechEnabled && isSpeaking} onClick={() => setFrameIndex((index) => index + 1)}>
                {frameIndex === frames.length - 1 ? 'Στην ερώτηση' : 'Επόμενη εικόνα'} <span aria-hidden="true">→</span>
              </button>}
            </div>
          ) : (
            <>
              <div className="story-text"><p>{exercise.instructions}</p></div>
              {exercise.imagePath && <div className="exercise-media"><img src={exercise.imagePath} alt={`Εικόνα για την άσκηση ${exercise.title}`} /></div>}
            </>
          )}
          {speechEnabled && <div className="voice-actions">
            <button className="hint-button" type="button" onClick={speakText} disabled={isLoadingAudio}>{isLoadingAudio ? 'Φόρτωση ήχου...' : 'Άκουσε το κείμενο'}</button>
            <button className="hint-button" type="button" onClick={stopAudio}>Σταμάτα τον ήχο</button>
          </div>}
          {storyComplete && <button className="hint-button" type="button" onClick={() => setShowHint((visible) => !visible)} aria-expanded={showHint}>☼ {showHint ? 'Κρύψε τη βοήθεια' : 'Θέλεις ένα στοιχείο;'}</button>}
          {showHint && <p className="hint">Μπορείς να το κάνεις με τον δικό σου ρυθμό. {exercise.instructions}</p>}
        </div>
        {storyComplete && <div className="question-panel">
          <p className="eyebrow">Η ερώτηση</p>
          <h2>{exercise.question}</h2>
          <div className="answer-list" role="radiogroup" aria-label="Επιλογές απάντησης">
            {exercise.options.map((option) => {
              const isSelected = selectedOptionId === option.id
              return (
                <button className={`answer-option${isSelected ? ' selected' : ''}`} type="button" role="radio" aria-checked={isSelected} disabled={isSubmitted} key={option.id} onClick={() => onSelect(option.id)}>
                  <span className="option-number">{option.label}</span>
                  {option.imagePath && <img className="option-image" src={option.imagePath} alt="" />}
                  <span>{option.detail}</span>
                  <span className="option-check" aria-hidden="true">{isSelected ? '●' : '○'}</span>
                </button>
              )
            })}
          </div>
          {!isSubmitted ? (
            <>
              <button className="hint-button" type="button" onClick={listenForAnswer}>{listening ? 'Σε ακούω...' : 'Απάντησε με τη φωνή σου'}</button>
              <button className="primary-button full-width" type="button" disabled={!selectedOptionId} onClick={onSubmit}>Έλεγξε την απάντηση <span aria-hidden="true">→</span></button>
            </>
          ) : (
            <div className={`feedback ${isCorrect ? 'feedback-correct' : 'feedback-try'}`} role="status">
              <span className="feedback-icon" aria-hidden="true">{isCorrect ? '✓' : '!'}</span>
              <p>{feedback}</p>
              <button className="primary-button full-width" type="button" onClick={onComplete}>Συνέχισε <span aria-hidden="true">→</span></button>
            </div>
          )}
        </div>}
      </div>
      {voiceMessage && <p className="voice-message" role="status">{voiceMessage}</p>}
    </section>
  )
}

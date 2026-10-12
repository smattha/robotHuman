import { useEffect, useRef, useState } from 'react'
import { useSpeak, useVoices } from 'react-text-to-speech'
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition'
import type { Exercise } from '../../domain/exercise'
import { matchSpokenOption } from '../../domain/speech'
import { fetchVoiceRssAudio, isVoiceRssConfigured } from '../../domain/voicerss-tts'

type ExercisePlayerProps = {
  exercise: Exercise
  progress: { current: number; total: number } | null
  selectedOptionId: string | null
  isSubmitted: boolean
  feedback: string | null
  isCorrect: boolean | null
  onSelect: (optionId: string) => void
  onSubmit: () => void
  onComplete: () => void
}

export function ExercisePlayer({ exercise, progress, selectedOptionId, isSubmitted, feedback, isCorrect, onSelect, onSubmit, onComplete }: ExercisePlayerProps) {
  const [showHint, setShowHint] = useState(false)
  const [frameIndex, setFrameIndex] = useState(0)
  const [voiceMessage, setVoiceMessage] = useState('')
  const [waitingForVoiceAnswer, setWaitingForVoiceAnswer] = useState(false)
  const [isFetchingOnlineAudio, setIsFetchingOnlineAudio] = useState(false)
  const { speak, stop } = useSpeak()
  const { voices } = useVoices()
  const { browserSupportsSpeechRecognition, finalTranscript, isMicrophoneAvailable, listening, resetTranscript } = useSpeechRecognition()
  const onlineAudioRef = useRef<HTMLAudioElement | null>(null)
  const frames = exercise.storyFrames ?? []
  const storyComplete = frames.length === 0 || frameIndex >= frames.length
  const currentFrame = frames.length > 0 ? frames[Math.min(frameIndex, frames.length - 1)] : undefined
  const greekVoice = voices.find((voice) => voice.lang.toLowerCase().startsWith('el'))

  useEffect(() => {
    return () => {
      stop()
      SpeechRecognition.abortListening()
      onlineAudioRef.current?.pause()
    }
  }, [stop])

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
    SpeechRecognition.startListening({ language: 'el-GR', interimResults: false }).catch(() => {
      setWaitingForVoiceAnswer(false)
      setVoiceMessage('Δεν ήταν δυνατή η αναγνώριση φωνής. Μπορείς να πατήσεις μία επιλογή.')
    })
  }

  async function speakText() {
    onlineAudioRef.current?.pause()
    stop()
    if (greekVoice) {
      speak(spokenText, { lang: 'el-GR', rate: 0.9, voiceURI: greekVoice.voiceURI })
      return
    }
    if (!isVoiceRssConfigured()) {
      speak(spokenText, { lang: 'el-GR', rate: 0.9 })
      return
    }
    setIsFetchingOnlineAudio(true)
    setVoiceMessage('')
    const result = await fetchVoiceRssAudio(spokenText)
    setIsFetchingOnlineAudio(false)
    if (!result.ok) {
      setVoiceMessage('Δεν ήταν δυνατή η αναπαραγωγή ήχου αυτή τη στιγμή. Μπορείς να διαβάσεις το κείμενο.')
      return
    }
    const audio = new Audio(result.audioDataUrl)
    onlineAudioRef.current = audio
    audio.play().catch(() => setVoiceMessage('Δεν ήταν δυνατή η αναπαραγωγή ήχου αυτή τη στιγμή. Μπορείς να διαβάσεις το κείμενο.'))
  }

  function stopAudio() {
    stop()
    SpeechRecognition.abortListening()
    onlineAudioRef.current?.pause()
    setWaitingForVoiceAnswer(false)
  }

  const spokenText = currentFrame?.text ?? `${exercise.instructions} ${exercise.question} ${exercise.options.map((option) => `${option.label}: ${option.detail}`).join('. ')}`

  return (
    <section className="page-section player-section" aria-labelledby="exercise-title">
      <div className="player-topline">
        <span className="step-label">Αποστολή {progress?.current ?? 1} / {progress?.total ?? 1}</span>
        <span className="category-pill">{exercise.category}</span>
      </div>
      <div className="progress-track" aria-label="Πρόοδος αποστολών"><span style={{ width: `${((progress?.current ?? 1) / (progress?.total ?? 1)) * 100}%` }} /></div>
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
              {!storyComplete && <button className="secondary-button" type="button" onClick={() => setFrameIndex((index) => index + 1)}>
                {frameIndex === frames.length - 1 ? 'Στην ερώτηση' : 'Επόμενη εικόνα'} <span aria-hidden="true">→</span>
              </button>}
            </div>
          ) : (
            <>
              <div className="story-text"><p>{exercise.instructions}</p></div>
              {exercise.imagePath && <div className="exercise-media"><img src={exercise.imagePath} alt={`Εικόνα για την άσκηση ${exercise.title}`} /></div>}
            </>
          )}
          <div className="voice-actions">
            <button className="hint-button" type="button" onClick={speakText} disabled={isFetchingOnlineAudio}>{isFetchingOnlineAudio ? 'Φόρτωση ήχου...' : 'Άκουσε το κείμενο'}</button>
            <button className="hint-button" type="button" onClick={stopAudio}>Σταμάτα τον ήχο</button>
          </div>
          {storyComplete && <button className="hint-button" type="button" onClick={() => setShowHint((visible) => !visible)} aria-expanded={showHint}>☼ {showHint ? 'Κρύψε τη βοήθεια' : 'Χρειάζεσαι βοήθεια;'}</button>}
          {showHint && <p className="hint">Ξαναδιάβασε προσεκτικά: {exercise.instructions}</p>}
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
              {voiceMessage && <p className="voice-message" role="status">{voiceMessage}</p>}
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
    </section>
  )
}

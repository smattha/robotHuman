import { useEffect } from 'react'
import type { StoryExercise as StoryExerciseModel } from '../../../domain/exercise-model'
import type { NarrationMode, StorySpeed } from '../../../domain/preferences'
import { getStoryFrameDuration } from '../../../domain/preferences'
import type { ReportedRuntimeState } from '../engine/useExerciseEngine'
import { useStoryPlayback } from '../../../hooks/use-story-playback'
import { AnswerGrid } from '../components/AnswerGrid'

type StoryExerciseProps = {
  exercise: StoryExerciseModel
  selectedOptionId: string | null
  isSubmitted: boolean
  narrationMode: NarrationMode
  speechEnabled: boolean
  storySpeed: StorySpeed
  onAnswer: (optionId: string) => void
  onRuntimeState: (state: ReportedRuntimeState) => void
}

export function StoryExercise({ exercise, selectedOptionId, isSubmitted, narrationMode, speechEnabled, storySpeed, onAnswer, onRuntimeState }: StoryExerciseProps) {
  const question = exercise.questions[0]
  const { phase, frameIndex, currentFrame, isNarrating, isPreparing, replay, nextFrame } = useStoryPlayback({
    frames: exercise.frames,
    questionText: question.text,
    storySpeed,
    narrationMode,
    speechEnabled,
    enabled: !isSubmitted,
  })

  useEffect(() => {
    onRuntimeState({ isNarrating, isPreparing, phase, frameIndex })
  }, [isNarrating, isPreparing, phase, frameIndex, onRuntimeState])

  const frameDuration = getStoryFrameDuration(storySpeed)
  const isLastFrame = frameIndex >= exercise.frames.length - 1

  if (phase === 'playing' && currentFrame) {
    return (
      <div className="story-panel">
        <p className="eyebrow">Η ιστορία</p>
        <div className="story-frame" key={frameIndex}>
          <img src={currentFrame.imagePath} alt={`Εικόνα ${frameIndex + 1} της ιστορίας ${exercise.title}`} />
          <p>{currentFrame.text}</p>
          <span className="frame-count">{frameIndex + 1} / {exercise.frames.length}</span>
        </div>
        <div className="frame-auto-advance" aria-hidden="true"><span key={frameIndex} style={{ animationDuration: `${frameDuration}ms` }} /></div>
        <div className="player-action-bar">
          <button className="secondary-button" type="button" onClick={nextFrame}>
            {isLastFrame ? 'Στην ερώτηση' : 'Επόμενη εικόνα'}
          </button>
          <button className="hint-button replay-button" type="button" onClick={() => void replay()} aria-label="Άκουσε ξανά">
            {isPreparing ? 'Ετοιμάζω τον ήχο...' : '🔊 Άκουσε ξανά'}
          </button>
        </div>
      </div>
    )
  }

  return (
    <div className="question-panel">
      <p className="eyebrow">Η ερώτηση</p>
      <h2 id="exercise-title">{question.text}</h2>
      <AnswerGrid options={question.options} selectedOptionId={selectedOptionId} isSubmitted={isSubmitted} onAnswer={onAnswer} />
      <div className="player-action-bar">
        {!isSubmitted && (
          <button className="hint-button replay-button" type="button" onClick={() => void replay()} aria-label="Άκουσε ξανά την ερώτηση">
            {isPreparing ? 'Ετοιμάζω τον ήχο...' : '🔊 Άκουσε ξανά'}
          </button>
        )}
      </div>
    </div>
  )
}

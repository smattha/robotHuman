import { useEffect } from 'react'
import type { ImageQuestionExercise } from '../../../domain/exercise-model'
import type { NarrationMode } from '../../../domain/preferences'
import type { ReportedRuntimeState } from '../engine/useExerciseEngine'
import { useNarration } from '../../../hooks/use-narration'
import { AnswerGrid } from '../components/AnswerGrid'

type ImageQuestionProps = {
  exercise: ImageQuestionExercise
  selectedOptionId: string | null
  isSubmitted: boolean
  narrationMode: NarrationMode
  speechEnabled: boolean
  onAnswer: (optionId: string) => void
  onRuntimeState: (state: ReportedRuntimeState) => void
}

export function ImageQuestion({ exercise, selectedOptionId, isSubmitted, narrationMode, speechEnabled, onAnswer, onRuntimeState }: ImageQuestionProps) {
  const question = exercise.question
  const narrationText = `${exercise.instructions} ${question.text}`
  const { isNarrating, isPreparing, replay } = useNarration({
    text: narrationText,
    narrationMode,
    speechEnabled,
    autoPlay: narrationMode === 'auto' && !isSubmitted,
  })

  useEffect(() => {
    onRuntimeState({ isNarrating, isPreparing, phase: 'question', frameIndex: null })
  }, [isNarrating, isPreparing, onRuntimeState])

  return (
    <div className={`question-panel${exercise.imagePath ? ' question-panel-with-reference' : ''}`}>
      <p className="eyebrow">Η ερώτηση</p>
      <h2 id="exercise-title">{question.text}</h2>
      {exercise.imagePath && <div className="question-reference"><img src={exercise.imagePath} alt={`Εικόνα για την άσκηση ${exercise.title}`} /></div>}
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

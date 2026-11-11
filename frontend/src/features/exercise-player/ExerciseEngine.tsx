import type { AnswerEvaluation, Exercise } from '../../domain/exercise'
import { categoryLabels } from '../../domain/exercise'
import type { ChildHelper as ChildHelperType, NarrationMode, StorySpeed } from '../../domain/preferences'
import { ChildHelper } from '../../components/child-helper/ChildHelper'
import { Confetti } from '../../components/confetti/Confetti'
import type { ExerciseEngineState } from './engine/useExerciseEngine'
import { useExerciseEngine } from './engine/useExerciseEngine'
import { ExerciseProgress } from './components/ExerciseProgress'
import { ExerciseRenderer } from './ExerciseRenderer'

type ExerciseEngineProps = {
  exercise: Exercise
  progress: { current: number; total: number } | null
  narrationMode: NarrationMode
  speechEnabled: boolean
  storySpeed: StorySpeed
  helper: ChildHelperType
  userName: string | null
  testMode: boolean
  onAnswer: (optionId: string, evaluation: AnswerEvaluation) => void
  onComplete: () => void
  onStateChange?: (state: ExerciseEngineState) => void
}

export function ExerciseEngine({ exercise, progress, narrationMode, speechEnabled, storySpeed, helper, userName, testMode, onAnswer, onComplete, onStateChange }: ExerciseEngineProps) {
  const { state, selectedOptionId, isSubmitted, feedback, isCorrect, celebrate, handleAnswer, onRuntimeState } = useExerciseEngine({ exercise, onAnswer, onComplete, onStateChange })

  const helperMessage = isSubmitted
    ? isCorrect ? 'Το σκέφτηκες πολύ καλά! Ετοιμάσου για την επόμενη.' : 'Δεν πειράζει! Κάθε δοκιμή μάς βοηθά να μάθουμε.'
    : state.isPreparing ? 'Άκουσε προσεκτικά...' : 'Κοίτα προσεκτικά και διάλεξε ό,τι σου φαίνεται σωστό.'

  return (
    <section className="page-section player-section" aria-labelledby="exercise-title">
      <Confetti trigger={celebrate} />
      <div className="player-topline">
        <span className="step-label">Αποστολή {progress?.current ?? 1} / {progress?.total ?? 1}</span>
        <span className="category-pill">{categoryLabels[exercise.category]}</span>
      </div>
      {userName && !testMode && <p className="player-greeting">Γεια σου, {userName}!</p>}
      {testMode && <p className="test-mode-banner" role="status">Δοκιμή: τίποτα δεν αποθηκεύεται</p>}
      {progress && <ExerciseProgress current={progress.current} total={progress.total} />}
      <ChildHelper helper={helper} playing={state.isNarrating} message={helperMessage} />
      <div className="player-body">
        <ExerciseRenderer
          exercise={exercise}
          selectedOptionId={selectedOptionId}
          isSubmitted={isSubmitted}
          narrationMode={narrationMode}
          speechEnabled={speechEnabled}
          storySpeed={storySpeed}
          onAnswer={handleAnswer}
          onRuntimeState={onRuntimeState}
        />
        {isSubmitted && (
          <div className={`feedback ${isCorrect ? 'feedback-correct' : 'feedback-try'}`} role="status">
            <span className="feedback-icon" aria-hidden="true">{isCorrect ? '✓' : '!'}</span>
            <p>{feedback}</p>
          </div>
        )}
      </div>
    </section>
  )
}

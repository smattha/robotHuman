import type { Exercise } from '../../domain/exercise'
import { isStory } from '../../domain/exercise'
import type { NarrationMode, StorySpeed } from '../../domain/preferences'
import type { ReportedRuntimeState } from './engine/useExerciseEngine'
import { ImageQuestion } from './templates/ImageQuestion'
import { StoryExercise } from './templates/StoryExercise'

type ExerciseRendererProps = {
  exercise: Exercise
  selectedOptionId: string | null
  isSubmitted: boolean
  narrationMode: NarrationMode
  speechEnabled: boolean
  storySpeed: StorySpeed
  onAnswer: (optionId: string) => void
  onRuntimeState: (state: ReportedRuntimeState) => void
}

export function ExerciseRenderer({ exercise, selectedOptionId, isSubmitted, narrationMode, speechEnabled, storySpeed, onAnswer, onRuntimeState }: ExerciseRendererProps) {
  if (isStory(exercise)) {
    return (
      <StoryExercise
        exercise={exercise}
        selectedOptionId={selectedOptionId}
        isSubmitted={isSubmitted}
        narrationMode={narrationMode}
        speechEnabled={speechEnabled}
        storySpeed={storySpeed}
        onAnswer={onAnswer}
        onRuntimeState={onRuntimeState}
      />
    )
  }

  return (
    <ImageQuestion
      exercise={exercise}
      selectedOptionId={selectedOptionId}
      isSubmitted={isSubmitted}
      narrationMode={narrationMode}
      speechEnabled={speechEnabled}
      onAnswer={onAnswer}
      onRuntimeState={onRuntimeState}
    />
  )
}

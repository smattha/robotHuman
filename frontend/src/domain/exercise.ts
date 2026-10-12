export type AnswerOption = {
  id: string
  label: string
  detail: string
  imagePath?: string
}

export type StoryFrame = {
  imagePath: string
  text: string
}

export type Exercise = {
  id: string
  title: string
  category: string
  description: string
  instructions: string
  question: string
  options: AnswerOption[]
  correctOptionId: string
  correctFeedback: string
  incorrectFeedback: string
  imagePath?: string
  storyFrames?: StoryFrame[]
}

export type AnswerEvaluation = {
  isCorrect: boolean
  feedback: string
}

export function evaluateAnswer(exercise: Exercise, optionId: string): AnswerEvaluation {
  const isCorrect = exercise.correctOptionId === optionId

  return {
    isCorrect,
    feedback: isCorrect ? exercise.correctFeedback : exercise.incorrectFeedback,
  }
}

export function validateExercise(exercise: Exercise): void {
  if (!exercise.id || !exercise.title || exercise.options.length === 0) {
    throw new Error(`Invalid exercise definition: ${exercise.id || 'missing id'}`)
  }

  if (!exercise.options.some((option) => option.id === exercise.correctOptionId)) {
    throw new Error(`Correct answer is not available for exercise: ${exercise.id}`)
  }
}

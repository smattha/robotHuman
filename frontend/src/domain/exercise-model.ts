export type ExerciseCategory =
  | 'math-quantitative'
  | 'observation-attention'
  | 'story-comprehension'
  | 'vocabulary-image'

export type SkillTag =
  | 'counting'
  | 'subtraction'
  | 'spatial-matching'
  | 'false-belief'
  | 'deception'
  | 'emotion-recognition'
  | 'image-recognition'

export const EXERCISE_CATEGORIES: readonly ExerciseCategory[] = [
  'math-quantitative',
  'observation-attention',
  'story-comprehension',
  'vocabulary-image',
] as const

export const categoryLabels: Record<ExerciseCategory, string> = {
  'math-quantitative': 'Μικροί γρίφοι',
  'observation-attention': 'Παρατήρηση',
  'story-comprehension': 'Ιστορίες',
  'vocabulary-image': 'Λέξεις και εικόνες',
}

export type AnswerOption = {
  id: string
  label: string
  detail: string
  imagePath?: string
}

export type Question = {
  id: string
  text: string
  options: AnswerOption[]
  correctOptionId: string
  correctFeedback: string
  incorrectFeedback: string
}

export type StoryFrame = {
  id: string
  imagePath: string
  text: string
}

type ExerciseBase = {
  id: string
  position: number
  title: string
  category: ExerciseCategory
  skillTags: SkillTag[]
  description: string
  instructions: string
}

export type ImageQuestionExercise = ExerciseBase & {
  type: 'image-question'
  imagePath?: string
  question: Question
}

export type StoryExercise = ExerciseBase & {
  type: 'story'
  frames: StoryFrame[]
  questions: Question[]
}

export type Exercise = ImageQuestionExercise | StoryExercise

export type AnswerEvaluation = {
  isCorrect: boolean
  feedback: string
}

export function isImageQuestion(exercise: Exercise): exercise is ImageQuestionExercise {
  return exercise.type === 'image-question'
}

export function isStory(exercise: Exercise): exercise is StoryExercise {
  return exercise.type === 'story'
}

export function getPrimaryQuestion(exercise: Exercise): Question {
  return isStory(exercise) ? exercise.questions[0] : exercise.question
}

export function getStoryFrames(exercise: Exercise): StoryFrame[] {
  return isStory(exercise) ? exercise.frames : []
}

export function evaluateQuestion(question: Question, optionId: string): AnswerEvaluation {
  const isCorrect = question.correctOptionId === optionId
  return {
    isCorrect,
    feedback: isCorrect ? question.correctFeedback : question.incorrectFeedback,
  }
}

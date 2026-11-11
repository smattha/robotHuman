import type { AnswerOption, Exercise, Question } from './exercise-model'
import { EXERCISE_CATEGORIES, isStory } from './exercise-model'

const MIN_OPTIONS = 2
const MAX_OPTIONS = 5
const MIN_STORY_FRAMES = 2

function validateQuestion(question: Question, exerciseId: string, problems: string[]): void {
  if (!question.id) problems.push(`${exerciseId}: question is missing an id`)
  if (!question.text) problems.push(`${exerciseId}/${question.id}: question is missing text`)

  if (question.options.length < MIN_OPTIONS || question.options.length > MAX_OPTIONS) {
    problems.push(`${exerciseId}/${question.id}: expected ${MIN_OPTIONS}-${MAX_OPTIONS} options, found ${question.options.length}`)
  }

  const optionIds = new Set<string>()
  for (const option of question.options) {
    if (!option.id) {
      problems.push(`${exerciseId}/${question.id}: an option is missing an id`)
      continue
    }
    if (optionIds.has(option.id)) problems.push(`${exerciseId}/${question.id}: duplicate option id "${option.id}"`)
    optionIds.add(option.id)
    if (!option.label) problems.push(`${exerciseId}/${question.id}/option ${option.id}: option is missing a label`)
    if (!option.detail) problems.push(`${exerciseId}/${question.id}/option ${option.id}: option is missing a detail`)
  }

  if (!question.options.some((option) => option.id === question.correctOptionId)) {
    problems.push(`${exerciseId}/${question.id}: correctOptionId "${question.correctOptionId}" does not match any option`)
  }

  if (!question.correctFeedback) problems.push(`${exerciseId}/${question.id}: question is missing correctFeedback`)
  if (!question.incorrectFeedback) problems.push(`${exerciseId}/${question.id}: question is missing incorrectFeedback`)
}

function validateOptionsHaveImages(options: AnswerOption[], where: string, problems: string[]): void {
  const hasAnyImage = options.some((option) => Boolean(option.imagePath))
  if (!hasAnyImage) return
  options.forEach((option) => {
    if (!option.imagePath) problems.push(`${where}/option ${option.id}: image is missing while other options have images`)
  })
}

export function validateExercise(exercise: Exercise): string[] {
  const problems: string[] = []

  if (!exercise.id) problems.push('exercise is missing an id')
  if (!exercise.title) problems.push(`${exercise.id}: exercise is missing a title`)
  if (!EXERCISE_CATEGORIES.includes(exercise.category)) {
    problems.push(`${exercise.id}: unknown category "${String(exercise.category)}"`)
  }
  if (exercise.skillTags.length === 0) problems.push(`${exercise.id}: exercise has no skill tags`)

  if (isStory(exercise)) {
    if (exercise.frames.length < MIN_STORY_FRAMES) {
      problems.push(`${exercise.id}: expected at least ${MIN_STORY_FRAMES} story frames, found ${exercise.frames.length}`)
    }
    const frameIds = new Set<string>()
    exercise.frames.forEach((frame) => {
      if (!frame.id) problems.push(`${exercise.id}: a story frame is missing an id`)
      if (frameIds.has(frame.id)) problems.push(`${exercise.id}: duplicate story frame id "${frame.id}"`)
      frameIds.add(frame.id)
      if (!frame.imagePath) problems.push(`${exercise.id}/frame ${frame.id}: story frame is missing an image`)
      if (!frame.text) problems.push(`${exercise.id}/frame ${frame.id}: story frame is missing text`)
    })
    if (exercise.questions.length === 0) problems.push(`${exercise.id}: story has no questions`)
    exercise.questions.forEach((question) => validateQuestion(question, exercise.id, problems))
  } else {
    validateQuestion(exercise.question, exercise.id, problems)
    validateOptionsHaveImages(exercise.question.options, `${exercise.id}/${exercise.question.id}`, problems)
  }

  return problems
}

export function validateExercises(exercises: Exercise[]): string[] {
  const problems: string[] = []
  const seenIds = new Set<string>()
  exercises.forEach((exercise) => {
    if (seenIds.has(exercise.id)) problems.push(`duplicate exercise id "${exercise.id}"`)
    seenIds.add(exercise.id)
    problems.push(...validateExercise(exercise))
  })
  return problems
}

import { describe, expect, it } from 'vitest'
import { evaluateQuestion, getPrimaryQuestion, isImageQuestion, isStory, validateExercises, validateExercise } from './exercise'
import { exercises, firstExercise } from '../content/exercises'

describe('exercise domain', () => {
  it('evaluates the correct answer', () => {
    const question = getPrimaryQuestion(firstExercise)
    expect(evaluateQuestion(question, 'four')).toEqual({
      isCorrect: true,
      feedback: question.correctFeedback,
    })
  })

  it('returns encouraging feedback for an incorrect answer', () => {
    const question = getPrimaryQuestion(firstExercise)
    expect(evaluateQuestion(question, 'two')).toEqual({
      isCorrect: false,
      feedback: question.incorrectFeedback,
    })
  })

  it('validates every exercise definition without problems', () => {
    exercises.forEach((exercise) => expect(validateExercise(exercise)).toEqual([]))
    expect(validateExercises(exercises)).toEqual([])
  })

  it('contains all twelve exercises from the legacy application', () => {
    expect(exercises).toHaveLength(12)
  })

  it('assigns each exercise to one of the four categories with at least one skill tag', () => {
    const categories = new Set(exercises.map((exercise) => exercise.category))
    expect(categories).toEqual(new Set(['math-quantitative', 'observation-attention', 'story-comprehension', 'vocabulary-image']))
    exercises.forEach((exercise) => expect(exercise.skillTags.length).toBeGreaterThan(0))
  })

  it('splits the exercises into eight image-question and four story templates', () => {
    const stories = exercises.filter((exercise) => exercise.type === 'story')
    const imageQuestions = exercises.filter((exercise) => exercise.type === 'image-question')
    expect(stories).toHaveLength(4)
    expect(imageQuestions).toHaveLength(8)
    stories.forEach((exercise) => {
      if (isStory(exercise)) expect(exercise.frames.length).toBeGreaterThanOrEqual(2)
    })
  })

  it('maps supplied visual content without making it mandatory for every exercise', () => {
    const lion = exercises.find(({ id }) => id === 'lion-and-ducklings')
    expect(lion).toBeDefined()
    if (lion && isImageQuestion(lion)) expect(lion.imagePath).toBe('/ex1/main-image.png')
    if (lion && isImageQuestion(lion)) expect(lion.question.options.every((option) => Boolean(option.imagePath))).toBe(true)

    const george = exercises.find(({ id }) => id === 'george-and-chocolate')
    if (george && isStory(george)) expect(george.frames).toHaveLength(2)

    const maximos = exercises.find(({ id }) => id === 'maximos-paper')
    if (maximos && isImageQuestion(maximos)) expect(maximos.question.options[4].imagePath).toBe('/ex8/answer-e.png')

    const pigeons = exercises.find(({ id }) => id === 'grey-pigeons')
    if (pigeons && isImageQuestion(pigeons)) expect(pigeons.imagePath).toBe('/ex11/main-image.png')
  })

  it('evaluates the kangaroo weight riddle correctly', () => {
    const exercise = exercises.find(({ id }) => id === 'kangaroo-mother')
    expect(exercise).toBeDefined()
    expect(evaluateQuestion(getPrimaryQuestion(exercise!), 'eight').isCorrect).toBe(true)
  })
})

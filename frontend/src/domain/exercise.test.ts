import { describe, expect, it } from 'vitest'
import { evaluateAnswer, validateExercise } from './exercise'
import { exercises, firstExercise } from '../content/exercises'

describe('exercise domain', () => {
  it('evaluates the correct answer', () => {
    expect(evaluateAnswer(firstExercise, 'four')).toEqual({
      isCorrect: true,
      feedback: firstExercise.correctFeedback,
    })
  })

  it('returns encouraging feedback for an incorrect answer', () => {
    expect(evaluateAnswer(firstExercise, 'two')).toEqual({
      isCorrect: false,
      feedback: firstExercise.incorrectFeedback,
    })
  })

  it('validates the exercise definition', () => {
    expect(() => validateExercise(firstExercise)).not.toThrow()
  })

  it('contains all twelve exercises from the legacy application', () => {
    expect(exercises).toHaveLength(12)
    exercises.forEach((exercise) => expect(() => validateExercise(exercise)).not.toThrow())
  })

  it('maps supplied visual content without making it mandatory for every exercise', () => {
    expect(firstExercise.imagePath).toBe('/ex1/main-image.png')
    expect(exercises.find(({ id }) => id === 'george-and-chocolate')?.storyFrames).toHaveLength(2)
    expect(exercises[0].options.every((option) => Boolean(option.imagePath))).toBe(true)
    expect(exercises[1].options.every((option) => Boolean(option.imagePath))).toBe(true)
    expect(exercises.find(({ id }) => id === 'maximos-paper')?.options[4].imagePath).toBe('/ex8/answer-e.png')
    expect(exercises.find(({ id }) => id === 'grey-pigeons')?.imagePath).toBe('/ex11/main-image.png')
  })

  it('evaluates the kangaroo weight riddle correctly', () => {
    const exercise = exercises.find(({ id }) => id === 'kangaroo-mother')

    expect(exercise).toBeDefined()
    expect(evaluateAnswer(exercise!, 'eight').isCorrect).toBe(true)
  })
})

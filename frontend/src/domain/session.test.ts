import { describe, expect, it } from 'vitest'
import { initialSessionState, sessionReducer } from './session'

describe('sessionReducer', () => {
  it('moves from welcome to the exercise library', () => {
    expect(sessionReducer(initialSessionState, { type: 'START' })).toMatchObject({ screen: 'library' })
  })

  it('does not allow changing an answer after submission', () => {
    const submitted = sessionReducer(
      { ...initialSessionState, screen: 'exercise', selectedOptionId: 'four', evaluation: { isCorrect: true, feedback: 'Well done' } },
      { type: 'SELECT_OPTION', optionId: 'two' },
    )

    expect(submitted.selectedOptionId).toBe('four')
  })

  it('starts a named run and advances without carrying over the previous answer', () => {
    const started = sessionReducer(initialSessionState, { type: 'START_ALL', userName: 'Alex' })
    const answered = sessionReducer(started, { type: 'SELECT_OPTION', optionId: 'four' })
    const next = sessionReducer(answered, { type: 'NEXT_EXERCISE' })
    expect(next).toMatchObject({ mode: 'all', userName: 'Alex', exerciseIndex: 1, selectedOptionId: null, evaluation: null })
  })
})

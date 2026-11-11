import { describe, expect, it } from 'vitest'
import { initialSessionState, sessionReducer } from './session'

describe('sessionReducer', () => {
  it('moves from welcome to the exercise library', () => {
    expect(sessionReducer(initialSessionState, { type: 'START' })).toMatchObject({ screen: 'library' })
  })

  it('starts a named run and advances to the next exercise', () => {
    const started = sessionReducer(initialSessionState, { type: 'START_ALL', userName: 'Alex' })
    const next = sessionReducer(started, { type: 'NEXT_EXERCISE' })
    expect(next).toMatchObject({ mode: 'all', userName: 'Alex', exerciseIndex: 1 })
  })

  it('resumes an adventure from its saved mission', () => {
    const resumed = sessionReducer(initialSessionState, { type: 'RESUME_ALL', userName: 'Alex', exerciseIndex: 4 })
    expect(resumed).toMatchObject({ screen: 'exercise', mode: 'all', userName: 'Alex', exerciseIndex: 4 })
  })

  it('continues the next exercise after a break', () => {
    const stateAtBreak = {
      ...initialSessionState,
      screen: 'exercise' as const,
      mode: 'all' as const,
      exerciseIndex: 2,
    }
    const onBreak = sessionReducer(stateAtBreak, { type: 'TAKE_BREAK' })
    const continued = sessionReducer(onBreak, { type: 'CONTINUE_AFTER_BREAK' })
    expect(continued).toMatchObject({ screen: 'exercise', exerciseIndex: 3 })
  })
})

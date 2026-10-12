import { describe, expect, it } from 'vitest'
import { createDigitSpanState, enterDigit, startDigitSpan, submitDigitSpan, tickDigitSpan } from './digit-span-logic'

describe('Digit Span task logic', () => {
  it('accepts a correctly recalled sequence and increases its length', () => {
    const started = startDigitSpan(createDigitSpanState(), 100)
    let answered = tickDigitSpan(tickDigitSpan(started, 100), 1000)
    for (const digit of started.sequence) answered = enterDigit(answered, digit)
    const submitted = submitDigitSpan(answered, 1300)

    expect(submitted.phase).toBe('showing')
    expect(submitted.trials[0].isCorrect).toBe(true)
    expect(submitted.level).toBe(2)
    expect(submitted.maxSequenceLength).toBe(1)
  })

  it('finishes after two consecutive incorrect responses', () => {
    let state = createDigitSpanState()
    for (let attempt = 0; attempt < 2; attempt += 1) {
      state = startDigitSpan(state, attempt * 2000)
      state = tickDigitSpan(tickDigitSpan(state, state.nextStepAt), state.nextStepAt + 900)
      const incorrectDigit = state.sequence[0] === '1' ? '2' : '1'
      state = enterDigit(state, incorrectDigit)
      state = submitDigitSpan(state, state.answerStartedAt + 100)
    }

    expect(state.phase).toBe('finished')
    expect(state.consecutiveErrors).toBe(2)
    expect(state.trials).toHaveLength(2)
  })
})

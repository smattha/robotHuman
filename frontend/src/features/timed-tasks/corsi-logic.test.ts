import { describe, expect, it } from 'vitest'
import { createCorsiState, respondCorsi, startCorsi, tickCorsi } from './corsi-logic'

describe('Corsi task logic', () => {
  it('reveals a sequence then accepts its ordered reproduction', () => {
    const started = startCorsi(createCorsiState(), 0)
    const firstTile = started.sequence[0]
    let ready = started
    for (let index = 0; index <= started.sequence.length; index += 1) ready = tickCorsi(ready, ready.nextStepAt)
    expect(ready.phase).toBe('answering')

    const afterFirst = respondCorsi(ready, firstTile, 2300)
    expect(afterFirst.answer).toEqual([firstTile])
    let completed = afterFirst
    for (const tile of started.sequence.slice(1)) completed = respondCorsi(completed, tile, 2400)

    expect(completed.phase).toBe('showing')
    expect(completed.trials[0].isCorrect).toBe(true)
    expect(completed.maxSequenceLength).toBe(3)
    expect(completed.level).toBe(4)
  })

  it('finishes after two consecutive errors', () => {
    let state = startCorsi(createCorsiState(), 0)
    for (let attempt = 0; attempt < 2; attempt += 1) {
      for (let index = 0; index <= state.sequence.length; index += 1) state = tickCorsi(state, state.nextStepAt)
      const wrongTile = (state.sequence[0] + 1) % 9
      state = respondCorsi(state, wrongTile, state.answerStartedAt + 100)
      if (attempt === 0) {
        for (let index = 0; index <= state.sequence.length; index += 1) state = tickCorsi(state, state.nextStepAt)
      }
    }
    expect(state.phase).toBe('finished')
    expect(state.totalErrors).toBe(2)
  })
})

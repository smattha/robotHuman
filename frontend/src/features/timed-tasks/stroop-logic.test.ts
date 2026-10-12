import { describe, expect, it } from 'vitest'
import { createStroopState, getStroopSummary, respondStroop, startStroop, tickStroop } from './stroop-logic'
import type { StroopState } from './stroop-logic'

function runningState(shouldRespond: boolean): StroopState {
  return { ...createStroopState(), phase: 'running', shouldRespond, word: 'red', ink: 'red', trialStartedAt: 1000, startedAt: 0 }
}

describe('stroop logic', () => {
  it('starts in the instruction phase', () => {
    expect(createStroopState().phase).toBe('instruction')
  })

  it('moves to running when started', () => {
    expect(startStroop(createStroopState(), 0).phase).toBe('running')
  })

  it('scores a press correct on a match', () => {
    const result = respondStroop(runningState(true), 1500)
    expect(result.trials).toHaveLength(1)
    expect(result.trials[0].isCorrect).toBe(true)
    expect(result.trials[0].responseTimeMs).toBe(500)
  })

  it('scores a press wrong on a mismatch', () => {
    const result = respondStroop(runningState(false), 1500)
    expect(result.trials[0].isCorrect).toBe(false)
  })

  it('scores a timeout correct on a mismatch (no press)', () => {
    const result = tickStroop(runningState(false), 3000)
    expect(result.trials[0].isCorrect).toBe(true)
    expect(result.trials[0].response).toBe('δεν πάτησε')
  })

  it('scores a timeout wrong on a match (no press)', () => {
    const result = tickStroop(runningState(true), 3000)
    expect(result.trials[0].isCorrect).toBe(false)
  })

  it('ignores a press before the task starts', () => {
    expect(respondStroop(createStroopState(), 1500).trials).toHaveLength(0)
  })

  it('summarises correct and wrong trials', () => {
    const state = { ...runningState(true), trials: [{ stimulus: 'a', response: 'b', isCorrect: true, responseTimeMs: 100 }, { stimulus: 'a', response: 'b', isCorrect: false, responseTimeMs: 300 }] }
    const summary = getStroopSummary(state)
    expect(summary.correctCount).toBe(1)
    expect(summary.wrongCount).toBe(1)
    expect(summary.meanResponseTimeMs).toBe(200)
  })
})

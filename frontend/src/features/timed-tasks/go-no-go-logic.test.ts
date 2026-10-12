import { describe, expect, it } from 'vitest'
import { createGoNoGoState, getGoNoGoSummary, respondGoNoGo, startGoNoGo, tickGoNoGo } from './go-no-go-logic'
import type { GoNoGoState } from './go-no-go-logic'

function runningState(isGo: boolean): GoNoGoState {
  return { ...createGoNoGoState(), phase: 'running', isGo, trialDisplayMs: isGo ? 2000 : 1000, trialStartedAt: 1000, startedAt: 0 }
}

describe('go-no-go logic', () => {
  it('starts in the instruction phase', () => {
    expect(createGoNoGoState().phase).toBe('instruction')
  })

  it('moves to running when started', () => {
    expect(startGoNoGo(createGoNoGoState(), 0).phase).toBe('running')
  })

  it('scores a press correct on a go signal', () => {
    expect(respondGoNoGo(runningState(true), 1500).trials[0].isCorrect).toBe(true)
  })

  it('scores a press wrong on a no-go signal', () => {
    expect(respondGoNoGo(runningState(false), 1500).trials[0].isCorrect).toBe(false)
  })

  it('scores a timeout correct on a no-go signal', () => {
    expect(tickGoNoGo(runningState(false), 2000).trials[0].isCorrect).toBe(true)
  })

  it('scores a timeout wrong on a go signal', () => {
    expect(tickGoNoGo(runningState(true), 3000).trials[0].isCorrect).toBe(false)
  })

  it('does not advance before the display time elapses', () => {
    expect(tickGoNoGo(runningState(true), 1500).trials).toHaveLength(0)
  })

  it('summarises correct and wrong trials', () => {
    const state = { ...runningState(true), trials: [{ stimulus: 'a', response: 'b', isCorrect: true, responseTimeMs: 100 }, { stimulus: 'a', response: 'b', isCorrect: false, responseTimeMs: 300 }] }
    const summary = getGoNoGoSummary(state)
    expect(summary.correctCount).toBe(1)
    expect(summary.wrongCount).toBe(1)
    expect(summary.meanResponseTimeMs).toBe(200)
  })
})

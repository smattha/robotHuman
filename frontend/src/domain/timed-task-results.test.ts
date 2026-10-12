import { beforeEach, describe, expect, it } from 'vitest'
import type { TimedTaskResult } from './timed-task'
import { clearTimedTaskResults, deleteTimedTaskResult, loadTimedTaskResults, saveTimedTaskResult } from './timed-task-results'

const result: TimedTaskResult = {
  id: 'one', taskId: 'stroop', userName: 'Alex', startedAt: '2026-10-05', completedAt: '2026-10-05', trials: [],
  summary: { totalTrials: 0, correctCount: 0, wrongCount: 0, meanResponseTimeMs: 0, maxSequenceLength: null },
}

describe('timed task results', () => {
  beforeEach(() => localStorage.clear())

  it('deletes only the selected task result', () => {
    const second = { ...result, id: 'two' }
    saveTimedTaskResult(result)
    saveTimedTaskResult(second)

    expect(deleteTimedTaskResult(result.id)).toBe(true)
    expect(loadTimedTaskResults()).toEqual([second])
  })

  it('clears all timed task results', () => {
    saveTimedTaskResult(result)
    expect(clearTimedTaskResults()).toBe(true)
    expect(loadTimedTaskResults()).toEqual([])
  })
})

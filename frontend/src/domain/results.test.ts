import { beforeEach, describe, expect, it } from 'vitest'
import { clearResults, deleteResult, loadResults, saveResult } from './results'

describe('test results', () => {
  beforeEach(() => localStorage.clear())

  it('stores answers under the named user', () => {
    const result = {
      id: 'test-1', userName: 'Alex', startedAt: '2026-10-05', completedAt: null,
      answers: [{ exerciseId: 'lion-and-ducklings', optionId: 'four', isCorrect: true, answeredAt: '2026-10-05' }],
    }
    expect(saveResult(result)).toBe(true)
    expect(loadResults()).toEqual([result])
  })

  it('returns an empty list when saved data is invalid', () => {
    localStorage.setItem('childrens-exercises-results-v1', '{broken')
    expect(loadResults()).toEqual([])
  })

  it('deletes one result without removing other results', () => {
    const first = { id: 'one', userName: 'Alex', startedAt: '2026-10-05', completedAt: null, answers: [] }
    const second = { ...first, id: 'two', userName: 'Niki' }
    saveResult(first)
    saveResult(second)

    expect(deleteResult(first.id)).toBe(true)
    expect(loadResults()).toEqual([second])
  })

  it('clears all exercise results', () => {
    saveResult({ id: 'one', userName: 'Alex', startedAt: '2026-10-05', completedAt: null, answers: [] })
    expect(clearResults()).toBe(true)
    expect(loadResults()).toEqual([])
  })
})

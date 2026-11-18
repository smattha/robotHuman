import { act, renderHook } from '@testing-library/react'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { useTimedTask } from './use-timed-task'

type Counter = { value: number; done: boolean }

function makeConfig(report: (state: Counter) => void) {
  return {
    create: () => ({ value: 0, done: false } as Counter),
    tick: (state: Counter, now: number) => (state.done ? state : { ...state, value: state.value + 1, done: now >= 1000 }),
    isFinished: (state: Counter) => state.done,
    report,
  }
}

describe('useTimedTask', () => {
  beforeEach(() => {
    vi.useFakeTimers()
    vi.setSystemTime(0)
  })

  afterEach(() => vi.useRealTimers())

  it('reports exactly once when the task finishes', () => {
    const report = vi.fn()
    const { result } = renderHook(() => useTimedTask(makeConfig(report)))
    act(() => {
      vi.advanceTimersByTime(1100)
    })
    expect(result.current.state.done).toBe(true)
    expect(report).toHaveBeenCalledTimes(1)
  })

  it('stops ticking after unmount and never reports', () => {
    const report = vi.fn()
    const { unmount } = renderHook(() => useTimedTask(makeConfig(report)))
    act(() => {
      vi.advanceTimersByTime(100)
    })
    unmount()
    act(() => {
      vi.advanceTimersByTime(2000)
    })
    expect(report).not.toHaveBeenCalled()
  })

  it('restarts from a fresh state', () => {
    const report = vi.fn()
    const { result } = renderHook(() => useTimedTask(makeConfig(report)))
    act(() => {
      vi.advanceTimersByTime(1100)
    })
    expect(report).toHaveBeenCalledTimes(1)
    act(() => {
      result.current.restart()
    })
    expect(result.current.state.value).toBe(0)
    expect(result.current.state.done).toBe(false)
  })
})

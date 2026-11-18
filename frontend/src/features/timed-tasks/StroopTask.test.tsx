import { act, render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { afterEach, describe, expect, it, vi } from 'vitest'
import { StroopTask } from './StroopTask'

describe('StroopTask', () => {
  afterEach(() => vi.useRealTimers())

  it('runs the game and reports exactly once when the time limit is reached', async () => {
    vi.useFakeTimers()
    vi.setSystemTime(0)
    const onComplete = vi.fn()
    const user = userEvent.setup({ advanceTimers: vi.advanceTimersByTime })
    render(<StroopTask userName="Alex" onExit={vi.fn()} onComplete={onComplete} helper="fox" narrationMode="muted" speechEnabled={false} />)

    expect(screen.getByRole('button', { name: 'Ξεκίνα' })).toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: 'Ξεκίνα' }))

    expect(screen.getByTestId('stroop-game')).toBeInTheDocument()
    expect(screen.getByRole('button', { name: 'Απόκριση' })).toBeEnabled()
    await user.click(screen.getByRole('button', { name: 'Απόκριση' }))

    act(() => {
      vi.advanceTimersByTime(30000)
    })

    expect(onComplete).toHaveBeenCalledTimes(1)
    const [taskId, trials] = onComplete.mock.calls[0]
    expect(taskId).toBe('stroop')
    expect(Array.isArray(trials)).toBe(true)
    expect(trials.length).toBeGreaterThan(0)
  })

  it('cleans up on unmount without reporting', async () => {
    vi.useFakeTimers()
    vi.setSystemTime(0)
    const onComplete = vi.fn()
    const user = userEvent.setup({ advanceTimers: vi.advanceTimersByTime })
    const { unmount } = render(<StroopTask userName="Alex" onExit={vi.fn()} onComplete={onComplete} helper="fox" narrationMode="muted" speechEnabled={false} />)

    await user.click(screen.getByRole('button', { name: 'Ξεκίνα' }))
    act(() => {
      vi.advanceTimersByTime(1000)
    })
    unmount()
    expect(onComplete).not.toHaveBeenCalled()
  })
})

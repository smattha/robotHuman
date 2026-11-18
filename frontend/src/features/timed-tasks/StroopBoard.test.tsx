import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { describe, expect, it, vi } from 'vitest'
import { COLOR_WORDS, createStroopState, type StroopState } from './stroop-logic'
import { StroopBoard } from './StroopBoard'

function boardState(overrides: Partial<StroopState>): StroopState {
  return { ...createStroopState(), ...overrides }
}

describe('StroopBoard', () => {
  it('renders the stimulus word in the ink colour', () => {
    render(<StroopBoard state={boardState({ phase: 'running', word: 'blue', ink: 'red' })} helper="fox" onRespond={vi.fn()} />)
    expect(screen.getByText(COLOR_WORDS.blue)).toHaveStyle({ color: '#d64545' })
  })

  it('invokes onRespond when the answer button is pressed', async () => {
    const onRespond = vi.fn()
    const user = userEvent.setup()
    render(<StroopBoard state={boardState({ phase: 'running', word: 'red', ink: 'red' })} helper="fox" onRespond={onRespond} />)
    await user.click(screen.getByRole('button', { name: 'Απόκριση' }))
    expect(onRespond).toHaveBeenCalledTimes(1)
  })

  it('disables the answer button once the trial has been answered', () => {
    render(<StroopBoard state={boardState({ phase: 'running', responded: true })} helper="fox" onRespond={vi.fn()} />)
    expect(screen.getByRole('button', { name: 'Απόκριση' })).toBeDisabled()
  })

  it('shows a completion message and hides the button when finished', () => {
    render(<StroopBoard state={boardState({ phase: 'finished' })} helper="fox" onRespond={vi.fn()} />)
    expect(screen.getByRole('status')).toHaveTextContent(/Μπράβο/i)
    expect(screen.queryByRole('button', { name: 'Απόκριση' })).not.toBeInTheDocument()
  })
})

import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { describe, expect, it, vi } from 'vitest'
import { createSartState, type SartState } from './sart-logic'
import { SartBoard } from './SartBoard'

function boardState(overrides: Partial<SartState>): SartState {
  return { ...createSartState(), ...overrides }
}

describe('SartBoard', () => {
  it('renders the current stimulus', () => {
    render(<SartBoard state={boardState({ phase: 'running', stimulus: '🍎' })} helper="unicorn" onRespond={vi.fn()} />)
    expect(screen.getByText('🍎')).toBeInTheDocument()
  })

  it('invokes onRespond when the answer button is pressed', async () => {
    const onRespond = vi.fn()
    const user = userEvent.setup()
    render(<SartBoard state={boardState({ phase: 'running', stimulus: '✈️' })} helper="unicorn" onRespond={onRespond} />)
    await user.click(screen.getByRole('button', { name: 'Απόκριση' }))
    expect(onRespond).toHaveBeenCalledTimes(1)
  })

  it('disables the answer button once the trial has been answered', () => {
    render(<SartBoard state={boardState({ phase: 'running', responded: true })} helper="unicorn" onRespond={vi.fn()} />)
    expect(screen.getByRole('button', { name: 'Απόκριση' })).toBeDisabled()
  })

  it('shows a completion message and hides the button when finished', () => {
    render(<SartBoard state={boardState({ phase: 'finished' })} helper="unicorn" onRespond={vi.fn()} />)
    expect(screen.getByRole('status')).toHaveTextContent(/Μπράβο/i)
    expect(screen.queryByRole('button', { name: 'Απόκριση' })).not.toBeInTheDocument()
  })
})

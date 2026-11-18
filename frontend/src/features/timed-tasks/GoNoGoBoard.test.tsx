import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { describe, expect, it, vi } from 'vitest'
import { createGoNoGoState, type GoNoGoState } from './go-no-go-logic'
import { GoNoGoBoard } from './GoNoGoBoard'

function boardState(overrides: Partial<GoNoGoState>): GoNoGoState {
  return { ...createGoNoGoState(), ...overrides }
}

describe('GoNoGoBoard', () => {
  it('renders the go word with an enabled answer button while running', () => {
    render(<GoNoGoBoard state={boardState({ phase: 'running', isGo: true })} helper="owl" onRespond={vi.fn()} />)
    expect(screen.getByText('Ξεκίνα')).toBeInTheDocument()
    expect(screen.getByRole('button', { name: 'Απόκριση' })).toBeEnabled()
  })

  it('renders the no-go word', () => {
    render(<GoNoGoBoard state={boardState({ phase: 'running', isGo: false })} helper="owl" onRespond={vi.fn()} />)
    expect(screen.getByText('Στοπ')).toBeInTheDocument()
  })

  it('invokes onRespond when the answer button is pressed', async () => {
    const onRespond = vi.fn()
    const user = userEvent.setup()
    render(<GoNoGoBoard state={boardState({ phase: 'running', isGo: true })} helper="owl" onRespond={onRespond} />)
    await user.click(screen.getByRole('button', { name: 'Απόκριση' }))
    expect(onRespond).toHaveBeenCalledTimes(1)
  })

  it('disables the answer button once the trial has been answered', () => {
    render(<GoNoGoBoard state={boardState({ phase: 'running', responded: true })} helper="owl" onRespond={vi.fn()} />)
    expect(screen.getByRole('button', { name: 'Απόκριση' })).toBeDisabled()
  })

  it('shows a completion message and hides the button when finished', () => {
    render(<GoNoGoBoard state={boardState({ phase: 'finished' })} helper="owl" onRespond={vi.fn()} />)
    expect(screen.getByRole('status')).toHaveTextContent(/Μπράβο/i)
    expect(screen.queryByRole('button', { name: 'Απόκριση' })).not.toBeInTheDocument()
  })
})

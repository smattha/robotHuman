import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { describe, expect, it, vi } from 'vitest'
import { createDigitSpanState, type DigitSpanState } from './digit-span-logic'
import { DigitSpanBoard } from './DigitSpanBoard'

function boardState(overrides: Partial<DigitSpanState>): DigitSpanState {
  return { ...createDigitSpanState(), ...overrides }
}

describe('DigitSpanBoard', () => {
  it('shows the current digit in the star while presenting the sequence', () => {
    render(<DigitSpanBoard state={boardState({ phase: 'showing', sequence: ['3', '7', '2'], sequenceIndex: 2 })} helper="unicorn" onEnterDigit={vi.fn()} onClear={vi.fn()} onSubmit={vi.fn()} />)
    expect(screen.getByText('7')).toBeInTheDocument()
  })

  it('invokes onEnterDigit when a digit key is pressed while answering', async () => {
    const onEnterDigit = vi.fn()
    const user = userEvent.setup()
    render(<DigitSpanBoard state={boardState({ phase: 'answering', sequence: ['3', '7'], answer: '' })} helper="unicorn" onEnterDigit={onEnterDigit} onClear={vi.fn()} onSubmit={vi.fn()} />)
    await user.click(screen.getByRole('button', { name: '5' }))
    expect(onEnterDigit).toHaveBeenCalledWith('5')
  })

  it('invokes onClear and onSubmit from the keypad', async () => {
    const onClear = vi.fn()
    const onSubmit = vi.fn()
    const user = userEvent.setup()
    render(<DigitSpanBoard state={boardState({ phase: 'answering', sequence: ['3', '7'], answer: '3' })} helper="unicorn" onEnterDigit={vi.fn()} onClear={onClear} onSubmit={onSubmit} />)
    await user.click(screen.getByRole('button', { name: 'Διόρθωση' }))
    expect(onClear).toHaveBeenCalledTimes(1)
    await user.click(screen.getByRole('button', { name: 'Συνέχεια' }))
    expect(onSubmit).toHaveBeenCalledTimes(1)
  })

  it('shows the typed answer while answering', () => {
    render(<DigitSpanBoard state={boardState({ phase: 'answering', sequence: ['3', '7'], answer: '37' })} helper="unicorn" onEnterDigit={vi.fn()} onClear={vi.fn()} onSubmit={vi.fn()} />)
    expect(screen.getByText('37')).toBeInTheDocument()
  })

  it('shows a completion message when finished', () => {
    render(<DigitSpanBoard state={boardState({ phase: 'finished' })} helper="unicorn" onEnterDigit={vi.fn()} onClear={vi.fn()} onSubmit={vi.fn()} />)
    expect(screen.getByRole('status')).toHaveTextContent(/Μπράβο/i)
  })
})

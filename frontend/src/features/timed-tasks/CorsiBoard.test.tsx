import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { describe, expect, it, vi } from 'vitest'
import { createCorsiState, type CorsiState } from './corsi-logic'
import { CorsiBoard } from './CorsiBoard'

function boardState(overrides: Partial<CorsiState>): CorsiState {
  return { ...createCorsiState(), ...overrides }
}

describe('CorsiBoard', () => {
  it('renders nine mushroom tiles', () => {
    render(<CorsiBoard state={boardState({ phase: 'showing', sequence: [0, 1, 2], sequenceIndex: 0 })} helper="fox" onTapTile={vi.fn()} />)
    expect(screen.getAllByRole('button', { name: /Μανιτάρι/ })).toHaveLength(9)
  })

  it('highlights the current tile while showing the sequence', () => {
    render(<CorsiBoard state={boardState({ phase: 'showing', sequence: [4, 1, 2], sequenceIndex: 1 })} helper="fox" onTapTile={vi.fn()} />)
    expect(screen.getByRole('button', { name: 'Μανιτάρι 5' })).toHaveClass('active')
  })

  it('keeps the tiles disabled while the sequence is shown', () => {
    render(<CorsiBoard state={boardState({ phase: 'showing', sequence: [0, 1, 2], sequenceIndex: 1 })} helper="fox" onTapTile={vi.fn()} />)
    expect(screen.getByRole('button', { name: 'Μανιτάρι 1' })).toBeDisabled()
  })

  it('invokes onTapTile with the tile index while answering', async () => {
    const onTapTile = vi.fn()
    const user = userEvent.setup()
    render(<CorsiBoard state={boardState({ phase: 'answering', sequence: [0, 1, 2], answer: [] })} helper="fox" onTapTile={onTapTile} />)
    await user.click(screen.getByRole('button', { name: 'Μανιτάρι 3' }))
    expect(onTapTile).toHaveBeenCalledWith(2)
  })

  it('shows a completion message when finished', () => {
    render(<CorsiBoard state={boardState({ phase: 'finished' })} helper="fox" onTapTile={vi.fn()} />)
    expect(screen.getByRole('status')).toHaveTextContent(/Μπράβο/i)
  })
})

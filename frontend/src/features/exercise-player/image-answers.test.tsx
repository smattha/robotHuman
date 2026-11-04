import { render, screen, within } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { beforeEach, expect, it } from 'vitest'
import { App } from '../../app/App'

beforeEach(() => localStorage.clear())

it('shows only images for visual answers and keeps practice results unsaved', async () => {
  const user = userEvent.setup()
  render(<App />)
  await user.click(screen.getByRole('button', { name: /Δες τις αποστολές/i }))
  const lionCard = screen.getByRole('heading', { name: 'Το λιοντάρι και τα παπάκια' }).closest('article')
  expect(lionCard).not.toBeNull()
  await user.click(within(lionCard!).getByRole('button', { name: /Δοκιμή χωρίς καταγραφή/i }))

  const answer = screen.getByRole('radio', { name: /Τέσσερα παπάκια/i })
  expect(answer.querySelector('img')).toHaveAttribute('src', '/ex1/answer-4.png')
  expect(answer.textContent).toBe('')
  await user.click(answer)
  expect(answer).toHaveAttribute('aria-checked', 'true')
  await user.click(screen.getByRole('button', { name: /Έλεγξε την απάντηση/i }))
  expect(localStorage.getItem('childrens-exercises-results-v1')).toBeNull()
})

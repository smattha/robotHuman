import { render, screen, within } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { beforeEach, expect, it } from 'vitest'
import { App } from '../../app/App'

beforeEach(() => localStorage.clear())

it('shows only images for visual answers and keeps practice results unsaved', async () => {
  const user = userEvent.setup()
  render(<App />)
  await user.click(screen.getByRole('button', { name: /Δες τις αποστολές/i }))
  const dogCard = screen.getByRole('heading', { name: 'Τι δείχνουν οι εικόνες 2' }).closest('article')
  expect(dogCard).not.toBeNull()
  await user.click(within(dogCard!).getByRole('button', { name: /Δοκιμή χωρίς καταγραφή/i }))

  const answer = screen.getByRole('radio', { name: /Σκυλί/i })
  expect(answer.querySelector('img')).toHaveAttribute('src', '/ex12/dog.png')
  expect(answer.textContent).toBe('')
  await user.click(answer)
  expect(answer).toHaveAttribute('aria-checked', 'true')
  expect(localStorage.getItem('childrens-exercises-results-v1')).toBeNull()
})

import { render, screen, within } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { beforeEach, describe, expect, it } from 'vitest'
import { saveResult } from '../domain/results'
import { saveTimedTaskResult } from '../domain/timed-task-results'
import { App } from './App'

describe('App', () => {
  beforeEach(() => localStorage.clear())

  async function startAsNewUser(user: ReturnType<typeof userEvent.setup>, name = 'Alex') {
    await user.click(screen.getByRole('button', { name: 'Νέος χρήστης' }))
    await user.type(screen.getByLabelText('Όνομα'), name)
    await user.click(screen.getByRole('button', { name: /Συνέχισε/i }))
    await user.click(screen.getByRole('button', { name: /^Ξεκινάμε/i }))
  }

  it('allows a child to complete the first exercise', async () => {
    const user = userEvent.setup()
    render(<App />)

    await startAsNewUser(user)
    const lionCard = screen.getByRole('heading', { name: 'Το λιοντάρι και τα παπάκια' }).closest('article')
    expect(lionCard).not.toBeNull()
    await user.click(within(lionCard!).getByRole('button', { name: /Παίξε τώρα/i }))
    await user.click(screen.getByRole('radio', { name: /Τέσσερα παπάκια/i }))
    await user.click(screen.getByRole('button', { name: /Έλεγξε την απάντηση/i }))

    expect(screen.getByText(/Μπράβο! Το βρήκες!/i)).toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: /Συνέχισε/i }))

    expect(screen.getByRole('heading', { name: /Μπράβο για την προσπάθειά σου/i })).toBeInTheDocument()
    expect(screen.getByText(/Κονκάρδα: Μικρός Εξερευνητής/)).toBeInTheDocument()
    expect(JSON.parse(localStorage.getItem('childrens-exercises-results-v1') ?? '[]')).toMatchObject([{
      userName: 'Alex', kind: 'single', completedAt: expect.any(String),
      answers: [{ exerciseId: 'lion-and-ducklings', optionId: 'four', isCorrect: true }],
    }])
    await user.click(screen.getByRole('button', { name: 'Στατιστικά' }))
    expect(screen.getByText(/Το λιοντάρι και τα παπάκια · 1\/1 σωστές/i)).toBeInTheDocument()
    expect(screen.getByText(/Κονκάρδα: Μικρός Εξερευνητής/)).toBeInTheDocument()
  })

  it('shows a preparation screen before the memory challenge instructions', async () => {
    const user = userEvent.setup()
    render(<App />)
    await startAsNewUser(user)
    const taskCard = screen.getByRole('heading', { name: 'Stroop' }).closest('article')
    await user.click(within(taskCard!).getByRole('button', { name: /Ξεκίνα δοκιμασία/i }))
    await user.click(screen.getByRole('button', { name: 'Ξεκίνα' }))

    expect(screen.getByRole('heading', { name: 'Ετοιμάσου για το Stroop' })).toBeInTheDocument()
    expect(screen.queryByRole('button', { name: 'Απόκριση' })).not.toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: /Δες τις οδηγίες/i }))
    expect(screen.getByRole('heading', { name: 'Ας κάνουμε μία πρόβα' })).toBeInTheDocument()
    expect(screen.getByText(/δεν καταγράφεται/i)).toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: /Ξεκίνα την κανονική δοκιμασία/i }))
    expect(screen.getByText(/Θα εμφανίζονται λέξεις χρωμάτων/i)).toBeInTheDocument()
  })

  it('opens statistics and requires confirmation before deleting an entry or all results', async () => {
    const user = userEvent.setup()
    saveResult({ id: 'exercise-one', userName: 'Alex', startedAt: '2026-10-05', completedAt: '2026-10-05', answers: [] })
    saveTimedTaskResult({
      id: 'timed-one', taskId: 'stroop', userName: 'Niki', startedAt: '2026-10-05', completedAt: '2026-10-05', trials: [],
      summary: { totalTrials: 0, correctCount: 0, wrongCount: 0, meanResponseTimeMs: 0, maxSequenceLength: null },
    })
    render(<App />)
    await user.click(screen.getByRole('button', { name: 'Στατιστικά' }))

    expect(screen.getByRole('heading', { name: 'Στατιστικά' })).toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: 'Διαγραφή αποτελέσματος για Alex' }))
    expect(localStorage.getItem('childrens-exercises-results-v1')).toContain('Alex')
    await user.click(screen.getByRole('button', { name: 'Ακύρωση' }))
    expect(screen.getByText('Alex')).toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: 'Διαγραφή αποτελέσματος για Alex' }))
    await user.click(within(screen.getByRole('alertdialog')).getByRole('button', { name: 'Διαγραφή' }))
    expect(screen.queryByText('Alex')).not.toBeInTheDocument()
    expect(screen.getByText('Niki')).toBeInTheDocument()

    await user.click(screen.getByRole('button', { name: 'Διαγραφή όλων' }))
    expect(localStorage.getItem('childrens-exercises-timed-tasks-v1')).toContain('Niki')
    await user.click(within(screen.getByRole('alertdialog')).getByRole('button', { name: 'Διαγραφή όλων' }))
    expect(screen.getByText('Δεν υπάρχουν ακόμα αποτελέσματα')).toBeInTheDocument()
  })

  it('starts a memory challenge only after preparation and practice screens', async () => {
    const user = userEvent.setup()
    render(<App />)
    await startAsNewUser(user)
    const taskCard = screen.getByRole('heading', { name: 'Stroop' }).closest('article')
    await user.click(within(taskCard!).getByRole('button', { name: /Ξεκίνα δοκιμασία/i }))
    await user.click(screen.getByRole('button', { name: 'Ξεκίνα' }))
    await user.click(screen.getByRole('button', { name: /Δες τις οδηγίες/i }))
    await user.click(screen.getByRole('button', { name: /Ξεκίνα την κανονική δοκιμασία/i }))
    await user.click(screen.getByRole('button', { name: 'Ξεκίνα' }))

    expect(screen.getByRole('button', { name: 'Απόκριση' })).toBeInTheDocument()
  })

  it('discards a cancelled memory challenge without changing saved results', async () => {
    const user = userEvent.setup()
    render(<App />)
    await startAsNewUser(user)
    const taskCard = screen.getByRole('heading', { name: 'Stroop' }).closest('article')
    await user.click(within(taskCard!).getByRole('button', { name: /Ξεκίνα δοκιμασία/i }))
    await user.click(screen.getByRole('button', { name: 'Ξεκίνα' }))
    await user.click(screen.getByRole('button', { name: 'Πίσω στις ασκήσεις' }))

    expect(screen.getByRole('heading', { name: 'Προκλήσεις Μνήμης και Προσοχής' })).toBeInTheDocument()
    expect(localStorage.getItem('childrens-exercises-timed-tasks-v1')).toBeNull()
  })

  it('stores the selected story speed in settings', async () => {
    const user = userEvent.setup()
    render(<App />)
    await user.click(screen.getByRole('button', { name: 'Ρυθμίσεις' }))

    expect(screen.getByRole('heading', { name: 'Ρυθμίσεις' })).toBeInTheDocument()
    expect(screen.getByRole('radio', { name: /Αργά/i })).toHaveAttribute('aria-checked', 'true')
    await user.click(screen.getByRole('radio', { name: /Γρήγορα/i }))
    expect(screen.getByRole('radio', { name: /Γρήγορα/i })).toHaveAttribute('aria-checked', 'true')
    expect(localStorage.getItem('childrens-exercises-preferences-v1')).toContain('fast')
  })

  it('warns about an existing name but lets the user continue', async () => {
    const user = userEvent.setup()
    localStorage.setItem('childrens-exercises-users-v1', JSON.stringify(['Alex']))
    render(<App />)

    await user.click(screen.getByRole('button', { name: 'Νέος χρήστης' }))
    await user.type(screen.getByLabelText('Όνομα'), 'Alex')
    expect(screen.getByText(/Υπάρχει ήδη χρήστης με αυτό το όνομα/i)).toBeInTheDocument()
    expect(screen.getByRole('button', { name: /Συνέχισε/i })).toBeEnabled()
    await user.click(screen.getByRole('button', { name: /Συνέχισε/i }))

    expect(screen.getByText('Γεια σου, Alex!')).toBeInTheDocument()
  })

  it('asks for a name before sidebar navigation when no user is active', async () => {
    const user = userEvent.setup()
    render(<App />)

    await user.click(screen.getByRole('button', { name: 'Ρυθμίσεις' }))

    expect(screen.getByRole('heading', { name: 'Πώς σε λένε;' })).toBeInTheDocument()
    expect(screen.queryByRole('heading', { name: 'Ρυθμίσεις' })).not.toBeInTheDocument()
  })

  it('opens statistics and settings without an active user', async () => {
    const user = userEvent.setup()
    render(<App />)

    await user.click(screen.getByRole('button', { name: 'Στατιστικά' }))
    expect(screen.getByRole('heading', { name: 'Στατιστικά' })).toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: 'Ρυθμίσεις' }))
    expect(screen.getByRole('heading', { name: 'Ρυθμίσεις' })).toBeInTheDocument()
  })

  it('continues an unfinished adventure from its next mission', async () => {
    const user = userEvent.setup()
    saveResult({
      id: 'unfinished-adventure', userName: 'Alex', startedAt: '2026-10-05', completedAt: null,
      answers: [{ exerciseId: 'lion-and-ducklings', optionId: 'four', isCorrect: true, answeredAt: '2026-10-05' }],
    })
    render(<App />)

    await user.click(screen.getByRole('button', { name: 'Νέος χρήστης' }))
    await user.type(screen.getByLabelText('Όνομα'), 'Alex')
    await user.click(screen.getByRole('button', { name: /Συνέχισε/i }))
    await user.click(screen.getByRole('button', { name: 'Ξεκίνα τη Μεγάλη Περιπέτεια' }))
    expect(screen.getByText('Η περιπέτεια του/της Alex περιμένει.')).toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: /Συνέχισε την Περιπέτεια/i }))

    expect(screen.getByText('Αποστολή 2 / 12')).toBeInTheDocument()
  })

  it('shows completed activities in the progress map', async () => {
    const user = userEvent.setup()
    saveResult({ id: 'exercise-one', userName: 'Alex', startedAt: '2026-10-05', completedAt: '2026-10-05', answers: [{ exerciseId: 'lion-and-ducklings', optionId: 'four', isCorrect: true, answeredAt: '2026-10-05' }] })
    saveTimedTaskResult({
      id: 'timed-one', taskId: 'stroop', userName: 'Alex', startedAt: '2026-10-05', completedAt: '2026-10-05', trials: [],
      summary: { totalTrials: 0, correctCount: 0, wrongCount: 0, meanResponseTimeMs: 0, maxSequenceLength: null },
    })
    render(<App />)
    await startAsNewUser(user)

    expect(screen.getByRole('heading', { name: 'Ο χάρτης των αποστολών' })).toBeInTheDocument()
    expect(screen.getByLabelText('Ολοκληρώθηκαν 1 από 12 Μικρές Αποστολές')).toBeInTheDocument()
    expect(screen.getByLabelText('Ολοκληρώθηκαν 1 από 5 Προκλήσεις Μνήμης')).toBeInTheDocument()
  })


  // it('starts a named test from the drawer and saves the first answer', async () => {
  //   const user = userEvent.setup()
  //   render(<App />)
  //   await user.click(screen.getByRole('button', { name: 'Ασκήσεις' }))
  //   expect(screen.getByLabelText('Επιλογή άσκησης')).toBeInTheDocument()
  //   await user.click(screen.getByRole('button', { name: 'Κλείσιμο' }))
  //   await user.click(screen.getByRole('button', { name: 'Test all' }))
  //   await user.type(screen.getByLabelText('Όνομα'), 'Alex')
  //   await user.click(screen.getByRole('button', { name: 'Ξεκίνα το τεστ' }))
  //   await user.click(screen.getByRole('radio', { name: /Τέσσερα παπάκια/i }))
  //   await user.click(screen.getByRole('button', { name: /Έλεγξε την απάντηση/i }))
  //   expect(JSON.parse(localStorage.getItem('childrens-exercises-results-v1') ?? '[]')[0].answers).toHaveLength(1)
  //   await user.click(screen.getByRole('button', { name: /Συνέχισε/i }))
  //   expect(screen.getByText('Αποστολή 2 / 12')).toBeInTheDocument()
  // })
  //
  // it('shows each story frame before allowing an answer', async () => {
  //   const user = userEvent.setup()
  //   render(<App />)
  //   await user.click(screen.getByRole('button', { name: 'Ασκήσεις' }))
  //   await user.click(screen.getByRole('button', { name: /03 Ο Γιωργάκης και η σοκολάτα/i }))
  //   expect(screen.queryByRole('radio')).not.toBeInTheDocument()
  //   await user.click(screen.getByRole('button', { name: /Επόμενη εικόνα/i }))
  //   await user.click(screen.getByRole('button', { name: /Στην ερώτηση/i }))
  //   expect(screen.getByRole('radio', { name: /Στο ντουλάπι/i })).toBeInTheDocument()
  // })
})

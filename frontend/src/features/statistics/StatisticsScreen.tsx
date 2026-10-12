import { useEffect, useState } from 'react'
import { exercises } from '../../content/exercises'
import type { TestResult } from '../../domain/results'
import type { TimedTaskResult } from '../../domain/timed-task'
import { timedTaskDefinitions } from '../timed-tasks/timed-task-definitions'

type DeletionTarget = { type: 'exercise' | 'timed'; id: string; label: string } | { type: 'all' }

type StatisticsScreenProps = {
  results: TestResult[]
  timedResults: TimedTaskResult[]
  onDelete: (type: 'exercise' | 'timed', id: string) => boolean
  onDeleteAll: () => boolean
}

export function StatisticsScreen({ results, timedResults, onDelete, onDeleteAll }: StatisticsScreenProps) {
  const [deletionTarget, setDeletionTarget] = useState<DeletionTarget | null>(null)
  const [deletionError, setDeletionError] = useState(false)
  const hasResults = results.length + timedResults.length > 0

  useEffect(() => {
    if (!deletionTarget) return
    function closeOnEscape(event: KeyboardEvent) {
      if (event.key === 'Escape') setDeletionTarget(null)
    }
    window.addEventListener('keydown', closeOnEscape)
    return () => window.removeEventListener('keydown', closeOnEscape)
  }, [deletionTarget])

  function confirmDeletion() {
    if (!deletionTarget) return
    const deleted = deletionTarget.type === 'all' ? onDeleteAll() : onDelete(deletionTarget.type, deletionTarget.id)
    if (deleted) setDeletionTarget(null)
    setDeletionError(!deleted)
  }

  return (
    <section className="page-section statistics-page" aria-labelledby="statistics-title">
      <div className="section-heading statistics-heading">
        <div>
          <p className="eyebrow">Αποτελέσματα σε αυτή τη συσκευή</p>
          <h1 id="statistics-title">Στατιστικά</h1>
          <p className="lead">Οι απαντήσεις και οι δοκιμασίες αποθηκεύονται μόνο σε αυτόν τον browser.</p>
        </div>
        {hasResults && <button className="delete-button" type="button" onClick={() => setDeletionTarget({ type: 'all' })}>Διαγραφή όλων</button>}
      </div>

      {deletionError && <p className="storage-warning" role="alert">Δεν ήταν δυνατή η διαγραφή. Δοκίμασε ξανά.</p>}
      {!hasResults && <div className="statistics-empty"><span aria-hidden="true">✧</span><h2>Δεν υπάρχουν ακόμα αποτελέσματα</h2><p>Όταν ολοκληρώσεις μια άσκηση, τα στατιστικά της θα εμφανιστούν εδώ.</p></div>}

      {results.length > 0 && <div className="statistics-group">
        <h2>Ασκήσεις <span>{results.length}</span></h2>
        <div className="statistics-entries">{results.map((result) => (
          <article key={result.id} className="result-entry">
            <div className="result-entry-header">
              <div><strong>{result.userName}</strong><p>{result.answers.filter((answer) => answer.isCorrect).length}/{result.answers.length} σωστές · {result.completedAt ? 'Ολοκληρώθηκε' : 'Σε εξέλιξη'} · {new Date(result.completedAt ?? result.startedAt).toLocaleString('el-GR')}</p></div>
              <button className="delete-button" type="button" onClick={() => setDeletionTarget({ type: 'exercise', id: result.id, label: result.userName })} aria-label={`Διαγραφή αποτελέσματος για ${result.userName}`}>Διαγραφή</button>
            </div>
            <details><summary>Απαντήσεις</summary>
              <ul>{result.answers.map((answer, index) => {
                const exercise = exercises.find((entry) => entry.id === answer.exerciseId)
                const option = exercise?.options.find((entry) => entry.id === answer.optionId)
                return <li key={`${answer.exerciseId}-${index}`}>{exercise?.title ?? answer.exerciseId}: {option?.detail ?? answer.optionId} · {answer.isCorrect ? 'Σωστό' : 'Λάθος'}</li>
              })}</ul>
            </details>
          </article>
        ))}</div>
      </div>}

      {timedResults.length > 0 && <div className="statistics-group">
        <h2>Χρονικές δοκιμασίες <span>{timedResults.length}</span></h2>
        <div className="statistics-entries">{timedResults.map((result) => {
          const taskTitle = timedTaskDefinitions.find((task) => task.id === result.taskId)?.title ?? result.taskId
          return <article key={result.id} className="result-entry">
            <div className="result-entry-header">
              <div><strong>{result.userName}</strong><p>{taskTitle} · {result.summary.correctCount}/{result.summary.totalTrials} σωστές · {new Date(result.completedAt).toLocaleString('el-GR')}</p></div>
              <button className="delete-button" type="button" onClick={() => setDeletionTarget({ type: 'timed', id: result.id, label: `${result.userName} · ${taskTitle}` })} aria-label={`Διαγραφή αποτελέσματος για ${result.userName} · ${taskTitle}`}>Διαγραφή</button>
            </div>
            <details><summary>Αναλυτικά αποτελέσματα</summary>
              <ul>{result.trials.map((trial, index) => <li key={`${result.id}-${index}`}>{trial.stimulus}: {trial.response} · {(trial.responseTimeMs / 1000).toFixed(2)}s · {trial.isCorrect ? 'Σωστό' : 'Λάθος'}</li>)}</ul>
            </details>
          </article>
        })}</div>
      </div>}

      {deletionTarget && <div className="modal-backdrop" onClick={() => setDeletionTarget(null)}>
        <section className="start-dialog confirmation-dialog" role="alertdialog" aria-modal="true" aria-labelledby="delete-title" aria-describedby="delete-description" onClick={(event) => event.stopPropagation()}>
          <h2 id="delete-title">Επιβεβαίωση διαγραφής</h2>
          <p id="delete-description">{deletionTarget.type === 'all'
            ? 'Θέλεις να διαγράψεις όλα τα αποθηκευμένα αποτελέσματα; Η ενέργεια δεν αναιρείται.'
            : `Θέλεις να διαγράψεις το αποτέλεσμα για ${deletionTarget.label}; Η ενέργεια δεν αναιρείται.`}</p>
          <div className="confirmation-actions">
            <button className="text-button" type="button" autoFocus onClick={() => setDeletionTarget(null)}>Ακύρωση</button>
            <button className="delete-button confirm-delete" type="button" onClick={confirmDeletion}>{deletionTarget.type === 'all' ? 'Διαγραφή όλων' : 'Διαγραφή'}</button>
          </div>
        </section>
      </div>}
    </section>
  )
}

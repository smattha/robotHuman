import { useEffect, useState } from 'react'
import { exercises } from '../../content/exercises'
import { getPrimaryQuestion } from '../../domain/exercise'
import type { TestResult } from '../../domain/results'
import type { TimedTaskResult } from '../../domain/timed-task'
import { downloadResultsCsv } from './export-results'
import { timedTaskDefinitions } from '../timed-tasks/timed-task-definitions'
import { BADGES, getEarnedBadgeIds } from '../../domain/badges'

type DeletionTarget = { type: 'exercise' | 'timed'; id: string; label: string } | { type: 'all' }

type StatisticsTab = 'summary' | 'list' | 'badges'

type StatisticsScreenProps = {
  results: TestResult[]
  timedResults: TimedTaskResult[]
  onDelete: (type: 'exercise' | 'timed', id: string) => boolean
  onDeleteAll: () => boolean
}

export function StatisticsScreen({ results, timedResults, onDelete, onDeleteAll }: StatisticsScreenProps) {
  const [activeTab, setActiveTab] = useState<StatisticsTab>('summary')
  const [deletionTarget, setDeletionTarget] = useState<DeletionTarget | null>(null)
  const [deletionError, setDeletionError] = useState(false)
  const hasResults = results.length + timedResults.length > 0
  const earnedBadges = getEarnedBadgeIds(results, timedResults)
  const totalAnswers = results.reduce((sum, result) => sum + result.answers.length, 0)
  const correctAnswers = results.reduce((sum, result) => sum + result.answers.filter((answer) => answer.isCorrect).length, 0)

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
      <div className="statistics-heading">
        <div>
          <p className="eyebrow">Αποτελέσματα σε αυτή τη συσκευή</p>
          <h1 id="statistics-title">Στατιστικά</h1>
          <p className="lead">Οι απαντήσεις και οι δοκιμασίες αποθηκεύονται μόνο σε αυτόν τον browser.</p>
        </div>
      </div>

      <div className="tab-bar" role="tablist" aria-label="Ενότητες στατιστικών">
        <button className={`tab-button${activeTab === 'summary' ? ' active' : ''}`} type="button" role="tab" aria-selected={activeTab === 'summary'} onClick={() => setActiveTab('summary')}>✨ Σύνοψη</button>
        <button className={`tab-button${activeTab === 'list' ? ' active' : ''}`} type="button" role="tab" aria-selected={activeTab === 'list'} onClick={() => setActiveTab('list')}>🗂️ Λίστα</button>
        <button className={`tab-button${activeTab === 'badges' ? ' active' : ''}`} type="button" role="tab" aria-selected={activeTab === 'badges'} onClick={() => setActiveTab('badges')}>⭐ Κονκάρδες</button>
      </div>

      {deletionError && <p className="storage-warning" role="alert">Δεν ήταν δυνατή η διαγραφή. Δοκίμασε ξανά.</p>}

      {activeTab === 'summary' && <div className="page-panel" role="tabpanel">
        <div className="stats-summary-grid">
          <div className="stats-summary-card"><strong>{totalAnswers}</strong><span>απαντήσεις σε αποστολές · {totalAnswers > 0 ? Math.round(correctAnswers * 100 / totalAnswers) : 0}% σωστές</span></div>
          <div className="stats-summary-card"><strong>{timedResults.length}</strong><span>χρονικές δοκιμασίες</span></div>
          <div className="stats-summary-card"><strong>{earnedBadges.size}/{BADGES.length}</strong><span>κονκάρδες</span></div>
        </div>
        {!hasResults && <div className="statistics-empty"><span aria-hidden="true">✧</span><h2>Δεν υπάρχουν ακόμα αποτελέσματα</h2><p>Όταν ολοκληρώσεις μια άσκηση, τα στατιστικά της θα εμφανιστούν εδώ.</p></div>}
      </div>}

      {activeTab === 'list' && <div className="page-panel" role="tabpanel">
        {hasResults && <div className="statistics-actions">
          <button className="secondary-button" type="button" onClick={() => downloadResultsCsv(results, timedResults)}>Λήψη CSV</button>
          <button className="secondary-button" type="button" onClick={() => window.print()}>Εκτύπωση</button>
          <button className="delete-button" type="button" onClick={() => setDeletionTarget({ type: 'all' })}>Διαγραφή όλων</button>
        </div>}
        {!hasResults && <div className="statistics-empty"><span aria-hidden="true">✧</span><h2>Δεν υπάρχουν ακόμα αποτελέσματα</h2><p>Όταν ολοκληρώσεις μια άσκηση, τα στατιστικά της θα εμφανιστούν εδώ.</p></div>}
        {results.length > 0 && <div className="statistics-group">
          <h2>Μικρές Αποστολές και Μεγάλη Περιπέτεια <span>{results.length}</span></h2>
          <div className="statistics-entries">{results.map((result) => {
            const isSingle = result.kind === 'single' || (result.kind === undefined && result.answers.length === 1 && result.completedAt === result.startedAt)
            return <article key={result.id} className="result-entry">
              <div className="result-entry-header">
                <div><strong>{result.userName}</strong><p>{isSingle
                  ? exercises.find((exercise) => exercise.id === result.answers[0].exerciseId)?.title ?? 'Μικρή Αποστολή'
                  : 'Μεγάλη Περιπέτεια'} · {result.answers.filter((answer) => answer.isCorrect).length}/{result.answers.length} σωστές · {result.completedAt ? 'Ολοκληρώθηκε' : 'Σε εξέλιξη'} · {new Date(result.completedAt ?? result.startedAt).toLocaleString('el-GR')}</p>{isSingle && <span className="mission-badge"><span aria-hidden="true">★</span> Κονκάρδα: Μικρός Εξερευνητής</span>}</div>
                <button className="delete-button" type="button" onClick={() => setDeletionTarget({ type: 'exercise', id: result.id, label: result.userName })} aria-label={`Διαγραφή αποτελέσματος για ${result.userName}`}>Διαγραφή</button>
              </div>
              <details><summary>Απαντήσεις</summary>
                <ul>{result.answers.map((answer, index) => {
                  const exercise = exercises.find((entry) => entry.id === answer.exerciseId)
                  const option = exercise ? getPrimaryQuestion(exercise).options.find((entry) => entry.id === answer.optionId) : undefined
                  return <li key={`${answer.exerciseId}-${index}`}>{exercise?.title ?? answer.exerciseId}: {option?.detail ?? answer.optionId} · {answer.isCorrect ? 'Σωστό' : 'Λάθος'}</li>
                })}</ul>
              </details>
            </article>
          })}</div>
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
      </div>}

      {activeTab === 'badges' && <div className="page-panel" role="tabpanel">
        <div className="badges-section" aria-labelledby="badges-title">
          <h2 id="badges-title">Κονκάρδες <span>{earnedBadges.size}/{BADGES.length}</span></h2>
          <div className="badge-grid">
            {BADGES.map((badge) => {
              const earned = earnedBadges.has(badge.id)
              return <div className={`badge-card${earned ? ' earned' : ''}`} key={badge.id} aria-label={`${badge.title}${earned ? '' : ' — δεν έχει κερδηθεί ακόμα'}`}>
                <span className="badge-icon" aria-hidden="true">{earned ? badge.icon : '🔒'}</span>
                <strong>{badge.title}</strong>
                <p>{badge.description}</p>
              </div>
            })}
          </div>
        </div>
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
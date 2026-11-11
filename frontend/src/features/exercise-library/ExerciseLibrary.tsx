import { useState } from 'react'
import type { Exercise } from '../../domain/exercise'
import { categoryLabels } from '../../domain/exercise'
import type { TestResult } from '../../domain/results'
import type { TimedTaskId, TimedTaskResult } from '../../domain/timed-task'
import type { TimedTaskDefinition } from '../timed-tasks/timed-task-definitions'
import { ProgressMap } from '../progress-map/ProgressMap'

export type LibraryTab = 'missions' | 'games'

const MISSIONS_PER_PAGE = 3

type ExerciseLibraryProps = {
  exercises: Exercise[]
  exerciseResults: TestResult[]
  timedTaskDefinitions: TimedTaskDefinition[]
  timedTaskResults: TimedTaskResult[]
  activeTab: LibraryTab
  onTabChange: (tab: LibraryTab) => void
  onSelect: (exercise: Exercise) => void
  onTest: (exercise: Exercise) => void
  onSelectTimedTask: (id: TimedTaskId) => void
}

export function ExerciseLibrary({ exercises, exerciseResults, timedTaskDefinitions, timedTaskResults, activeTab, onTabChange, onSelect, onTest, onSelectTimedTask }: ExerciseLibraryProps) {
  const [page, setPage] = useState(0)
  const pageCount = Math.max(1, Math.ceil(exercises.length / MISSIONS_PER_PAGE))
  const pageStart = page * MISSIONS_PER_PAGE
  const visibleExercises = exercises.slice(pageStart, pageStart + MISSIONS_PER_PAGE)

  return (
    <section className="page-section library-hub" aria-labelledby="library-title">
      <div className="tab-bar" role="tablist" aria-label="Βιβλιοθήκη δραστηριοτήτων">
        <button className={`tab-button${activeTab === 'missions' ? ' active' : ''}`} type="button" role="tab" aria-selected={activeTab === 'missions'} onClick={() => onTabChange('missions')}>🗺️ Αποστολές</button>
        <button className={`tab-button${activeTab === 'games' ? ' active' : ''}`} type="button" role="tab" aria-selected={activeTab === 'games'} onClick={() => { onTabChange('games'); setPage(0) }}>🧠 Παιχνίδια σκέψης</button>
      </div>

      {activeTab === 'missions' && <div className="page-panel" role="tabpanel">
        <ProgressMap compact exercises={exercises} exerciseResults={exerciseResults} timedTaskDefinitions={timedTaskDefinitions} timedTaskResults={timedTaskResults} />
        <div className="section-heading">
          <div>
            <p className="eyebrow">Ο δικός σου χάρτης περιπέτειας</p>
            <h1 id="library-title">Ποια αποστολή θα διαλέξεις;</h1>
          </div>
          <span className="counter">{exercises.length} αποστολές σε περιμένουν ✨</span>
        </div>
        <div className="exercise-grid">
          {visibleExercises.map((exercise) => (
            <article className="exercise-card compact" key={exercise.id}>
              <div className="exercise-icon" aria-hidden="true">{['🔍', '🧩', '🎨', '🧠', '🌟'][exercises.indexOf(exercise) % 5]}</div>
              <div className="exercise-card-copy">
                <p className="card-category">Μικρή αποστολή · {categoryLabels[exercise.category]}</p>
                <h2>{exercise.title}</h2>
                <p>{exercise.description}</p>
              </div>
              <div className="exercise-card-actions">
                <button className="secondary-button" type="button" onClick={() => onSelect(exercise)}>Παίξε και κράτησε την πρόοδο <span aria-hidden="true">→</span></button>
                <button className="secondary-button test-button" type="button" onClick={() => onTest(exercise)}>Δοκιμή χωρίς καταγραφή</button>
              </div>
            </article>
          ))}
        </div>
        {pageCount > 1 && <div className="page-dots" role="group" aria-label="Σελίδες αποστολών">
          {Array.from({ length: pageCount }, (_, index) => (
            <button className={`page-dot${page === index ? ' active' : ''}`} type="button" aria-label={`Σελίδα ${index + 1}`} aria-current={page === index ? 'page' : undefined} onClick={() => setPage(index)}>{index + 1}</button>
          ))}
        </div>}
      </div>}

      {activeTab === 'games' && <div className="page-panel" role="tabpanel" aria-label="Προκλήσεις Μνήμης και Προσοχής">
        <div className="section-heading">
          <div>
            <p className="eyebrow">Δραστηριότητες μνήμης και προσοχής</p>
            <h2 id="timed-tasks-title">Προκλήσεις Μνήμης και Προσοχής</h2>
          </div>
        </div>
        <div className="timed-task-grid">
          {timedTaskDefinitions.map((task) => (
            <article className="timed-task-card" key={task.id}>
              <div className="exercise-icon" aria-hidden="true">{task.icon}</div>
              <p className="card-category">{task.category}</p>
              <h3>{task.title}</h3>
              <p>{task.description}</p>
              <button className="secondary-button" type="button" onClick={() => onSelectTimedTask(task.id)}>Ξεκίνα δοκιμασία <span aria-hidden="true">↗</span></button>
            </article>
          ))}
        </div>
      </div>}
    </section>
  )
}
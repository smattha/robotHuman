import type { Exercise } from '../../domain/exercise'
import type { TestResult } from '../../domain/results'
import type { TimedTaskResult } from '../../domain/timed-task'
import type { TimedTaskDefinition } from '../timed-tasks/timed-task-definitions'
import { ProgressMap } from '../progress-map/ProgressMap'

type ExerciseLibraryProps = {
  exercises: Exercise[]
  exerciseResults: TestResult[]
  timedTaskDefinitions: TimedTaskDefinition[]
  timedTaskResults: TimedTaskResult[]
  onSelect: (exercise: Exercise) => void
}

export function ExerciseLibrary({ exercises, exerciseResults, timedTaskDefinitions, timedTaskResults, onSelect }: ExerciseLibraryProps) {
  return (
    <section className="page-section library-section" aria-labelledby="library-title">
      <div className="section-heading">
        <div>
          <p className="eyebrow">Ο δικός σου χάρτης περιπέτειας</p>
          <h1 id="library-title">Ποια αποστολή θα διαλέξεις;</h1>
        </div>
        <span className="counter">{exercises.length} αποστολές σε περιμένουν ✨</span>
      </div>
      <ProgressMap exercises={exercises} exerciseResults={exerciseResults} timedTaskDefinitions={timedTaskDefinitions} timedTaskResults={timedTaskResults} />
      <div className="exercise-grid">
        {exercises.map((exercise) => (
          <article className="exercise-card" key={exercise.id}>
            <div className="exercise-icon" aria-hidden="true">{['🔍', '🧩', '🎨', '🧠', '🌟'][exercises.indexOf(exercise) % 5]}</div>
            <div className="exercise-card-copy">
              <p className="card-category">Μικρή αποστολή · {exercise.category}</p>
              <h2>{exercise.title}</h2>
              <p>{exercise.description}</p>
            </div>
            <button className="secondary-button" type="button" onClick={() => onSelect(exercise)}>Δοκίμασέ την <span aria-hidden="true">→</span></button>
          </article>
        ))}
      </div>
    </section>
  )
}

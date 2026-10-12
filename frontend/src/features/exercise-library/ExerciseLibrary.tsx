import type { Exercise } from '../../domain/exercise'

type ExerciseLibraryProps = {
  exercises: Exercise[]
  onSelect: (exercise: Exercise) => void
}

export function ExerciseLibrary({ exercises, onSelect }: ExerciseLibraryProps) {
  return (
    <section className="page-section library-section" aria-labelledby="library-title">
      <div className="section-heading">
        <div>
          <p className="eyebrow">Η γωνιά των αποστολών</p>
          <h1 id="library-title">Διάλεξε μια αποστολή</h1>
        </div>
        <span className="counter">{exercises.length} διαθέσιμες</span>
      </div>
      <div className="exercise-grid">
        {exercises.map((exercise) => (
          <article className="exercise-card" key={exercise.id}>
            <div className="exercise-icon" aria-hidden="true">♢</div>
            <div className="exercise-card-copy">
              <p className="card-category">{exercise.category}</p>
              <h2>{exercise.title}</h2>
              <p>{exercise.description}</p>
            </div>
            <button className="secondary-button" type="button" onClick={() => onSelect(exercise)}>Παίξε τώρα <span aria-hidden="true">↗</span></button>
          </article>
        ))}
      </div>
    </section>
  )
}

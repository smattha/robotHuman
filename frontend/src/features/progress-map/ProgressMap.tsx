import type { Exercise } from '../../domain/exercise'
import type { TestResult } from '../../domain/results'
import type { TimedTaskResult } from '../../domain/timed-task'
import type { TimedTaskDefinition } from '../timed-tasks/timed-task-definitions'

type ProgressMapProps = {
  exercises: Exercise[]
  exerciseResults: TestResult[]
  timedTaskDefinitions: TimedTaskDefinition[]
  timedTaskResults: TimedTaskResult[]
}

function hasCompletedExercise(exerciseId: string, results: TestResult[]): boolean {
  return results.some((result) => result.answers.some((answer) => answer.exerciseId === exerciseId))
}

function hasCompletedTimedTask(taskId: string, results: TimedTaskResult[]): boolean {
  return results.some((result) => result.taskId === taskId)
}

export function ProgressMap({ exercises, exerciseResults, timedTaskDefinitions, timedTaskResults }: ProgressMapProps) {
  const completedExercises = exercises.filter((exercise) => hasCompletedExercise(exercise.id, exerciseResults)).length
  const completedTimedTasks = timedTaskDefinitions.filter((task) => hasCompletedTimedTask(task.id, timedTaskResults)).length

  return (
    <section className="progress-map" aria-labelledby="progress-map-title">
      <div className="progress-map-heading">
        <div>
          <p className="eyebrow">Τα κατορθώματά σου</p>
          <h2 id="progress-map-title">Ο χάρτης της περιπέτειάς σου</h2>
          <p>Κάθε αστεράκι θυμίζει κάτι καινούριο που δοκίμασες. Προχωράς με τον δικό σου ρυθμό!</p>
        </div>
        <span className="progress-map-star" aria-hidden="true">✦</span>
      </div>
      <div className="progress-map-groups">
        <div className="progress-map-group">
          <div className="progress-map-group-heading">
            <h3>Μικρές Αποστολές</h3>
            <span>{completedExercises} / {exercises.length}</span>
          </div>
          <ol className="progress-map-nodes" aria-label={`Ολοκληρώθηκαν ${completedExercises} από ${exercises.length} Μικρές Αποστολές`}>
            {exercises.map((exercise, index) => {
              const completed = hasCompletedExercise(exercise.id, exerciseResults)
              return <li className={completed ? 'completed' : ''} key={exercise.id} title={exercise.title} aria-label={`${exercise.title}: ${completed ? 'ολοκληρώθηκε' : 'δεν έχει ολοκληρωθεί'}`}><span>{completed ? '★' : index + 1}</span></li>
            })}
          </ol>
        </div>
        <div className="progress-map-group">
          <div className="progress-map-group-heading">
            <h3>Προκλήσεις Μνήμης</h3>
            <span>{completedTimedTasks} / {timedTaskDefinitions.length}</span>
          </div>
          <ol className="progress-map-nodes timed" aria-label={`Ολοκληρώθηκαν ${completedTimedTasks} από ${timedTaskDefinitions.length} Προκλήσεις Μνήμης`}>
            {timedTaskDefinitions.map((task) => {
              const completed = hasCompletedTimedTask(task.id, timedTaskResults)
              return <li className={completed ? 'completed' : ''} key={task.id} title={task.title} aria-label={`${task.title}: ${completed ? 'ολοκληρώθηκε' : 'δεν έχει ολοκληρωθεί'}`}><span>{completed ? '★' : task.icon}</span></li>
            })}
          </ol>
        </div>
      </div>
    </section>
  )
}

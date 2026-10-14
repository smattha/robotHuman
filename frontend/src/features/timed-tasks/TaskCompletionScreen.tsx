import type { TimedTaskResult } from '../../domain/timed-task'
import type { ChildHelper } from '../../domain/preferences'
import { timedTaskDefinitions } from './timed-task-definitions'

type TaskCompletionScreenProps = {
  result: TimedTaskResult
  saved: boolean
  onStatistics: () => void
  onBack: () => void
  helper: ChildHelper
}

const helperIcons: Record<ChildHelper, string> = { robot: '🤖', fox: '🦊', owl: '🦉', unicorn: '🦄' }

export function TaskCompletionScreen({ result, saved, onStatistics, onBack, helper }: TaskCompletionScreenProps) {
  const taskTitle = timedTaskDefinitions.find((task) => task.id === result.taskId)?.title ?? result.taskId

  return (
    <section className="page-section completion-screen" aria-labelledby="task-completion-title">
      <div className="completion-confetti" aria-hidden="true">✦ ✧ ✦</div>
      <div className="child-helper" aria-hidden="true">{helperIcons[helper]}</div>
      <div className="completion-icon" aria-hidden="true">✓</div>
      <p className="eyebrow">{taskTitle}</p>
      <h1 id="task-completion-title">Ολοκλήρωσες το παιχνίδι!</h1>
      <p className="lead">Μπράβο, {result.userName}! Έκανες {result.summary.totalTrials} γύρους και έδωσες τον καλύτερό σου εαυτό.</p>
      <p>{saved ? 'Το αποτέλεσμα αποθηκεύτηκε σε αυτή τη συσκευή.' : 'Δεν ήταν δυνατή η αποθήκευση του αποτελέσματος σε αυτή τη συσκευή.'}</p>
      <div className="completion-actions">
        <button className="primary-button" type="button" onClick={onStatistics}>Δες τα στατιστικά</button>
        <button className="text-button" type="button" onClick={onBack}>Πίσω στις ασκήσεις</button>
      </div>
    </section>
  )
}

import type { TimedTaskDefinition } from './timed-task-definitions'
import type { ChildHelper } from '../../domain/preferences'

type TaskPreparationScreenProps = {
  task: TimedTaskDefinition
  userName: string
  onContinue: () => void
  onBack: () => void
  helper: ChildHelper
}

const helperIcons: Record<ChildHelper, string> = { robot: '🤖', fox: '🦊', owl: '🦉', unicorn: '🦄' }

export function TaskPreparationScreen({ task, userName, onContinue, onBack, helper }: TaskPreparationScreenProps) {
  return (
    <section className="page-section task-transition" aria-labelledby="task-preparation-title">
      <div className="task-transition-card">
        <span className="task-transition-icon" aria-hidden="true">{task.icon}</span>
        <span className="child-helper" aria-hidden="true">{helperIcons[helper]}</span>
        <p className="eyebrow">Επόμενη δοκιμασία · {task.category}</p>
        <h1 id="task-preparation-title">Ετοιμάσου για το {task.title}</h1>
        <p className="lead">{task.description}</p>
        <p className="task-user">Παίκτης: {userName}</p>
        <p>Στην επόμενη οθόνη θα διαβάσεις τις οδηγίες. Η δοκιμασία ξεκινά μόνο όταν πατήσεις «Ξεκίνα».</p>
        <div className="task-transition-actions">
          <button className="primary-button" type="button" onClick={onContinue}>Δες τις οδηγίες <span aria-hidden="true">→</span></button>
          <button className="text-button" type="button" onClick={onBack}>Πίσω στις ασκήσεις</button>
        </div>
      </div>
    </section>
  )
}

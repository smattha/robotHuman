import type { TimedTaskId } from '../../domain/timed-task'
import type { ChildHelper } from '../../domain/preferences'
import type { TimedTaskDefinition } from './timed-task-definitions'

type PracticeContent = {
  instruction: string
  example: string
  reminder: string
}

const practiceContent: Record<TimedTaskId, PracticeContent> = {
  stroop: {
    instruction: 'Πάτησε μόνο όταν το χρώμα της λέξης ταιριάζει με αυτό που λέει η λέξη.',
    example: 'Η λέξη «Κόκκινο» γραμμένη με κόκκινο χρώμα σημαίνει: πατάω.',
    reminder: 'Αν η λέξη και το χρώμα δεν ταιριάζουν, περιμένω.',
  },
  'go-no-go': {
    instruction: 'Πάτησε μόνο όταν δεις «Ξεκίνα».',
    example: 'Όταν δεις «Ξεκίνα», πατάς το κουμπί.',
    reminder: 'Όταν δεις «Στοπ», δεν πατάς.',
  },
  sart: {
    instruction: 'Πάτησε σε κάθε εικόνα, εκτός από το μήλο.',
    example: 'Για τη μπάλα ή το αυτοκίνητο, πατάς το κουμπί.',
    reminder: 'Για το μήλο, δεν πατάς.',
  },
  corsi: {
    instruction: 'Παρακολούθησε ποια πλακίδια φωτίζονται και πάτησέ τα με την ίδια σειρά.',
    example: 'Αν φωτιστούν πρώτα το 2 και μετά το 5, πατάς 2 και μετά 5.',
    reminder: 'Περίμενε να τελειώσει η φωτεινή σειρά πριν απαντήσεις.',
  },
  'digit-span': {
    instruction: 'Θυμήσου τα ψηφία και πληκτρολόγησέ τα με την ίδια σειρά.',
    example: 'Αν δεις 4 και μετά 7, γράφεις 47.',
    reminder: 'Περίμενε να κρυφτούν τα ψηφία πριν απαντήσεις.',
  },
}

type TaskPracticeScreenProps = {
  task: TimedTaskDefinition
  onStart: () => void
  onBack: () => void
  helper: ChildHelper
}

const helperIcons: Record<ChildHelper, string> = { robot: '🤖', fox: '🦊', owl: '🦉', unicorn: '🦄' }

export function TaskPracticeScreen({ task, onStart, onBack, helper }: TaskPracticeScreenProps) {
  const content = practiceContent[task.id]
  return (
    <section className="page-section task-practice" aria-labelledby="practice-title">
      <div className="task-practice-card">
        <span className="task-transition-icon" aria-hidden="true">{task.icon}</span>
        <span className="child-helper" aria-hidden="true">{helperIcons[helper]}</span>
        <p className="eyebrow">Δοκιμαστικός γύρος · δεν καταγράφεται</p>
        <h1 id="practice-title">Ας κάνουμε μία πρόβα</h1>
        <p className="lead">{content.instruction}</p>
        <div className="practice-example">
          <span aria-hidden="true">💡</span>
          <p>{content.example}</p>
        </div>
        <p className="practice-reminder">{content.reminder}</p>
        <div className="task-transition-actions">
          <button className="primary-button" type="button" onClick={onStart}>Ξεκίνα την κανονική δοκιμασία <span aria-hidden="true">→</span></button>
          <button className="text-button" type="button" onClick={onBack}>Πίσω στις ασκήσεις</button>
        </div>
      </div>
    </section>
  )
}

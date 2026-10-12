import type { TaskSummary, TimedTaskId, Trial } from '../../domain/timed-task'
import { createSartState, getSartSummary, respondSart, startSart, tickSart } from './sart-logic'
import { TimedTaskFrame } from './TimedTaskFrame'
import { useTimedTask } from './use-timed-task'

type SartTaskProps = {
  userName: string
  onExit: () => void
  onComplete: (taskId: TimedTaskId, trials: Trial[], summary: TaskSummary) => void
}

export function SartTask({ userName, onExit, onComplete }: SartTaskProps) {
  const { state, setState } = useTimedTask({
    create: createSartState,
    tick: tickSart,
    isFinished: (current) => current.phase === 'finished',
    report: (current) => onComplete('sart', current.trials, getSartSummary(current)),
  })

  return (
    <TimedTaskFrame title="SART" category="Προσοχή" onExit={onExit}>
      {state.phase === 'instruction' && (
        <div className="task-instruction">
          <p className="lead">Θα εμφανίζονται διάφορες εικόνες. Πάτησε «Απόκριση» σε κάθε εικόνα, εκτός από το μήλο. Έχεις ένα λεπτό.</p>
          <p className="task-user">Παίκτης: {userName}</p>
          <button className="primary-button" type="button" onClick={() => setState((previous) => startSart(previous, Date.now()))}>Ξεκίνα</button>
        </div>
      )}
      {state.phase === 'running' && (
        <div className="task-running">
          <div className="sart-stimulus" aria-label={state.isApple ? 'Μήλο' : 'Αντικείμενο'}>{state.stimulus}</div>
          <button className="primary-button full-width" type="button" onClick={() => setState((previous) => respondSart(previous, Date.now()))}>Απόκριση</button>
        </div>
      )}
    </TimedTaskFrame>
  )
}

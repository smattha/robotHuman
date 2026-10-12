import type { TaskSummary, TimedTaskId, Trial } from '../../domain/timed-task'
import { createGoNoGoState, getGoNoGoSummary, respondGoNoGo, startGoNoGo, tickGoNoGo } from './go-no-go-logic'
import { TimedTaskFrame } from './TimedTaskFrame'
import { useTimedTask } from './use-timed-task'

type GoNoGoTaskProps = {
  userName: string
  onExit: () => void
  onComplete: (taskId: TimedTaskId, trials: Trial[], summary: TaskSummary) => void
}

export function GoNoGoTask({ userName, onExit, onComplete }: GoNoGoTaskProps) {
  const { state, setState } = useTimedTask({
    create: createGoNoGoState,
    tick: tickGoNoGo,
    isFinished: (current) => current.phase === 'finished',
    report: (current) => onComplete('go-no-go', current.trials, getGoNoGoSummary(current)),
  })

  return (
    <TimedTaskFrame title="Go / No-Go" category="Προσοχή" onExit={onExit}>
      {state.phase === 'instruction' && (
        <div className="task-instruction">
          <p className="lead">Θα εμφανίζονται οι λέξεις «Ξεκίνα» και «Στοπ». Πάτησε «Απόκριση» μόνο όταν βλέπεις «Ξεκίνα» και μην πατάς όταν βλέπεις «Στοπ».</p>
          <p className="task-user">Παίκτης: {userName}</p>
          <button className="primary-button" type="button" onClick={() => setState((previous) => startGoNoGo(previous, Date.now()))}>Ξεκίνα</button>
        </div>
      )}
      {state.phase === 'running' && (
        <div className="task-running">
          <div className={`go-nogo-word ${state.isGo ? 'go' : 'nogo'}`}>{state.isGo ? 'Ξεκίνα' : 'Στοπ'}</div>
          <button className="primary-button full-width" type="button" onClick={() => setState((previous) => respondGoNoGo(previous, Date.now()))}>Απόκριση</button>
        </div>
      )}
    </TimedTaskFrame>
  )
}

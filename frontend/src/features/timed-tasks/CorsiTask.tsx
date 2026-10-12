import type { TaskSummary, TimedTaskId, Trial } from '../../domain/timed-task'
import { createCorsiState, getCorsiSummary, respondCorsi, startCorsi, tickCorsi } from './corsi-logic'
import { TimedTaskFrame } from './TimedTaskFrame'
import { useTimedTask } from './use-timed-task'

type CorsiTaskProps = {
  userName: string
  onExit: () => void
  onComplete: (taskId: TimedTaskId, trials: Trial[], summary: TaskSummary) => void
}

export function CorsiTask({ userName, onExit, onComplete }: CorsiTaskProps) {
  const { state, setState } = useTimedTask({
    create: createCorsiState,
    tick: tickCorsi,
    isFinished: (current) => current.phase === 'finished',
    report: (current) => onComplete('corsi', current.trials, getCorsiSummary(current)),
  })

  return (
    <TimedTaskFrame title="Corsi" category="Μνήμη" onExit={onExit}>
      {state.phase === 'instruction' && (
        <div className="task-instruction">
          <p className="lead">Θα εμφανιστούν εννέα πλακίδια. Παρακολούθησε τη σειρά που φωτίζονται και πάτησέ τα με την ίδια σειρά. Κάθε σωστή απάντηση προσθέτει ένα πλακίδιο.</p>
          <p className="task-user">Παίκτης: {userName}</p>
          <button className="primary-button" type="button" onClick={() => setState((previous) => startCorsi(previous, Date.now()))}>Ξεκίνα</button>
        </div>
      )}
      {(state.phase === 'showing' || state.phase === 'answering') && (
        <div className="sequence-task">
          <p className="sequence-status" aria-live="polite">
            {state.phase === 'showing' ? 'Παρακολούθησε τη σειρά' : 'Επανάλαβε τη σειρά'} · επίπεδο {state.level}
          </p>
          <div className="corsi-board" aria-label="Πίνακας με εννέα πλακίδια">
            {Array.from({ length: 9 }, (_, tile) => (
              <button
                className={`corsi-tile${state.phase === 'showing' && state.sequenceIndex > 0 && state.sequence[state.sequenceIndex - 1] === tile ? ' active' : ''}`}
                key={tile}
                type="button"
                disabled={state.phase !== 'answering'}
                aria-label={`Πλακίδιο ${tile + 1}`}
                onClick={() => setState((previous) => respondCorsi(previous, tile, Date.now()))}
              >{tile + 1}</button>
            ))}
          </div>
          <p className="sequence-status" aria-live="polite">{state.phase === 'answering' ? `Επιλογές: ${state.answer.length} / ${state.sequence.length}` : ' '}</p>
        </div>
      )}
    </TimedTaskFrame>
  )
}

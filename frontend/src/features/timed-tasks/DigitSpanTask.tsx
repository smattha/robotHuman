import type { TaskSummary, TimedTaskId, Trial } from '../../domain/timed-task'
import { clearDigit, createDigitSpanState, enterDigit, getDigitSpanSummary, startDigitSpan, submitDigitSpan, tickDigitSpan } from './digit-span-logic'
import { TimedTaskFrame } from './TimedTaskFrame'
import { useTimedTask } from './use-timed-task'

type DigitSpanTaskProps = {
  userName: string
  onExit: () => void
  onComplete: (taskId: TimedTaskId, trials: Trial[], summary: TaskSummary) => void
}

export function DigitSpanTask({ userName, onExit, onComplete }: DigitSpanTaskProps) {
  const { state, setState } = useTimedTask({
    create: createDigitSpanState,
    tick: tickDigitSpan,
    isFinished: (current) => current.phase === 'finished',
    report: (current) => onComplete('digit-span', current.trials, getDigitSpanSummary(current)),
  })

  return (
    <TimedTaskFrame title="Digit Span" category="Μνήμη" onExit={onExit}>
      {state.phase === 'instruction' && (
        <div className="task-instruction">
          <p className="lead">Θα εμφανιστεί μια ακολουθία ψηφίων. Θυμήσου την και πληκτρολόγησέ την με την ίδια σειρά. Η ακολουθία μεγαλώνει μετά από κάθε σωστή απάντηση. Το παιχνίδι τελειώνει μετά από δύο διαδοχικά λάθη.</p>
          <p className="task-user">Παίκτης: {userName}</p>
          <button className="primary-button" type="button" onClick={() => setState((previous) => startDigitSpan(previous, Date.now()))}>Ξεκίνα</button>
        </div>
      )}
      {(state.phase === 'showing' || state.phase === 'answering') && (
        <div className="sequence-task">
          <p className="sequence-status" aria-live="polite">
            {state.phase === 'showing' ? 'Θυμήσου τα ψηφία' : 'Πληκτρολόγησε τη σειρά'} · επίπεδο {state.level}
          </p>
          <div className="digit-stimulus" aria-live="assertive" aria-label={state.phase === 'showing' ? `Ψηφίο ${state.sequence[state.sequenceIndex - 1] ?? ''}` : 'Τα ψηφία έχουν κρυφτεί'}>
            {state.phase === 'showing' ? state.sequence[state.sequenceIndex - 1] ?? ' ' : '•••'}
          </div>
          {state.phase === 'answering' && (
            <>
              <output className="digit-answer" aria-label="Η απάντησή σου">{state.answer || ' '}</output>
              <div className="digit-keypad">
                {['1', '2', '3', '4', '5', '6', '7', '8', '9', 'clear', '0', 'submit'].map((key) => (
                  <button
                    className={key === 'submit' ? 'primary-button' : 'digit-key'}
                    key={key}
                    type="button"
                    disabled={key === 'submit' && state.answer.length === 0}
                    onClick={() => {
                      if (key === 'clear') setState((previous) => clearDigit(previous))
                      else if (key === 'submit') setState((previous) => submitDigitSpan(previous, Date.now()))
                      else setState((previous) => enterDigit(previous, key))
                    }}
                  >{key === 'clear' ? 'Διόρθωση' : key === 'submit' ? 'Συνέχεια' : key}</button>
                ))}
              </div>
            </>
          )}
        </div>
      )}
    </TimedTaskFrame>
  )
}

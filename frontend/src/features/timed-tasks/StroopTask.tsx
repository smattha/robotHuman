import type { TaskSummary, TimedTaskId, Trial } from '../../domain/timed-task'
import { COLOR_WORDS, createStroopState, getStroopSummary, respondStroop, startStroop, tickStroop } from './stroop-logic'
import type { StroopColor } from './stroop-logic'
import { TimedTaskFrame } from './TimedTaskFrame'
import { useTimedTask } from './use-timed-task'

const INK_COLORS: Record<StroopColor, string> = {
  red: '#d64545',
  green: '#3f9d5a',
  blue: '#3a6fd8',
  yellow: '#d9a400',
}

type StroopTaskProps = {
  userName: string
  onExit: () => void
  onComplete: (taskId: TimedTaskId, trials: Trial[], summary: TaskSummary) => void
}

export function StroopTask({ userName, onExit, onComplete }: StroopTaskProps) {
  const { state, setState } = useTimedTask({
    create: createStroopState,
    tick: tickStroop,
    isFinished: (current) => current.phase === 'finished',
    report: (current) => onComplete('stroop', current.trials, getStroopSummary(current)),
  })

  return (
    <TimedTaskFrame title="Stroop" category="Προσοχή" onExit={onExit}>
      {state.phase === 'instruction' && (
        <div className="task-instruction">
          <p className="lead">Θα εμφανίζονται λέξεις χρωμάτων. Πάτησε «Απόκριση» μόνο όταν το χρώμα με το οποίο γράφεται η λέξη ταιριάζει με το νόημά της.</p>
          <p className="task-user">Παίκτης: {userName}</p>
          <button className="primary-button" type="button" onClick={() => setState((previous) => startStroop(previous, Date.now()))}>Ξεκίνα</button>
        </div>
      )}
      {state.phase === 'running' && (
        <div className="task-running">
          <div className="stroop-word" style={{ color: INK_COLORS[state.ink] }}>{COLOR_WORDS[state.word]}</div>
          <button className="primary-button full-width" type="button" onClick={() => setState((previous) => respondStroop(previous, Date.now()))}>Απόκριση</button>
        </div>
      )}
    </TimedTaskFrame>
  )
}

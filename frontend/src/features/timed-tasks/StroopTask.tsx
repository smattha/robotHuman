import type { ChildHelper, NarrationMode } from '../../domain/preferences'
import type { TaskSummary, TimedTaskId, Trial } from '../../domain/timed-task'
import { InstructionBriefing } from './InstructionBriefing'
import { createStroopState, getStroopSummary, respondStroop, startStroop, tickStroop } from './stroop-logic'
import { PhaserGame } from '../phaser/PhaserGame'
import { StroopScene } from './phaser/StroopScene'
import { TimedTaskFrame } from './TimedTaskFrame'
import { useTimedTask } from './use-timed-task'

type StroopTaskProps = {
  userName: string
  onExit: () => void
  onComplete: (taskId: TimedTaskId, trials: Trial[], summary: TaskSummary) => void
  helper: ChildHelper
  narrationMode: NarrationMode
  speechEnabled: boolean
}

const INSTRUCTION =
  'Θα εμφανίζονται λέξεις χρωμάτων. Πάτησε «Απόκριση» μόνο όταν το χρώμα με το οποίο γράφεται η λέξη ταιριάζει με το νόημά της.'

export function StroopTask({ userName, onExit, onComplete, helper, narrationMode, speechEnabled }: StroopTaskProps) {
  const { state, setState } = useTimedTask({
    create: createStroopState,
    tick: tickStroop,
    isFinished: (current) => current.phase === 'finished',
    report: (current) => onComplete('stroop', current.trials, getStroopSummary(current)),
  })

  return (
    <TimedTaskFrame title="Stroop" category="Προσοχή" onExit={onExit}>
      {state.phase === 'instruction' && (
        <InstructionBriefing
          helper={helper}
          message={INSTRUCTION}
          userName={userName}
          narrationMode={narrationMode}
          speechEnabled={speechEnabled}
          onStart={() => setState((previous) => startStroop(previous, Date.now()))}
        />
      )}
      {state.phase !== 'instruction' && (
        <PhaserGame
          scene={StroopScene}
          sceneProps={{
            phase: state.phase,
            word: state.word,
            ink: state.ink,
            trialStartedAt: state.trialStartedAt,
            helper,
            onRespond: () => setState((previous) => respondStroop(previous, Date.now())),
          }}
          testId="stroop-game"
          ariaLabel="Παιχνίδι προσοχής με τα μαγικά χρώματα"
        />
      )}
    </TimedTaskFrame>
  )
}

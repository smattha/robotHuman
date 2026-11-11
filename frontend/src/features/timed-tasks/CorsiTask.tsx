import type { ChildHelper, NarrationMode } from '../../domain/preferences'
import type { TaskSummary, TimedTaskId, Trial } from '../../domain/timed-task'
import { InstructionBriefing } from './InstructionBriefing'
import { createCorsiState, getCorsiSummary, respondCorsi, startCorsi, tickCorsi } from './corsi-logic'
import { CorsiScene } from './phaser/CorsiScene'
import { PhaserGame } from '../phaser/PhaserGame'
import { TimedTaskFrame } from './TimedTaskFrame'
import { useTimedTask } from './use-timed-task'

type CorsiTaskProps = {
  userName: string
  onExit: () => void
  onComplete: (taskId: TimedTaskId, trials: Trial[], summary: TaskSummary) => void
  helper: ChildHelper
  narrationMode: NarrationMode
  speechEnabled: boolean
}

const INSTRUCTION =
  'Θα φωτίσουν μανιτάρια ένα-ένα σε μια σειρά. Θυμήσου τη σειρά και πάτησέ τα με την ίδια σειρά. Κάθε σωστή απάντηση προσθέτει ένα μανιτάρι.'

export function CorsiTask({ userName, onExit, onComplete, helper, narrationMode, speechEnabled }: CorsiTaskProps) {
  const { state, setState } = useTimedTask({
    create: createCorsiState,
    tick: tickCorsi,
    isFinished: (current) => current.phase === 'finished',
    report: (current) => onComplete('corsi', current.trials, getCorsiSummary(current)),
  })

  return (
    <TimedTaskFrame title="Corsi" category="Μνήμη" onExit={onExit}>
      {state.phase === 'instruction' && (
        <InstructionBriefing
          helper={helper}
          message={INSTRUCTION}
          userName={userName}
          narrationMode={narrationMode}
          speechEnabled={speechEnabled}
          onStart={() => setState((previous) => startCorsi(previous, Date.now()))}
        />
      )}
      {state.phase !== 'instruction' && (
        <PhaserGame
          scene={CorsiScene}
          sceneProps={{
            phase: state.phase,
            sequence: state.sequence,
            sequenceIndex: state.sequenceIndex,
            level: state.level,
            answerLength: state.answer.length,
            helper,
            onTapTile: (tile: number) => setState((previous) => respondCorsi(previous, tile, Date.now())),
          }}
          testId="corsi-game"
          ariaLabel="Παιχνίδι μνήμης με μανιτάρια"
        />
      )}
    </TimedTaskFrame>
  )
}

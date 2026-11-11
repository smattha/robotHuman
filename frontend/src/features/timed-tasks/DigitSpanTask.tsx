import type { ChildHelper, NarrationMode } from '../../domain/preferences'
import type { TaskSummary, TimedTaskId, Trial } from '../../domain/timed-task'
import { InstructionBriefing } from './InstructionBriefing'
import { clearDigit, createDigitSpanState, enterDigit, getDigitSpanSummary, startDigitSpan, submitDigitSpan, tickDigitSpan } from './digit-span-logic'
import { DigitSpanScene } from './phaser/DigitSpanScene'
import { PhaserGame } from '../phaser/PhaserGame'
import { TimedTaskFrame } from './TimedTaskFrame'
import { useTimedTask } from './use-timed-task'

type DigitSpanTaskProps = {
  userName: string
  onExit: () => void
  onComplete: (taskId: TimedTaskId, trials: Trial[], summary: TaskSummary) => void
  helper: ChildHelper
  narrationMode: NarrationMode
  speechEnabled: boolean
}

const INSTRUCTION =
  'Θα εμφανιστούν ψηφία ένα-ένα σε ένα αστέρι. Θυμήσου τη σειρά και πληκτρολόγησέ την με τα κουμπιά. Η ακολουθία μεγαλώνει μετά από κάθε σωστή απάντηση. Το παιχνίδι τελειώνει μετά από δύο διαδοχικά λάθη.'

export function DigitSpanTask({ userName, onExit, onComplete, helper, narrationMode, speechEnabled }: DigitSpanTaskProps) {
  const { state, setState } = useTimedTask({
    create: createDigitSpanState,
    tick: tickDigitSpan,
    isFinished: (current) => current.phase === 'finished',
    report: (current) => onComplete('digit-span', current.trials, getDigitSpanSummary(current)),
  })

  return (
    <TimedTaskFrame title="Digit Span" category="Μνήμη" onExit={onExit}>
      {state.phase === 'instruction' && (
        <InstructionBriefing
          helper={helper}
          message={INSTRUCTION}
          userName={userName}
          narrationMode={narrationMode}
          speechEnabled={speechEnabled}
          onStart={() => setState((previous) => startDigitSpan(previous, Date.now()))}
        />
      )}
      {state.phase !== 'instruction' && (
        <PhaserGame
          scene={DigitSpanScene}
          sceneProps={{
            phase: state.phase,
            sequence: state.sequence,
            sequenceIndex: state.sequenceIndex,
            level: state.level,
            answer: state.answer,
            helper,
            onEnterDigit: (digit: string) => setState((previous) => enterDigit(previous, digit)),
            onClear: () => setState((previous) => clearDigit(previous)),
            onSubmit: () => setState((previous) => submitDigitSpan(previous, Date.now())),
          }}
          testId="digit-span-game"
          ariaLabel="Παιχνίδι μνήμης με τα μαγικά αστέρια"
        />
      )}
    </TimedTaskFrame>
  )
}

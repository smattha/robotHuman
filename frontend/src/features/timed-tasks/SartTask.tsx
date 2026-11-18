import type { ChildHelper, NarrationMode } from '../../domain/preferences'
import type { TaskSummary, TimedTaskId, Trial } from '../../domain/timed-task'
import { InstructionBriefing } from './InstructionBriefing'
import { createSartState, getSartSummary, respondSart, startSart, tickSart } from './sart-logic'
import { SartBoard } from './SartBoard'
import { TimedTaskFrame } from './TimedTaskFrame'
import { useTimedTask } from './use-timed-task'

type SartTaskProps = {
  userName: string
  onExit: () => void
  onComplete: (taskId: TimedTaskId, trials: Trial[], summary: TaskSummary) => void
  helper: ChildHelper
  narrationMode: NarrationMode
  speechEnabled: boolean
}

const INSTRUCTION = 'Θα εμφανίζονται διάφορα αντικείμενα στο καλάθι. Πάτησε «Απόκριση» σε κάθε αντικείμενο, εκτός από το μήλο. Έχεις ένα λεπτό.'

export function SartTask({ userName, onExit, onComplete, helper, narrationMode, speechEnabled }: SartTaskProps) {
  const { state, setState } = useTimedTask({
    create: createSartState,
    tick: tickSart,
    isFinished: (current) => current.phase === 'finished',
    report: (current) => onComplete('sart', current.trials, getSartSummary(current)),
  })

  return (
    <TimedTaskFrame title="SART" category="Προσοχή" onExit={onExit}>
      {state.phase === 'instruction' && (
        <InstructionBriefing
          helper={helper}
          message={INSTRUCTION}
          userName={userName}
          narrationMode={narrationMode}
          speechEnabled={speechEnabled}
          onStart={() => setState((previous) => startSart(previous, Date.now()))}
        />
      )}
      {state.phase !== 'instruction' && (
        <SartBoard
          state={state}
          helper={helper}
          onRespond={() => setState((previous) => respondSart(previous, Date.now()))}
        />
      )}
    </TimedTaskFrame>
  )
}

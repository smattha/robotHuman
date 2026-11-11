import type { ChildHelper, NarrationMode } from '../../domain/preferences'
import type { TaskSummary, TimedTaskId, Trial } from '../../domain/timed-task'
import { InstructionBriefing } from './InstructionBriefing'
import { createGoNoGoState, getGoNoGoSummary, respondGoNoGo, startGoNoGo, tickGoNoGo } from './go-no-go-logic'
import { GoNoGoScene } from './phaser/GoNoGoScene'
import { PhaserGame } from '../phaser/PhaserGame'
import { TimedTaskFrame } from './TimedTaskFrame'
import { useTimedTask } from './use-timed-task'

type GoNoGoTaskProps = {
  userName: string
  onExit: () => void
  onComplete: (taskId: TimedTaskId, trials: Trial[], summary: TaskSummary) => void
  helper: ChildHelper
  narrationMode: NarrationMode
  speechEnabled: boolean
}

const INSTRUCTION =
  'Θα εμφανίζονται οι λέξεις «Ξεκίνα» και «Στοπ». Πάτησε «Απόκριση» μόνο όταν βλέπεις «Ξεκίνα» και μην πατάς όταν βλέπεις «Στοπ».'

export function GoNoGoTask({ userName, onExit, onComplete, helper, narrationMode, speechEnabled }: GoNoGoTaskProps) {
  const { state, setState } = useTimedTask({
    create: createGoNoGoState,
    tick: tickGoNoGo,
    isFinished: (current) => current.phase === 'finished',
    report: (current) => onComplete('go-no-go', current.trials, getGoNoGoSummary(current)),
  })

  return (
    <TimedTaskFrame title="Go / No-Go" category="Προσοχή" onExit={onExit}>
      {state.phase === 'instruction' && (
        <InstructionBriefing
          helper={helper}
          message={INSTRUCTION}
          userName={userName}
          narrationMode={narrationMode}
          speechEnabled={speechEnabled}
          onStart={() => setState((previous) => startGoNoGo(previous, Date.now()))}
        />
      )}
      {state.phase !== 'instruction' && (
        <PhaserGame
          scene={GoNoGoScene}
          sceneProps={{
            phase: state.phase,
            isGo: state.isGo,
            trialStartedAt: state.trialStartedAt,
            helper,
            onRespond: () => setState((previous) => respondGoNoGo(previous, Date.now())),
          }}
          testId="go-nogo-game"
          ariaLabel="Παιχνίδι προσοχής Ξεκίνα Στοπ"
        />
      )}
    </TimedTaskFrame>
  )
}

import type { ChildHelper } from '../../domain/preferences'
import type { SartState } from './sart-logic'
import { TimedGameShell } from './TimedGameShell'

type SartBoardProps = {
  state: SartState
  helper: ChildHelper
  onRespond: () => void
}

export function SartBoard({ state, helper, onRespond }: SartBoardProps) {
  const finished = state.phase === 'finished'
  const canRespond = state.phase === 'running' && !state.responded

  return (
    <TimedGameShell
      helper={helper}
      theme="forest"
      testId="sart-game"
      ariaLabel="Παιχνίδι προσοχής με το μαγικό καλάθι"
      status={<span>Δοκιμές: {state.trials.length}</span>}
    >
      <div className="sart-stimulus-wrap">
        <span className="sart-stimulus" aria-hidden="true">{state.stimulus}</span>
        <span className="sart-basket" aria-hidden="true">🧺</span>
      </div>
      {finished ? (
        <p className="game-done" role="status">Μπράβο! Ολοκληρώθηκε η δοκιμή.</p>
      ) : (
        <button className="stroop-button" type="button" disabled={!canRespond} onClick={onRespond}>Απόκριση</button>
      )}
    </TimedGameShell>
  )
}

import type { ChildHelper } from '../../domain/preferences'
import type { GoNoGoState } from './go-no-go-logic'
import { TimedGameShell } from './TimedGameShell'

type GoNoGoBoardProps = {
  state: GoNoGoState
  helper: ChildHelper
  onRespond: () => void
}

export function GoNoGoBoard({ state, helper, onRespond }: GoNoGoBoardProps) {
  const finished = state.phase === 'finished'
  const canRespond = state.phase === 'running' && !state.responded

  return (
    <TimedGameShell
      helper={helper}
      theme="forest"
      testId="go-nogo-game"
      ariaLabel="Παιχνίδι προσοχής Ξεκίνα Στοπ"
      status={<span>Δοκιμές: {state.trials.length}</span>}
    >
      <div className="game-panel">
        <p className={`go-nogo-word ${state.isGo ? 'go' : 'nogo'}`}>{state.isGo ? 'Ξεκίνα' : 'Στοπ'}</p>
      </div>
      {finished ? (
        <p className="game-done" role="status">Μπράβο! Ολοκληρώθηκε η δοκιμή.</p>
      ) : (
        <button className="stroop-button" type="button" disabled={!canRespond} onClick={onRespond}>Απόκριση</button>
      )}
    </TimedGameShell>
  )
}

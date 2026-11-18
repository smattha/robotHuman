import type { ChildHelper } from '../../domain/preferences'
import { COLOR_WORDS, type StroopColor, type StroopState } from './stroop-logic'
import { TimedGameShell } from './TimedGameShell'

const INK_COLORS: Record<StroopColor, string> = {
  red: '#d64545',
  green: '#3f9d5a',
  blue: '#3a6fd8',
  yellow: '#d9a400',
}

type StroopBoardProps = {
  state: StroopState
  helper: ChildHelper
  onRespond: () => void
}

export function StroopBoard({ state, helper, onRespond }: StroopBoardProps) {
  const finished = state.phase === 'finished'
  const canRespond = state.phase === 'running' && !state.responded

  return (
    <TimedGameShell
      helper={helper}
      theme="workshop"
      testId="stroop-game"
      ariaLabel="Παιχνίδι προσοχής με τα μαγικά χρώματα"
      status={<span>Δοκιμές: {state.trials.length}</span>}
    >
      <div className="stroop-panel">
        <p className="stroop-word" style={{ color: INK_COLORS[state.ink] }}>{COLOR_WORDS[state.word]}</p>
      </div>
      <span className="stroop-cauldron" aria-hidden="true">⚗️</span>
      {finished ? (
        <p className="game-done" role="status">Μπράβο! Ολοκληρώθηκε η δοκιμή.</p>
      ) : (
        <button className="stroop-button" type="button" disabled={!canRespond} onClick={onRespond}>Απόκριση</button>
      )}
    </TimedGameShell>
  )
}

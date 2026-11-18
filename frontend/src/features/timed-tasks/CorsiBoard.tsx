import type { ChildHelper } from '../../domain/preferences'
import type { CorsiState } from './corsi-logic'
import { TimedGameShell } from './TimedGameShell'

const TILES = [0, 1, 2, 3, 4, 5, 6, 7, 8]

type CorsiBoardProps = {
  state: CorsiState
  helper: ChildHelper
  onTapTile: (tile: number) => void
}

export function CorsiBoard({ state, helper, onTapTile }: CorsiBoardProps) {
  const lit = state.phase === 'showing' && state.sequenceIndex > 0 ? state.sequence[state.sequenceIndex - 1] : -1
  const statusLabel =
    state.phase === 'showing'
      ? 'Παρακολούθησε τη σειρά'
      : state.phase === 'answering'
        ? `Επανάλαβε · ${state.answer.length}/${state.sequence.length}`
        : 'Τέλος!'

  return (
    <TimedGameShell helper={helper} theme="forest" testId="corsi-game" ariaLabel="Παιχνίδι μνήμης με μανιτάρια">
      <p className="game-status-line">{`${statusLabel} · επίπεδο ${state.level}`}</p>
      <div className="corsi-board">
        {TILES.map((tile) => (
          <button
            key={tile}
            type="button"
            className={`corsi-tile${tile === lit ? ' active' : ''}`}
            disabled={state.phase !== 'answering'}
            onClick={() => onTapTile(tile)}
            aria-label={`Μανιτάρι ${tile + 1}`}
          >
            <span aria-hidden="true">🍄</span>
          </button>
        ))}
      </div>
      {state.phase === 'finished' && <p className="game-done" role="status">Μπράβο! Ολοκληρώθηκε η δοκιμή.</p>}
    </TimedGameShell>
  )
}

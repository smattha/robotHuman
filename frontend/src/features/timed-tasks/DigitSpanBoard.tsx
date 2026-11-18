import type { ChildHelper } from '../../domain/preferences'
import type { DigitSpanState } from './digit-span-logic'
import { TimedGameShell } from './TimedGameShell'

const KEYS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'clear', '0', 'submit'] as const

type DigitSpanBoardProps = {
  state: DigitSpanState
  helper: ChildHelper
  onEnterDigit: (digit: string) => void
  onClear: () => void
  onSubmit: () => void
}

export function DigitSpanBoard({ state, helper, onEnterDigit, onClear, onSubmit }: DigitSpanBoardProps) {
  const showing = state.phase === 'showing'
  const answering = state.phase === 'answering'
  const statusLabel = showing ? 'Θυμήσου τα ψηφία' : answering ? 'Πληκτρολόγησε τη σειρά' : 'Τέλος!'
  const currentDigit = showing && state.sequenceIndex > 0 ? state.sequence[state.sequenceIndex - 1] : ''

  function handleKey(key: (typeof KEYS)[number]) {
    if (key === 'clear') onClear()
    else if (key === 'submit') onSubmit()
    else onEnterDigit(key)
  }

  return (
    <TimedGameShell helper={helper} theme="night" testId="digit-span-game" ariaLabel="Παιχνίδι μνήμης με τα μαγικά αστέρια">
      <p className="game-status-line">{`${statusLabel} · επίπεδο ${state.level}`}</p>
      {showing && <div className="digit-star" aria-hidden="true">{currentDigit}</div>}
      {answering && (
        <>
          <div className="digit-answer">{state.answer || '\u00A0'}</div>
          <div className="digit-keypad">
            {KEYS.map((key) => (
              <button
                key={key}
                type="button"
                className={`digit-key${key === 'submit' ? ' digit-key--submit' : ''}${key === 'clear' ? ' digit-key--clear' : ''}`}
                onClick={() => handleKey(key)}
              >
                {key === 'submit' ? 'Συνέχεια' : key === 'clear' ? 'Διόρθωση' : key}
              </button>
            ))}
          </div>
        </>
      )}
      {state.phase === 'finished' && <p className="game-done" role="status">Μπράβο! Ολοκληρώθηκε η δοκιμή.</p>}
    </TimedGameShell>
  )
}

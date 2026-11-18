import type { ReactNode } from 'react'
import type { ChildHelper } from '../../domain/preferences'
import { GameCharacter } from './GameCharacter'

export type GameTheme = 'workshop' | 'forest' | 'night' | 'clearing'

type TimedGameShellProps = {
  helper: ChildHelper
  theme: GameTheme
  status?: ReactNode
  testId?: string
  ariaLabel: string
  children: ReactNode
}

export function TimedGameShell({ helper, theme, status, testId, ariaLabel, children }: TimedGameShellProps) {
  return (
    <div className={`game-shell game-shell--${theme}`} data-testid={testId} role="region" aria-label={ariaLabel}>
      <div className="game-shell-top">
        <GameCharacter helper={helper} />
        {status ? <div className="game-shell-status">{status}</div> : null}
      </div>
      <div className="game-shell-stage">{children}</div>
    </div>
  )
}

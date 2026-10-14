import type { ChildHelper as ChildHelperType } from '../../domain/preferences'

type ChildHelperProps = {
  helper: ChildHelperType
  message: string
  compact?: boolean
}

const helperCharacters: Record<ChildHelperType, { name: string; icon: string; color: string }> = {
  robot: { name: 'Ρόμπι', icon: '🤖', color: 'robot' },
  fox: { name: 'Φοίβος', icon: '🦊', color: 'fox' },
  owl: { name: 'Ίρις', icon: '🦉', color: 'owl' },
  unicorn: { name: 'Νεφέλη', icon: '🦄', color: 'unicorn' },
}

export function ChildHelper({ helper, message, compact = false }: ChildHelperProps) {
  const character = helperCharacters[helper]

  return (
    <aside className={`child-helper-card${compact ? ' compact' : ''} helper-${character.color}`} aria-label={`${character.name}, ο βοηθός σου`}>
      <span className="child-helper-art" aria-hidden="true">{character.icon}</span>
      <span className="child-helper-copy">
        <strong>{character.name}, ο βοηθός σου</strong>
        <span>{message}</span>
      </span>
    </aside>
  )
}

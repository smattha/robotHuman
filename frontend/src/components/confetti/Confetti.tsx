const CONFETTI_COLORS = ['#ff6b9d', '#ffb347', '#2eb87a', '#6b3fa0', '#ffd66b', '#4ea8ff']

type ConfettiPiece = {
  left: number
  delay: number
  duration: number
  color: string
  size: number
  rotate: number
}

function createPieces(count: number): ConfettiPiece[] {
  return Array.from({ length: count }, (_, index) => ({
    left: Math.random() * 100,
    delay: Math.random() * 0.7,
    duration: 1.6 + Math.random() * 1.4,
    color: CONFETTI_COLORS[index % CONFETTI_COLORS.length],
    size: 8 + Math.random() * 7,
    rotate: Math.random() * 360,
  }))
}

type ConfettiProps = {
  trigger: boolean
  count?: number
}

export function Confetti({ trigger, count = 44 }: ConfettiProps) {
  if (!trigger) return null

  const pieces = createPieces(count)

  return (
    <div className="confetti-layer" aria-hidden="true">
      {pieces.map((piece, index) => (
        <span
          key={`${index}-${piece.left}-${piece.delay}`}
          className="confetti-piece"
          style={{
            left: `${piece.left}%`,
            background: piece.color,
            width: `${piece.size}px`,
            height: `${Math.round(piece.size * 0.45)}px`,
            animationDelay: `${piece.delay}s`,
            animationDuration: `${piece.duration}s`,
            transform: `rotate(${piece.rotate}deg)`,
          }}
        />
      ))}
    </div>
  )
}
import { useMemo, useState } from 'react'

type ParentalGateProps = {
  onPass: () => void
  onClose: () => void
}

function randomBetween(min: number, max: number): number {
  return Math.floor(Math.random() * (max - min + 1)) + min
}

export function ParentalGate({ onPass, onClose }: ParentalGateProps) {
  const [problem] = useState(() => {
    const a = randomBetween(4, 9)
    const b = randomBetween(1, a - 1)
    return { a, b, answer: a - b }
  })
  const [selected, setSelected] = useState<number | null>(null)
  const [error, setError] = useState(false)

  const options = useMemo(() => {
    const set = new Set<number>([problem.answer])
    let guard = 0
    while (set.size < 4 && guard < 50) {
      set.add(Math.max(0, problem.answer + randomBetween(-3, 3)))
      guard += 1
    }
    return [...set].sort(() => Math.random() - 0.5)
  }, [problem])

  function choose(value: number) {
    if (value === problem.answer) {
      onPass()
      return
    }
    setSelected(value)
    setError(true)
  }

  return (
    <div className="modal-backdrop" onClick={onClose}>
      <section className="parental-gate start-dialog" role="dialog" aria-modal="true" aria-labelledby="parental-gate-title" onClick={(event) => event.stopPropagation()}>
        <button className="close-button" type="button" aria-label="Κλείσιμο" onClick={onClose}>×</button>
        <p className="eyebrow">Για τους μεγάλους</p>
        <h2 id="parental-gate-title">Αυτός ο χώρος είναι για γονείς και κηδεμόνες</h2>
        <p className="parental-gate-question">Για να συνεχίσεις, πόσο κάνει το {problem.a} - {problem.b}?</p>
        <div className="parental-gate-options">
          {options.map((option) => (
            <button key={option} type="button" className={`parental-gate-option${selected === option && error ? ' wrong' : ''}`} onClick={() => choose(option)}>{option}</button>
          ))}
        </div>
        {error && <p className="parental-gate-error" role="alert">Δεν είναι σωστό. Δοκίμασε ξανά.</p>}
      </section>
    </div>
  )
}

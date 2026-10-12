import { useEffect } from 'react'

type TimedTaskFrameProps = {
  title: string
  category: string
  onExit: () => void
  children: React.ReactNode
}

export function TimedTaskFrame({ title, category, onExit, children }: TimedTaskFrameProps) {
  useEffect(() => {
    function exitOnEscape(event: KeyboardEvent) {
      if (event.key === 'Escape') onExit()
    }
    window.addEventListener('keydown', exitOnEscape)
    return () => window.removeEventListener('keydown', exitOnEscape)
  }, [onExit])

  return (
    <section className="page-section timed-task-section" aria-labelledby="timed-task-title">
      <div className="player-topline">
        <span className="category-pill">{category}</span>
        <button className="text-button" type="button" onClick={onExit}>Τερματισμός · Esc</button>
      </div>
      <h1 id="timed-task-title">{title}</h1>
      {children}
    </section>
  )
}

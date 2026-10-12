import { useState } from 'react'

type TaskNameDialogProps = {
  taskTitle: string
  onStart: (name: string) => void
  onClose: () => void
}

export function TaskNameDialog({ taskTitle, onStart, onClose }: TaskNameDialogProps) {
  const [name, setName] = useState('')

  return (
    <div className="modal-backdrop" onClick={onClose}>
      <section className="start-dialog" role="dialog" aria-modal="true" aria-labelledby="task-name-title" onClick={(event) => event.stopPropagation()}>
        <button className="close-button" type="button" aria-label="Κλείσιμο" onClick={onClose}>×</button>
        <p className="eyebrow">{taskTitle}</p>
        <h2 id="task-name-title">Πώς σε λένε;</h2>
        <p>Τα αποτελέσματα μένουν μόνο σε αυτόν τον browser.</p>
        <form onSubmit={(event) => { event.preventDefault(); if (name.trim()) onStart(name.trim()) }}>
          <label htmlFor="task-name-input">Όνομα</label>
          <input id="task-name-input" autoFocus maxLength={80} required value={name} onChange={(event) => setName(event.target.value)} />
          <button className="primary-button full-width" type="submit" disabled={!name.trim()}>Ξεκίνα</button>
        </form>
      </section>
    </div>
  )
}

import { useState } from 'react'

type StartTestDialogProps = {
  onStart: (name: string) => void
  onClose: () => void
}

export function StartTestDialog({ onStart, onClose }: StartTestDialogProps) {
  const [name, setName] = useState('')

  return (
    <div className="modal-backdrop" onClick={onClose}>
      <section className="start-dialog" role="dialog" aria-modal="true" aria-labelledby="test-dialog-title" onClick={(event) => event.stopPropagation()}>
        <button className="close-button" type="button" aria-label="Κλείσιμο" onClick={onClose}>×</button>
        <p className="eyebrow">Όλες οι ασκήσεις</p>
        <h2 id="test-dialog-title">Πώς σε λένε;</h2>
        <p>Θα κάνουμε όλες τις αποστολές με τη σειρά. Τα αποτελέσματα μένουν μόνο σε αυτόν τον browser.</p>
        <form onSubmit={(event) => { event.preventDefault(); if (name.trim()) onStart(name.trim()) }}>
          <label htmlFor="test-user-name">Όνομα</label>
          <input id="test-user-name" autoFocus maxLength={80} required value={name} onChange={(event) => setName(event.target.value)} />
          <button className="primary-button full-width" type="submit" disabled={!name.trim()}>Ξεκίνα το τεστ</button>
        </form>
      </section>
    </div>
  )
}

import { useState } from 'react'

type NewUserDialogProps = {
  existingUserNames: string[]
  onSave: (userName: string) => void
  onClose: () => void
}

function isDuplicateName(name: string, existingUserNames: string[]): boolean {
  return existingUserNames.some((existingName) => existingName.localeCompare(name.trim(), 'el', { sensitivity: 'accent' }) === 0)
}

export function NewUserDialog({ existingUserNames, onSave, onClose }: NewUserDialogProps) {
  const [name, setName] = useState('')
  const duplicateName = isDuplicateName(name, existingUserNames)

  return (
    <div className="modal-backdrop" onClick={onClose}>
      <section className="start-dialog" role="dialog" aria-modal="true" aria-labelledby="new-user-title" onClick={(event) => event.stopPropagation()}>
        <button className="close-button" type="button" aria-label="Κλείσιμο" onClick={onClose}>×</button>
        <p className="eyebrow">Νέος χρήστης</p>
        <h2 id="new-user-title">Πώς σε λένε;</h2>
        <p>Το όνομα βοηθά να κρατάμε τις προσπάθειες ξεχωριστές σε αυτή τη συσκευή.</p>
        <form onSubmit={(event) => { event.preventDefault(); if (name.trim()) onSave(name.trim()) }}>
          <label htmlFor="new-user-name">Όνομα</label>
          <input id="new-user-name" autoFocus maxLength={80} required value={name} onChange={(event) => setName(event.target.value)} />
          {duplicateName && <p className="duplicate-name-warning" role="status">Υπάρχει ήδη χρήστης με αυτό το όνομα. Μπορείς να συνεχίσεις αν είναι το ίδιο άτομο.</p>}
          <button className="primary-button full-width" type="submit" disabled={!name.trim()}>Συνέχισε <span aria-hidden="true">→</span></button>
        </form>
      </section>
    </div>
  )
}

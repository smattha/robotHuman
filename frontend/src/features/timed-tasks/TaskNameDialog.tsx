type TaskNameDialogProps = {
  taskTitle: string
  userName: string
  onStart: () => void
  onClose: () => void
}

export function TaskNameDialog({ taskTitle, userName, onStart, onClose }: TaskNameDialogProps) {

  return (
    <div className="modal-backdrop" onClick={onClose}>
      <section className="start-dialog" role="dialog" aria-modal="true" aria-labelledby="task-name-title" onClick={(event) => event.stopPropagation()}>
        <button className="close-button" type="button" aria-label="Κλείσιμο" onClick={onClose}>×</button>
        <p className="eyebrow">{taskTitle}</p>
        <h2 id="task-name-title">Έτοιμος/η, {userName};</h2>
        <p>Τα αποτελέσματα μένουν μόνο σε αυτόν τον browser.</p>
        <button className="primary-button full-width" type="button" onClick={onStart}>Ξεκίνα</button>
      </section>
    </div>
  )
}

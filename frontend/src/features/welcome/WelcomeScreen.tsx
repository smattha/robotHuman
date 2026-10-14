type WelcomeScreenProps = {
  onStart: () => void
  onNewUser: () => void
  userName: string | null
}

export function WelcomeScreen({ onStart, onNewUser, userName }: WelcomeScreenProps) {
  return (
    <section className="welcome-screen page-section" aria-labelledby="welcome-title">
      <div className="welcome-copy">
        <p className="eyebrow">Η περιπέτειά σου αρχίζει εδώ</p>
        <h1 id="welcome-title">Πάμε να ανακαλύψουμε κάτι καινούριο;</h1>
        <p className="lead">{userName ? `Γεια σου, ${userName}! Κάθε μικρή αποστολή είναι μια νέα ευκαιρία να δοκιμάσεις τις ιδέες σου.` : 'Παρατήρησε, σκέψου και δοκίμασε. Εδώ κάθε προσπάθεια μετράει!'}</p>
        <div className="welcome-actions">
          {!userName && <button className="welcome-user-button" type="button" onClick={onNewUser}>Διάλεξε το όνομά σου <span aria-hidden="true">→</span></button>}
          <button className="primary-button" type="button" onClick={onStart} disabled={!userName}>Πάμε για αποστολή <span aria-hidden="true">→</span></button>
          {userName && <button className="welcome-user-button" type="button" onClick={onNewUser}>Παίξε με άλλο όνομα <span aria-hidden="true">→</span></button>}
        </div>
        {!userName && <p className="welcome-name-hint">Πρώτα γράψε το όνομά σου και μετά ξεκινάμε μαζί.</p>}
      </div>
      <div className="welcome-art" aria-hidden="true">
        <div className="sun">☼</div>
        <div className="paper-card paper-card-back" />
        <div className="paper-card paper-card-front">
          <span className="card-star">✦</span>
          <strong>Παίξε</strong>
          <span>και ανακάλυψε!</span>
        </div>
        <div className="doodle doodle-left">⌁</div>
        <div className="doodle doodle-right">✳</div>
      </div>
    </section>
  )
}

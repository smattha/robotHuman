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
        <p className="welcome-quest"><span aria-hidden="true">✦</span> Διάλεξε αποστολή, άκουσε την ιστορία και βρες την απάντηση!</p>
        <div className="welcome-actions">
          {!userName && <button className="welcome-user-button" type="button" onClick={onNewUser}>Διάλεξε το όνομά σου <span aria-hidden="true">→</span></button>}
          <button className="primary-button" type="button" onClick={onStart}>Δες τις αποστολές <span aria-hidden="true">→</span></button>
          {userName && <button className="welcome-user-button" type="button" onClick={onNewUser}>Παίξε με άλλο όνομα <span aria-hidden="true">→</span></button>}
        </div>
        {!userName && <p className="welcome-name-hint">Μπορείς να δοκιμάσεις χωρίς όνομα. Για να αποθηκεύονται οι απαντήσεις σου, διάλεξε πρώτα το όνομά σου.</p>}
      </div>
      <div className="welcome-art" aria-hidden="true">
        <div className="sun">☼</div>
        <div className="paper-card paper-card-back" />
        <div className="paper-card paper-card-front">
          <span className="card-star">✦</span>
          <strong>Παίξε</strong>
          <span>και ανακάλυψε!</span>
        </div>
        <span className="welcome-character welcome-character-fox">🦊</span>
        <span className="welcome-character welcome-character-owl">🦉</span>
        <span className="welcome-character welcome-character-robot">🤖</span>
        <div className="doodle doodle-left">⌁</div>
        <div className="doodle doodle-right">✳</div>
      </div>
    </section>
  )
}

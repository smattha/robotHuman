type WelcomeScreenProps = {
  onStart: () => void
  onNewUser: () => void
  userName: string | null
}

export function WelcomeScreen({ onStart, onNewUser, userName }: WelcomeScreenProps) {
  return (
    <section className="welcome-screen page-section" aria-labelledby="welcome-title">
      <div className="welcome-copy">
        <p className="eyebrow">Καλώς ήρθες</p>
        <h1 id="welcome-title">Έτοιμος για μια μικρή αποστολή;</h1>
        <p className="lead">{userName ? `Γεια σου, ${userName}!` : 'Λύσε γρίφους, παρατήρησε προσεκτικά και ανακάλυψε πόσα μπορείς να κάνεις.'}</p>
        <div className="welcome-actions">
          {!userName && <button className="welcome-user-button" type="button" onClick={onNewUser}>Νέος χρήστης <span aria-hidden="true">→</span></button>}
          <button className="primary-button" type="button" onClick={onStart} disabled={!userName}>Ξεκινάμε <span aria-hidden="true">→</span></button>
          {userName && <button className="welcome-user-button" type="button" onClick={onNewUser}>Νέος χρήστης <span aria-hidden="true">→</span></button>}
        </div>
        {!userName && <p className="welcome-name-hint">Πάτησε «Νέος χρήστης» για να ξεκινήσεις.</p>}
      </div>
      <div className="welcome-art" aria-hidden="true">
        <div className="sun">☼</div>
        <div className="paper-card paper-card-back" />
        <div className="paper-card paper-card-front">
          <span className="card-star">✦</span>
          <strong>Σκέψου</strong>
          <span>και βρες!</span>
        </div>
        <div className="doodle doodle-left">⌁</div>
        <div className="doodle doodle-right">✳</div>
      </div>
    </section>
  )
}

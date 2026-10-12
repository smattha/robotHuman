type WelcomeScreenProps = {
  onStart: () => void
}

export function WelcomeScreen({ onStart }: WelcomeScreenProps) {
  return (
    <section className="welcome-screen page-section" aria-labelledby="welcome-title">
      <div className="welcome-copy">
        <p className="eyebrow">Καλώς ήρθες</p>
        <h1 id="welcome-title">Έτοιμος για μια μικρή αποστολή;</h1>
        <p className="lead">Λύσε γρίφους, παρατήρησε προσεκτικά και ανακάλυψε πόσα μπορείς να κάνεις.</p>
        <button className="primary-button" type="button" onClick={onStart}>Ξεκινάμε <span aria-hidden="true">→</span></button>
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

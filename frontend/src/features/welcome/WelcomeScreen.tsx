type WelcomeScreenProps = {
  onStart: () => void
  onLibrary: () => void
  onNewUser: () => void
  userName: string | null
}

export function WelcomeScreen({ onStart, onLibrary, onNewUser, userName }: WelcomeScreenProps) {
  return (
    <section className="welcome-screen page-section" aria-labelledby="welcome-title">
      <div className="welcome-copy">
        <p className="eyebrow">Η μαγική περιπέτεια</p>
        <h1 id="welcome-title">Πάμε να παίξουμε μαζί τον Φοίβο;</h1>
        <p className="lead">{userName ? `Γεια σου, ${userName}! Ο Φοίβος σε περιμένει για παιχνίδια και ανακαλύψεις.` : 'Ο Φοίβος ο αλεπούς σε περιμένει για παιχνίδια και ανακαλύψεις!'}</p>
        <div className="welcome-actions">
          <button className="play-button" type="button" onClick={onStart}><span aria-hidden="true">▶</span> ΠΑΙΞΕ</button>
          <button className="welcome-secondary" type="button" onClick={onLibrary}>Δες τις αποστολές</button>
          {!userName
            ? <button className="welcome-user-button" type="button" onClick={onNewUser}>Διάλεξε το όνομά σου <span aria-hidden="true">→</span></button>
            : <button className="welcome-user-button" type="button" onClick={onNewUser}>Παίξε με άλλο όνομα <span aria-hidden="true">→</span></button>}
        </div>
      </div>
      <div className="welcome-art" aria-hidden="true">
        <div className="forest">
          <span className="tree tree-1">🌲</span>
          <span className="tree tree-2">🌳</span>
          <span className="tree tree-3">🌲</span>
          <span className="mushroom">🍄</span>
        </div>
        <div className="sun">☼</div>
        <span className="cloud cloud-1">☁</span>
        <span className="cloud cloud-2">☁</span>
        <span className="welcome-character welcome-character-fox welcome-fox">🦊</span>
        <span className="welcome-character welcome-character-owl">🦉</span>
        <div className="doodle doodle-left">⌁</div>
        <div className="doodle doodle-right">✳</div>
      </div>
    </section>
  )
}

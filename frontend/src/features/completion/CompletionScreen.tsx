import type { TestResult } from '../../domain/results'
import type { ChildHelper } from '../../domain/preferences'

type CompletionScreenProps = {
  isCorrect: boolean
  isSingle: boolean
  result: TestResult | null
  helper: ChildHelper
  onRestart: () => void
  onHome: () => void
}

const helperIcons: Record<ChildHelper, string> = { robot: '🤖', fox: '🦊', owl: '🦉', unicorn: '🦄' }

export function CompletionScreen({ isCorrect, isSingle, result, helper, onRestart, onHome }: CompletionScreenProps) {
  return (
    <section className="completion-screen page-section" aria-labelledby="completion-title">
      <div className="completion-confetti" aria-hidden="true">✦ · ✧ · ✦</div>
      <div className="child-helper" aria-hidden="true">{helperIcons[helper]}</div>
      <div className="completion-icon" aria-hidden="true">{isCorrect ? '✓' : '★'}</div>
      <p className="eyebrow">Αποστολή ολοκληρώθηκε</p>
      <h1 id="completion-title">Τα κατάφερες, εξερευνητή!</h1>
      <p className="lead">Μπράβο που δοκίμασες! Κάθε ιδέα και κάθε προσπάθεια σε βοηθά να ανακαλύπτεις περισσότερα.</p>
      {isSingle && <p className="mission-badge"><span aria-hidden="true">★</span> Κονκάρδα: Μικρός Εξερευνητής</p>}
      {result && <p className="lead">{result.userName}: {result.answers.filter((answer) => answer.isCorrect).length} σωστές από {result.answers.length} ασκήσεις.</p>}
      <div className="completion-actions">
        <button className="primary-button" type="button" onClick={onRestart}>Ξαναπαίξε <span aria-hidden="true">↻</span></button>
        <button className="text-button" type="button" onClick={onHome}>Πίσω στις αποστολές</button>
      </div>
    </section>
  )
}

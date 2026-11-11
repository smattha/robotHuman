import type { TestResult } from '../../domain/results'
import type { ChildHelper } from '../../domain/preferences'
import type { NarrationMode } from '../../domain/preferences'
import { ChildHelper as ChildHelperComponent } from '../../components/child-helper/ChildHelper'
import { useNarration } from '../../hooks/use-narration'

type CompletionScreenProps = {
  isCorrect: boolean
  isSingle: boolean
  result: TestResult | null
  helper: ChildHelper
  narrationMode: NarrationMode
  speechEnabled: boolean
  onRestart: () => void
  onHome: () => void
}

const CELEBRATION_MESSAGE = 'Μπράβο! Τα κατάφερες! Είσαι σπουδαίος εξερευνητής!'

export function CompletionScreen({ isCorrect, isSingle, result, helper, narrationMode, speechEnabled, onRestart, onHome }: CompletionScreenProps) {
  const { isNarrating, isPreparing, replay } = useNarration({ text: CELEBRATION_MESSAGE, narrationMode, speechEnabled, autoPlay: narrationMode === 'auto' })
  const helperMessage = isPreparing ? 'Σε συγχαίρω!' : 'Τα κατάφερες! Πήγαμε ό,τι καλύτερα!'

  return (
    <section className="completion-screen page-section" aria-labelledby="completion-title">
      <ChildHelperComponent helper={helper} playing={isNarrating} message={helperMessage} />
      <div className="completion-icon" aria-hidden="true">{isCorrect ? '✓' : '★'}</div>
      <p className="eyebrow">Αποστολή ολοκληρώθηκε</p>
      <h1 id="completion-title">Τα κατάφερες, εξερευνητή!</h1>
      <p className="lead">Μπράβο που δοκίμασες! Κάθε ιδέα και κάθε προσπάθεια σε βοηθά να ανακαλύπτεις περισσότερα.</p>
      {isSingle && <p className="mission-badge"><span aria-hidden="true">★</span> Κονκάρδα: Μικρός Εξερευνητής</p>}
      {result && <p className="lead">{result.userName}: {result.answers.filter((answer) => answer.isCorrect).length} σωστές από {result.answers.length} ασκήσεις.</p>}
      <div className="completion-actions">
        <button className="primary-button play-again-button" type="button" onClick={onRestart}>ΠΑΙΞΕ ΞΑΝΑ <span aria-hidden="true">↻</span></button>
        <button className="text-button" type="button" onClick={onHome}>Πίσω στις αποστολές</button>
        <button className="hint-button replay-button" type="button" onClick={() => void replay()} aria-label="Άκουσε ξανά">🔊 Άκουσε ξανά</button>
      </div>
    </section>
  )
}

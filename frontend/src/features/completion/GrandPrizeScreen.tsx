import { Confetti } from '../../components/confetti/Confetti'
import { ChildHelper } from '../../components/child-helper/ChildHelper'
import type { ChildHelper as ChildHelperType } from '../../domain/preferences'
import type { TestResult } from '../../domain/results'

type GrandPrizeScreenProps = {
  result: TestResult | null
  helper: ChildHelperType
  onRestart: () => void
  onHome: () => void
}

export function GrandPrizeScreen({ result, helper, onRestart, onHome }: GrandPrizeScreenProps) {
  const totalCount = result?.answers.length ?? 0
  const correctCount = result?.answers.filter((answer) => answer.isCorrect).length ?? 0

  return (
    <section className="page-section completion-screen" aria-labelledby="grand-prize-title">
      <Confetti trigger count={70} />
      <div className="completion-confetti" aria-hidden="true">✦ · ✧ · ✦</div>
      <div className="grand-prize-trophy" aria-hidden="true">🏆</div>
      <div className="child-helper" aria-hidden="true">🎉</div>
      <p className="eyebrow">Μεγάλη Περιπέτεια</p>
      <h1 id="grand-prize-title">Μεγάλο Βραβείο!</h1>
      <p className="lead">Ολοκλήρωσες όλες τις μικρές αποστολές! Είσαι επίσημα Μικρός Εξερευνητής!</p>
      {result && <p className="mission-badge"><span aria-hidden="true">★</span> {result.userName}: {correctCount} σωστές από {totalCount} αποστολές</p>}
      <ChildHelper helper={helper} message="Έκανες μια καταπληκτική διαδρομή! Είμαι πολύ περήφανος για σένα." />
      <div className="completion-actions">
        <button className="primary-button" type="button" onClick={onRestart}>Ξαναπαίξε την περιπέτεια <span aria-hidden="true">↻</span></button>
        <button className="text-button" type="button" onClick={onHome}>Πίσω στην αρχή</button>
      </div>
    </section>
  )
}
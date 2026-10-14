import type { ChildHelper } from '../../domain/preferences'

type BreakScreenProps = {
  completedCount: number
  totalCount: number
  onContinue: () => void
  onFinish: () => void
  helper: ChildHelper
}

const helperIcons: Record<ChildHelper, string> = { robot: '🤖', fox: '🦊', owl: '🦉', unicorn: '🦄' }

export function BreakScreen({ completedCount, totalCount, onContinue, onFinish, helper }: BreakScreenProps) {
  return (
    <section className="page-section break-screen" aria-labelledby="break-title">
      <div className="break-card">
        <div className="break-icon" aria-hidden="true">🌈</div>
        <div className="child-helper" aria-hidden="true">{helperIcons[helper]}</div>
        <p className="eyebrow">Μικρό διάλειμμα</p>
        <h1 id="break-title">Τα πας υπέροχα!</h1>
        <p className="lead">Έκανες {completedCount} από τις {totalCount} αποστολές! Πάρε μια ανάσα ή ένα μικρό τέντωμα. Συνέχισε όποτε νιώσεις έτοιμος/η.</p>
        <div className="break-progress" aria-label={`Ολοκληρώθηκαν ${completedCount} από ${totalCount} ασκήσεις`}>
          <span style={{ width: `${(completedCount / totalCount) * 100}%` }} />
        </div>
        <div className="completion-actions">
          <button className="primary-button" type="button" onClick={onContinue}>Συνεχίζουμε! <span aria-hidden="true">→</span></button>
          <button className="text-button" type="button" onClick={onFinish}>Θέλω να σταματήσω εδώ</button>
        </div>
      </div>
    </section>
  )
}

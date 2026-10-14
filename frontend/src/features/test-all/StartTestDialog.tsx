import type { TestResult } from '../../domain/results'

type StartTestDialogProps = {
  onStart: () => void
  resumableResult: TestResult | null
  onResume: () => void
  onClose: () => void
}

export function StartTestDialog({ onStart, resumableResult, onResume, onClose }: StartTestDialogProps) {
  return (
    <div className="modal-backdrop" onClick={onClose}>
      <section className="start-dialog" role="dialog" aria-modal="true" aria-labelledby="test-dialog-title" onClick={(event) => event.stopPropagation()}>
        <button className="close-button" type="button" aria-label="Κλείσιμο" onClick={onClose}>×</button>
        <p className="eyebrow">Όλες οι ασκήσεις</p>
        <h2 id="test-dialog-title">Η Μεγάλη Περιπέτεια</h2>
        <p>Θα κάνουμε όλες τις Μικρές Αποστολές με τη σειρά. Τα αποτελέσματα μένουν μόνο σε αυτόν τον browser.</p>
        {resumableResult && (
          <div className="resume-adventure">
            <strong>Η περιπέτεια του/της {resumableResult.userName} περιμένει.</strong>
            <p>Έχουν ολοκληρωθεί {resumableResult.answers.length} αποστολές.</p>
            <button className="primary-button full-width" type="button" onClick={onResume}>Συνέχισε την Περιπέτεια <span aria-hidden="true">→</span></button>
          </div>
        )}
        <h3>Ξεκίνα νέα Περιπέτεια</h3>
        <button className="secondary-dialog-button full-width" type="button" onClick={onStart}>Ξεκίνα νέα Περιπέτεια</button>
      </section>
    </div>
  )
}

import type { TaskSummary, Trial } from '../../domain/timed-task'

type TaskResultsTableProps = {
  summary: TaskSummary
  trials: Trial[]
  stimulusLabel: string
  responseLabel: string
  maxSequenceLengthLabel?: string
}

export function TaskResultsTable({ summary, trials, stimulusLabel, responseLabel, maxSequenceLengthLabel }: TaskResultsTableProps) {
  const sequenceLabel = maxSequenceLengthLabel && summary.maxSequenceLength !== null
    ? <div><strong>{summary.maxSequenceLength}</strong> {maxSequenceLengthLabel}</div>
    : null

  return (
    <div className="task-results">
      <div className="task-summary">
        <div><strong>{summary.correctCount}</strong> σωστές</div>
        <div><strong>{summary.wrongCount}</strong> λάθος</div>
        <div><strong>{summary.totalTrials}</strong> συνολικά</div>
        <div><strong>{(summary.meanResponseTimeMs / 1000).toFixed(1)}s</strong> μέσος χρόνος</div>
        {sequenceLabel}
      </div>
      {trials.length > 0 && (
        <table className="task-trial-table">
          <thead>
            <tr><th>{stimulusLabel}</th><th>{responseLabel}</th><th>Χρόνος</th><th>Αποτέλεσμα</th></tr>
          </thead>
          <tbody>
            {trials.map((trial, index) => (
              <tr key={index}>
                <td>{trial.stimulus}</td>
                <td>{trial.response}</td>
                <td>{(trial.responseTimeMs / 1000).toFixed(2)}s</td>
                <td>{trial.isCorrect ? 'Σωστό' : 'Λάθος'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  )
}

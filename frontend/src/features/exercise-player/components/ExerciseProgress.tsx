type ExerciseProgressProps = {
  current: number
  total: number
}

export function ExerciseProgress({ current, total }: ExerciseProgressProps) {
  return (
    <div className="progress-track" aria-label="Πρόοδος αποστολών">
      <span style={{ width: `${(current / total) * 100}%` }} />
    </div>
  )
}

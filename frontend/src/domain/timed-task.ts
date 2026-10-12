export type TimedTaskId = 'stroop' | 'go-no-go' | 'sart' | 'corsi' | 'digit-span'

export type Trial = {
  stimulus: string
  response: string
  isCorrect: boolean
  responseTimeMs: number
}

export type TaskSummary = {
  totalTrials: number
  correctCount: number
  wrongCount: number
  meanResponseTimeMs: number
  maxSequenceLength: number | null
}

export type TimedTaskResult = {
  id: string
  taskId: TimedTaskId
  userName: string
  startedAt: string
  completedAt: string
  trials: Trial[]
  summary: TaskSummary
}

export function summarizeTrials(trials: Trial[], maxSequenceLength: number | null): TaskSummary {
  const totalTrials = trials.length
  const correctCount = trials.filter((trial) => trial.isCorrect).length
  const wrongCount = totalTrials - correctCount
  const meanResponseTimeMs = totalTrials === 0
    ? 0
    : Math.round(trials.reduce((total, trial) => total + trial.responseTimeMs, 0) / totalTrials)

  return { totalTrials, correctCount, wrongCount, meanResponseTimeMs, maxSequenceLength }
}

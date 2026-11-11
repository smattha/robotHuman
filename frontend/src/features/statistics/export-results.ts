import { exercises } from '../../content/exercises'
import { getPrimaryQuestion } from '../../domain/exercise'
import type { TestResult } from '../../domain/results'
import type { TimedTaskResult } from '../../domain/timed-task'
import { timedTaskDefinitions } from '../timed-tasks/timed-task-definitions'

function escapeCsvValue(value: string): string {
  return `"${value.replace(/"/g, '""')}"`
}

function triggerDownload(filename: string, content: string): void {
  const blob = new Blob(['\uFEFF', content], { type: 'text/csv;charset=utf-8' })
  const url = URL.createObjectURL(blob)
  const link = document.createElement('a')
  link.href = url
  link.download = filename
  document.body.appendChild(link)
  link.click()
  link.remove()
  URL.revokeObjectURL(url)
}

function formatDate(value: string): string {
  return new Date(value).toLocaleString('el-GR')
}

function exerciseResultToRows(result: TestResult): string[] {
  const isSingle = result.kind === 'single' || (result.kind === undefined && result.answers.length === 1 && result.completedAt === result.startedAt)
  const title = isSingle
    ? exercises.find((exercise) => exercise.id === result.answers[0]?.exerciseId)?.title ?? 'Μικρή Αποστολή'
    : 'Μεγάλη Περιπέτεια'
  const correctCount = result.answers.filter((answer) => answer.isCorrect).length
  return result.answers.map((answer) => {
    const exercise = exercises.find((entry) => entry.id === answer.exerciseId)
    const option = exercise ? getPrimaryQuestion(exercise).options.find((entry) => entry.id === answer.optionId) : undefined
    return [
      result.userName,
      isSingle ? 'Μικρή Αποστολή' : 'Μεγάλη Περιπέτεια',
      title,
      exercise?.title ?? answer.exerciseId,
      option?.detail ?? answer.optionId,
      answer.isCorrect ? 'Σωστό' : 'Νέα δοκιμή',
      formatDate(answer.answeredAt),
    ].map(escapeCsvValue).join(',')
  }).concat([`${escapeCsvValue(result.userName)},${escapeCsvValue(isSingle ? 'Μικρή Αποστολή' : 'Μεγάλη Περιπέτεια')},${escapeCsvValue(title)},Σύνολο: ${correctCount}/${result.answers.length},,,`])
}

function timedResultToRow(result: TimedTaskResult): string {
  const taskTitle = timedTaskDefinitions.find((task) => task.id === result.taskId)?.title ?? result.taskId
  return [result.userName, 'Χρονική δοκιμασία', taskTitle, `${result.summary.correctCount}/${result.summary.totalTrials}`, formatDate(result.completedAt)].map(escapeCsvValue).join(',')
}

export function downloadResultsCsv(results: TestResult[], timedResults: TimedTaskResult[]): void {
  const header = ['Παιδί', 'Τύπος', 'Δραστηριότητα', 'Λεπτομέρεια', 'Αποτέλεσμα', 'Ημερομηνία', 'Επιλογή'].map(escapeCsvValue).join(',')
  const exerciseRows = results.flatMap(exerciseResultToRows)
  const timedHeader = ['Παιδί', 'Τύπος', 'Δραστηριότητα', 'Σκορ', 'Ημερομηνία'].map(escapeCsvValue).join(',')
  const timedRows = timedResults.map(timedResultToRow)
  const content = [header, ...exerciseRows, '', timedHeader, ...timedRows].join('\n')
  triggerDownload('mikres-apostoles-apotelesmata.csv', content)
}
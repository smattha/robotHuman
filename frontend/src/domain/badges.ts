import type { TestResult } from './results'
import type { TimedTaskResult } from './timed-task'

export type Badge = {
  id: string
  title: string
  description: string
  icon: string
}

export const BADGES: Badge[] = [
  { id: 'first-star', title: 'Πρώτο Αστέρι', description: 'Πρώτη σωστή απάντηση σε άσκηση', icon: '⭐' },
  { id: 'little-explorer', title: 'Μικρός Εξερευνητής', description: 'Ολοκλήρωσε μια μικρή αποστολή σωστά', icon: '🧭' },
  { id: 'great-adventure', title: 'Μεγάλη Περιπέτεια', description: 'Ολοκλήρωσε και τις 12 αποστολές σε μια σειρά', icon: '🗺️' },
  { id: 'perfect-run', title: 'Τέλεια Επίδοση', description: 'Τουλάχιστον 3 σωστές απαντήσεις στη σειρά', icon: '🎯' },
  { id: 'ten-results', title: 'Δέκα Προσπάθειες', description: '10 αποθηκευμένα αποτελέσματα', icon: '💪' },
  { id: 'memory-master', title: 'Κυρίαρχος της Μνήμης', description: 'Ολοκλήρωσε μια χρονική δοκιμασία', icon: '🧠' },
  { id: 'all-challenges', title: 'Όλες οι Προκλήσεις', description: 'Ολοκλήρωσε και τις 5 χρονικές δοκιμασίες', icon: '🏆' },
  { id: 'quick-wit', title: 'Γρήγορο Μυαλό', description: 'Σκορ 90% και πάνω σε χρονική δοκιμασία', icon: '⚡' },
]

export function isSingleExerciseResult(result: TestResult): boolean {
  return result.kind === 'single' || (result.kind === undefined && result.answers.length === 1 && result.completedAt === result.startedAt)
}

export function getEarnedBadgeIds(results: TestResult[], timedResults: TimedTaskResult[]): Set<string> {
  const earned = new Set<string>()

  if (results.some((result) => result.answers.some((answer) => answer.isCorrect))) earned.add('first-star')

  if (results.some((result) => isSingleExerciseResult(result) && result.completedAt && result.answers[0]?.isCorrect)) earned.add('little-explorer')

  if (results.some((result) => result.completedAt && result.answers.length === 12)) earned.add('great-adventure')

  if (results.some((result) => result.answers.length >= 3 && result.answers.every((answer) => answer.isCorrect))) earned.add('perfect-run')

  if (results.length >= 10) earned.add('ten-results')

  if (timedResults.length > 0) earned.add('memory-master')

  const completedTaskIds = new Set(timedResults.map((result) => result.taskId))
  if (completedTaskIds.size >= 5) earned.add('all-challenges')

  if (timedResults.some((result) => result.summary.totalTrials > 0 && result.summary.correctCount / result.summary.totalTrials >= 0.9)) earned.add('quick-wit')

  return earned
}
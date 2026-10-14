export type ExerciseResult = {
  exerciseId: string
  optionId: string
  isCorrect: boolean
  answeredAt: string
}

export type TestResult = {
  id: string
  userName: string
  startedAt: string
  completedAt: string | null
  answers: ExerciseResult[]
  kind?: 'single'
}

const STORAGE_KEY = 'childrens-exercises-results-v1'

export function loadResults(): TestResult[] {
  try {
    const parsed: unknown = JSON.parse(localStorage.getItem(STORAGE_KEY) ?? '[]')
    return Array.isArray(parsed) ? parsed.filter((result): result is TestResult =>
      typeof result === 'object' && result !== null && typeof result.id === 'string' &&
      typeof result.userName === 'string' && Array.isArray(result.answers)) : []
  } catch {
    return []
  }
}

export function saveResult(result: TestResult): boolean {
  try {
    const existing = loadResults().filter((entry) => entry.id !== result.id)
    localStorage.setItem(STORAGE_KEY, JSON.stringify([...existing, result]))
    return true
  } catch {
    return false
  }
}

export function deleteResult(id: string): boolean {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(loadResults().filter((entry) => entry.id !== id)))
    return true
  } catch {
    return false
  }
}

export function clearResults(): boolean {
  try {
    localStorage.removeItem(STORAGE_KEY)
    return true
  } catch {
    return false
  }
}

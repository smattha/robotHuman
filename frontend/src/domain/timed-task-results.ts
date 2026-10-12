import type { TimedTaskResult } from './timed-task'

const STORAGE_KEY = 'childrens-exercises-timed-tasks-v1'

export function loadTimedTaskResults(): TimedTaskResult[] {
  try {
    const parsed: unknown = JSON.parse(localStorage.getItem(STORAGE_KEY) ?? '[]')
    return Array.isArray(parsed)
      ? parsed.filter((result): result is TimedTaskResult => {
          if (typeof result !== 'object' || result === null) return false
          const candidate = result as Record<string, unknown>
          return typeof candidate.id === 'string' && typeof candidate.taskId === 'string' && Array.isArray(candidate.trials)
        })
      : []
  } catch {
    return []
  }
}

export function saveTimedTaskResult(result: TimedTaskResult): boolean {
  try {
    const existing = loadTimedTaskResults().filter((entry) => entry.id !== result.id)
    localStorage.setItem(STORAGE_KEY, JSON.stringify([...existing, result]))
    return true
  } catch {
    return false
  }
}

export function deleteTimedTaskResult(id: string): boolean {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(loadTimedTaskResults().filter((entry) => entry.id !== id)))
    return true
  } catch {
    return false
  }
}

export function clearTimedTaskResults(): boolean {
  try {
    localStorage.removeItem(STORAGE_KEY)
    return true
  } catch {
    return false
  }
}

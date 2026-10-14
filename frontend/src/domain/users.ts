const STORAGE_KEY = 'childrens-exercises-users-v1'

export function loadUserNames(): string[] {
  try {
    const parsed: unknown = JSON.parse(localStorage.getItem(STORAGE_KEY) ?? '[]')
    return Array.isArray(parsed) ? parsed.filter((name): name is string => typeof name === 'string' && name.trim().length > 0) : []
  } catch {
    return []
  }
}

export function saveUserName(userName: string): boolean {
  try {
    const normalizedName = userName.trim()
    const userNames = loadUserNames()
    if (!userNames.some((name) => name.localeCompare(normalizedName, 'el', { sensitivity: 'accent' }) === 0)) {
      localStorage.setItem(STORAGE_KEY, JSON.stringify([...userNames, normalizedName]))
    }
    return true
  } catch {
    return false
  }
}

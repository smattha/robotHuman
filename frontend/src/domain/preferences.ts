export type StorySpeed = 'slow' | 'normal' | 'fast'
export type ChildHelper = 'robot' | 'fox' | 'owl' | 'unicorn'

export type Preferences = {
  storySpeed: StorySpeed
  childHelper: ChildHelper
  largeButtons: boolean
  reducedMotion: boolean
  highContrast: boolean
  speechEnabled: boolean
}

const STORAGE_KEY = 'childrens-exercises-preferences-v1'

export const DEFAULT_PREFERENCES: Preferences = {
  storySpeed: 'slow',
  childHelper: 'robot',
  largeButtons: false,
  reducedMotion: false,
  highContrast: false,
  speechEnabled: true,
}

export const storySpeedDurations: Record<StorySpeed, number> = {
  slow: 6000,
  normal: 4000,
  fast: 2500,
}

export function getStoryFrameDuration(storySpeed: StorySpeed): number {
  return storySpeedDurations[storySpeed]
}

export function loadPreferences(): Preferences {
  try {
    const parsed: unknown = JSON.parse(localStorage.getItem(STORAGE_KEY) ?? '{}')
    if (typeof parsed !== 'object' || parsed === null) return DEFAULT_PREFERENCES
    const storedPreferences = parsed as Record<string, unknown>
    const storySpeed = storedPreferences.storySpeed
    const childHelper = storedPreferences.childHelper
    if (storySpeed !== 'slow' && storySpeed !== 'normal' && storySpeed !== 'fast') return DEFAULT_PREFERENCES
    return {
      storySpeed,
      childHelper: childHelper === 'fox' || childHelper === 'owl' || childHelper === 'unicorn' ? childHelper : 'robot',
      largeButtons: storedPreferences.largeButtons === true,
      reducedMotion: storedPreferences.reducedMotion === true,
      highContrast: storedPreferences.highContrast === true,
      speechEnabled: storedPreferences.speechEnabled !== false,
    }
  } catch {
    return DEFAULT_PREFERENCES
  }
}

export function savePreferences(preferences: Preferences): boolean {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(preferences))
    return true
  } catch {
    return false
  }
}

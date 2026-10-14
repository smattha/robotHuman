import { beforeEach, describe, expect, it } from 'vitest'
import { DEFAULT_PREFERENCES, getStoryFrameDuration, loadPreferences, savePreferences } from './preferences'

describe('preferences', () => {
  beforeEach(() => localStorage.clear())

  it('uses the slow story speed by default', () => {
    expect(loadPreferences()).toEqual(DEFAULT_PREFERENCES)
    expect(getStoryFrameDuration(DEFAULT_PREFERENCES.storySpeed)).toBe(6000)
  })

  it('stores and loads selected preferences', () => {
    expect(savePreferences({ storySpeed: 'fast', childHelper: 'owl', largeButtons: true, reducedMotion: true, highContrast: true, speechEnabled: false })).toBe(true)
    expect(loadPreferences()).toEqual({ storySpeed: 'fast', childHelper: 'owl', largeButtons: true, reducedMotion: true, highContrast: true, speechEnabled: false })
    expect(getStoryFrameDuration('fast')).toBe(2500)
  })

  it('falls back to defaults for an unsupported stored speed', () => {
    localStorage.setItem('childrens-exercises-preferences-v1', JSON.stringify({ storySpeed: 'instant' }))
    expect(loadPreferences()).toEqual(DEFAULT_PREFERENCES)
  })

  it('uses the robot helper for saved preferences from before helper selection', () => {
    localStorage.setItem('childrens-exercises-preferences-v1', JSON.stringify({ storySpeed: 'normal' }))
    expect(loadPreferences()).toEqual({ storySpeed: 'normal', childHelper: 'robot', largeButtons: false, reducedMotion: false, highContrast: false, speechEnabled: true })
  })
})

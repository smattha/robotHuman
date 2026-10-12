import { describe, expect, it } from 'vitest'
import { matchSpokenOption } from './speech'
import { exercises } from '../content/exercises'

describe('matchSpokenOption', () => {
  it('matches Greek number words to numbered answers', () => {
    expect(matchSpokenOption('τέσσερα', exercises[0].options)).toBe('four')
  })

  it('matches an answer description', () => {
    expect(matchSpokenOption('Στο ψυγείο', exercises[2].options)).toBe('fridge')
  })

  it('does not guess an unclear answer', () => {
    expect(matchSpokenOption('δεν ξέρω', exercises[0].options)).toBeNull()
  })
})

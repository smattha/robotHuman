import { describe, expect, it } from 'vitest'
import { getPrimaryQuestion } from './exercise'
import { matchSpokenOption } from './speech'
import { exercises } from '../content/exercises'

describe('matchSpokenOption', () => {
  it('matches Greek number words to numbered answers', () => {
    expect(matchSpokenOption('τέσσερα', getPrimaryQuestion(exercises[0]).options)).toBe('four')
  })

  it('matches an answer description', () => {
    expect(matchSpokenOption('Στο ψυγείο', getPrimaryQuestion(exercises[2]).options)).toBe('fridge')
  })

  it('does not guess an unclear answer', () => {
    expect(matchSpokenOption('δεν ξέρω', getPrimaryQuestion(exercises[0]).options)).toBeNull()
  })
})

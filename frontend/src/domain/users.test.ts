import { beforeEach, describe, expect, it } from 'vitest'
import { loadUserNames, saveUserName } from './users'

describe('users', () => {
  beforeEach(() => localStorage.clear())

  it('stores a new user name once', () => {
    expect(saveUserName('Alex')).toBe(true)
    expect(saveUserName('alex')).toBe(true)
    expect(loadUserNames()).toEqual(['Alex'])
  })

  it('returns an empty list for invalid saved data', () => {
    localStorage.setItem('childrens-exercises-users-v1', '{broken')
    expect(loadUserNames()).toEqual([])
  })
})

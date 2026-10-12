import type { TaskSummary, Trial } from '../../domain/timed-task'
import { summarizeTrials } from '../../domain/timed-task'

const OBJECTS = ['✈️', '⚽', '🚗', '🎄', '🚢', '🍬', '🚜']
const APPLE = '🍎'
const APPLE_PROBABILITY = 0.2
const TRIAL_DISPLAY_MS = 2000
const TOTAL_LIMIT_MS = 60000

export type SartState = {
  phase: 'instruction' | 'running' | 'finished'
  trials: Trial[]
  isApple: boolean
  stimulus: string
  trialStartedAt: number
  responded: boolean
  startedAt: number
}

function createTrial(): { isApple: boolean; stimulus: string } {
  const isApple = Math.random() < APPLE_PROBABILITY
  return { isApple, stimulus: isApple ? APPLE : OBJECTS[Math.floor(Math.random() * OBJECTS.length)] }
}

export function createSartState(): SartState {
  return { phase: 'instruction', trials: [], isApple: false, stimulus: OBJECTS[0], trialStartedAt: 0, responded: false, startedAt: 0 }
}

export function startSart(state: SartState, now: number): SartState {
  return { ...state, ...createTrial(), phase: 'running', startedAt: now, trialStartedAt: now, responded: false }
}

function advance(state: SartState, now: number): SartState {
  if (now - state.startedAt >= TOTAL_LIMIT_MS) {
    return { ...state, phase: 'finished' }
  }
  return { ...state, ...createTrial(), trialStartedAt: now, responded: false }
}

export function respondSart(state: SartState, now: number): SartState {
  if (state.phase !== 'running' || state.responded) {
    return state
  }
  const trial: Trial = { stimulus: state.stimulus, response: 'πάτησε', isCorrect: !state.isApple, responseTimeMs: Math.max(0, now - state.trialStartedAt) }
  return advance({ ...state, trials: [...state.trials, trial], responded: true }, now)
}

export function tickSart(state: SartState, now: number): SartState {
  if (state.phase !== 'running' || state.responded) {
    return state
  }
  if (now - state.trialStartedAt < TRIAL_DISPLAY_MS) {
    return state
  }
  const trial: Trial = { stimulus: state.stimulus, response: 'δεν πάτησε', isCorrect: state.isApple, responseTimeMs: TRIAL_DISPLAY_MS }
  return advance({ ...state, trials: [...state.trials, trial] }, now)
}

export function getSartSummary(state: SartState): TaskSummary {
  return summarizeTrials(state.trials, null)
}

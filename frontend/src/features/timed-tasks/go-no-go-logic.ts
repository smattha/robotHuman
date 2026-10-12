import type { TaskSummary, Trial } from '../../domain/timed-task'
import { summarizeTrials } from '../../domain/timed-task'

const GO_DISPLAY_MS = 2000
const NO_GO_DISPLAY_MS = 1000
const TOTAL_LIMIT_MS = 20000

export type GoNoGoState = {
  phase: 'instruction' | 'running' | 'finished'
  trials: Trial[]
  isGo: boolean
  trialDisplayMs: number
  trialStartedAt: number
  responded: boolean
  startedAt: number
}

function createTrial(): { isGo: boolean; trialDisplayMs: number } {
  const isGo = Math.random() < 0.5
  return { isGo, trialDisplayMs: isGo ? GO_DISPLAY_MS : NO_GO_DISPLAY_MS }
}

export function createGoNoGoState(): GoNoGoState {
  return { phase: 'instruction', trials: [], isGo: true, trialDisplayMs: GO_DISPLAY_MS, trialStartedAt: 0, responded: false, startedAt: 0 }
}

export function startGoNoGo(state: GoNoGoState, now: number): GoNoGoState {
  return { ...state, ...createTrial(), phase: 'running', startedAt: now, trialStartedAt: now, responded: false }
}

function advance(state: GoNoGoState, now: number): GoNoGoState {
  if (now - state.startedAt >= TOTAL_LIMIT_MS) {
    return { ...state, phase: 'finished' }
  }
  return { ...state, ...createTrial(), trialStartedAt: now, responded: false }
}

export function respondGoNoGo(state: GoNoGoState, now: number): GoNoGoState {
  if (state.phase !== 'running' || state.responded) {
    return state
  }
  const trial: Trial = { stimulus: state.isGo ? 'Ξεκίνα' : 'Στοπ', response: 'πάτησε', isCorrect: state.isGo, responseTimeMs: Math.max(0, now - state.trialStartedAt) }
  return advance({ ...state, trials: [...state.trials, trial], responded: true }, now)
}

export function tickGoNoGo(state: GoNoGoState, now: number): GoNoGoState {
  if (state.phase !== 'running' || state.responded) {
    return state
  }
  if (now - state.trialStartedAt < state.trialDisplayMs) {
    return state
  }
  const trial: Trial = { stimulus: state.isGo ? 'Ξεκίνα' : 'Στοπ', response: 'δεν πάτησε', isCorrect: !state.isGo, responseTimeMs: state.trialDisplayMs }
  return advance({ ...state, trials: [...state.trials, trial] }, now)
}

export function getGoNoGoSummary(state: GoNoGoState): TaskSummary {
  return summarizeTrials(state.trials, null)
}

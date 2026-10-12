import type { TaskSummary, Trial } from '../../domain/timed-task'
import { summarizeTrials } from '../../domain/timed-task'

const COLORS = ['red', 'green', 'blue', 'yellow'] as const
export type StroopColor = (typeof COLORS)[number]

export const COLOR_WORDS: Record<StroopColor, string> = {
  red: 'Κόκκινο',
  green: 'Πράσινο',
  blue: 'Μπλε',
  yellow: 'Κίτρινο',
}

const TRIAL_DISPLAY_MS = 2000
const TOTAL_LIMIT_MS = 30000

export type StroopState = {
  phase: 'instruction' | 'running' | 'finished'
  trials: Trial[]
  word: StroopColor
  ink: StroopColor
  shouldRespond: boolean
  trialStartedAt: number
  responded: boolean
  startedAt: number
}

function randomColor(): StroopColor {
  return COLORS[Math.floor(Math.random() * COLORS.length)]
}

function createTrial(): { word: StroopColor; ink: StroopColor; shouldRespond: boolean } {
  const ink = randomColor()
  const isMatch = Math.random() < 0.5
  const word = isMatch ? ink : randomColor()
  return { word, ink, shouldRespond: word === ink }
}

function stimulusLabel(word: StroopColor, ink: StroopColor): string {
  return `${COLOR_WORDS[word]} (χρώμα: ${COLOR_WORDS[ink]})`
}

export function createStroopState(): StroopState {
  return {
    phase: 'instruction',
    trials: [],
    word: 'red',
    ink: 'red',
    shouldRespond: true,
    trialStartedAt: 0,
    responded: false,
    startedAt: 0,
  }
}

export function startStroop(state: StroopState, now: number): StroopState {
  return { ...state, ...createTrial(), phase: 'running', startedAt: now, trialStartedAt: now, responded: false }
}

function advance(state: StroopState, now: number): StroopState {
  if (now - state.startedAt >= TOTAL_LIMIT_MS) return { ...state, phase: 'finished' }
  return { ...state, ...createTrial(), trialStartedAt: now, responded: false }
}

export function respondStroop(state: StroopState, now: number): StroopState {
  if (state.phase !== 'running' || state.responded) return state
  const trial: Trial = {
    stimulus: stimulusLabel(state.word, state.ink),
    response: 'πάτησε',
    isCorrect: state.shouldRespond,
    responseTimeMs: Math.max(0, now - state.trialStartedAt),
  }
  return advance({ ...state, trials: [...state.trials, trial], responded: true }, now)
}

export function tickStroop(state: StroopState, now: number): StroopState {
  if (state.phase !== 'running' || state.responded) return state
  if (now - state.trialStartedAt < TRIAL_DISPLAY_MS) return state
  const trial: Trial = {
    stimulus: stimulusLabel(state.word, state.ink),
    response: 'δεν πάτησε',
    isCorrect: !state.shouldRespond,
    responseTimeMs: TRIAL_DISPLAY_MS,
  }
  return advance({ ...state, trials: [...state.trials, trial] }, now)
}

export function getStroopSummary(state: StroopState): TaskSummary {
  return summarizeTrials(state.trials, null)
}

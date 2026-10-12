import type { TaskSummary, Trial } from '../../domain/timed-task'
import { summarizeTrials } from '../../domain/timed-task'

const TILE_COUNT = 9
const STARTING_SEQUENCE_LENGTH = 3
const MAX_ERRORS = 3
const DISPLAY_STEP_MS = 650

export type CorsiState = {
  phase: 'instruction' | 'showing' | 'answering' | 'finished'
  sequence: number[]
  answer: number[]
  trials: Trial[]
  level: number
  consecutiveErrors: number
  totalErrors: number
  sequenceIndex: number
  nextStepAt: number
  answerStartedAt: number
  maxSequenceLength: number
}

function createSequence(length: number): number[] {
  const tiles = Array.from({ length: TILE_COUNT }, (_, index) => index)
  return tiles.sort(() => Math.random() - 0.5).slice(0, length)
}

export function createCorsiState(): CorsiState {
  return {
    phase: 'instruction', sequence: [], answer: [], trials: [], level: STARTING_SEQUENCE_LENGTH,
    consecutiveErrors: 0, totalErrors: 0, sequenceIndex: 0, nextStepAt: 0,
    answerStartedAt: 0, maxSequenceLength: 0,
  }
}

export function startCorsi(state: CorsiState, now: number): CorsiState {
  return {
    ...state, phase: 'showing', sequence: createSequence(state.level), answer: [],
    sequenceIndex: 0, nextStepAt: now, answerStartedAt: 0,
  }
}

export function tickCorsi(state: CorsiState, now: number): CorsiState {
  if (state.phase !== 'showing' || now < state.nextStepAt) return state
  if (state.sequenceIndex >= state.sequence.length) {
    return { ...state, phase: 'answering', answerStartedAt: now }
  }
  return { ...state, sequenceIndex: state.sequenceIndex + 1, nextStepAt: now + DISPLAY_STEP_MS }
}

export function respondCorsi(state: CorsiState, tile: number, now: number): CorsiState {
  if (state.phase !== 'answering' || tile < 0 || tile >= TILE_COUNT) return state
  const answer = [...state.answer, tile]
  const expected = state.sequence[answer.length - 1]
  if (tile !== expected) {
    const trial: Trial = {
      stimulus: state.sequence.map((value) => value + 1).join('-'),
      response: answer.map((value) => value + 1).join('-'),
      isCorrect: false,
      responseTimeMs: Math.max(0, now - state.answerStartedAt),
    }
    const consecutiveErrors = state.consecutiveErrors + 1
    const totalErrors = state.totalErrors + 1
    if (consecutiveErrors >= 2 || totalErrors >= MAX_ERRORS) {
      return { ...state, phase: 'finished', answer, trials: [...state.trials, trial], consecutiveErrors, totalErrors }
    }
    return {
      ...state, phase: 'showing', answer: [], sequence: createSequence(state.level),
      sequenceIndex: 0, nextStepAt: now + 1000, consecutiveErrors, totalErrors,
      trials: [...state.trials, trial],
    }
  }
  if (answer.length < state.sequence.length) return { ...state, answer }

  const trial: Trial = {
    stimulus: state.sequence.map((value) => value + 1).join('-'),
    response: answer.map((value) => value + 1).join('-'),
    isCorrect: true,
    responseTimeMs: Math.max(0, now - state.answerStartedAt),
  }
  const level = state.level + 1
  return {
    ...state, phase: 'showing', level, answer: [], sequence: createSequence(level),
    sequenceIndex: 0, nextStepAt: now + 1000, answerStartedAt: 0, consecutiveErrors: 0,
    maxSequenceLength: Math.max(state.maxSequenceLength, state.level), trials: [...state.trials, trial],
  }
}

export function getCorsiSummary(state: CorsiState): TaskSummary {
  return summarizeTrials(state.trials, state.maxSequenceLength)
}

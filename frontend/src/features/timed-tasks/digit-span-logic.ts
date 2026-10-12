import type { TaskSummary, Trial } from '../../domain/timed-task'
import { summarizeTrials } from '../../domain/timed-task'

const MAX_CONSECUTIVE_ERRORS = 2
const DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
const PRESENT_DIGIT_MS = 800

export type DigitSpanState = {
  phase: 'instruction' | 'showing' | 'answering' | 'finished'
  sequence: string[]
  answer: string
  trials: Trial[]
  level: number
  consecutiveErrors: number
  sequenceIndex: number
  nextStepAt: number
  answerStartedAt: number
  maxSequenceLength: number
}

function createSequence(length: number): string[] {
  return Array.from({ length }, () => DIGITS[Math.floor(Math.random() * DIGITS.length)])
}

export function createDigitSpanState(): DigitSpanState {
  return {
    phase: 'instruction', sequence: [], answer: '', trials: [], level: 1,
    consecutiveErrors: 0, sequenceIndex: 0, nextStepAt: 0, answerStartedAt: 0,
    maxSequenceLength: 0,
  }
}

export function startDigitSpan(state: DigitSpanState, now: number): DigitSpanState {
  return {
    ...state, phase: 'showing', sequence: createSequence(state.level), answer: '',
    sequenceIndex: 0, nextStepAt: now,
  }
}

export function tickDigitSpan(state: DigitSpanState, now: number): DigitSpanState {
  if (state.phase !== 'showing' || now < state.nextStepAt) return state
  if (state.sequenceIndex >= state.sequence.length) {
    return { ...state, phase: 'answering', sequenceIndex: 0, answerStartedAt: now }
  }
  return { ...state, sequenceIndex: state.sequenceIndex + 1, nextStepAt: now + PRESENT_DIGIT_MS }
}

export function enterDigit(state: DigitSpanState, digit: string): DigitSpanState {
  if (state.phase !== 'answering' || !DIGITS.includes(digit)) return state
  return { ...state, answer: state.answer + digit }
}

export function clearDigit(state: DigitSpanState): DigitSpanState {
  if (state.phase !== 'answering' || state.answer.length === 0) return state
  return { ...state, answer: state.answer.slice(0, -1) }
}

export function submitDigitSpan(state: DigitSpanState, now: number): DigitSpanState {
  if (state.phase !== 'answering' || state.answer.length === 0) return state
  const expected = state.sequence.join('')
  const isCorrect = state.answer === expected
  const trial: Trial = {
    stimulus: expected,
    response: state.answer,
    isCorrect,
    responseTimeMs: Math.max(0, now - state.answerStartedAt),
  }
  const trials = [...state.trials, trial]
  const consecutiveErrors = isCorrect ? 0 : state.consecutiveErrors + 1
  if (consecutiveErrors >= MAX_CONSECUTIVE_ERRORS) {
    return { ...state, phase: 'finished', trials, consecutiveErrors }
  }
  const level = isCorrect ? state.level + 1 : state.level
  return {
    ...state, phase: 'showing', trials, consecutiveErrors, level,
    maxSequenceLength: isCorrect ? Math.max(state.maxSequenceLength, state.level) : state.maxSequenceLength,
    sequence: createSequence(level), answer: '', sequenceIndex: 0, nextStepAt: now + 800,
  }
}

export function getDigitSpanSummary(state: DigitSpanState): TaskSummary {
  return summarizeTrials(state.trials, state.maxSequenceLength)
}

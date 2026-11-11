import { useCallback, useEffect, useRef, useState } from 'react'
import type { AnswerEvaluation, Exercise } from '../../../domain/exercise'
import { evaluateQuestion, getPrimaryQuestion } from '../../../domain/exercise'
import { playCorrectSound, playIncorrectSound } from '../../../domain/sound-effects'

export type ExerciseEnginePhase = 'question' | 'playing' | 'submitted'

export type ExerciseEngineState = {
  phase: ExerciseEnginePhase
  frameIndex: number | null
  selectedOptionId: string | null
  isSubmitted: boolean
  isCorrect: boolean | null
  feedback: string | null
  isNarrating: boolean
  isPreparing: boolean
}

export type ReportedRuntimeState = {
  isNarrating: boolean
  isPreparing: boolean
  phase: 'question' | 'playing'
  frameIndex: number | null
}

type UseExerciseEngineOptions = {
  exercise: Exercise
  onAnswer: (optionId: string, evaluation: AnswerEvaluation) => void
  onComplete: () => void
  onStateChange?: (state: ExerciseEngineState) => void
}

const AUTO_ADVANCE_MS = 3000
const INITIAL_REPORTED: ReportedRuntimeState = { isNarrating: false, isPreparing: false, phase: 'question', frameIndex: null }

export function useExerciseEngine({ exercise, onAnswer, onComplete, onStateChange }: UseExerciseEngineOptions) {
  const [selectedOptionId, setSelectedOptionId] = useState<string | null>(null)
  const [evaluation, setEvaluation] = useState<AnswerEvaluation | null>(null)
  const [celebrate, setCelebrate] = useState(false)
  const [reported, setReported] = useState<ReportedRuntimeState>(INITIAL_REPORTED)
  const feedbackHandledRef = useRef(false)
  const isSubmitted = evaluation !== null

  useEffect(() => {
    setSelectedOptionId(null)
    setEvaluation(null)
    setCelebrate(false)
    feedbackHandledRef.current = false
  }, [exercise.id])

  useEffect(() => {
    if (!isSubmitted || feedbackHandledRef.current) return
    feedbackHandledRef.current = true
    if (evaluation?.isCorrect) {
      setCelebrate(true)
      playCorrectSound()
    } else {
      playIncorrectSound()
    }
  }, [isSubmitted, evaluation])

  const onCompleteRef = useRef(onComplete)
  onCompleteRef.current = onComplete
  useEffect(() => {
    if (!isSubmitted) return
    const timer = setTimeout(() => onCompleteRef.current(), AUTO_ADVANCE_MS)
    return () => clearTimeout(timer)
  }, [isSubmitted])

  const handleAnswer = useCallback((optionId: string) => {
    if (evaluation) return
    const result = evaluateQuestion(getPrimaryQuestion(exercise), optionId)
    setSelectedOptionId(optionId)
    setEvaluation(result)
    onAnswer(optionId, result)
  }, [exercise, evaluation, onAnswer])

  const onRuntimeState = useCallback((next: ReportedRuntimeState) => {
    setReported((prev) => (
      prev.isNarrating === next.isNarrating
        && prev.isPreparing === next.isPreparing
        && prev.phase === next.phase
        && prev.frameIndex === next.frameIndex
        ? prev
        : next
    ))
  }, [])

  const state: ExerciseEngineState = {
    phase: isSubmitted ? 'submitted' : reported.phase,
    frameIndex: isSubmitted ? null : reported.frameIndex,
    selectedOptionId,
    isSubmitted,
    isCorrect: evaluation?.isCorrect ?? null,
    feedback: evaluation?.feedback ?? null,
    isNarrating: reported.isNarrating,
    isPreparing: reported.isPreparing,
  }

  const onStateChangeRef = useRef(onStateChange)
  onStateChangeRef.current = onStateChange
  useEffect(() => {
    onStateChangeRef.current?.(state)
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [state.phase, state.frameIndex, state.selectedOptionId, state.isSubmitted, state.isCorrect, state.isNarrating, state.isPreparing])

  return {
    state,
    selectedOptionId,
    isSubmitted,
    feedback: evaluation?.feedback ?? null,
    isCorrect: evaluation?.isCorrect ?? null,
    celebrate,
    handleAnswer,
    onRuntimeState,
  }
}

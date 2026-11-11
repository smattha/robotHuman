import type { Exercise } from '../domain/exercise'

const exerciseModules = import.meta.glob<{ default: Exercise }>(
  ['./image-question/*/index.ts', './story/*/index.ts'],
  { eager: true },
)

export const exercises: Exercise[] = Object.values(exerciseModules)
  .map((module) => module.default)
  .sort((a, b) => a.position - b.position)

export const firstExercise = exercises[0]

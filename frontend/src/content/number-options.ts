import type { AnswerOption } from '../domain/exercise'

export function numberOptions(): AnswerOption[] {
  return [
    { id: 'one', label: '1', detail: 'Ένα' },
    { id: 'two', label: '2', detail: 'Δύο' },
    { id: 'three', label: '3', detail: 'Τρία' },
    { id: 'four', label: '4', detail: 'Τέσσερα' },
    { id: 'five', label: '5', detail: 'Πέντε' },
  ]
}

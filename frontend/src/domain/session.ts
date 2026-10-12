import type { AnswerEvaluation } from './exercise'

export type Screen = 'welcome' | 'library' | 'exercise' | 'completed'

export type SessionState = {
  screen: Screen
  exerciseIndex: number
  mode: 'single' | 'all'
  userName: string | null
  selectedOptionId: string | null
  evaluation: AnswerEvaluation | null
}

export type SessionAction =
  | { type: 'START' }
  | { type: 'OPEN_EXERCISE'; index: number }
  | { type: 'START_ALL'; userName: string }
  | { type: 'SELECT_OPTION'; optionId: string }
  | { type: 'SUBMIT_ANSWER'; evaluation: AnswerEvaluation }
  | { type: 'COMPLETE' }
  | { type: 'NEXT_EXERCISE' }
  | { type: 'RESTART' }
  | { type: 'BACK_TO_LIBRARY' }

export const initialSessionState: SessionState = {
  screen: 'welcome',
  exerciseIndex: 0,
  mode: 'single',
  userName: null,
  selectedOptionId: null,
  evaluation: null,
}

export function sessionReducer(state: SessionState, action: SessionAction): SessionState {
  switch (action.type) {
    case 'START':
      return { ...initialSessionState, screen: 'library' }
    case 'OPEN_EXERCISE':
      return { ...initialSessionState, screen: 'exercise', exerciseIndex: action.index }
    case 'START_ALL':
      return { ...initialSessionState, screen: 'exercise', mode: 'all', userName: action.userName }
    case 'SELECT_OPTION':
      return state.evaluation ? state : { ...state, selectedOptionId: action.optionId }
    case 'SUBMIT_ANSWER':
      return { ...state, evaluation: action.evaluation }
    case 'COMPLETE':
      return { ...state, screen: 'completed' }
    case 'NEXT_EXERCISE':
      return { ...state, exerciseIndex: state.exerciseIndex + 1, selectedOptionId: null, evaluation: null }
    case 'RESTART':
      return { ...initialSessionState, screen: 'exercise', exerciseIndex: state.exerciseIndex }
    case 'BACK_TO_LIBRARY':
      return { ...initialSessionState, screen: 'library' }
  }
}

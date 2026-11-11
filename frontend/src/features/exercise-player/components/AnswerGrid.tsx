import type { AnswerOption } from '../../../domain/exercise-model'

type AnswerGridProps = {
  options: AnswerOption[]
  selectedOptionId: string | null
  isSubmitted: boolean
  onAnswer: (optionId: string) => void
  ariaLabel?: string
}

export function AnswerGrid({ options, selectedOptionId, isSubmitted, onAnswer, ariaLabel = 'Επιλογές απάντησης' }: AnswerGridProps) {
  return (
    <div className="answer-list" role="radiogroup" aria-label={ariaLabel}>
      {options.map((option) => {
        const isSelected = selectedOptionId === option.id
        return (
          <button
            className={`answer-option${option.imagePath ? ' answer-option-image' : ''}${isSelected ? ' selected' : ''}`}
            type="button"
            role="radio"
            aria-label={`${option.label}: ${option.detail}`}
            aria-checked={isSelected}
            disabled={isSubmitted}
            key={option.id}
            onClick={() => onAnswer(option.id)}
          >
            {option.imagePath ? (
              <img className="option-image" src={option.imagePath} alt="" />
            ) : (
              <>
                <span className="option-number" aria-hidden="true">{option.label}</span>
                <span className="option-detail" aria-hidden="true">{option.detail}</span>
                <span className="option-check" aria-hidden="true">{isSelected ? '●' : '○'}</span>
              </>
            )}
          </button>
        )
      })}
    </div>
  )
}

import type { AnswerOption } from './exercise'

function normalize(text: string): string {
  return text.toLocaleLowerCase('el-GR').normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[^\p{L}\p{N}]+/gu, ' ').trim()
}

const NUMBER_WORDS: Record<string, string> = {
  '1': 'ενα', '2': 'δυο', '3': 'τρια', '4': 'τεσσερα', '5': 'πεντε', '8': 'οκτω',
}
const LETTER_WORDS: Record<string, string> = { 'Α': 'αλφα', 'Β': 'βητα', 'Γ': 'γαμμα', 'Δ': 'δελτα', 'Ε': 'εψιλον' }

export function matchSpokenOption(transcript: string, options: AnswerOption[]): string | null {
  const spoken = normalize(transcript)
  if (!spoken) return null
  const exact = options.find((option) => {
    const labels = [option.label, option.detail, NUMBER_WORDS[option.label], LETTER_WORDS[option.label]].filter((value): value is string => Boolean(value))
    return labels.some((label) => normalize(label) === spoken)
  })
  if (exact) return exact.id

  const candidates = options.filter((option) => {
    const detail = normalize(option.detail).split(' ')
    return detail.some((word) => word.length > 3 && spoken.split(' ').includes(word))
  })
  return candidates.length === 1 ? candidates[0].id : null
}

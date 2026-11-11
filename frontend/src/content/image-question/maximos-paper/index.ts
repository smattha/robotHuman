import type { ImageQuestionExercise } from '../../../domain/exercise'

const maximosPaper: ImageQuestionExercise = {
  id: 'maximos-paper',
  position: 8,
  type: 'image-question',
  title: 'Ο Μάξιμος',
  category: 'observation-attention',
  skillTags: ['spatial-matching'],
  description: 'Βρες το κομμάτι χαρτιού που ταιριάζει.',
  instructions: 'Ο Μάξιμος έκοψε ένα φύλλο χαρτί στα δύο. Κοίτα το κομμάτι που φαίνεται επάνω και βρες το άλλο του μισό.',
  imagePath: '/ex8/main-image.png',
  question: {
    id: 'which-paper-half',
    text: 'Ποιο από τα κομμάτια είναι το άλλο μισό του χαρτιού;',
    options: [
      { id: 'alpha', label: 'Α', detail: 'Επιλογή Α', imagePath: '/ex8/answer-a.png' },
      { id: 'beta', label: 'Β', detail: 'Επιλογή Β', imagePath: '/ex8/answer-b.png' },
      { id: 'gamma', label: 'Γ', detail: 'Επιλογή Γ', imagePath: '/ex8/answer-c.png' },
      { id: 'delta', label: 'Δ', detail: 'Επιλογή Δ', imagePath: '/ex8/answer-d.png' },
      { id: 'epsilon', label: 'Ε', detail: 'Επιλογή Ε', imagePath: '/ex8/answer-e.png' },
    ],
    correctOptionId: 'epsilon',
    correctFeedback: 'Μπράβο! Βρήκες το κομμάτι που ταιριάζει.',
    incorrectFeedback: 'Καλή προσπάθεια! Κοίτα προσεκτικά το σχήμα της κομμένης πλευράς.',
  },
}

export default maximosPaper

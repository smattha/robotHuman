import type { ImageQuestionExercise } from '../../../domain/exercise'

const objectRiddle: ImageQuestionExercise = {
  id: 'object-riddle',
  position: 2,
  type: 'image-question',
  title: 'Άσκηση προσοχής',
  category: 'observation-attention',
  skillTags: ['spatial-matching'],
  description: 'Βρες με ποιο αντικείμενο μοιάζει η κεντρική εικόνα.',
  instructions: 'Κοίτα προσεκτικά την κεντρική εικόνα και διάλεξε την επιλογή που σου φαίνεται σωστή.',
  imagePath: '/ex2/main-image.png',
  question: {
    id: 'which-object-matches',
    text: 'Με ποιο αντικείμενο μοιάζει η κεντρική εικόνα;',
    options: [
      { id: 'alpha', label: 'Α', detail: 'Επιλογή Α', imagePath: '/ex2/answer-a.png' },
      { id: 'beta', label: 'Β', detail: 'Επιλογή Β', imagePath: '/ex2/answer-b.png' },
      { id: 'gamma', label: 'Γ', detail: 'Επιλογή Γ', imagePath: '/ex2/answer-c.png' },
      { id: 'delta', label: 'Δ', detail: 'Επιλογή Δ', imagePath: '/ex2/answer-d.png' },
      { id: 'epsilon', label: 'Ε', detail: 'Επιλογή Ε', imagePath: '/ex2/answer-e.png' },
    ],
    correctOptionId: 'alpha',
    correctFeedback: 'Μπράβο! Διάλεξες τη σωστή επιλογή.',
    incorrectFeedback: 'Καλή προσπάθεια! Κοίτα ξανά τις λεπτομέρειες της εικόνας.',
  },
}

export default objectRiddle

import type { ImageQuestionExercise } from '../../../domain/exercise'

const kangarooMother: ImageQuestionExercise = {
  id: 'kangaroo-mother',
  position: 7,
  type: 'image-question',
  title: 'Η μαμά καγκουρό',
  category: 'math-quantitative',
  skillTags: ['subtraction'],
  description: 'Ένας γρίφος με βάρος και αριθμούς.',
  instructions: 'Η μαμά καγκουρό με το μωρό της ζυγίζουν 60 κιλά. Η μαμά μόνη της ζυγίζει 52 κιλά.',
  imagePath: '/ex7/main-image.png',
  question: {
    id: 'baby-weight',
    text: 'Πόσα κιλά ζυγίζει το μωρό της;',
    options: [
      { id: 'four', label: '4', detail: 'Τέσσερα κιλά' },
      { id: 'eight', label: '8', detail: 'Οκτώ κιλά' },
      { id: 'thirty', label: '30', detail: 'Τριάντα κιλά' },
      { id: 'fifty-six', label: '56', detail: 'Πενήντα έξι κιλά' },
      { id: 'one-hundred-twelve', label: '112', detail: 'Εκατόν δώδεκα κιλά' },
    ],
    correctOptionId: 'eight',
    correctFeedback: 'Μπράβο! 60 μείον 52 κάνει 8.',
    incorrectFeedback: 'Καλή προσπάθεια! Σκέψου πόσα κιλά μένουν όταν αφαιρέσεις το βάρος της μαμάς.',
  },
}

export default kangarooMother

import type { ImageQuestionExercise } from '../../../domain/exercise'

const lionAndDucklings: ImageQuestionExercise = {
  id: 'lion-and-ducklings',
  position: 1,
  type: 'image-question',
  title: 'Το λιοντάρι και τα παπάκια',
  category: 'math-quantitative',
  skillTags: ['counting'],
  description: 'Ένας γρίφος με ζώα και αριθμούς.',
  instructions: 'Διάβασε προσεκτικά τις προτάσεις και διάλεξε την απάντηση που πιστεύεις ότι είναι σωστή.',
  imagePath: '/ex1/main-image.png',
  question: {
    id: 'how-many-ducklings',
    text: 'Πόσα παπάκια ζυγίζουν το ίδιο με το λιοντάρι;',
    options: [
      { id: 'one', label: '1', detail: 'Ένα παπάκι', imagePath: '/ex1/answer-1.png' },
      { id: 'two', label: '2', detail: 'Δύο παπάκια', imagePath: '/ex1/answer-2.png' },
      { id: 'three', label: '3', detail: 'Τρία παπάκια', imagePath: '/ex1/answer-3.png' },
      { id: 'four', label: '4', detail: 'Τέσσερα παπάκια', imagePath: '/ex1/answer-4.png' },
      { id: 'five', label: '5', detail: 'Πέντε παπάκια', imagePath: '/ex1/answer-5.png' },
    ],
    correctOptionId: 'four',
    correctFeedback: 'Μπράβο! Το βρήκες! Το λιοντάρι ζυγίζει όσο τέσσερα παπάκια.',
    incorrectFeedback: 'Καλή προσπάθεια! Σκέψου: ένα λιοντάρι είναι όσο δύο σκυλάκια και κάθε σκυλάκι όσο δύο παπάκια.',
  },
}

export default lionAndDucklings

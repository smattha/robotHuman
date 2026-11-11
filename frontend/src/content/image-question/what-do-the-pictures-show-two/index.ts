import type { ImageQuestionExercise } from '../../../domain/exercise'

const whatDoThePicturesShowTwo: ImageQuestionExercise = {
  id: 'what-do-the-pictures-show-two',
  position: 12,
  type: 'image-question',
  title: 'Τι δείχνουν οι εικόνες 2',
  category: 'vocabulary-image',
  skillTags: ['image-recognition'],
  description: 'Ονόμασε αυτό που βλέπεις στην εικόνα.',
  instructions: 'Στην αρχική έκδοση η δραστηριότητα δείχνει μια εικόνα σκύλου. Διάλεξε τη λέξη που την περιγράφει.',
  question: {
    id: 'what-does-the-picture-show',
    text: 'Τι δείχνει η εικόνα;',
    options: [
      { id: 'dog', label: 'Α', detail: 'Σκυλί', imagePath: '/ex12/dog.png' },
      { id: 'apple', label: 'Β', detail: 'Μήλο', imagePath: '/ex12/apple.png' },
    ],
    correctOptionId: 'dog',
    correctFeedback: 'Μπράβο! Η εικόνα δείχνει ένα σκυλί.',
    incorrectFeedback: 'Καλή προσπάθεια! Κοίτα ξανά το ζώο στην εικόνα.',
  },
}

export default whatDoThePicturesShowTwo

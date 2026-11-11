import type { ImageQuestionExercise } from '../../../domain/exercise'

const whatDoThePicturesShow: ImageQuestionExercise = {
  id: 'what-do-the-pictures-show',
  position: 6,
  type: 'image-question',
  title: 'Τι δείχνουν οι εικόνες',
  category: 'vocabulary-image',
  skillTags: ['image-recognition'],
  description: 'Ονόμασε αυτό που βλέπεις στην εικόνα.',
  instructions: 'Στην αρχική έκδοση η δραστηριότητα δείχνει μια εικόνα αλόγου. Διάλεξε τη λέξη που την περιγράφει.',
  question: {
    id: 'what-does-the-picture-show',
    text: 'Τι δείχνει η εικόνα;',
    options: [
      { id: 'horse', label: 'Α', detail: 'Άλογο', imagePath: '/ex6/horse.png' },
      { id: 'orange', label: 'Β', detail: 'Πορτοκάλι', imagePath: '/ex6/orange.png' },
    ],
    correctOptionId: 'horse',
    correctFeedback: 'Μπράβο! Η εικόνα δείχνει ένα άλογο.',
    incorrectFeedback: 'Καλή προσπάθεια! Κοίτα ξανά το ζώο στην εικόνα.',
  },
}

export default whatDoThePicturesShow

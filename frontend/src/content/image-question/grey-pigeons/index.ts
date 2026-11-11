import type { ImageQuestionExercise } from '../../../domain/exercise'
import { numberOptions } from '../../number-options'

const greyPigeons: ImageQuestionExercise = {
  id: 'grey-pigeons',
  position: 11,
  type: 'image-question',
  title: 'Τα γκρι περιστέρια',
  category: 'observation-attention',
  skillTags: ['counting'],
  description: 'Μέτρησε πόσα γκρι περιστέρια υπάρχουν.',
  instructions: 'Κοίτα προσεκτικά την εικόνα και μέτρησε μόνο τα γκρι περιστέρια.',
  imagePath: '/ex11/main-image.png',
  question: {
    id: 'how-many-grey-pigeons',
    text: 'Πόσα γκρι περιστέρια υπάρχουν;',
    options: numberOptions(),
    correctOptionId: 'three',
    correctFeedback: 'Μπράβο! Βρήκες τρία γκρι περιστέρια.',
    incorrectFeedback: 'Καλή προσπάθεια! Κοίτα ξανά μόνο τα περιστέρια με γκρι χρώμα.',
  },
}

export default greyPigeons

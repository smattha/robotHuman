import type { ImageQuestionExercise } from '../../../domain/exercise'
import { numberOptions } from '../../number-options'

const hatRiddle: ImageQuestionExercise = {
  id: 'hat-riddle',
  position: 5,
  type: 'image-question',
  title: 'Παιχνίδι με γρίφους',
  category: 'observation-attention',
  skillTags: ['counting'],
  description: 'Μέτρησε προσεκτικά τους ανθρώπους που φορούν καπέλο.',
  instructions: 'Κοίτα προσεκτικά την εικόνα της άσκησης και μέτρησε πριν απαντήσεις.',
  imagePath: '/ex5/main-image.png',
  question: {
    id: 'how-many-hats',
    text: 'Πόσοι άνθρωποι φορούν καπέλο;',
    options: numberOptions(),
    correctOptionId: 'two',
    correctFeedback: 'Μπράβο! Βρήκες δύο ανθρώπους με καπέλο.',
    incorrectFeedback: 'Καλή προσπάθεια! Μέτρησε ξανά έναν έναν τους ανθρώπους με καπέλο.',
  },
}

export default hatRiddle

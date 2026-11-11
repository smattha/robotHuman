import type { StoryExercise } from '../../../domain/exercise'

const mariaAndMother: StoryExercise = {
  id: 'maria-and-mother',
  position: 4,
  type: 'story',
  title: 'Η Μαρία και η μαμά της',
  category: 'story-comprehension',
  skillTags: ['emotion-recognition'],
  description: 'Βρες ποιος είπε κάτι που ίσως στεναχώρησε έναν ήρωα.',
  instructions: 'Η Μαρία είναι τριών ετών. Μια φίλη της μαμάς της έρχεται επίσκεψη και η μαμά λέει πως δεν έχει γνωρίσει τον γιο της φίλης.',
  frames: [
    { id: 'maria-frame-1', imagePath: '/ex4/story-1.png', text: 'Η Μαρία είναι ένα μικρό κορίτσι τριών ετών.' },
    { id: 'maria-frame-2', imagePath: '/ex4/story-2.png', text: 'Το κουδούνι χτυπά και η μαμά της Μαρίας ανοίγει την πόρτα.' },
    { id: 'maria-frame-3', imagePath: '/ex4/story-3.png', text: 'Μια φίλη της μαμάς έρχεται επίσκεψη.' },
    { id: 'maria-frame-4', imagePath: '/ex4/story-4.png', text: 'Η μαμά της Μαρίας χαιρετά τη φίλη της.' },
    { id: 'maria-frame-5', imagePath: '/ex4/story-5.png', text: 'Η μαμά λέει πως δεν έχει γνωρίσει τον γιο της φίλης.' },
  ],
  questions: [
    {
      id: 'who-said-it',
      text: 'Ποιος είπε κάτι που μπορεί να στεναχώρησε ή να θύμωσε κάποιον;',
      options: [
        { id: 'maria', label: 'Α', detail: 'Η Μαρία', imagePath: '/ex4/answer-maria.png' },
        { id: 'mother', label: 'Β', detail: 'Η μαμά', imagePath: '/ex4/answer-mother.png' },
        { id: 'friend', label: 'Γ', detail: 'Η φίλη', imagePath: '/ex4/answer-friend.png' },
      ],
      correctOptionId: 'friend',
      correctFeedback: 'Μπράβο! Διάλεξες τη φίλη.',
      incorrectFeedback: 'Καλή προσπάθεια! Σκέψου ξανά ποιος μίλησε στην ιστορία.',
    },
  ],
}

export default mariaAndMother

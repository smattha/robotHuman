import type { StoryExercise } from '../../../domain/exercise'

const georgeAndChocolate: StoryExercise = {
  id: 'george-and-chocolate',
  position: 3,
  type: 'story',
  title: 'Ο Γιωργάκης και η σοκολάτα',
  category: 'story-comprehension',
  skillTags: ['false-belief'],
  description: 'Άκουσε μια ιστορία και σκέψου τι θα κάνει ο Γιωργάκης.',
  instructions: 'Ο Γιωργάκης έκρυψε τη σοκολάτα στο ντουλάπι. Όσο έπαιζε έξω, η γιαγιά του τη βρήκε και την έβαλε στο ψυγείο.',
  frames: [
    { id: 'george-frame-1', imagePath: '/ex3/story-1.png', text: 'Ο Γιωργάκης κρύβει τη σοκολάτα στο ντουλάπι πριν βγει έξω.' },
    { id: 'george-frame-2', imagePath: '/ex3/story-2.png', text: 'Η γιαγιά βρίσκει τη σοκολάτα και τη βάζει στο ψυγείο, χωρίς να το δει ο Γιωργάκης.' },
  ],
  questions: [
    {
      id: 'where-will-george-look',
      text: 'Όταν ο Γιωργάκης γυρίσει σπίτι, πού θα ψάξει για τη σοκολάτα του;',
      options: [
        { id: 'cupboard', label: 'Α', detail: 'Στο ντουλάπι', imagePath: '/ex3/answer-cupboard.png' },
        { id: 'fridge', label: 'Β', detail: 'Στο ψυγείο', imagePath: '/ex3/answer-fridge.png' },
      ],
      correctOptionId: 'cupboard',
      correctFeedback: 'Μπράβο! Ο Γιωργάκης δεν ξέρει ότι η γιαγιά έβαλε τη σοκολάτα στο ψυγείο.',
      incorrectFeedback: 'Καλή προσπάθεια! Θυμήσου πού έκρυψε ο ίδιος τη σοκολάτα πριν βγει έξω.',
    },
  ],
}

export default georgeAndChocolate

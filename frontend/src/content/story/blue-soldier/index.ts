import type { StoryExercise } from '../../../domain/exercise'

const blueSoldier: StoryExercise = {
  id: 'blue-soldier',
  position: 9,
  type: 'story',
  title: 'Ο μικρός στρατιώτης',
  category: 'story-comprehension',
  skillTags: ['deception'],
  description: 'Άκουσε την ιστορία και σκέψου τι θα απαντήσει ο στρατιώτης.',
  instructions: 'Ένας μπλε στρατιώτης ξέρει ότι τα τανκς είναι στο βουνό. Θέλει να ξεγελάσει τους αντιπάλους που τον ρωτούν πού βρίσκονται.',
  frames: [
    { id: 'soldier-frame-1', imagePath: '/ex9/story-1.png', text: 'Ο κόκκινος στρατός συναντά έναν στρατιώτη του μπλε στρατού.' },
    { id: 'soldier-frame-2', imagePath: '/ex9/story-2.png', text: 'Τον ρωτούν αν τα τανκς βρίσκονται στη θάλασσα ή στο βουνό.' },
    { id: 'soldier-frame-3', imagePath: '/ex9/story-3.png', text: 'Τα τανκς είναι στο βουνό, αλλά ο μπλε στρατιώτης θέλει να τους ξεγελάσει.' },
  ],
  questions: [
    {
      id: 'soldier-answer',
      text: 'Τι θα απαντήσει ο μπλε στρατιώτης;',
      options: [
        { id: 'mountain', label: 'Α', detail: 'Στο βουνό', imagePath: '/ex9/answer-mountain.png' },
        { id: 'sea', label: 'Β', detail: 'Στη θάλασσα', imagePath: '/ex9/answer-sea.png' },
      ],
      correctOptionId: 'sea',
      correctFeedback: 'Μπράβο! Για να τους ξεγελάσει, θα πει ότι τα τανκς είναι στη θάλασσα.',
      incorrectFeedback: 'Καλή προσπάθεια! Θυμήσου ότι θέλει να δώσει λάθος πληροφορία στους αντιπάλους.',
    },
  ],
}

export default blueSoldier

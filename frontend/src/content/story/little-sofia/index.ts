import type { StoryExercise } from '../../../domain/exercise'

const littleSofia: StoryExercise = {
  id: 'little-sofia',
  position: 10,
  type: 'story',
  title: 'Η μικρή Σοφία',
  category: 'story-comprehension',
  skillTags: ['emotion-recognition'],
  description: 'Βρες ποιος είπε κάτι που μπορεί να στεναχώρησε κάποιον.',
  instructions: 'Η Σοφία χαίρεται για τη νέα κασετίνα της. Η φίλη της λέει ότι η κασετίνα είναι απαίσια.',
  frames: [
    { id: 'sofia-frame-1', imagePath: '/ex10/story-1.png', text: 'Η Σοφία είναι μαθήτρια στην τρίτη δημοτικού.' },
    { id: 'sofia-frame-2', imagePath: '/ex10/story-2.png', text: 'Χαίρεται για την καινούρια της κασετίνα.' },
    { id: 'sofia-frame-3', imagePath: '/ex10/story-3.png', text: 'Η φίλη της μπαίνει στην τάξη.' },
    { id: 'sofia-frame-4', imagePath: '/ex10/story-4.png', text: 'Η φίλη λέει πως δεν της αρέσει η κασετίνα της Σοφίας.' },
  ],
  questions: [
    {
      id: 'who-upset-sofia',
      text: 'Ποιος είπε κάτι που μπορεί να στεναχώρησε τη Σοφία;',
      options: [
        { id: 'sofia', label: 'Α', detail: 'Η Σοφία', imagePath: '/ex10/answer-sofia.png' },
        { id: 'friend', label: 'Β', detail: 'Η φίλη της', imagePath: '/ex10/answer-friend.png' },
      ],
      correctOptionId: 'friend',
      correctFeedback: 'Μπράβο! Η φίλη είπε το σχόλιο για την κασετίνα.',
      incorrectFeedback: 'Καλή προσπάθεια! Σκέψου ποιος είπε τα λόγια για την κασετίνα.',
    },
  ],
}

export default littleSofia

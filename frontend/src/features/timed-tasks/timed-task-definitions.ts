import type { TimedTaskId } from '../../domain/timed-task'

export type TimedTaskDefinition = {
  id: TimedTaskId
  title: string
  category: string
  description: string
  icon: string
}

export const timedTaskDefinitions: TimedTaskDefinition[] = [
  { id: 'stroop', title: 'Stroop', category: 'Προσοχή', description: 'Πάτησε όταν το χρώμα της λέξης ταιριάζει με το νόημά της.', icon: '✎' },
  { id: 'go-no-go', title: 'Go / No-Go', category: 'Απόκριση', description: 'Πάτησε στο «Ξεκίνα», αγνόησε το «Στοπ».', icon: '◉' },
  { id: 'sart', title: 'SART', category: 'Προσοχή', description: 'Πάτησε σε κάθε εικόνα, εκτός αν είναι μήλο.', icon: '❍' },
  { id: 'corsi', title: 'Corsi', category: 'Μνήμη', description: 'Επανάλαβε τη σειρά πλακακιών που κλείδωσε το πιθηκάκι.', icon: '▦' },
  { id: 'digit-span', title: 'Digit Span', category: 'Μνήμη', description: 'Κράτησε στο μυαλό σου και επανάλαβε την ακολουθία ψηφίων.', icon: '№' },
]

import Phaser from 'phaser'
import { LionScaleScene } from './LionScaleScene'
import { KangarooScaleScene } from './KangarooScaleScene'
import { ObjectSpotlightScene } from './ObjectSpotlightScene'
import { HatCountScene } from './HatCountScene'
import { PaperMatchScene } from './PaperMatchScene'
import { PigeonCountScene } from './PigeonCountScene'

export const EXERCISE_SCENES: Record<string, typeof Phaser.Scene> = {
  'lion-scale': LionScaleScene,
  'kangaroo-scale': KangarooScaleScene,
  'object-spotlight': ObjectSpotlightScene,
  'hat-count': HatCountScene,
  'paper-match': PaperMatchScene,
  'pigeon-count': PigeonCountScene,
}

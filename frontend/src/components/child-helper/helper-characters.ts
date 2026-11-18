import type { ChildHelper as ChildHelperType } from '../../domain/preferences'

export const helperCharacters: Record<ChildHelperType, { name: string; icon: string; color: string; video: string }> = {
  robot: { name: 'Ρόμπι', icon: '🤖', color: 'robot', video: '/videos/robot.mp4' },
  fox: { name: 'Φοίβος', icon: '🦊', color: 'fox', video: '/videos/fox.mp4' },
  owl: { name: 'Ίρις', icon: '🦉', color: 'owl', video: '/videos/owl.mp4' },
  unicorn: { name: 'Νεφέλη', icon: '🦄', color: 'unicorn', video: '/videos/unicorn.mp4' },
}

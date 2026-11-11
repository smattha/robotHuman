export const palette = {
  nightTop: 0x1a1442,
  nightBottom: 0x2d2160,
  forestTop: 0x1f4d3a,
  forestBottom: 0x2f6b4f,
  workshopTop: 0x3a2a5a,
  workshopBottom: 0x5a3f7a,
  clearingTop: 0x24503f,
  clearingBottom: 0x3a7355,
  basketTop: 0x2a5040,
  basketBottom: 0x3f6b52,
  starGold: 0xffd76a,
  starGlow: 0xfff0b3,
  mushroomRed: 0xe0564a,
  mushroomCream: 0xfff0d6,
  mushroomGlow: 0xffb347,
  butterfly: 0xff8fcf,
  butterflyWing: 0xffc2e5,
  bee: 0xffc93c,
  beeStripe: 0x3a2a1a,
  cauldron: 0x4a4a6a,
  cauldronGlow: 0x9b6bff,
  basketWood: 0xb5824a,
  basketWeave: 0x8a5a2a,
  text: 0xffffff,
  textSoft: 0xd9d2ff,
  correct: 0x4dd4a0,
  wrong: 0xff8a7a,
  accent: 0xff8fcf,
} as const

export type CharacterKind = 'fox' | 'owl' | 'unicorn' | 'robot'

export const characterColors: Record<CharacterKind, { main: number; belly: number; accent: number; name: string }> = {
  fox: { main: 0xf08a3c, belly: 0xfff0d6, accent: 0xd96a1a, name: 'Φοίβος' },
  owl: { main: 0x8a6a4a, belly: 0xf0e0c0, accent: 0x5a4030, name: 'Ίρις' },
  unicorn: { main: 0xf0e0ff, belly: 0xffffff, accent: 0xb388ff, name: 'Νεφέλη' },
  robot: { main: 0x7a8aa0, belly: 0xd0d8e0, accent: 0x4a5a70, name: 'Ρόμπι' },
}

export type GameStore<T> = {
  props: T
  version: number
}

export function createGameStore<T>(props: T): GameStore<T> {
  return { props, version: 0 }
}

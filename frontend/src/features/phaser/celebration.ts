import Phaser from 'phaser'

const SPARK_TEXTURE = 'phaser-spark'

function ensureSparkTexture(scene: Phaser.Scene): void {
  if (scene.textures.exists(SPARK_TEXTURE)) return
  const g = scene.make.graphics({ x: 0, y: 0 }, false)
  g.fillStyle(0xffffff, 1)
  g.fillCircle(8, 8, 8)
  g.generateTexture(SPARK_TEXTURE, 16, 16)
  g.destroy()
}

export function celebrate(scene: Phaser.Scene, x: number, y: number): void {
  ensureSparkTexture(scene)
  const emitter = scene.add.particles(x, y, SPARK_TEXTURE, {
    speed: { min: 60, max: 170 },
    scale: { start: 1, end: 0 },
    lifespan: 650,
    quantity: 16,
    tint: [0xffd76a, 0xff9ec4, 0x8fd3ff, 0x9be7a0],
    blendMode: 'ADD',
  })
  scene.time.delayedCall(700, () => emitter.destroy())
}

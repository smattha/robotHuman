let audioContext: AudioContext | null = null

function getAudioContext(): AudioContext {
  if (!audioContext) audioContext = new AudioContext()
  if (audioContext.state === 'suspended') void audioContext.resume()
  return audioContext
}

function playTone(context: AudioContext, frequency: number, startTime: number, volume: number, duration: number): void {
  const oscillator = context.createOscillator()
  const gain = context.createGain()
  oscillator.type = 'sine'
  oscillator.frequency.value = frequency
  gain.gain.setValueAtTime(0.0001, startTime)
  gain.gain.exponentialRampToValueAtTime(volume, startTime + 0.02)
  gain.gain.exponentialRampToValueAtTime(0.0001, startTime + duration)
  oscillator.connect(gain)
  gain.connect(context.destination)
  oscillator.start(startTime)
  oscillator.stop(startTime + duration + 0.05)
}

export function playCorrectSound(): void {
  try {
    const context = getAudioContext()
    const now = context.currentTime
    playTone(context, 523.25, now, 0.18, 0.16)
    playTone(context, 659.25, now + 0.12, 0.18, 0.18)
    playTone(context, 783.99, now + 0.24, 0.2, 0.26)
  } catch {
    // Sound effects are optional; the visual feedback still guides the child.
  }
}

export function playIncorrectSound(): void {
  try {
    const context = getAudioContext()
    const now = context.currentTime
    playTone(context, 392.0, now, 0.14, 0.22)
    playTone(context, 329.63, now + 0.2, 0.12, 0.3)
  } catch {
    // Sound effects are optional; the visual feedback still guides the child.
  }
}
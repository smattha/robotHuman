import { beforeEach, describe, expect, it, vi } from 'vitest'
import { exercises } from '../content/exercises'

const { create } = vi.hoisted(() => ({ create: vi.fn() }))

vi.mock('@mintplex-labs/piper-tts-web', () => ({ TtsSession: { create }, WASM_BASE: 'https://example.invalid/piper' }))

describe('getGreekVoiceSession', () => {
  beforeEach(() => {
    create.mockReset()
    vi.resetModules()
    Object.defineProperty(navigator, 'storage', { configurable: true, value: undefined })
  })

  it('shares initialization between preloading and playback', async () => {
    const session = { predict: vi.fn() }
    create.mockResolvedValue(session)
    const { getGreekVoiceSession } = await import('./greek-voice')

    const first = getGreekVoiceSession()
    const second = getGreekVoiceSession()

    expect(first).toBe(second)
    expect(await first).toBe(session)
    expect(create).toHaveBeenCalledTimes(1)
    expect(create).toHaveBeenCalledWith(expect.objectContaining({ voiceId: 'el_GR-rapunzelina-low' }))
  })

  it('allows a retry after initialization fails', async () => {
    create.mockRejectedValueOnce(new Error('Unavailable')).mockResolvedValueOnce({ predict: vi.fn() })
    const { getGreekVoiceSession } = await import('./greek-voice')

    await expect(getGreekVoiceSession()).rejects.toThrow('Unavailable')
    await expect(getGreekVoiceSession()).resolves.toHaveProperty('predict')
    expect(create).toHaveBeenCalledTimes(2)
  })

  it('prepares the exact story frames and question audio used by the player', async () => {
    const predict = vi.fn(async (text: string) => new Blob([text], { type: 'audio/x-wav' }))
    create.mockResolvedValue({ predict })
    const { getExerciseSpeechTexts, getGreekVoiceAudio, prepareGreekVoiceAudio } = await import('./greek-voice')
    const exercise = exercises.find((item) => item.id === 'george-and-chocolate')
    if (!exercise) throw new Error('Story exercise missing')
    const texts = getExerciseSpeechTexts(exercise)

    await prepareGreekVoiceAudio([exercise])

    expect(texts).toHaveLength(3)
    expect(predict.mock.calls.map(([text]) => text)).toEqual(texts)
    await getGreekVoiceAudio(texts[0])
    expect(predict).toHaveBeenCalledTimes(3)
  })
})

import type { Exercise } from './exercise'

export const GREEK_VOICE_ID = 'el_GR-rapunzelina-low'
const MODEL_SIZE_BYTES = 63104526
const AUDIO_DIRECTORY = 'exercise-audio-v1'
type AudioJob = { text: string; resolve: (wav: Blob) => void; reject: (error: unknown) => void }
export type GreekVoicePreparationStatus = {
  completed: number
  total: number
  state: 'idle' | 'preparing' | 'complete' | 'error'
}
let sessionPromise: Promise<import('@mintplex-labs/piper-tts-web').TtsSession> | undefined
const audioPromises = new Map<string, Promise<Blob>>()
let preparationPromise: Promise<void> | undefined
const audioJobs: AudioJob[] = []
let processingJobs = false
let preparationStatus: GreekVoicePreparationStatus = { completed: 0, total: 0, state: 'idle' }
const preparationListeners = new Set<(status: GreekVoicePreparationStatus) => void>()

function updatePreparationStatus(status: GreekVoicePreparationStatus): void {
  preparationStatus = status
  preparationListeners.forEach((listener) => listener(status))
}

export function getGreekVoicePreparationStatus(): GreekVoicePreparationStatus {
  return preparationStatus
}

export function subscribeToGreekVoicePreparation(listener: (status: GreekVoicePreparationStatus) => void): () => void {
  preparationListeners.add(listener)
  listener(preparationStatus)
  return () => preparationListeners.delete(listener)
}

export function getExerciseSpokenText(exercise: Exercise): string {
  return `${exercise.instructions} ${exercise.question} ${exercise.options.map((option) => `${option.label}: ${option.detail}`).join('. ')}`
}

export function getExerciseSpeechTexts(exercise: Exercise): string[] {
  return [...new Set([...(exercise.storyFrames?.map((frame) => frame.text) ?? []), getExerciseSpokenText(exercise)])]
}

async function audioFile(text: string, create: boolean): Promise<FileSystemFileHandle> {
  const root = await navigator.storage.getDirectory()
  const directory = await root.getDirectoryHandle(AUDIO_DIRECTORY, { create })
  const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(`${GREEK_VOICE_ID}:${text}`))
  const name = `${Array.from(new Uint8Array(digest), (byte) => byte.toString(16).padStart(2, '0')).join('')}.wav`
  return directory.getFileHandle(name, { create })
}

export function getGreekVoiceAudio(text: string, prioritize = false): Promise<Blob> {
  const existing = audioPromises.get(text)
  if (existing) return existing

  const promise = (async () => {
    const storageAvailable = Boolean(navigator.storage && globalThis.crypto?.subtle)
    if (storageAvailable) {
      try {
        const cached = await (await audioFile(text, false)).getFile()
        if (cached.size > 0) return cached
      } catch {
        // Missing or unavailable cached audio can be generated normally.
      }
    }

    const wav = await new Promise<Blob>((resolve, reject) => {
      const job = { text, resolve, reject }
      if (prioritize) audioJobs.unshift(job)
      else audioJobs.push(job)
      void processAudioJobs()
    })
    if (storageAvailable) {
      try {
        const writable = await (await audioFile(text, true)).createWritable()
        await writable.write(wav)
        await writable.close()
      } catch {
        // Playback still works when the browser cannot persist generated audio.
      }
    }
    return wav
  })()

  audioPromises.set(text, promise)
  void promise.catch(() => audioPromises.delete(text))
  return promise
}

async function processAudioJobs(): Promise<void> {
  if (processingJobs) return
  processingJobs = true
  while (audioJobs.length > 0) {
    const job = audioJobs.shift()
    if (!job) continue
    try {
      job.resolve(await (await getGreekVoiceSession()).predict(job.text))
    } catch (error) {
      job.reject(error)
    }
  }
  processingJobs = false
}


export function prepareGreekVoiceAudio(exercises: Exercise[]): Promise<void> {
  if (!preparationPromise) {
    preparationPromise = prepareAllGreekVoiceAudio(exercises).catch((error: unknown) => {
      preparationPromise = undefined
      throw error
    })
  }
  return preparationPromise
}

async function prepareAllGreekVoiceAudio(exercises: Exercise[]): Promise<void> {
  const texts = [...new Set(exercises.flatMap(getExerciseSpeechTexts))]
  updatePreparationStatus({ completed: 0, total: texts.length, state: 'preparing' })
  try {
    await getGreekVoiceSession()
  } catch (error) {
    updatePreparationStatus({ completed: 0, total: texts.length, state: 'error' })
    throw error
  }
  let completed = 0
  for (const text of texts) {
    try {
      await getGreekVoiceAudio(text)
    } catch {
      // Continue preparing the remaining clips if one synthesis fails.
    }
    completed += 1
    updatePreparationStatus({ completed, total: texts.length, state: 'preparing' })
  }
  updatePreparationStatus({ completed, total: texts.length, state: 'complete' })
}

export function getGreekVoiceSession(): Promise<import('@mintplex-labs/piper-tts-web').TtsSession> {
  if (!sessionPromise) {
    sessionPromise = import('@mintplex-labs/piper-tts-web').then(({ TtsSession, WASM_BASE }) => TtsSession.create({
      voiceId: GREEK_VOICE_ID,
      wasmPaths: {
        onnxWasm: `${import.meta.env.BASE_URL}onnx-runtime/`,
        piperData: `${WASM_BASE}.data`,
        piperWasm: `${WASM_BASE}.wasm`,
      },
    })).catch((error: unknown) => {
      sessionPromise = undefined
      throw error
    })
  }
  return sessionPromise
}

export async function isGreekVoiceStored(): Promise<boolean> {
  if (!navigator.storage?.getDirectory) return false

  try {
    const root = await navigator.storage.getDirectory()
    const directory = await root.getDirectoryHandle('piper')
    const model = await (await directory.getFileHandle(`${GREEK_VOICE_ID}.onnx`)).getFile()
    const config = await (await directory.getFileHandle(`${GREEK_VOICE_ID}.onnx.json`)).getFile()
    return model.size === MODEL_SIZE_BYTES && config.size > 0
  } catch {
    return false
  }
}

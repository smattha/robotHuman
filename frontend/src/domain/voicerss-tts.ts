const VOICERSS_ENDPOINT = 'https://api.voicerss.org/'

export type VoiceRssResult =
  | { ok: true; audioDataUrl: string }
  | { ok: false; reason: 'missing-key' | 'request-failed' | 'api-error' }

function getApiKey(): string | undefined {
  return import.meta.env.VITE_VOICERSS_API_KEY
}

export function isVoiceRssConfigured(): boolean {
  return Boolean(getApiKey())
}

export async function fetchVoiceRssAudio(text: string): Promise<VoiceRssResult> {
  const apiKey = getApiKey()
  if (!apiKey) return { ok: false, reason: 'missing-key' }

  const params = new URLSearchParams({
    key: apiKey,
    hl: 'el-gr',
    src: text,
    c: 'MP3',
    f: '44khz_16bit_mono',
    b64: 'true',
  })

  try {
    const response = await fetch(`${VOICERSS_ENDPOINT}?${params.toString()}`)
    if (!response.ok) return { ok: false, reason: 'request-failed' }
    const body = await response.text()
    if (body.startsWith('ERROR')) return { ok: false, reason: 'api-error' }
    return { ok: true, audioDataUrl: body }
  } catch {
    return { ok: false, reason: 'request-failed' }
  }
}

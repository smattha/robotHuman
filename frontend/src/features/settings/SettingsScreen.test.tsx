import { render, screen, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { beforeEach, describe, expect, it, vi } from 'vitest'
import { DEFAULT_PREFERENCES } from '../../domain/preferences'
import { SettingsScreen } from './SettingsScreen'

const { download } = vi.hoisted(() => ({ download: vi.fn() }))

vi.mock('@mintplex-labs/piper-tts-web', () => ({ download }))

describe('SettingsScreen voice download', () => {
  const files = new Map<string, number>()

  beforeEach(() => {
    files.clear()
    download.mockReset()
    Object.defineProperty(navigator, 'storage', {
      configurable: true,
      value: {
        getDirectory: async () => ({
          getDirectoryHandle: async () => ({
            getFileHandle: async (name: string) => {
              if (!files.has(name)) throw new Error('Not downloaded')
              return { getFile: async () => ({ size: files.get(name) }) }
            },
          }),
        }),
      },
    })
  })

  function renderSettings() {
    return render(<SettingsScreen preferences={DEFAULT_PREFERENCES} onStorySpeedChange={vi.fn()} onChildHelperChange={vi.fn()} onAccessibilityChange={vi.fn()} onSpeechEnabledChange={vi.fn()} />)
  }

  it('downloads the Greek model on request and recognizes it on revisit', async () => {
    const user = userEvent.setup()
    download.mockImplementation(async (_voiceId: string, onProgress: (progress: { loaded: number; total: number }) => void) => {
      onProgress({ loaded: 63104526, total: 63104526 })
      files.set('el_GR-rapunzelina-low.onnx', 63104526)
      files.set('el_GR-rapunzelina-low.onnx.json', 4198)
    })

    const view = renderSettings()
    await user.click(await screen.findByRole('button', { name: 'Λήψη ελληνικής φωνής' }))

    expect(download).toHaveBeenCalledWith('el_GR-rapunzelina-low', expect.any(Function))
    expect(await screen.findByText('Η ελληνική φωνή είναι έτοιμη σε αυτόν τον browser.')).toBeInTheDocument()
    view.unmount()
    renderSettings()
    expect(await screen.findByText('Η ελληνική φωνή είναι έτοιμη σε αυτόν τον browser.')).toBeInTheDocument()
    expect(screen.queryByRole('button', { name: 'Λήψη ελληνικής φωνής' })).not.toBeInTheDocument()
  })

  it('allows retrying when the download fails', async () => {
    const user = userEvent.setup()
    download.mockRejectedValue(new Error('Network unavailable'))
    renderSettings()

    await user.click(await screen.findByRole('button', { name: 'Λήψη ελληνικής φωνής' }))

    await waitFor(() => expect(screen.getByText(/Η λήψη δεν ολοκληρώθηκε/)).toBeInTheDocument())
    expect(screen.getByRole('button', { name: 'Λήψη ελληνικής φωνής' })).toBeEnabled()
  })
})

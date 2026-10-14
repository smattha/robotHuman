import { useEffect, useRef, useState } from 'react'
import { exercises } from '../../content/exercises'
import { GREEK_VOICE_ID, getGreekVoicePreparationStatus, isGreekVoiceStored, prepareGreekVoiceAudio, subscribeToGreekVoicePreparation } from '../../domain/greek-voice'
import type { GreekVoicePreparationStatus } from '../../domain/greek-voice'
import type { ChildHelper, Preferences, StorySpeed } from '../../domain/preferences'

type SettingsScreenProps = {
  preferences: Preferences
  onStorySpeedChange: (storySpeed: StorySpeed) => void
  onChildHelperChange: (childHelper: ChildHelper) => void
  onAccessibilityChange: (setting: 'largeButtons' | 'reducedMotion' | 'highContrast', enabled: boolean) => void
  onSpeechEnabledChange: (enabled: boolean) => void
}

const speedOptions: { value: StorySpeed; title: string; description: string }[] = [
  { value: 'slow', title: 'Αργά', description: '6 δευτερόλεπτα για κάθε εικόνα' },
  { value: 'normal', title: 'Κανονικά', description: '4 δευτερόλεπτα για κάθε εικόνα' },
  { value: 'fast', title: 'Γρήγορα', description: '2,5 δευτερόλεπτα για κάθε εικόνα' },
]

const helperOptions: { value: ChildHelper; icon: string; title: string; description: string }[] = [
  { value: 'robot', icon: '🤖', title: 'Ρόμπι το ρομπότ', description: 'Ήρεμος και έξυπνος βοηθός' },
  { value: 'fox', icon: '🦊', title: 'Φοίβος η αλεπού', description: 'Περίεργος και χαμογελαστός βοηθός' },
  { value: 'owl', icon: '🦉', title: 'Ίρις η κουκουβάγια', description: 'Παρατηρητική και ήρεμη βοηθός' },
  { value: 'unicorn', icon: '🦄', title: 'Νεφέλη ο μονόκερος', description: 'Φωτεινή και παιχνιδιάρικη βοηθός' },
]

export function SettingsScreen({ preferences, onStorySpeedChange, onChildHelperChange, onAccessibilityChange, onSpeechEnabledChange }: SettingsScreenProps) {
  const [voiceStatus, setVoiceStatus] = useState<'checking' | 'available' | 'missing' | 'downloading' | 'error'>('checking')
  const [downloadPercent, setDownloadPercent] = useState<number | null>(null)
  const [preparationStatus, setPreparationStatus] = useState<GreekVoicePreparationStatus>(getGreekVoicePreparationStatus)
  const activeRef = useRef(true)

  useEffect(() => {
    activeRef.current = true
    isGreekVoiceStored().then((available) => {
      if (activeRef.current) setVoiceStatus(available ? 'available' : 'missing')
    })
    return () => { activeRef.current = false }
  }, [])

  useEffect(() => subscribeToGreekVoicePreparation(setPreparationStatus), [])

  async function downloadGreekVoice() {
    if (voiceStatus === 'downloading') return
    setVoiceStatus('downloading')
    setDownloadPercent(null)
    try {
      if (!navigator.storage?.getDirectory) throw new Error('Browser storage unavailable')
      const { download } = await import('@mintplex-labs/piper-tts-web')
      await download(GREEK_VOICE_ID, ({ loaded, total }) => {
        if (activeRef.current && total > 0) setDownloadPercent(Math.min(100, Math.round(loaded * 100 / total)))
      })
      // The library resolves before its asynchronous browser-storage writes finish.
      for (let attempt = 0; attempt < 60; attempt += 1) {
        if (await isGreekVoiceStored()) {
          if (activeRef.current) setVoiceStatus('available')
          void prepareGreekVoiceAudio(exercises).catch(() => {})
          return
        }
        await new Promise((resolve) => setTimeout(resolve, 500))
      }
      throw new Error('Voice model was not stored')
    } catch {
      if (activeRef.current) setVoiceStatus('error')
    }
  }

  return (
    <section className="page-section settings-page" aria-labelledby="settings-title">
      <p className="eyebrow">Ρύθμισε την εμπειρία</p>
      <h1 id="settings-title">Ρυθμίσεις</h1>
      <p className="lead">Διάλεξε πόσο γρήγορα θα αλλάζουν οι εικόνες στις ιστορίες.</p>
      <div className="settings-card">
        <h2>Ελληνική φωνή</h2>
        <label className="accessibility-option">
          <span><strong>Εκφώνηση οδηγιών</strong><small>Ενεργοποιεί ή απενεργοποιεί την εκφώνηση των ασκήσεων.</small></span>
          <input type="checkbox" checked={preferences.speechEnabled} onChange={(event) => onSpeechEnabledChange(event.target.checked)} />
        </label>
        <p>Αν θέλεις να ακούς τις αποστολές, κατέβασε τη φωνή μία φορά σε αυτόν τον browser (περίπου 63 MB). Η λήψη χρειάζεται σύνδεση στο διαδίκτυο.</p>
        {voiceStatus === 'missing' || voiceStatus === 'error' ? (
          <button className="secondary-button" type="button" onClick={downloadGreekVoice}>Λήψη ελληνικής φωνής</button>
        ) : null}
        <p role="status" aria-live="polite">
          {voiceStatus === 'checking' && 'Έλεγχος αποθηκευμένης φωνής...'}
          {voiceStatus === 'available' && 'Η ελληνική φωνή είναι έτοιμη σε αυτόν τον browser.'}
          {voiceStatus === 'missing' && 'Η φωνή δεν έχει ληφθεί ακόμη.'}
          {voiceStatus === 'downloading' && (downloadPercent === null ? 'Προετοιμασία λήψης...' : downloadPercent === 100 ? 'Αποθήκευση φωνής στον browser...' : `Λήψη φωνής: ${downloadPercent}%`)}
          {voiceStatus === 'error' && 'Η λήψη δεν ολοκληρώθηκε. Έλεγξε τη σύνδεση και τον διαθέσιμο χώρο και δοκίμασε ξανά.'}
        </p>
        {voiceStatus === 'downloading' && downloadPercent !== null && <progress value={downloadPercent} max={100} aria-label="Πρόοδος λήψης ελληνικής φωνής" style={{ width: '100%' }} />}
        {preparationStatus.total > 0 && <p role="status" aria-live="polite">
          {preparationStatus.state === 'preparing' && `Δημιουργία προτάσεων: ${preparationStatus.completed} από ${preparationStatus.total}`}
          {preparationStatus.state === 'complete' && `Η δημιουργία ολοκληρώθηκε: ${preparationStatus.completed} από ${preparationStatus.total} προτάσεις.`}
          {preparationStatus.state === 'error' && 'Η δημιουργία των προτάσεων σταμάτησε. Θα γίνει νέα προσπάθεια όταν ζητηθεί ήχος.'}
        </p>}
        {preparationStatus.state === 'preparing' && <progress value={preparationStatus.completed} max={preparationStatus.total} aria-label="Πρόοδος δημιουργίας προτάσεων" style={{ width: '100%' }} />}
      </div>
      <div className="settings-card">
        <h2>Ταχύτητα ιστοριών</h2>
        <p>Η επιλογή αυτή δεν επηρεάζει τις Προκλήσεις Μνήμης και Προσοχής.</p>
        <div className="speed-options" role="radiogroup" aria-label="Ταχύτητα ιστοριών">
          {speedOptions.map((option) => {
            const selected = preferences.storySpeed === option.value
            return (
              <button
                className={`speed-option${selected ? ' selected' : ''}`}
                type="button"
                role="radio"
                aria-checked={selected}
                key={option.value}
                onClick={() => onStorySpeedChange(option.value)}
              >
                <span className="speed-option-icon" aria-hidden="true">{option.value === 'slow' ? '🐢' : option.value === 'normal' ? '🚶' : '🚀'}</span>
                <span><strong>{option.title}</strong><small>{option.description}</small></span>
              </button>
            )
          })}
        </div>
      </div>
      <div className="settings-card">
        <h2>Ο βοηθός σου</h2>
        <p>Διάλεξε ποιος φίλος θα είναι δίπλα σου στις αποστολές και θα σε ενθαρρύνει.</p>
        <div className="helper-options" role="radiogroup" aria-label="Επιλογή βοηθού">
          {helperOptions.map((option) => {
            const selected = preferences.childHelper === option.value
            return (
              <button
                className={`helper-option${selected ? ' selected' : ''}`}
                type="button"
                role="radio"
                aria-checked={selected}
                key={option.value}
                onClick={() => onChildHelperChange(option.value)}
              >
                <span className="helper-option-icon" aria-hidden="true">{option.icon}</span>
                <span><strong>{option.title}</strong><small>{option.description}</small></span>
              </button>
            )
          })}
        </div>
      </div>
      <div className="settings-card">
        <h2>Ευκολότερη προβολή</h2>
        <p>Ρύθμισε την εμφάνιση ώστε να είναι πιο άνετη για εσένα.</p>
        <div className="accessibility-options">
          <label className="accessibility-option">
            <span><strong>Μεγαλύτερα κουμπιά</strong><small>Κάνει τα κουμπιά πιο εύκολα στο πάτημα.</small></span>
            <input type="checkbox" checked={preferences.largeButtons} onChange={(event) => onAccessibilityChange('largeButtons', event.target.checked)} />
          </label>
          <label className="accessibility-option">
            <span><strong>Λιγότερη κίνηση</strong><small>Σταματά τις μικρές κινήσεις και τα animations.</small></span>
            <input type="checkbox" checked={preferences.reducedMotion} onChange={(event) => onAccessibilityChange('reducedMotion', event.target.checked)} />
          </label>
          <label className="accessibility-option">
            <span><strong>Υψηλή αντίθεση</strong><small>Κάνει τα χρώματα και το κείμενο πιο έντονα.</small></span>
            <input type="checkbox" checked={preferences.highContrast} onChange={(event) => onAccessibilityChange('highContrast', event.target.checked)} />
          </label>
        </div>
      </div>
    </section>
  )
}

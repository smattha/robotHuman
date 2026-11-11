import { useEffect, useState } from 'react'
import type { Exercise } from '../../domain/exercise'

type AppShellProps = {
  children: React.ReactNode
  exercises: Exercise[]
  onHome: () => void
  onLibrary: () => void
  onSelectExercise: (index: number) => void
  onTestAll: () => void
  onPartB: () => void
  onStatistics: () => void
  onSettings: () => void
  onRequireUser: () => boolean
  onSwitchUser: () => void
  activityActive: boolean
  showBottomNav: boolean
}

export function AppShell({ children, exercises, onHome, onLibrary, onSelectExercise, onTestAll, onPartB, onStatistics, onSettings, onRequireUser, onSwitchUser, activityActive, showBottomNav }: AppShellProps) {
  const [sidebarOpen, setSidebarOpen] = useState(false)
  const [exerciseListOpen, setExerciseListOpen] = useState(false)

  useEffect(() => {
    if (!sidebarOpen && !exerciseListOpen) return
    function closeOnEscape(event: KeyboardEvent) {
      if (event.key === 'Escape') {
        setSidebarOpen(false)
        setExerciseListOpen(false)
      }
    }
    window.addEventListener('keydown', closeOnEscape)
    return () => window.removeEventListener('keydown', closeOnEscape)
  }, [exerciseListOpen, sidebarOpen])

  function closeSidebar() {
    setSidebarOpen(false)
  }

  return (
    <div className="app-shell">
      {sidebarOpen && <div className="sidebar-backdrop" onClick={closeSidebar} />}
      <aside className={`sidebar${sidebarOpen ? ' open' : ''}`}>
        <div className="sidebar-brand-row">
          <button className="brand" type="button" onClick={() => { onHome(); setExerciseListOpen(false); closeSidebar() }} aria-label="Επιστροφή στην αρχική">
            <span className="brand-mark" aria-hidden="true">✦</span>
            <span>Μικρές Αποστολές</span>
          </button>
          <button className="close-button sidebar-close" type="button" aria-label="Κλείσιμο μενού" onClick={closeSidebar}>×</button>
        </div>
        <nav className="sidebar-nav" aria-label="Κύριο μενού">
          <button className="sidebar-link test" type="button" onClick={() => { if (!onRequireUser()) return; onTestAll(); setExerciseListOpen(false); closeSidebar() }}>🌈 Μεγάλη περιπέτεια</button>
          <button className="sidebar-link" type="button" onClick={() => { onLibrary(); setExerciseListOpen(false); closeSidebar() }}>🗺️ Όλες οι αποστολές</button>
          <button
            className="sidebar-link exercise-menu-toggle"
            type="button"
            aria-expanded={exerciseListOpen}
            aria-controls="exercise-menu-list"
            onClick={() => {
              setExerciseListOpen((open) => !open)
            }}
          >
            🗺️ Μικρές αποστολές <span aria-hidden="true">{exerciseListOpen ? '−' : '+'}</span>
          </button>
          {exerciseListOpen && (
            <div className="exercise-dropdown" id="exercise-menu-list">
              <nav aria-label="Διαθέσιμες μικρές αποστολές">
                {exercises.map((exercise, index) => (
                  <button
                    type="button"
                    key={exercise.id}
                    onClick={() => {
                      onSelectExercise(index)
                      setExerciseListOpen(false)
                      closeSidebar()
                    }}
                  >
                    <span>{String(index + 1).padStart(2, '0')}</span>{exercise.title}
                  </button>
                ))}
              </nav>
            </div>
          )}
          <button className="sidebar-link" type="button" onClick={() => { onPartB(); setExerciseListOpen(false); closeSidebar() }}>🧠 Παιχνίδια σκέψης</button>
          <button className="sidebar-link" type="button" onClick={() => { onStatistics(); setExerciseListOpen(false); closeSidebar() }}>⭐ Τα κατορθώματά μου</button>
          <button className="sidebar-link" type="button" onClick={() => { onSettings(); setExerciseListOpen(false); closeSidebar() }}>⚙️ Ρυθμίσεις</button>
          <button className="sidebar-link" type="button" onClick={() => { onSwitchUser(); setExerciseListOpen(false); closeSidebar() }}>🔁 Αλλαγή χρήστη</button>
        </nav>
        <footer className="footer">Κάθε προσπάθεια είναι ένα κατόρθωμα!</footer>
      </aside>
      <div className="main-area">
        <div className="mobile-topbar">
          <span className="mobile-topbar-mark" aria-hidden="true">✦</span>
          <span className="mobile-topbar-title">Μικρές Αποστολές</span>
          {activityActive && <button className="mobile-home-button" type="button" aria-label="Πίσω στις αποστολές" onClick={onHome}>Πίσω</button>}
        </div>
        <main>{children}</main>
        {showBottomNav && !activityActive && <nav className="bottom-nav" aria-label="Γρήγορη πλοήγηση">
          <button type="button" onClick={() => { onLibrary(); closeSidebar() }}><span aria-hidden="true">⌂</span>Αποστολές</button>
          <button type="button" onClick={() => { onPartB(); closeSidebar() }}><span aria-hidden="true">✧</span>Παιχνίδια</button>
          <button type="button" onClick={() => { onStatistics(); closeSidebar() }}><span aria-hidden="true">★</span>Πρόοδος</button>
          <button type="button" aria-label="Άνοιγμα μενού" aria-expanded={sidebarOpen} onClick={() => setSidebarOpen(true)}><span aria-hidden="true">☰</span>Μενού</button>
        </nav>}
      </div>
    </div>
  )
}

import { useEffect, useState } from 'react'
import type { Exercise } from '../../domain/exercise'

type AppShellProps = {
  children: React.ReactNode
  exercises: Exercise[]
  onHome: () => void
  onSelectExercise: (index: number) => void
  onTestAll: () => void
  onStatistics: () => void
}

export function AppShell({ children, exercises, onHome, onSelectExercise, onTestAll, onStatistics }: AppShellProps) {
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
          <button
            className="sidebar-link exercise-menu-toggle"
            type="button"
            aria-expanded={exerciseListOpen}
            aria-controls="exercise-menu-list"
            onClick={() => setExerciseListOpen((open) => !open)}
          >
            Ασκήσεις <span aria-hidden="true">{exerciseListOpen ? '−' : '+'}</span>
          </button>
          {exerciseListOpen && (
            <div className="exercise-dropdown" id="exercise-menu-list">
              <nav aria-label="Διαθέσιμες ασκήσεις">
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
          <button className="sidebar-link test" type="button" onClick={() => { onTestAll(); setExerciseListOpen(false); closeSidebar() }}>Test all</button>
          <button className="sidebar-link" type="button" onClick={() => { onStatistics(); setExerciseListOpen(false); closeSidebar() }}>Στατιστικά</button>
        </nav>
        <footer className="footer">Ένα βήμα τη φορά. Μπορείς!</footer>
      </aside>
      <div className="main-area">
        <div className="mobile-topbar">
          <button className="mobile-menu-button" type="button" aria-label="Μενού" aria-expanded={sidebarOpen} onClick={() => setSidebarOpen(true)}>☰</button>
          <span className="mobile-topbar-title">Μικρές Αποστολές</span>
        </div>
        <main>{children}</main>
      </div>
    </div>
  )
}

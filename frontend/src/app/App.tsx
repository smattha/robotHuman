import { useEffect, useReducer, useState } from 'react'
import { exercises } from '../content/exercises'
import { evaluateAnswer } from '../domain/exercise'
import { isGreekVoiceStored, prepareGreekVoiceAudio } from '../domain/greek-voice'
import { clearResults, deleteResult, loadResults, saveResult } from '../domain/results'
import type { TestResult } from '../domain/results'
import { initialSessionState, sessionReducer } from '../state/exercise-session-reducer'
import { AppShell } from '../components/app-shell/AppShell'
import { CompletionScreen } from '../features/completion/CompletionScreen'
import { ExerciseLibrary } from '../features/exercise-library/ExerciseLibrary'
import { ExercisePlayer } from '../features/exercise-player/ExercisePlayer'
import { StartTestDialog } from '../features/test-all/StartTestDialog'
import { BreakScreen } from '../features/test-all/BreakScreen'
import { WelcomeScreen } from '../features/welcome/WelcomeScreen'
import type { TimedTaskId, TaskSummary, Trial, TimedTaskResult } from '../domain/timed-task'
import { clearTimedTaskResults, deleteTimedTaskResult, loadTimedTaskResults, saveTimedTaskResult } from '../domain/timed-task-results'
import { timedTaskDefinitions } from '../features/timed-tasks/timed-task-definitions'
import { TaskNameDialog } from '../features/timed-tasks/TaskNameDialog'
import { StroopTask } from '../features/timed-tasks/StroopTask'
import { GoNoGoTask } from '../features/timed-tasks/GoNoGoTask'
import { CorsiTask } from '../features/timed-tasks/CorsiTask'
import { DigitSpanTask } from '../features/timed-tasks/DigitSpanTask'
import { SartTask } from '../features/timed-tasks/SartTask'
import { TaskPreparationScreen } from '../features/timed-tasks/TaskPreparationScreen'
import { TaskCompletionScreen } from '../features/timed-tasks/TaskCompletionScreen'
import { TaskPracticeScreen } from '../features/timed-tasks/TaskPracticeScreen'
import { StatisticsScreen } from '../features/statistics/StatisticsScreen'
import { getStoryFrameDuration, loadPreferences, savePreferences } from '../domain/preferences'
import type { ChildHelper, StorySpeed } from '../domain/preferences'
import { SettingsScreen } from '../features/settings/SettingsScreen'
import { loadUserNames, saveUserName } from '../domain/users'
import { NewUserDialog } from '../features/welcome/NewUserDialog'

export function App() {
  const [state, dispatch] = useReducer(sessionReducer, initialSessionState)
  const [dialogOpen, setDialogOpen] = useState(false)
  const [activeResult, setActiveResult] = useState<TestResult | null>(null)
  const [savedResults, setSavedResults] = useState(loadResults)
  const [storageError, setStorageError] = useState(false)
  const [timedTaskResults, setTimedTaskResults] = useState(loadTimedTaskResults)
  const [selectedTimedTask, setSelectedTimedTask] = useState<TimedTaskId | null>(null)
  const [activeTimedTask, setActiveTimedTask] = useState<{ id: TimedTaskId; userName: string } | null>(null)
  const [preparedTimedTask, setPreparedTimedTask] = useState<{ id: TimedTaskId; userName: string } | null>(null)
  const [practicingTimedTask, setPracticingTimedTask] = useState<{ id: TimedTaskId; userName: string } | null>(null)
  const [completedTimedTask, setCompletedTimedTask] = useState<{ result: TimedTaskResult; saved: boolean } | null>(null)
  const [showStatistics, setShowStatistics] = useState(false)
  const [showSettings, setShowSettings] = useState(false)
  const [preferences, setPreferences] = useState(loadPreferences)
  const [userName, setUserName] = useState<string | null>(null)
  const [userNames, setUserNames] = useState(loadUserNames)
  const [newUserDialogOpen, setNewUserDialogOpen] = useState(false)
  const exercise = exercises[state.exerciseIndex]

  useEffect(() => {
    let active = true
    void isGreekVoiceStored().then((stored) => {
      if (active && stored && preferences.speechEnabled) void prepareGreekVoiceAudio(exercises).catch(() => {})
    }).catch(() => {})
    return () => { active = false }
  }, [preferences.speechEnabled])

  useEffect(() => {
    if (!dialogOpen) return
    function closeOnEscape(event: KeyboardEvent) {
      if (event.key === 'Escape') setDialogOpen(false)
    }
    window.addEventListener('keydown', closeOnEscape)
    return () => window.removeEventListener('keydown', closeOnEscape)
  }, [dialogOpen])

  function goHome() {
    if (activeResult && !activeResult.completedAt) {
      const interrupted = { ...activeResult, completedAt: new Date().toISOString() }
      setStorageError(!saveResult(interrupted))
      setSavedResults(loadResults())
    }
    dispatch({ type: 'GO_TO_WELCOME' })
    setActiveResult(null)
    setDialogOpen(false)
    setSelectedTimedTask(null)
    setPreparedTimedTask(null)
    setPracticingTimedTask(null)
    setActiveTimedTask(null)
    setCompletedTimedTask(null)
    setShowStatistics(false)
    setShowSettings(false)
  }

  function leaveTimedTask() {
    setActiveTimedTask(null)
    setPreparedTimedTask(null)
    setPracticingTimedTask(null)
    setCompletedTimedTask(null)
    setSelectedTimedTask(null)
    dispatch({ type: 'BACK_TO_LIBRARY' })
  }

  function openStatistics() {
    if (activeTimedTask || preparedTimedTask || practicingTimedTask || completedTimedTask) leaveTimedTask()
    else goHome()
    setDialogOpen(false)
    setSelectedTimedTask(null)
    setSavedResults(loadResults())
    setTimedTaskResults(loadTimedTaskResults())
    setShowStatistics(true)
  }

  function openSettings() {
    if (activeTimedTask || preparedTimedTask || practicingTimedTask || completedTimedTask) leaveTimedTask()
    else goHome()
    setDialogOpen(false)
    setSelectedTimedTask(null)
    setShowSettings(true)
  }

  function changeStorySpeed(storySpeed: StorySpeed) {
    const updated = { ...preferences, storySpeed }
    setPreferences(updated)
    setStorageError(!savePreferences(updated))
  }

  function changeChildHelper(childHelper: ChildHelper) {
    const updated = { ...preferences, childHelper }
    setPreferences(updated)
    setStorageError(!savePreferences(updated))
  }

  function changeAccessibility(setting: 'largeButtons' | 'reducedMotion' | 'highContrast', enabled: boolean) {
    const updated = { ...preferences, [setting]: enabled }
    setPreferences(updated)
    setStorageError(!savePreferences(updated))
  }

  function changeSpeechEnabled(speechEnabled: boolean) {
    const updated = { ...preferences, speechEnabled }
    setPreferences(updated)
    setStorageError(!savePreferences(updated))
    if (speechEnabled) void isGreekVoiceStored().then((stored) => {
      if (stored) void prepareGreekVoiceAudio(exercises).catch(() => {})
    }).catch(() => {})
  }

  function openExercise(index: number) {
    if (activeResult && !activeResult.completedAt) {
      const interrupted = { ...activeResult, completedAt: new Date().toISOString() }
      setStorageError(!saveResult(interrupted))
      setSavedResults(loadResults())
    }
    setActiveResult(null)
    setSelectedTimedTask(null)
    setPreparedTimedTask(null)
    setPracticingTimedTask(null)
    setActiveTimedTask(null)
    setCompletedTimedTask(null)
    setShowStatistics(false)
    setShowSettings(false)
    dispatch({ type: 'OPEN_EXERCISE', index })
  }

  function selectTimedTask(id: TimedTaskId) {
    setActiveResult(null)
    setStorageError(false)
    setSelectedTimedTask(id)
  }

  function startExerciseLibrary() {
    setActiveResult(null)
    setStorageError(false)
    dispatch({ type: 'START' })
  }

  function startAll() {
    if (!userName) return
    const result: TestResult = {
      id: crypto.randomUUID(), userName, startedAt: new Date().toISOString(), completedAt: null, answers: [],
    }
    setActiveResult(result)
    setStorageError(!saveResult(result))
    setSavedResults(loadResults())
    setDialogOpen(false)
    dispatch({ type: 'START_ALL', userName })
  }

  function resumeAll() {
    const resumableResult = getResumableResult()
    if (!resumableResult) return
    setActiveResult(resumableResult)
    setDialogOpen(false)
    dispatch({ type: 'RESUME_ALL', userName: resumableResult.userName, exerciseIndex: resumableResult.answers.length })
  }

  function getResumableResult(): TestResult | null {
    return savedResults.find((result) => result.completedAt === null && result.answers.length < exercises.length) ?? null
  }

  function submitAnswer() {
    if (!state.selectedOptionId || state.evaluation) return
    const evaluation = evaluateAnswer(exercise, state.selectedOptionId)
    dispatch({ type: 'SUBMIT_ANSWER', evaluation })
    const answer = {
      exerciseId: exercise.id, optionId: state.selectedOptionId,
      isCorrect: evaluation.isCorrect, answeredAt: new Date().toISOString(),
    }
    if (activeResult) {
      const updated = { ...activeResult, answers: [...activeResult.answers, answer] }
      setActiveResult(updated)
      setStorageError(!saveResult(updated))
      setSavedResults(loadResults())
    } else if (userName) {
      const result: TestResult = {
        id: crypto.randomUUID(), userName, startedAt: answer.answeredAt, completedAt: answer.answeredAt, answers: [answer], kind: 'single',
      }
      setStorageError(!saveResult(result))
      setSavedResults(loadResults())
    }
  }

  function continueTest() {
    if (state.mode === 'all' && state.exerciseIndex < exercises.length - 1) {
      if (shouldShowBreak()) dispatch({ type: 'TAKE_BREAK' })
      else dispatch({ type: 'NEXT_EXERCISE' })
      return
    }
    if (activeResult) {
      const completed = { ...activeResult, completedAt: new Date().toISOString() }
      setActiveResult(completed)
      setStorageError(!saveResult(completed))
      setSavedResults(loadResults())
    }
    dispatch({ type: 'COMPLETE' })
  }

  function shouldShowBreak(): boolean {
    const completedCount = state.exerciseIndex + 1
    return completedCount % 3 === 0
  }

  function finishTestLater() {
    if (activeResult) {
      setStorageError(!saveResult(activeResult))
      setSavedResults(loadResults())
    }
    setActiveResult(null)
    dispatch({ type: 'BACK_TO_LIBRARY' })
  }

  function openTestDialog() {
    if (activeTimedTask || preparedTimedTask || practicingTimedTask || completedTimedTask) leaveTimedTask()
    else goHome()
    setSelectedTimedTask(null)
    setDialogOpen(true)
  }

  function openPartB() {
    if (activeTimedTask || preparedTimedTask || practicingTimedTask || completedTimedTask) leaveTimedTask()
    else goHome()
    setSelectedTimedTask(null)
    setDialogOpen(false)
    dispatch({ type: 'BACK_TO_LIBRARY' })
    setTimeout(() => document.getElementById('timed-tasks')?.scrollIntoView({ behavior: 'smooth' }), 50)
  }

  function finishTimedTask(taskId: TimedTaskId, userName: string, trials: Trial[], summary: TaskSummary) {
    const result: TimedTaskResult = {
      id: crypto.randomUUID(), taskId, userName,
      startedAt: new Date().toISOString(),
      completedAt: new Date().toISOString(), trials, summary,
    }
    const saved = saveTimedTaskResult(result)
    if (saved) setTimedTaskResults(loadTimedTaskResults())
    setActiveTimedTask(null)
    setCompletedTimedTask({ result, saved })
  }

  function startTimedTask() {
    if (!selectedTimedTask || !userName) return
    setPreparedTimedTask({ id: selectedTimedTask, userName })
    setSelectedTimedTask(null)
  }

  function saveNewUser(userName: string) {
    setStorageError(!saveUserName(userName))
    setUserName(userName)
    setUserNames(loadUserNames())
    setNewUserDialogOpen(false)
  }

  function requireUser(): boolean {
    if (userName) return true
    setNewUserDialogOpen(true)
    return false
  }

  function removeResult(type: 'exercise' | 'timed', id: string): boolean {
    const deleted = type === 'exercise' ? deleteResult(id) : deleteTimedTaskResult(id)
    if (deleted) {
      setSavedResults(loadResults())
      setTimedTaskResults(loadTimedTaskResults())
    }
    return deleted
  }

  function removeAllResults(): boolean {
    const exerciseDeleted = clearResults()
    const timedDeleted = clearTimedTaskResults()
    setSavedResults(loadResults())
    setTimedTaskResults(loadTimedTaskResults())
    return exerciseDeleted && timedDeleted
  }

  return (
    <div className={`${preferences.largeButtons ? 'large-buttons' : ''}${preferences.reducedMotion ? ' reduced-motion' : ''}${preferences.highContrast ? ' high-contrast' : ''}`}>
      <AppShell exercises={exercises} onHome={goHome} onSelectExercise={openExercise} onTestAll={openTestDialog} onPartB={openPartB} onStatistics={openStatistics} onSettings={openSettings} onRequireUser={requireUser}>
      {showStatistics && <StatisticsScreen results={savedResults} timedResults={timedTaskResults} onDelete={removeResult} onDeleteAll={removeAllResults} />}
      {showSettings && <SettingsScreen preferences={preferences} onStorySpeedChange={changeStorySpeed} onChildHelperChange={changeChildHelper} onAccessibilityChange={changeAccessibility} onSpeechEnabledChange={changeSpeechEnabled} />}
      {!showStatistics && !showSettings && !activeTimedTask && !preparedTimedTask && !practicingTimedTask && !completedTimedTask && state.screen === 'welcome' && <WelcomeScreen onStart={startExerciseLibrary} onNewUser={() => setNewUserDialogOpen(true)} userName={userName} />}
      {!showStatistics && !showSettings && !activeTimedTask && !preparedTimedTask && !practicingTimedTask && !completedTimedTask && state.screen === 'library' && (
        <>
          <ExerciseLibrary
            exercises={exercises}
            exerciseResults={savedResults}
            timedTaskDefinitions={timedTaskDefinitions}
            timedTaskResults={timedTaskResults}
            onSelect={(selected) => openExercise(exercises.indexOf(selected))}
          />
          <section id="timed-tasks" className="page-section timed-task-library" aria-labelledby="timed-tasks-title">
            <div className="section-heading"><div><p className="eyebrow">Δραστηριότητες μνήμης και προσοχής</p><h2 id="timed-tasks-title">Προκλήσεις Μνήμης και Προσοχής</h2></div></div>
            <div className="timed-task-grid">
              {timedTaskDefinitions.map((task) => (
                <article className="timed-task-card" key={task.id}>
                  <div className="exercise-icon" aria-hidden="true">{task.icon}</div>
                  <p className="card-category">{task.category}</p>
                  <h3>{task.title}</h3>
                  <p>{task.description}</p>
                  <button className="secondary-button" type="button" onClick={() => selectTimedTask(task.id)}>Ξεκίνα δοκιμασία <span aria-hidden="true">↗</span></button>
                </article>
              ))}
            </div>
          </section>
        </>
      )}
      {!showStatistics && !showSettings && !activeTimedTask && !preparedTimedTask && !practicingTimedTask && !completedTimedTask && state.screen === 'exercise' && (
        <ExercisePlayer
          key={`${state.mode}-${state.exerciseIndex}`}
          exercise={exercise}
          progress={state.mode === 'all' ? { current: state.exerciseIndex + 1, total: exercises.length } : null}
          selectedOptionId={state.selectedOptionId}
          isSubmitted={state.evaluation !== null}
          feedback={state.evaluation?.feedback ?? null}
          isCorrect={state.evaluation?.isCorrect ?? null}
          onSelect={(optionId) => dispatch({ type: 'SELECT_OPTION', optionId })}
          onSubmit={submitAnswer}
          onComplete={continueTest}
          storyFrameDurationMs={getStoryFrameDuration(preferences.storySpeed)}
          speechEnabled={preferences.speechEnabled}
        />
      )}
      {!showStatistics && !showSettings && !activeTimedTask && !preparedTimedTask && !practicingTimedTask && !completedTimedTask && state.screen === 'break' && (
        <BreakScreen
          completedCount={state.exerciseIndex + 1}
          totalCount={exercises.length}
          onContinue={() => dispatch({ type: 'CONTINUE_AFTER_BREAK' })}
          onFinish={finishTestLater}
          helper={preferences.childHelper}
        />
      )}
      {!showStatistics && !showSettings && !activeTimedTask && !preparedTimedTask && !practicingTimedTask && !completedTimedTask && state.screen === 'completed' && (
        <CompletionScreen
          isCorrect={state.evaluation?.isCorrect ?? false}
          result={activeResult}
          isSingle={state.mode === 'single'}
          helper={preferences.childHelper}
          onRestart={() => state.mode === 'all' ? setDialogOpen(true) : dispatch({ type: 'RESTART' })}
          onHome={goHome}
        />
      )}
      {preparedTimedTask && <TaskPreparationScreen
        task={timedTaskDefinitions.find((task) => task.id === preparedTimedTask.id)!}
        userName={preparedTimedTask.userName}
        onContinue={() => { setPracticingTimedTask(preparedTimedTask); setPreparedTimedTask(null) }}
        onBack={leaveTimedTask}
        helper={preferences.childHelper}
      />}
      {practicingTimedTask && <TaskPracticeScreen
        task={timedTaskDefinitions.find((task) => task.id === practicingTimedTask.id)!}
        onStart={() => { setActiveTimedTask(practicingTimedTask); setPracticingTimedTask(null) }}
        onBack={leaveTimedTask}
        helper={preferences.childHelper}
      />}
      {completedTimedTask && <TaskCompletionScreen
        result={completedTimedTask.result}
        saved={completedTimedTask.saved}
        onStatistics={openStatistics}
        onBack={leaveTimedTask}
        helper={preferences.childHelper}
      />}
      {activeTimedTask && (
        <>
          {activeTimedTask.id === 'stroop' && <StroopTask key="stroop" userName={activeTimedTask.userName} onExit={leaveTimedTask} onComplete={(id, trials, summary) => finishTimedTask(id, activeTimedTask.userName, trials, summary)} />}
          {activeTimedTask.id === 'go-no-go' && <GoNoGoTask key="go-no-go" userName={activeTimedTask.userName} onExit={leaveTimedTask} onComplete={(id, trials, summary) => finishTimedTask(id, activeTimedTask.userName, trials, summary)} />}
          {activeTimedTask.id === 'sart' && <SartTask key="sart" userName={activeTimedTask.userName} onExit={leaveTimedTask} onComplete={(id, trials, summary) => finishTimedTask(id, activeTimedTask.userName, trials, summary)} />}
          {activeTimedTask.id === 'corsi' && <CorsiTask key="corsi" userName={activeTimedTask.userName} onExit={leaveTimedTask} onComplete={(id, trials, summary) => finishTimedTask(id, activeTimedTask.userName, trials, summary)} />}
          {activeTimedTask.id === 'digit-span' && <DigitSpanTask key="digit-span" userName={activeTimedTask.userName} onExit={leaveTimedTask} onComplete={(id, trials, summary) => finishTimedTask(id, activeTimedTask.userName, trials, summary)} />}
        </>
      )}
      {storageError && !showStatistics && !showSettings && <p className="storage-warning" role="alert">Δεν ήταν δυνατή η αποθήκευση. Οι απαντήσεις μένουν μόνο μέχρι να κλείσει η σελίδα.</p>}
      {dialogOpen && <StartTestDialog onStart={startAll} resumableResult={getResumableResult()} onResume={resumeAll} onClose={() => setDialogOpen(false)} />}
      {selectedTimedTask && userName && <TaskNameDialog taskTitle={timedTaskDefinitions.find((task) => task.id === selectedTimedTask)?.title ?? ''} userName={userName} onStart={startTimedTask} onClose={() => setSelectedTimedTask(null)} />}
      {newUserDialogOpen && <NewUserDialog existingUserNames={userNames} onSave={saveNewUser} onClose={() => setNewUserDialogOpen(false)} />}
      </AppShell>
    </div>
  )
}

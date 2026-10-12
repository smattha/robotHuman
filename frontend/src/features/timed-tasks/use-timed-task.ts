import { useEffect, useRef, useState } from 'react'

type TimedTaskConfig<T> = {
  create: () => T
  tick: (state: T, now: number) => T
  isFinished: (state: T) => boolean
  report: (state: T) => void
}

const TICK_MS = 50

export function useTimedTask<T>({ create, tick, isFinished, report }: TimedTaskConfig<T>) {
  const [state, setState] = useState<T>(create)
  const reportedRef = useRef(false)

  useEffect(() => {
    const interval = setInterval(() => setState((previous) => tick(previous, Date.now())), TICK_MS)
    return () => clearInterval(interval)
  }, [tick])

  const finished = isFinished(state)

  useEffect(() => {
    if (finished && !reportedRef.current) {
      reportedRef.current = true
      report(state)
    }
  }, [finished, state, report])

  function restart() {
    reportedRef.current = false
    setState(create())
  }

  return { state, setState, restart }
}

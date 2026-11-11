import type { ChildHelper, NarrationMode } from '../../domain/preferences'
import { ChildHelper as ChildHelperCard } from '../../components/child-helper/ChildHelper'
import { useNarration } from '../../hooks/use-narration'

type InstructionBriefingProps = {
  helper: ChildHelper
  message: string
  userName: string
  narrationMode: NarrationMode
  speechEnabled: boolean
  onStart: () => void
}

export function InstructionBriefing({ helper, message, userName, narrationMode, speechEnabled, onStart }: InstructionBriefingProps) {
  const { isNarrating, replay } = useNarration({ text: message, narrationMode, speechEnabled, autoPlay: true })

  return (
    <div className="task-instruction">
      <ChildHelperCard helper={helper} message={message} playing={isNarrating} />
      <p className="task-user">Παίκτης: {userName}</p>
      <div className="instruction-actions">
        <button className="primary-button" type="button" onClick={onStart}>Ξεκίνα</button>
        <button className="text-button" type="button" onClick={() => void replay()}>Άκου ξανά</button>
      </div>
    </div>
  )
}

# Plan: Web application for children’s exercises

## Goal

Create a browser-based version of the existing child-exercise application. The webapp should preserve the core experience—selecting one of several exercises, presenting visual/story content, collecting answers, giving immediate encouragement, collecting difficulty feedback, moving through exercises, and storing/viewing results—while removing the current desktop/ROS dependencies from the first web release.

## Current state

- The existing application is a Python/PyQt5 desktop application launched from `user_interface/mainMenu.py`.
- `MainWindowModel` in `user_interface/model/mainWindowModel.py` defines 12 exercises, descriptions, UI state, image paths, navigation signals, feedback state, and SQLite persistence.
- `MenuView` in `user_interface/views/menuView.py` is the main shell. It contains exercise selection, 12 exercise buttons, stacked pages, results navigation, and a separate timed “fish/shark” attention game.
- Exercise controllers are split across `user_interface/exersiceController/`: `ControllerType1`, `ControllerType2`, `ControllerExersice5`, and `ControllerExersice6`, with shared progression/answer/feedback behavior in `RootController.py`.
- Results are persisted as one wide SQLAlchemy table in `user_interface/model/Results.py`, with fixed columns for answers and feedback for exercises 1–12.
- Audio, speech recognition, hand detection, and robot movement are coupled through `user_interface/rosInterface/audioServiceInterface.py`, `audio_service`, `robot_face`, and ROS launch files. These must be treated as optional integrations, not prerequisites for the web MVP.
- The existing source contains technical debt and likely defects (duplicated methods, hard-coded filesystem paths, UI/worker-thread coupling, inconsistent state properties, and fixed exercise-specific result columns). The webapp should not reproduce these implementation details.
- Existing exercises are primarily represented by code and referenced image/audio resources. Before implementation, the complete exercise assets and exact prompts/answer choices should be inventoried from the repository.

## Proposed product scope

### MVP user flow

1. Welcome screen with a simple child-friendly start action.
2. Optional child/session information screen. Prefer a nickname or locally generated session ID rather than requiring personal data.
3. Exercise library with cards showing title, image, short description, and start action.
4. Exercise player that supports:
   - instructions and optional audio playback;
   - image/story steps;
   - multiple-choice, button, text, and timed interaction types as needed by the existing exercises;
   - explicit next/back/finish controls;
   - keyboard and touch support;
   - accessible labels and large controls.
5. Immediate, encouraging feedback after an answer without exposing sensitive performance language.
6. Optional “how difficult was it?” feedback using three child-friendly choices.
7. Completion summary with exercise results and a restart/home action.
8. Adult/results view protected by a simple local access mechanism, if results are retained.

### Exercise model

Replace the 12 fixed answer/result columns with data-driven exercise definitions. Each exercise should have an ID, title, description, category, age guidance, ordered steps, media references, interaction type, answer options, accepted answers or scoring rule, feedback text, and difficulty-feedback configuration. A single player should render the common flow while allowing exercise-specific step behavior.

### Initial release boundaries

- Browser-only operation first; no ROS, robot movement, microphone recognition, or hand detection required.
- Use browser audio playback only where an audio asset exists; provide visible text and controls as fallback.
- Store progress/results locally for the first release, preferably in IndexedDB or a small local-storage abstraction. Design interfaces so a server API can replace it later.
- Do not expose child-identifying data in URLs, logs, analytics, or public result pages.

## Ordered implementation plan

### 1. Confirm requirements and inventory the existing content

- Agree on target users, supported languages (the current content is Greek), age range, device types, offline requirements, and whether an adult dashboard is required.
- Inventory every exercise controller, UI page, image, audio file, prompt, answer, expected answer, feedback message, and multi-step transition.
- Separate reusable exercise types from special cases such as the fish/shark timed game.
- Define the MVP exercise set; recommend starting with 2–3 representative exercises rather than all 12.
- Identify licensing/consent requirements for images, voices, child data, and any third-party assets.

### 2. Establish the webapp foundation

- Create a standalone frontend application in a new webapp directory or repository area, using the team’s approved React/Vite/TypeScript conventions.
- Configure strict TypeScript, linting, formatting, unit/component testing, and a production build.
- Add responsive layout and a child-friendly visual design system: high contrast, large targets, simple language, predictable navigation, reduced distractions, and reduced-motion support.
- Define route/state boundaries for welcome, exercise library, exercise player, completion, and adult results.

### 3. Define domain types and content format

- Create typed models for `Exercise`, `ExerciseStep`, `MediaAsset`, `Interaction`, `AnswerOption`, `AnswerResult`, `DifficultyFeedback`, `Session`, and `ExerciseAttempt`.
- Store exercise content in versioned JSON/TypeScript data files initially, with media paths separate from logic.
- Use stable exercise IDs and step IDs so saved sessions remain compatible when titles or ordering change.
- Define scoring semantics explicitly: exact answer, accepted-answer list, ordered sequence, timed response, or custom evaluator.
- Add content validation tests that reject missing IDs, unreachable steps, missing assets, invalid answer references, and missing feedback.

### 4. Implement the shared exercise player

- Build a state machine/reducer for session lifecycle: not started, instruction, active step, answer submitted, feedback, difficulty feedback, completed, paused, and error.
- Keep exercise evaluation pure and testable; do not mix scoring with UI effects.
- Implement reusable renderers for the interaction types identified during inventory.
- Add a progress indicator, repeat-instruction action, answer lock after submission, next-step behavior, and restart behavior.
- Ensure feedback is encouraging and deterministic, and that a child can continue without needing a keyboard.
- Add an audio abstraction with play/pause/replay, browser capability handling, and text fallback. Keep speech recognition behind an optional adapter for a later phase.

### 5. Implement navigation and session management

- Build the exercise library from content definitions rather than hard-coded 12 buttons/pages.
- Track the current session, selected exercise, attempt timestamps, answer state, score/accuracy where appropriate, and self-reported difficulty.
- Prevent accidental loss of an active attempt when navigating away; provide a clear confirmation or save/resume behavior.
- Support restarting one exercise and starting a new session without carrying over stale answers.

### 6. Implement persistence and results

- Introduce a repository interface such as `SessionRepository` and `ResultsRepository` so local persistence can later be replaced by an API.
- Store normalized attempt records rather than one wide record with `answerEx1` through `answerEx12` equivalents.
- Handle schema versioning, corrupt/partial records, clearing data, and unavailable storage gracefully.
- Add an adult-only results view with filtering by date/session and a clear-data action if results are retained.
- Document data retention and privacy behavior before enabling persistence in a deployed environment.

### 7. Migrate content and media

- Convert the selected MVP exercises from the existing controller-specific logic into the typed content format.
- Copy or reference only approved media assets; optimize images and audio for browser loading.
- Provide missing-asset and unsupported-audio fallbacks.
- Validate the Greek text, punctuation, answer options, and child-appropriate wording with a subject-matter reviewer.

### 8. Add the timed attention game as a separate feature

- Model the fish/shark activity independently from the story/question player because it uses timers, keyboard events, reaction-time measurement, and a different scoring model.
- Implement a deterministic test mode with seeded/randomized sequences and an accessible start/stop flow.
- Define the metrics precisely: number of fish, shark inhibition errors, valid hits, reaction time, timeout behavior, and final accuracy.
- Avoid treating the current implementation’s `+0.01` accuracy adjustment or fixed 100-item limit as requirements; confirm intended scoring first.

### 9. Testing and verification

- Unit test exercise evaluators, reducer transitions, persistence serialization, content validation, timed-game scoring, and navigation edge cases.
- Component-test keyboard, touch, screen-reader labels, answer submission, feedback, replay, next, restart, and error states.
- Run browser-level tests for the complete happy path and interrupted/resumed sessions.
- Test responsive layouts on desktop, tablet, and mobile sizes, plus Chrome/Firefox/Safari-compatible behavior as required.
- Test no-audio, slow-network, missing-media, disabled-storage, refresh-during-exercise, and malformed-content scenarios.
- Run accessibility checks and manual keyboard navigation; target WCAG 2.2 AA where appropriate.
- Verify that no ROS/Python dependency is needed to start the browser MVP and that production builds contain no secrets or local filesystem paths.

### 10. Deployment and future integrations

- Build a static deployment first if local-only persistence is sufficient.
- If centralized results, authentication, content management, or multi-device sessions are required, add a backend API and database in a later phase.
- Define optional adapters for text-to-speech, speech-to-text, hand/gesture input, and robot control. Keep these outside the core exercise domain so the webapp remains usable without hardware.
- Add monitoring that excludes child answers and personally identifiable data from logs.

## Verification criteria

- A child can start an exercise, complete all steps, answer through the supported interaction, receive feedback, rate difficulty, and return home without adult/ROS hardware.
- The same player can render all MVP exercise definitions without exercise-specific page duplication.
- Refresh, back navigation, missing audio, missing image, and unavailable local storage have defined, tested behavior.
- Results contain normalized attempts with exercise/step IDs, timestamps, answer outcome, and difficulty feedback, without requiring fixed columns per exercise.
- The timed attention activity reports agreed metrics and does not count shark presses as successful fish hits.
- The application is responsive, keyboard/touch accessible, child-friendly, and free of hard-coded developer filesystem paths.

## Risks and open questions

1. **Content ambiguity:** The repository lists 12 exercise titles, but the full prompts and rules are distributed across controller/data classes and external assets. A content inventory and subject-matter approval are required before implementation.
2. **Language:** Existing text is Greek. Confirm whether Greek-only is acceptable or whether the content model must support translations from the beginning.
3. **Hardware parity:** It is not yet clear whether web users need speech recognition, microphone input, hand gestures, or robot feedback. These materially change browser permissions, architecture, testing, and privacy requirements.
4. **Results privacy:** Confirm whether results are for local research use, shared with professionals, or uploaded centrally. This determines consent, authentication, retention, and backend scope.
5. **Target devices:** Confirm whether the app runs on a touch tablet, desktop with keyboard, a kiosk, or all three.
6. **Offline mode:** The current desktop app is local. Decide whether the webapp must work fully offline; this affects asset packaging, service workers, and persistence.
7. **Assessment semantics:** Confirm whether answers are scored as correct/incorrect, whether partial credit exists, and whether reaction time is clinically meaningful.
8. **Scope:** Recommend an MVP with 2–3 exercises plus the timed game, followed by migration of the remaining exercises after the player architecture is validated.

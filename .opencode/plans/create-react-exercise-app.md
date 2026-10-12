# Plan: Create the initial React exercise webapp

## Goal

Create a new React webapp from scratch in `frontend/`, using Vite and strict TypeScript. The first increment will provide the application shell, welcome/library/player flow, and one working child-friendly exercise. ROS, robot movement, speech recognition, and gesture detection are explicitly deferred and must not be required by the first version.

## Current state

- The repository currently contains a Python/PyQt5/ROS application and has no `package.json`, React app, or frontend build configuration.
- The existing desktop app starts from `user_interface/mainMenu.py` and contains 12 exercises, shared controllers, image-based/story-based flows, feedback, and persisted results.
- The existing content is Greek and includes exercise names in `user_interface/model/mainWindowModel.py`; the implementation should reuse confirmed content but should not copy the old hard-coded UI architecture.
- There are no repository-local `AGENTS.md` files and no existing frontend conventions to preserve.
- The new app should be isolated in `frontend/` so the existing Python/ROS application remains unchanged.

## Decisions already made

- Directory: `frontend/`
- Stack: React + Vite + TypeScript
- First scope: application shell plus one working exercise
- Future integrations: ROS, robot movement, speech recognition, and gesture detection will be optional future adapters, not part of the initial app.

## Proposed implementation

### 1. Create the frontend project foundation

- Initialize a Vite React TypeScript project under `frontend/`.
- Add standard scripts for development, production build, preview, linting, and tests.
- Configure strict TypeScript and avoid `any`.
- Add a basic test setup suitable for React Testing Library and browser-like component tests.
- Add a frontend-specific README explaining setup, commands, and the intentionally deferred hardware integrations.
- Ensure generated dependency/build directories are ignored without modifying the existing Python behavior.

### 2. Establish the initial application structure

Use a feature-oriented structure such as:

```text
frontend/
  src/
    app/
      app.tsx
      routes.tsx
    components/
      app-shell/
      buttons/
      progress/
    features/
      exercise-library/
      exercise-player/
      welcome/
      completion/
    domain/
      exercise.ts
      session.ts
      result.ts
    content/
      exercises.ts
    state/
      exercise-session-reducer.ts
    styles/
    main.tsx
```

- Use named exports and functional components.
- Keep domain models independent of React and browser APIs.
- Keep exercise content separate from player rendering and evaluation logic.
- Avoid introducing backend, ROS, or authentication code at this stage.

### 3. Define the first domain model

- Define typed models for an exercise, exercise step, media asset, answer option, answer submission, feedback, session state, and attempt result.
- Support at least the first interaction type: multiple-choice answer selection.
- Design the types so future steps can support stories, images, timers, text input, audio, and custom interaction evaluators without redesigning the whole app.
- Use stable IDs for exercise and step records.

### 4. Add the first exercise content

- Select one simple exercise from the existing application after checking its controller/data class and referenced assets.
- Add its title, child-friendly instructions, available answer options, accepted answer, positive feedback, retry/incorrect feedback, and completion behavior to typed content data.
- If the original exercise requires robot/audio behavior, replace that dependency with visible text and optional browser audio only if a valid asset is available.
- Do not invent clinical or educational claims; retain only confirmed exercise behavior.

### 5. Build the user flow

Implement these screens/views:

1. **Welcome:** title, short explanation, and large start button.
2. **Exercise library:** display the first exercise as an exercise card with title, description, and start action. The structure should allow additional exercise cards later.
3. **Exercise player:** show progress, instructions, answer options, submit/continue behavior, and feedback.
4. **Completion:** show a friendly completion message and actions to return to the library or restart.

- Use client-side routing or a small explicit screen state, but choose one approach consistently.
- Prevent answer changes after submission unless the exercise explicitly supports retry.
- Make all actions usable by mouse, keyboard, and touch.
- Include visible focus states, accessible names, semantic headings, and adequate button sizes.

### 6. Implement session state

- Use a reducer or equivalent explicit state machine for welcome, library, active exercise, submitted answer, feedback, and completed states.
- Store current exercise ID, current step ID, selected answer, answer outcome, and completion status.
- Reset state correctly when restarting or beginning a new exercise.
- Keep scoring/evaluation as a pure function with no UI or persistence side effects.
- Do not add persistence until the first in-memory flow is working and tested; reserve a repository abstraction for the next increment.

### 7. Add child-friendly visual design

- Use a calm, high-contrast palette, large typography, rounded cards, clear icons/labels, and minimal navigation choices.
- Avoid excessive animation and provide reduced-motion behavior.
- Make the layout responsive for tablet, desktop, and smaller screens.
- Keep language simple and supportive; use “try again”/“good effort” rather than punitive wording.
- Centralize spacing, colors, typography, and interaction states so future exercise screens remain consistent.

### 8. Add tests and verification

- Unit-test the first exercise evaluator and all reducer/state transitions.
- Component-test the welcome screen, exercise card, answer selection, submission, correct feedback, incorrect feedback, restart, and completion navigation.
- Test keyboard navigation and accessible labels for the main controls.
- Validate the content object at test time so missing IDs/options/accepted answers fail clearly.
- Run the frontend lint/typecheck/test/build commands after implementation.
- Do not launch the built application automatically; provide the user with the command to run it manually.

## Future-ready boundaries

- Create an `audio` or `integration` interface only when needed by the first exercise; browser audio should be optional and non-blocking.
- Later integrations should be adapters outside the domain/player core:
  - ROS adapter for robot commands;
  - text-to-speech adapter;
  - speech-to-text adapter;
  - gesture/hand-detection adapter.
- Each adapter must have a no-op or unavailable fallback so the webapp remains functional without hardware or browser permissions.
- Keep future backend persistence behind repository interfaces rather than coupling components to `localStorage`, IndexedDB, or a remote API.

## Risks and open questions

1. The exact first exercise has not yet been selected. The executor should choose the simplest confirmed exercise after reviewing its controller/data class and assets, or ask for the user’s choice before content migration.
2. The repository contains image paths pointing to the old `/robotApp` filesystem layout. Assets must be copied or re-mapped into frontend-managed public/static paths; do not retain those absolute paths.
3. The current exercise text is Greek. Confirm whether the first version should remain Greek-only or whether translation keys should be introduced immediately.
4. The old application’s SQLite results and adult results view are outside this first increment. They should be planned separately after the in-memory exercise flow is validated.
5. Dependency installation and project scaffolding are execution steps. They must be performed only after leaving plan mode and with the existing repository state checked first.

## Acceptance criteria

- `frontend/` is a self-contained Vite React TypeScript application.
- The app can be started manually with the documented development command.
- A user can navigate Welcome → Exercise Library → First Exercise → Feedback → Completion → Library.
- The first exercise works without ROS, Python, robot hardware, microphone permissions, or gesture detection.
- The exercise is responsive and supports keyboard, mouse, and touch interaction.
- Tests cover the evaluator, state transitions, and main user flow.
- Production build, typecheck, lint, and tests pass.

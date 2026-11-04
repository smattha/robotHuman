# Μικρές Αποστολές

React web application for the children's exercise experience in this repository. Runs as a browser PWA and as a native Android app (Capacitor).

## Requirements

- Node.js 20 or newer
- npm
- For Android builds: Android Studio with the Android SDK

## Commands

Run these commands from `frontend/`:

```bash
npm install
npm run dev
npm run lint
npm run test
npm run build
```

### Android (Capacitor)

```bash
npm run build
npm run android:sync    # copies the fresh dist into android/
npm run android:open    # opens the project in Android Studio
```

Build the signed APK/AAB from Android Studio (Build → Generate Signed App Bundle / APK). The app id is `com.mikresapostoles.app` and the app name is «Μικρές Αποστολές». Launcher icons are generated from `scripts/generate-icons.mjs` (PWA) and `scripts/generate-android-icons.mjs` (Android mipmaps).

## Features

- 12 story exercises plus 5 memory/attention challenges (Stroop, Go/No-Go, SART, Corsi, Digit Span).
- Child-friendly UI with a selectable helper character (Ρόμπι 🤖, Φοίβος 🦊, Ίρις 🦉, Νεφέλη 🦄).
- The helper plays its own animated video while the Greek narration is speaking.
- Greek text-to-speech (Piper TTS, local) and optional speech recognition where the browser supports them.
- Confetti and reward sounds on correct answers, plus a Grand Prize screen after completing all missions.
- Statistics with CSV export and print view.
- PWA: installable, offline-capable (service worker in `images/sw.js`, manifest, generated icons).

## Mobile-first layout

The UI is designed for portrait smartphones first (360–430px), then tablets and desktops. Key points:

- Bottom navigation (Αποστολές / Παιχνίδια / Πρόοδος / Μενού) on phones; it is hidden while an activity is running.
- The exercise player is a full-screen experience: story on top, question below, and a fixed bottom action bar for the main action (thumb reach).
- Dialogs open as bottom sheets on small screens.
- Safe areas (`env(safe-area-inset-*)`) are respected; the viewport uses `viewport-fit=cover`.
- Touch targets are at least 44px. `largeButtons` grows them further.

## Native (Capacitor) notes

- Audio is user-initiated: narration starts on tap (avoids mobile autoplay blocks). The Piper voice model downloads only from Ρυθμίσεις, never automatically.
- Audio and speech recognition are paused when the tab/app is hidden.
- No browser-only APIs are used outside the existing service worker and speech features; the app runs unchanged in a WebView.
- The Piper TTS engine and the generated WAV clips are the largest runtime assets; the Greek voice is a one-time ~63 MB download.

## Privacy

Named test results, including the selected answer for each exercise, are saved in this browser's local storage and displayed on the exercise library. This is device-local storage, not an authenticated or encrypted record system; avoid entering identifying child information on shared devices. The microphone starts only when **Απάντησε με τη φωνή σου** is pressed. Spoken answers require manual confirmation with **Έλεγξε την απάντηση**. Some browsers may process microphone input using an external speech service; use the on-screen answer buttons if that is not acceptable.

## Exercise images

The app serves images from `images/` (configured as Vite's `publicDir`), so files under `images/ex1` through `images/ex12` are served at root-level URLs such as `/ex1/main-image.png`.

Exercises 1 and 2 show their supplied answer images; exercises 3, 4, 9 and 10 display ordered story images. Exercises 5 and 11 show their single main image. Helper animations live under `images/videos/`.
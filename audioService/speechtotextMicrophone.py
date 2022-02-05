#!/usr/bin/env python3
import speech_recognition as sr


filename='recording1.wav'
# initialize the recognizer
r = sr.Recognizer()

with sr.Microphone() as source:
    audio_data = r.listen(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data,language='el')
    print(text)
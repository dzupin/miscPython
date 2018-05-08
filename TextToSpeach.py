import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()

engine.say("Get ready for some very long text sentence.")
engine.say("Pyttsx is a good text to speech conversion library in python but it was written only in python2 untill now ! Even some fair amount of googling didn't help much to get a tts library compatible with Python3. There is however , one library gTTS which works perfectly in python3 but it needs internet connection to work since it relies on google to get the audio data.But Pyttsx is completely offline and works seemlesly and has multiple tts-engine support.The codes in this repos are modified version of the pyttsx module of python 2.x and most of it is implemented from westonpace's repo. The purpose of creating this repo is to help those who want to have an offline tts lib for Python3 and don't want to port it from python2 to python3 themselves.")
engine.runAndWait()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate+50)
engine.say('Fast pace. The quick brown fox jumped over the lazy dog.')
engine.runAndWait()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-100)
engine.say('Slow pace. The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
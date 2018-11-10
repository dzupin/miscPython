#Internet dependent text to speach
from gtts import gTTS

tts = gTTS(text='The quick brown fox jumped over the lazy dog.', lang='en')
tts.save('Audiofile.mp3')
tts = gTTS(text="Pyttsx is a good text to speech conversion library in python but it was written only in python2. Untill now!", lang='en')
tts.save('Audiofile2.mp3')

#Now lets play saved audio mp3 files
import time
from pygame import mixer # Load the required library
mixer.init()
mixer.music.load('Audiofile.mp3')
mixer.music.play()
time.sleep(6)
mixer.music.load('Audiofile2.mp3')
mixer.music.play()
time.sleep(12)

#Offline text to speach
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   print(voice.id)
   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
#On my computer I have 2 voices and the first one sounds better to me. Therefore I will set speech to use the first one.
engine.setProperty('voice', voices[0].id)

engine.say("Get ready for some very long text sentence.")
# Default speech rate is too fast so I will slow it down a little
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
engine.say("Pyttsx is a good text to speech conversion library in python but it was written only in python2 untill now! Pyttsx works with Python 3 and it has multiple tts-engine support.")
engine.runAndWait()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate+50)
engine.say('Fast pace. The quick brown fox jumped over the lazy dog.')
engine.runAndWait()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-100)
engine.say('Slow pace. The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
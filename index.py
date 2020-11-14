# from gtts import gTTS
# from playsound import playsound

# audio = 'test.mp3'
# language = 'es'

# sp = gTTS(text = "Esta es una prueba, no funciono el playsound", lang=language, slow=False)

# sp.save(audio)

import os
import subprocess
import pytube
from pydub import AudioSegment

yt = pytube.YouTube('https://www.youtube.com/watch?v=le1QF3uoQNg')

video = yt.streams.first().download()
nameFile = yt.title

AudioSegment.from_file(video).export(nameFile, format="mp3")

if bool(AudioSegment):
    os.remove(video)
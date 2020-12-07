import os, time
import playsound as ps
import speech_recognition as sr
from gtts import gTTS

class audio:
    filename = 'No'
    message = 'text'

    def __init__ (self,filename):
        self.filename = filename
    
    def play(self,message):
        self.message = message
        tts = gTTS(text=message, lang='en')
        filename = self.filename
        tts.save(filename)
        ps.playsound(filename)

test = audio('hello.mp3')
test.play('testtttttttttttttttttttttttttttttttttttttttttttttttttttttt')
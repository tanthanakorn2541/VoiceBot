import os, time
import playsound as ps
import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator
from datetime import datetime
import webbrowser
import pyttsx3

class audio:
    filename = 'No'
    message = 'text'

    def __init__ (self,filename):
        self.filename = filename
    
    def save_sound(self,message):
        self.message = message
        tts = gTTS(text=message, lang='th')
        filename = self.filename 
        tts.save(filename)

    def play_sound(self):
        ps.playsound(self.filename)
    

def get_order():
    r = sr.Recognizer()
    with sr.Microphone() as Source:
        sound = r.listen(Source)
        said = ''
        try:
            said = r.recognize_google(sound, None,'th')
            print(said)

        except Exception as e:
            print("Exception:" + str(e))

    return said
    
access = pyttsx3.init()
voices = access.getProperty('voices')
access.setProperty('voice', voices[0].id)

def speak(sound):
    print('ACCESS: ' + sound)
    access.say(sound)
    access.runAndWait()

speak(' At your service, sir.')


while True:

    order = get_order()
    order

    if "เปิด Visual Studio Code" in order or "Open Visual Studio Code" in order:
        speak('Got it sir, In progress to open Visual Studio Code')
        os.startfile('C:/Users/Tan Thanakorn/AppData/Local/Programs/Microsoft VS Code/code.exe')

    elif "เปิด Google Chrome" in order or "เปิด Chrome" in order:
        speak('Got it sir, In progress to open Google Chrome')
        os.startfile('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe')

    elif 'เปิดอีเมล' in order:
        speak('Will do, sir')
        webbrowser.open('https://outlook.live.com')

    elif "ปิดระบบ" in order or "ขอบใจ" in order:
        speak('Enjoy yourself, sir.')
        break


# เตรียมตัวแปรไว้แปลภาษา ด้วย google translate
# translator = Translator()
# # เตรียมตัวแปรไว้คอยรับเสียงจากไมค์
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     while True:
#         # 1. รอรับเสียงพูดจากไมค์
#         print(str(datetime.now()) + ' 1.รอรับเสียงพูดจากไมค์')
#         audio = r.listen(source)           
#         # 2. แปลงเสียงเป็นข้อความภาษาไทย
#         print(str(datetime.now()) + ' 2.แปลงเสียงเป็นข้อความภาษาไทย')
#         said = r.recognize_google(audio, None,'th')
#         print(str(datetime.now()) + '    ข้อความที่ได้ : ' + said)







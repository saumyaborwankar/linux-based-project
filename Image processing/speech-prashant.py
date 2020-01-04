import pyaudio
import time
import os
import speech_recognition as str

def speech_execution():
    mic=str.Microphone()
    rec=str.Recognizer()

    with mic as source:
        os.system("tput setaf 1")
        print("say :")
        time.sleep(1)
        audio=rec.listen(source)
        text=rec.recognize_google(audio)
        os.system("tput setaf 3")
        print(text)
        if "remote" in text:

            return "remote"
        else:
            return "local"       

def speech_bool():
    mic=str.Microphone()
    rec=str.Recognizer()

    with mic as source:
        print("say :")
        time.sleep(1)
        audio=rec.listen(source)
        text=rec.recognize_google(audio)
        if "No" in text or "no" in text :
            return 1
        else:
            return 0    
            
def speech():
    mic=str.Microphone()
    rec=str.Recognizer()
    with mic as source:
        print("say :")     
        audio=rec.listen(source)
        text=rec.recognize_google(audio)
        print(text)
        if "date" in text and "get" in text:
            return 1
        elif "calendar" in text and "get" in text:
            return 2    
        elif "open" in text and "take" in text:
            return 3
        elif "photo" in text and "save" in text:
            return 4
        elif "open" in text and "Firefox" in text:
            return 5
        elif "set" in text and "static" in text:
            return 6
        elif "custom" in text and "command" in text:
            return 7
        elif "install" in text and "python" in text:
            return 8                     
        else:
            return 0   

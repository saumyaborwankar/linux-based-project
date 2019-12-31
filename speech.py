import speech_recognition as sr
mic=sr.Microphone()
rec=sr.Recognizer()

with mic as source:
    print("Say:")
    audio=rec.listen(source)
    text=rec.recognize_google(audio)
    print(text)

import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def SpeakText(string):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=0.2)
    audio = r.listen(source)

    text = r.recognize_google(audio)
    text = text.lower()

    print("Du hast gesagt:"+"\n"+text)
    SpeakText(text)
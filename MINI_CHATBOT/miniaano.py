import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr  # pip install SpeechRecognition
import wikipedia  # pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui  # pip install pyautogui
import psutil  # pip install psutil
import pyjokes
import pywhatkit
#from PIL import ImageGrab
#import numpy as np
import cv2
#from win32api import GetSystemMetrics
#import googletrans
import gtts
from email.message import EmailMessage

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak("Hello,I'M YOUR VIRTUAL ASSISTANCE,MINIAANO! How MAY I HELP YOU")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # forfemale voice
voicerate = 210
engine.setProperty('rate', voicerate)


def date():
    date = datetime.datetime.now().strftime("%Y-%M-%D")
    speak("Today's date ")
    speak(date)


def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("current time ")
    speak(time)


def wishme():
    speak("WELCOME BACK")
    speak("at")
    time()
    speak("on")
    date()
    hour = datetime.datetime.now().hour
    if hour >= 5 and hour <= 12:
        speak("GOOD MORNING")
    elif hour >= 12 and hour <= 18:
        speak("GOOD AFTERNOON")
    elif hour >= 18 and hour <= 24:
        speak("GOOD EVENING")
    else:
        speak("GOOD NIGHT")
    speak("MINIAANO,AT YOUR SERVICE")


def cpu():
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)


def takeCommand():
    with sr.Microphone() as source:
        print("Listening...")
        listener = sr.Recognizer()
        listener.pause_threshold = 1
        audio = listener.listen(source)

    try:
        print("Recongnizning...")
        query = listener.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('surbhigusain74@gmail.com', 'googlesurbhi')
    server.sendmail('surbhigusain74@gmail.com', to, content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\hp\OneDrive\\Pictures\\Screenshots\\ss.png")


def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        print(query)
        if "time" in query:
            time()
        elif "date" in query:
            date()

        elif "logout" in query:
            os.system("shutdown -l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif 'remember that' in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("you said me to remember that"+data)
            remember = open('notes.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'do you remember anything about' in query:
            remember = open('notes.txt', 'r')
            speak("you said me to remember that" + remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("Screenshot taken")

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'offline' in query:
            quit()

        elif 'play song' in query:
            song = query.replace('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)

        elif 'who is' in query:
            speak("Searching...")
            person = query.replace('who', '')
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)
        # elif 'send email' in query:
            # try:
            #speak("What should I say?")
            #content = takeCommand()
            #to = 'xyz@gmail.com'
            # sendEmail(to,content)
            #speak("Email has been sent!")
            # except Exception as e:
            # print(e)
            #speak("Uable to send the email")

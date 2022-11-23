import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import os
from pygame import mixer
import sys
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)
def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

speak('Hello I am Tau, How may I help you?')
def myCommand():
    r = sr.Recognizer()                                                                               
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.energy_threshold =10000
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
    except sr.UnknownValueError:
        speak('Searching')
        query = str(input('Command: '))
        # myCommand()
    return query
if __name__ == '__main__':
    while True:
        query = myCommand();
        query = query.lower()
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')
        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')
        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')
       
        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye, may be meet again')
            sys.exit()
        elif 'hello' in query:
            speak('Hello dear')
        elif 'bye' in query:
            speak('Bye,may we meet again')
            sys.exit()
       
            
       
        elif 'what are you' in query:
            speak('I am Tau!,I was written by Anuj and Abhishek in language called python.If you provide me internet connection i can search things for you in wikipedia.I can also open some applications for you.')
        elif 'do you exist' in query:
            speak('yes but in computer program!!!')
        elif 'who made you' in query:
            speak('Anuj and Abhishek')
        else:
            query = query
            speak('Searching...')
            try:
                results = wikipedia.summary(query, sentences=2)
                speak('Got it.')
                speak('WIKIPEDIA says - ')
                speak(results)
            except:
                webbrowser.open('www.google.com/search?q='+query)
        speak('How may I help you?')

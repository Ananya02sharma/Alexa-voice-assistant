import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import datetime
import pyjokes
import smtplib 
import pyaudio
import os
import time
import phonenumbers
import wikipedia
import PyPDF2




from phonenumbers import geocoder
from phonenumbers import carrier


def speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("not recognized")



def speechtxt(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speechtxt("Good Morning!")

    elif hour>=12 and hour<18:
        speechtxt("Good Afternoon!")   

    else:
        speechtxt("Good Evening!")  

    speechtxt("I am Alexa . Please tell me how may I help you")

wishMe()

if __name__ == '__main__' :

    while True :
    # if speech().lower() == "alexa":
        data1 = speech().lower()
    
        if "your name" in data1:
            name = "my name is alexa"
            speechtxt(name)
        
        elif "what are you " in data1:
            ans = "i am a machine"
            speechtxt(ans)
        
        elif "time" in data1:
            time = datetime.datetime.now().strftime("%I%M%p")
            speechtxt(time)
        
        elif "youtube" in data1:
            wb.open("https://www.youtube.com/")
            speechtxt("it is opened")
        
        elif "whatsapp" in data1:
            wb.open("https://web.whatsapp.com/")
            speechtxt("it is opened")
        
        elif "code" in data1:
            wb.open("https://leetcode.com/problemset/all/")
            speechtxt("it is opened")
        
        elif "mail" in data1:
            wb.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
            speechtxt("it is opened")
        
        elif "laugh" in data1:
            joke1 = pyjokes.get_joke(language="en",category="all")
            print(joke1)
            speechtxt(joke1)
        
        elif "phone" in data1:
            number = input()
            ch_number =  phonenumbers.parse(number,"CH")
            ans = geocoder.description_for_number(ch_number, "en")
            servicenum = phonenumbers.parse(number,"RO")
            sim = carrier.name_for_number( servicenum,"en")
            print(ans)
            print(sim)
            speechtxt(ans)
            speechtxt(sim)

        elif "pdf" in data1 :
            book = open('op.pdf','rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            page = pdfreader.getPage(1)
            text = page.extractText()
            speechtxt(text)
            
        
        elif 'wikipedia' in data1:
            speechtxt("searching wikipedia")
            data1 = data1.replace("wikipdia","")
            results = wikipedia.summary(data1, sentences=2) 
            speechtxt("according to Wikipedia")
            print(results)
            speechtxt(results)
        
        
        
        elif "bye" in data1:
            speechtxt("bye have a niceday")
            break
        
        time.sleep(3)
        
else:
   speechtxt("thank you")        


    

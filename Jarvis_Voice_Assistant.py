import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import keyboard

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty("voices",voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("i am your assistant! sir how may i help you today")
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("\n i didnt heard that can you say it again")
        speak(" i didnt heard that can you say it again")
        return "None"
    return query

if __name__ == "__main__":
    greet()
    while True:

        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
       
        elif "open" in query:
            query = query.replace("open","")
            webbrowser.open(f"{query}.com")
            speak(f"opening {query}")

        elif "search" in query:
            query = query.replace("search","")
            url = "https://www.google.com/search?q=" + query
            webbrowser.open(url)
            speak(f"searching {query}")
        elif "stop" in query:
            print("stoping all functions")
            speak("stoping all functions")
            break
        elif "time" in query:
            time1 = time.strftime("%H:%M:%S")
            speak(time1)
        elif "date" in query:
            date = time.strftime("%d %m %Y")
            speak(date)
        elif "type" in query:
            query = query.replace("type","")
            # time.sleep(3)
            keyboard.write(query)
            speak(f"typing {query}")
            keyboard.press_and_release("enter")
    


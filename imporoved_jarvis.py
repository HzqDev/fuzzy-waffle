import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import keyboard
import logging

# -------------------- Configuration --------------------
ASSISTANT_NAME = "edith"   # Change as desired
GREET_USER = True                   # Option to greet user on start
INCLUSIVE_GREETING = True           # Use gender-neutral greetings

# -------------------- Logging Setup --------------------
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# -------------------- Text-to-Speech Engine --------------------
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id if len(voices) > 1 else voices[0].id)

def speak(audio: str):
    logging.info(f"Assistant: {audio}")
    engine.say(audio)
    engine.runAndWait()

# -------------------- Greeting Function --------------------
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        greet_time = "Good morning"
    elif 12 <= hour < 18:
        greet_time = "Good afternoon"
    else:
        greet_time = "Good evening"
    if INCLUSIVE_GREETING:
        speak(f"{greet_time}! I'm {ASSISTANT_NAME}. How may I help you today?")
    else:
        speak(f"{greet_time}, sir! I'm {ASSISTANT_NAME}. How may I help you today?")

# -------------------- Command Listening Function --------------------
def take_command() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=7)
        except Exception as e:
            logging.error(f"Microphone error: {e}")
            speak("Sorry, I'm having trouble accessing the microphone.")
            return ""
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""
    except Exception as e:
        logging.error(f"Recognition error: {e}")
        speak("An error occurred while recognizing your speech.")
        return ""

# -------------------- Command Handlers --------------------
def handle_wikipedia(query: str):
    topic = query.replace("wikipedia", "").strip()
    if not topic:
        speak("Please specify what you want to search on Wikipedia.")
        return
    speak("Searching Wikipedia...")
    try:
        results = wikipedia.summary(topic, sentences=2)
        speak("According to Wikipedia:")
        print(results)
        speak(results)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There are multiple results for that topic. Can you be more specific?")
        print(f"Disambiguation options: {e.options}")
    except wikipedia.exceptions.PageError:
        speak("I couldn't find any result for that topic on Wikipedia.")
    except Exception as e:
        logging.error(f"Wikipedia error: {e}")
        speak("Sorry, I couldn't fetch Wikipedia results at this time.")

def handle_open(query: str):
    site = query.replace("open", "").strip().replace(" ", "")
    if not site:
        speak("Please specify the website to open.")
        return
    url = f"https://{site}.com"
    speak(f"Opening {site}.")
    try:
        chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    except Exception as e:
        logging.error(f"Webbrowser error: {e}")
        speak("Sorry, I couldn't open the website.")


def handle_search(query: str):
    search_term = query.replace("search", "").strip()
    if not search_term:
        speak("Please specify what you want to search for.")
        return
    url = f"https://www.google.com/search?q={search_term}"
    speak(f"Searching Google for {search_term}.")
    try:
        webbrowser.open(url)
    except Exception as e:
        logging.error(f"Webbrowser error: {e}")
        speak("Sorry, I couldn't perform the search.")

def handle_time():
    current_time = time.strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")

def handle_date():
    current_date = time.strftime("%A, %B %d, %Y")
    speak(f"Today's date is {current_date}")

def handle_type(query: str):
    to_type = query.replace("type", "", 1).strip()
    if not to_type:
        speak("Please specify what you want me to type.")
        return
    try:
        keyboard.write(to_type)
        speak(f"Typing: {to_type}")
        keyboard.press_and_release("enter")
    except Exception as e:
        logging.error(f"Keyboard typing error: {e}")
        speak("Sorry, I couldn't type that out.")

def handle_help():
    help_text = (
        "You can ask me to do things like:\n"
        "- Search Wikipedia: 'wikipedia Albert Einstein'\n"
        "- Open a website: 'open github'\n"
        "- Search Google: 'search Python programming'\n"
        "- Tell the time: 'what is the time'\n"
        "- Tell the date: 'what is the date today'\n"
        "- Type text: 'type Hello, world!'\n"
        "- Stop: 'stop'\n"
        "How can I help you?"
    )
    speak(help_text)

# -------------------- Command Routing --------------------
def process_query(query: str) -> bool:
    if not query:
        return True  # Keep running
    if "wikipedia" in query:
        handle_wikipedia(query)
    elif query.startswith("open"):
        handle_open(query)
    elif query.startswith("search"):
        handle_search(query)
    elif "time" in query:
        handle_time()
    elif "date" in query:
        handle_date()
    elif query.startswith("type"):
        handle_type(query)
    elif "help" in query:
        handle_help()
    elif "stop" in query or "exit" in query or "quit" in query:
        speak("Stopping all functions. Goodbye!")
        return False  # Stop running
    else:
        speak("Sorry, I didn't understand that command. Say 'help' to know what I can do.")
    return True

# -------------------- Main Assistant Loop --------------------
def main():
    if GREET_USER:
        greet()
    running = True
    while running:
        query = take_command()
        running = process_query(query)

if __name__ == "__main__":
    main()

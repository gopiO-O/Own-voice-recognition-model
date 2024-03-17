import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1])

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def routines():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("I am your companion, How can I help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Koora is Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")

    except:
        print("Say that again....")
        return "None"
    return query


routines()
while True:
    query = takecommand().lower()

    if "who are you" in query:
        speak("I am your AI companion")
        webbrowser.open("facebook.com")
    elif "open google" in query:
        webbrowser.open("google.com")
        speak("do you want me to search by koora")
        a = takecommand().lower()
        if "yes" in a:
            while True:
              speak("Koora is Listening...")
              s = takecommand().lower()
              if "close" in s:
                speak("exit google...")
                break
              elif "none" not in s:
                webbrowser.open_new_tab(f"http://www.google.com/search?q={s}")
          

    elif "time now" in query:
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time now is {time_now}")

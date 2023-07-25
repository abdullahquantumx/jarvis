import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyautogui
import os
import time
import pywhatkit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    # print(hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am Jarvis Sir.How may I help you.")


def takeCommand():

    # it takes microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print("Say that again please....")
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')


            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
                webbrowser.open("google.com")

        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'whatsapp' in query:
            webbrowser.open("whatsapp.com")

        elif 'message' in query:  # sending whatsapp message particularly to one person at mentioned time
            pywhatkit.sendwhatmsg('+91XXXXXXXXXX','hello',23,5) # mention the time so that message will be delivered at that time only

        elif 'instagram' in query:
            webbrowser.open("instagram.com")

        elif 'gmail' in query:
            webbrowser.open("gmail.com")

        elif 'spotify' in query:
            os.system("spotify")
            time.sleep(10)
            pyautogui.hotkey('ctrl', 'l')
            pyautogui.write('ghungroo', interval=0.1)
            for key in ['enter', 'pagedown', 'tab', 'enter', 'enter']:
               time.sleep(1)
               pyautogui.press(key)

        elif 'time' in query:
          t = datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"Sir,the time is {t}")
        elif 'quit' in query:
            speak("Quiting Sir ")
            break

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pywhatkit


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish_me():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I'm Jarvis , May I Help You With Anything")

def searchGoogle(query):
    query = query.replace("google", "")
    query = query.replace("google search", "")
    query = query.replace('jarvis', '')

    speak("This is what I have found")

    try:
        pywhatkit.search(query)
        result = wikipedia.summary(query, sentences=1)
        speak(result)

    except Exception as e:
        speak("Sorry, I could not find anything")



def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='eng-ind')
        print(f"User Said {query}\n")
    except Exception as e:
        speak("Please Say That Again")
        print("Say That Again Please...")
        return "None"
    return query


if __name__=="__main__":
    wish_me()
    while True:
        query=takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching WikiPedia..")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According To wikipeida")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open chatgpt' in query:
            webbrowser.open("chat.openai.com")

        elif 'open email' in query:
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

        elif 'open google' in query:
            webbrowser.open('https://www.google.com/')

        elif 'open wikipedia' in query:
            webbrowser.open('https://www.wikipedia.org/')

        elif 'stack overflow' in query:
            webbrowser.open('https://stackoverflow.com/')

        elif 'open whatsapp' in query:
            webbrowser.open('https://web.whatsapp.com/')

        elif 'open zoro' in query:
            webbrowser.open("https://zoro.to/")

        elif "how are you" in query:
            speak("I am Fine Sir , How are you")

        elif 'I am fine' in query:
            speak("Great to hear that sir, How can I help you today")


        elif 'prime video' in query:
            webbrowser.open('https://www.primevideo.com/')

        elif 'open netflix' in query:
            webbrowser.open("https://www.netflix.com/in/")

        elif 'python' in query:
            file="C:\\Users\\SURENDRAN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\IDLE (Python 3.9 64-bit).lnk"
            os.startfile(file)

        elif 'the time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The Time Is {time}")

        elif 'play music' in query:
            speak("playing music sir ")
            file_path="C:\\Users\\SURENDRAN\\OneDrive\\Desktop\\music"
            songs=os.listdir(file_path)
            os.startfile(os.path.join(file_path,random.choice(songs)))




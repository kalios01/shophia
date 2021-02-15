import urllib
import pyttsx3 as p  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import re
import urllib.request
import urllib.parse

engine = p.init("sapi5")
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def shutdown():
    speak('understood sir')
    speak('connecting to command prompt')
    speak('shutting down your computer')
    os.system('shutdown -s')


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak(" Myself shophia . Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='hindi-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('opening youtube...')
            webbrowser.open("https://www.youtube.com/")
        elif 'open google' in query:
            speak('opening google...')
            webbrowser.open("https://www.google.com")
        elif 'open whatsapp' in query:
            speak('opening whatsapp...')
            webbrowser.open("https://web.whatsapp.com/")
        elif 'open facebook' in query:
            speak('opening facebook...')
            webbrowser.open("https://facebook.com")
        elif 'classes' in query:
            speak('connecting to Shivpal Sir...')
            webbrowser.open("https://us04web.zoom.us/j/7430197119?pwd=MUJJQUJJYXRFazZyT09ZZUg4WjJGQT09")
        elif 'school physics' in query:
            speak('connecting to Rahul Sir...')
            webbrowser.open("https://us04web.zoom.us/j/9978774988?pwd=WUR2TkpvS3l4VHN5d1FKNlZ1MXBmQT09")
        elif 'school mathematics' in query:
            speak('connecting to majid Sir...')
            webbrowser.open("https://us04web.zoom.us/j/75153720754?pwd=WmxWYklJRnFEeVRGNm9BUTZzeWpyUT09")
        elif 'school chemistry' in query:
            speak('connecting to Arshad Sir...')
            webbrowser.open("https://us04web.zoom.us/j/6290298637?pwd=SnUzZzZWSWpyL213RTV2d2M1WHkxUT09")
        elif 'computer science' in query:
            speak('connecting to Shagufa Miss...')
            webbrowser.open("https://us04web.zoom.us/j/5746326607?pwd=79VsN7Xo71LoXO771E9c1SBnVm2Do2U")
        elif 'english' in query:
            speak('connecting to Surbhi Miss...')
            webbrowser.open("https://us04web.zoom.us/j/6137411281?pwd=ha4TStOiodecCs4nS2XLpWMabkaf")
        elif 'hollywood song' in query:
            webbrowser.open("https://www.youtube.com/watch?v=kJQP7kiw5Fk&list=PL15B1E77BB5708555")
        elif 'bollywood song' in query:
            webbrowser.open("https://www.youtube.com/watch?v=xvYBg6MWPbM&list=PL9bw4S5ePsEG1Ovrxj9o2RLx43ALFoFyU")
        elif 'travel song' in query:
            webbrowser.open("https://www.youtube.com/watch?v=T5eQ-Vo_3EQ")
        elif 'workout song' in query:
            webbrowser.open("https://www.youtube.com/watch?v=L0QbRB54jR4")
        elif 'quit' in query:
            speak('have a nice day Sir...')
            os._exit()


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'email to receiver name' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "your email"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")
            except:
                speak("ooh some error occurred try again")

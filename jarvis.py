import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pywhatkit
import os
import wikipedia
import pyautogui
import time
import cv2



Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices', voices[0].id)
Assistant.setProperty('rate', 170)

def Speak(audio):
    print("  ")
    Assistant.say(audio)
    print(f"{audio}")
    print("  ")
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("nexus is listening....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("nexus is searching....")
            query = command.recognize_google(audio, language='en-US')
            print(f"user said: {query}")

        except Exception as Error:
            return "none"

        return query.lower()

def TaskExe():




    def Music():
        Speak("tell me the name of the song sir")
        musicName = takecommand()

        if 'once upon a time' in musicName:
            os.startfile('C:\\Users\\User\\OneDrive\\Desktop\\songs\\Once-Upon-a-Time.mp3')

        elif 'Lokiverse' in musicName:
            os.startfile('C:\\Users\\User\\OneDrive\\Desktop\\songs\\Lokiverse.mp3')

        else:
            pywhatkit.playonyt(musicName)

        Speak("done sir! enjoy your song sir")

    def Whatsapp():
        Speak("tell me the name of the contact you want to send message to sir")
        name = takecommand()

        if 'amma' in name:
            Speak("Tell me the message sir")
            msg = takecommand()
            Speak("Tell me the time sir")
            Speak("time in hour")
            hour = int(takecommand())
            Speak("time in minutes")
            mino = int(takecommand())
            pywhatkit.sendwhatmsg("+96891464921", msg, hour, mino, 20)
            Speak("ok sir sending the whatsapp message to amma")

        elif 'daddy' in name:
            Speak("Tell me the message sir")
            msg = takecommand()
            Speak("Tell me the time sir")
            Speak("time in hour")
            hour = int(takecommand())
            Speak("time in minutes")
            mino = int(takecommand())
            pywhatkit.sendwhatmsg("+96895116479", msg, hour, mino, 20)
            Speak("ok sir sending the whatsapp message to daddy")

        else:
            Speak("Tell me the phone number")
            Phone = int(takecommand())
            ph = '+968' + Phone
            Speak("Tell me the message sir")
            msg = takecommand()
            Speak("Tell me the time sir")
            Speak("time in hour")
            hour = int(takecommand())
            Speak("time in minutes")
            mino = int(takecommand())
            pywhatkit.sendwhatmsg(ph, msg, hour, mino, 20)
            Speak("ok sir sending the whatsapp message to amma")





        Speak("your command has been successfully completed")


    while True:

        query = takecommand()

        tt = time.strftime("%I:%M %p")

        if "hello" in query:
            Speak(f"hi sir  its {tt} how may i help you?")

        elif "how are you" in query:
            Speak("im good sir thank you for asking how may i help you")

        elif "you need a break" in query:
          Speak("ok sir call me when you need me and have a great day...")
          break

        elif 'thank you' in query:
            Speak("no problem i am always there for you")

        elif "bye" in query:
            Speak("ok sir bye see you later")
            break

        elif "i am good" in query:
            Speak("thats nice sir how may i help you")

        elif "youtube search" in query:
            Speak("ok sir this is what i found for your search sir")
            query = query.replace("nexus","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Done sir")

        elif "google search" in query:
            Speak("This is what i found for your search sir")
            query = query.replace("nexus", "")
            query = query.replace("google search", "")
            pywhatkit.search(query)
            Speak("Done sir")

        elif "website" in query:
            Speak("ok sir launching website")
            query = query.replace("nexus", "")
            query = query.replace("website", "")
            web1 = query.replace("open", "")
            web2 = "https://www." + web1 + ".com"
            webbrowser.open(web2)
            Speak("launched sir")

        elif "launch" in query:
            Speak("tell me the name of the website sir")
            name = takecommand()
            web = "https://www." + name + ".com"
            webbrowser.open(web)
            Speak("done sir")

        elif 'music' in query:
            Music()

        elif 'wikipedia' in query:
            Speak("Searching wikipedia...")
            query = query.replace("nexus", "")
            query = query.replace("wikipedia", "")
            wiki = wikipedia.summary(query, 2)
            Speak(f"According to wikipedia : {wiki}")

        elif 'whatsapp message' in query:
            Whatsapp()



        elif "screenshot" in query:
            Speak("sir please hold on im taking the screenshot")
            time.sleep(4)
            img = pyautogui.screenshot()
            Speak("sir what name should i save this picture to")
            name = takecommand()
            img.save(f"{name}.jpeg")




            Speak("done sir any other help")



TaskExe()
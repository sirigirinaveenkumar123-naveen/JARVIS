import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import subprocess

recognizer=sr.Recognizer()
def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open brave" in c.lower():
        subprocess.Popen([
            "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
            "https://brave.com"
        ])
   
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    
if __name__=="__main__":
    speak("Initializing Jarvis....")
    while True:
        r=sr.Recognizer()
        print("Recognizing....")

        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio=r.listen(source,timeout=5,phrase_time_limit=5)
            word = r.recognize_google(audio)
            print("You said:", word)
            if(word.lower()=="jarvis"):
                print("Yaa")
                speak("Yes Naveen, How can I help You ?")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print(f"Error{e}")
            
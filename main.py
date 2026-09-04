import speech_recognition as sr
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def say(text):
    speaker.Speak(text)

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio =r.listen(source)
        query = r.recognize_google(audio, language="en-IN")
        print(f"User said : {query}")
        return query

if __name__ == '__main__':
    print("Listening.....")
    text=takeCommand()
    say(text)
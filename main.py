import speech_recognition as sr
import win32com.client
import webbrowser

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def say(text):
    speaker.Speak(text)

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio =r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-IN")
            print(f"User said : {query}")
            return query
        except Exception as e:
            return "Please Repeat Closer to the microphone"
if __name__ == '__main__':
    say("Hello sir, How may I help you?")
    print("Listening.....")
    query=takeCommand()
    sites= [["youtube","https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google","https://www.google.com"],["chat gpt","https://www.chatgpt.com"]]
    for site in sites:
        if f"open {site[0]}".lower() in query.lower():
            say(f"Opening{site[0]}")
            webbrowser.open(site[1])
            
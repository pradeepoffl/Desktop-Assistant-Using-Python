#conditional approach
import pyttsx3 
import speech_recognition as sr
import datetime 

#Taking voice from my system
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id) # checking male/ female voice
#print(type(voices))

engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)
#speak function

def speak(text):
    """
    This function takes text and returns voice
    Args:
        text (_typ_): string
    """
    engine.say(text)
    engine.runAndWait()
#speak("I'm your desktop assistant, How can I help you? ")

# speech recognition function


def takeCommand():
    """
    This function will recognize voice & return text
    """
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing..")
            query=r.recognize_google(audio,language='en-in')
            print(f'user said : {query}\n')
        
        except Exception as e:
            print("Can you say that again please...")
            return "None"
        return query
#text=takeCommand()
#speak(text)

def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good moring pradeep, how are you doing ? ")
    elif hour>=12 and hour<18:
        speak("Good Afternoon pradeep, how are you doing ")
    else:
        speak("Good Evening pradeep, how are you doing")

    speak("I am your Desktop assistant. how can i help you?")



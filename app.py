from src.helper import speak, takeCommand, wish_me
import datetime
import wikipedia
import webbrowser
import os
import streamlit as st

# all the defined function are call here.

if __name__ == "__main__": 
    
    st.title("Hello...!")
    st.title("I am your Desktop assistant")
    wish_me()
    while True:

        
        #speak("I'm your desktop assistant, How can I help you? ")
        query=takeCommand().lower()
        print(query)

        #condition approach zujagar approach

        if "wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif "google" in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'now the time is {strTime}')

        elif "ok bye" or "bye" or "go to sleep" in query:
            speak("Thanks bye Take care")
            exit()






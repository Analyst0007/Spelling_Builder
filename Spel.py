# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 13:49:49 2025

@author: Hemal
"""

import streamlit as st
import speech_recognition as sr
import pyttsx3

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Please say a word...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            st.write(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            st.write("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            st.write("Could not request results; check your network connection.")
            return None

def spell_word(word):
    engine = pyttsx3.init()
    for letter in word:
        engine.say(letter)
        engine.runAndWait()

def main():
    st.title("Speech to Spelling App")
    st.write("Click the button and say a word to get its spelling.")

    if st.button("Start"):
        word = recognize_speech()
        if word:
            st.write(f"Spelling: {word}")
            spell_word(word)

if __name__ == "__main__":
    main()

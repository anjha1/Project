import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 130)

text = "hello i am Anjha and what is your name"

engine.say(text)
engine.runAndWait()  

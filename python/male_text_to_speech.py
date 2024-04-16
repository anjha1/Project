import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 130)

text = "hello i am Anjha"

engine.say(text)
engine.runAndWait()  

import pyjokes
import flask
import pyttsx3 as speach
# jokes = pyjokes.get_jokes()
# print(jokes)

engine = speach.init()
engine.say("Radhe Radhe")
engine.runAndWait()
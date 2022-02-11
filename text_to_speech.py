from audioop import ratecv
import pyttsx3

#Initialize the object or Object creation
engine=pyttsx3.init()

#Setting VOICE
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) #Id[0] is for male voice

#Setting a speak rate
rate=engine.getProperty('rate')
engine.setProperty('rate',125)

#Defining a function to get a input
def speakTocom(str):
    engine.say(str)
    engine.runAndWait()

speakTocom("Hello Akash,You are a great person") # Calling a function to execute text to speech
engine.say('My current speaking rate is '+ str(rate))
engine.runAndWait()

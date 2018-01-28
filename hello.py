import speech_recognition as sr
import speech
import time

response = speech.input("Say something, please.")
speech.say("You said " + response)

def callback(phrase, listener):
    if phrase == "goodbye":
        listener.stoplistening()
    speech.say(phrase)

listener = speech.listenforanything(callback)
while listener.islistening():
    time.sleep(.5)

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

msg = "Szeretem az Orsit"
print(msg)
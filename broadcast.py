import pyttsx3


def init(string):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'zh')
    engine.setProperty('rate', 142)
    engine.say(string)
    engine.runAndWait()

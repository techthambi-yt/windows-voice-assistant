import speech_recognition as sr
import pyttsx3
import pyautogui as pg
import time
r = sr.Recognizer()
error_count=0
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def sollu(msg):
    engine.say(msg)
    print(msg)
    engine.runAndWait()
def kelu():
    sollu("listening now")
    with sr.Microphone() as source2:
            audio2 = r.listen(source2,phrase_time_limit=3)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            return MyText
def shutdown():
     sollu("i am shutting down")
     sollu("see u later")
     quit()
while(1):   
    if error_count==3:
       shutdown()
    try:
            vin= kelu()
            sollu(vin)
            error_count=0
            if vin=="who are you":
                sollu("hii")
                sollu("i am a voice assistant created by christo as a python project")
                sollu("ask help to know about all commands")
            if vin=="bye bye":
                shutdown()
            if vin=="volume up" or vin=="volumeup" or vin=="unmute":
                pg.press("volumeup",presses=50)
            if vin=="mute": 
                pg.press("volumedown",presses=50)
            if vin=="screenshot" or vin=="snip":
                pg.hotkey("win","prntscrn")
            if vin=="desktop":
                pg.hotkey("win","d")
            if vin=="file explorer" or vin=="my computer" or vin=="this pc":
                pg.hotkey("win","d")
            if vin=="notepad":
                pg.hotkey("win","s")
                pg.typewrite("notepad")
                pg.press("enter")
            if vin=="switch tab":
                pg.hotkey("alt","tab")
            if vin=="shutdown" or vin=="shut down":
                pg.hotkey("win","d")
                pg.hotkey("alt","f4")
                pg.press("enter")
            if vin=="open":
                sollu("which app should i open")
                openinput=kelu()
                pg.hotkey("win","s")
                pg.typewrite(openinput)
                pg.press("enter")
            if vin=="change voice":
                sollu("boy or girl")
                voicechange=kelu()
                if voicechange=="boy":
                    engine.setProperty('voice',voices[0].id)
                    sollu("voicechange successful")
                elif voicechange=="girl":
                    engine.setProperty('voice',voices[1].id)
                    sollu("voicechange successful")
                else:
                    sollu("voicechange unsuccessful")
            if vin=="type":
                sollu("what should i type")
                typeinput=" "
                while(typeinput!="exit"):
                    typeinput=kelu()
                    pg.typewrite(typeinput)
            time.sleep(1)
    except sr.RequestError as e:
        sollu("please connect to internet and try again")
        time.sleep(2)
        error_count+=1
    except sr.UnknownValueError:
        sollu("i cant understand you sorry")
        error_count+=1
import pyttsx3, keyboard, speech_recognition as sr

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    try:
        engine.say(text)
        engine.startLoop(False)
        while engine.isBusy():
            if keyboard.is_pressed("esc") or keyboard.is_pressed("enter") or keyboard.is_pressed("space"):
                engine.stop()
                return
            engine.iterate()
        engine.endLoop()
    except Exception as e:
        print(f"[Speak Error] {e}")

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            return recognizer.recognize_google(audio).lower()
        except:
            return ""

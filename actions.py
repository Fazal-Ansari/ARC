import os, subprocess, datetime, pyautogui, webbrowser, wikipedia
from services import SERVICES

INTENTS = {
    "screenshot": ["take screenshot"],
    "notepad": ["open notepad"],
    "cmd": ["open cmd"],
    "calculator": ["open calculator"],
    "camera": ["take photo"],
    "paint": ["open paint"],
    "explorer": ["open explorer"],
    "excel": ["open excel"],
    "word": ["open word"],
    "powerpoint": ["open powerpoint"],
    "settings": ["open settings"],
    "maps": ["location of"],
    "google_search": ["search"],
    "wikipedia": ["define"],
    "video": ["play"],
    "exit": ["exit"]
}

def launch(cmd): return subprocess.Popen(cmd, shell=True)

def perform_action(text, intent):
    try:
        if intent == "screenshot":
            path = r"C:\Screenshots"
            os.makedirs(path, exist_ok=True)
            name = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            pyautogui.screenshot().save(os.path.join(path, name))
            return "Screenshot saved."

        elif intent in ["notepad", "cmd", "calculator", "camera", "paint", "explorer", "settings"]:
            return f"{intent} opened." if launch(f"start {intent}") else "Failed."

        elif intent == "maps":
            webbrowser.open(f"https://www.google.com/maps/search/{text}")
            return "Showing map."

        elif intent == "google_search":
            webbrowser.open(f"https://www.google.com/search?q={text}")
            return "Searching Google."

        elif intent == "wikipedia":
            try:
                return wikipedia.summary(text, sentences=2)
            except:
                return "No results on Wikipedia."

        elif intent in SERVICES:
            webbrowser.open(SERVICES[intent])
            return f"Opening {intent.title()}."

    except Exception as e:
        return str(e)

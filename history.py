import json, os
from config import CHAT_HISTORY_FILE

chat_history = []

def load_chat_history():
    global chat_history
    if os.path.exists(CHAT_HISTORY_FILE):
        with open(CHAT_HISTORY_FILE, "r", encoding="utf-8") as file:
            chat_history = json.load(file)
    else:
        chat_history = [{
            "role": "system",
            "content": "You provide short and concise one-line answers. Avoid explanations unless asked."
        }]

load_chat_history()

def append_to_history(role, content):
    chat_history.append({"role": role, "content": content})
    if len(chat_history) > 20:
        chat_history.pop(1)

def save_chat_history():
    with open(CHAT_HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(chat_history, file, indent=4)

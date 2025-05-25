from flask import Flask, request, jsonify, render_template
from audio import speak
from nlp import generate_response
from intents import detect_intent
from actions import perform_action
from history import save_chat_history

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input.strip():
        return jsonify({"response": "I didn't catch that. Can you say it again?"})

    intent = detect_intent(user_input)
    result = perform_action(user_input, intent)
    if not result:
        result = generate_response(user_input)

    # 🔊 Speak response before sending
    speak(result)

    save_chat_history()
    return jsonify({"response": result})

if __name__ == "__main__":
    app.run(debug=True)

import requests
from config import groq_api_key, MAX_HISTORY
from history import chat_history, append_to_history

def generate_response(transcription):
    append_to_history("user", transcription)

    # Add system prompt if starting a new session
    if not any(msg["role"] == "system" for msg in chat_history):
        chat_history.insert(0, {
            "role": "system",
            "content": "You are a helpful and conversational AI assistant."
        })

    payload = {
        "model": "llama3-8b-8192",
        "messages": chat_history[-MAX_HISTORY:],  # Limit to last N exchanges
        "max_tokens": 150,
        "temperature": 0.7
    }

    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            json=payload,
            headers=headers
        )

        if response.status_code == 200:
            data = response.json()
            reply = data["choices"][0]["message"]["content"]

            # Handle empty reply
            if not reply.strip():
                reply = "Hmm... I didn't catch that. Can you say it another way?"

            append_to_history("assistant", reply)
            return reply
        else:
            return f"API error: {response.status_code} - {response.text}"

    except Exception as e:
        return f"Error while contacting Groq API: {e}"


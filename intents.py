from fuzzywuzzy import fuzz
from actions import INTENTS
from services import SERVICE_KEYWORDS

def detect_intent(user_input):
    best_score, best_intent = 0, None

    for intent, keywords in {**INTENTS, **SERVICE_KEYWORDS}.items():
        for keyword in keywords:
            score = fuzz.token_set_ratio(user_input, keyword)
            if score > best_score:
                best_score = score
                best_intent = intent

    return best_intent if best_score >= 70 else "other"

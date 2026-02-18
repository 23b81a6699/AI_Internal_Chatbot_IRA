import os
from nlp_engine import get_answer

def chatbot_response(query):
    if not os.path.exists("data/website_text.txt"):
        return "⚠️ Website not processed yet."

    with open("data/website_text.txt", "r", encoding="utf-8") as f:
        text = f.read()

    if len(text.strip()) < 50:
        return "⚠️ Website content could not be extracted properly."

    return get_answer(query, text)

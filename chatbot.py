from nlp_engine import get_answer

def chatbot_response(query):
    with open("data/website_text.txt", "r", encoding="utf-8") as f:
        text = f.read()

    return get_answer(query, text)
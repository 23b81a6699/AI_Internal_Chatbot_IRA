from nlp_engine import get_answer


def chatbot_response(query: str, website_text: str) -> str:
    return get_answer(query, website_text)

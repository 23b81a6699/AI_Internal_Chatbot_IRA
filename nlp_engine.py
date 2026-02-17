from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_answer(user_query: str, website_text: str) -> str:
    if not website_text.strip():
        return "I could not find website data yet. Please process the college website first."

    chunks = [chunk.strip() for chunk in website_text.replace("\n", ". ").split(".") if chunk.strip()]
    if not chunks:
        return "No relevant information found in the indexed website pages."

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(chunks + [user_query])

    similarities = cosine_similarity(vectors[-1], vectors[:-1])[0]
    best_idx = int(similarities.argmax())
    best_score = float(similarities[best_idx])

    if best_score < 0.05:
        return (
            "I could not find an exact match from the indexed website pages. "
            "Please ask a more specific question (for example: fees, timetable, admissions, hostel, exams)."
        )

    return chunks[best_idx]

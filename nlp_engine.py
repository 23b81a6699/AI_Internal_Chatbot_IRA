from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_answer(user_query, website_text):
    sentences = website_text.split(".")
    sentences = [s.strip() for s in sentences if s.strip()]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(sentences + [user_query])

    similarity = cosine_similarity(vectors[-1], vectors[:-1])
    best_match = similarity.argmax()

    return sentences[best_match] if sentences else "No relevant information found."

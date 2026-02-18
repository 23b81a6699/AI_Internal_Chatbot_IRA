from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def get_answer(query, text):

    sentences = [s.strip() for s in text.split(".") if len(s.strip()) > 40]

    if not sentences:
        return "No sufficient information found."

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(sentences + [query])

    similarity = cosine_similarity(vectors[-1], vectors[:-1]).flatten()

    top_indices = similarity.argsort()[-3:][::-1]

    best_score = similarity[top_indices[0]]

    if best_score < 0.07:
        return "I could not find a clear answer on the website."

    answer = ". ".join([sentences[i] for i in top_indices])

    return answer

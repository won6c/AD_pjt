import random
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from library.models import Book

def get_recommendations(query=None):
    books = list(Book.objects.all())
    if not books:
        return [], None

    base_book = None
    if query:
        for book in books:
            if query.lower() in book.title.lower():
                base_book = book
                break
    if not base_book:
        base_book = random.choice(books)

    documents = [f"{book.keyword or ''} {book.description or ''}" for book in books]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)
    base_idx = books.index(base_book)
    sim_scores = cosine_similarity(tfidf_matrix[base_idx], tfidf_matrix).flatten()
    similar_indices = np.argsort(sim_scores)[::-1][1:6]
    recommended_books = [books[i] for i in similar_indices]

    return recommended_books, base_book
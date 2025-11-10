import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def get_recommendations(user_id, ratings, movies):
    user_ratings = ratings[ratings['userId'] == user_id]
    merged = pd.merge(user_ratings, movies, on='movieId')

    vectorizer = CountVectorizer()
    movie_matrix = vectorizer.fit_transform(movies['genres'])

    similarity = cosine_similarity(movie_matrix)
    sim_scores = similarity[user_ratings['movieId'].values[0]]

    movies['score'] = sim_scores
    recommended = movies.sort_values('score', ascending=False).head(10)

    return recommended[['title', 'genres']]

from utils.recommender import get_recommendations
import pandas as pd

if __name__ == "__main__":
    movies_df = pd.read_csv("data/movies.csv")
    ratings_df = pd.read_csv("data/ratings.csv")

    # Recommend movies for user_id = 1
    recommended = get_recommendations(user_id=1, ratings=ratings_df, movies=movies_df)
    print("Recommended Movies:")
    print(recommended)

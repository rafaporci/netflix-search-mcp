import pandas as pd

def find_movies(genres, country, year, k = 5):
    # Read the CSV file
    movies = pd.read_csv('./netflix_movies_detailed_up_to_2025.csv')

    # Filter by year
    filtered = movies[movies['release_year'] == year]

    # Filter by country (case-insensitive, substring match)
    if country:
        filtered = filtered[filtered['country'].str.contains(country, case=False, na=False)]

    # Filter by genres (all genres in the list must be present)
    if genres:
        for genre in genres:
            filtered = filtered[filtered['genres'].str.contains(genre, case=False, na=False)]

    # Sort by rating (descending)
    filtered = filtered.sort_values(by='rating', ascending=False)

    # Return top k movies as a DataFrame
    return filtered.head(k)
    
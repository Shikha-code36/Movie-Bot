import pandas as pd

df = pd.read_csv('data/movie_prep.csv')
df['MovieDetails'] = df.apply(lambda x: f"{x['title']}\nDate: {x['release_date']}\nRating: {x['vote_average']}\nPlot: {x['overview']}", axis=1)

def get_movie_details(movie_name):
    # Search for the movie by its title in the DataFrame
    movie = df[df['title'].str.lower() == movie_name.lower()]

    if movie.empty:
        return "Sorry, I couldn't find any information about that movie."

    # Extract movie details from the 'MovieDetails' column directly
    movie_details = movie['MovieDetails'].values[0]

    return movie_details

def get_movies_by_genre(genre):
    # Search for movies in the specified genre in the DataFrame
    movies = df[df['genres'].str.contains(genre, case=False, na=False)].sort_values(by='vote_average', ascending=False)['MovieDetails']

    if movies.empty:
        return "Sorry, I couldn't find any movies in that genre."

    # Join movie details with a newline character to separate movies on different lines
    movie_list = movies.str.cat(sep='\n\n')
    return movie_list

def get_movies_by_mood(mood):
    # Create a dictionary of moods mapped to genres (you can customize this dictionary based on your preference)
    mood_genre_mapping = {
        "happy": "Comedy",
        "sad": "Drama",
        "action": "Action",
        "adventure": "Adventure",
        "boring": "Thriller"
    }

    if mood.lower() in mood_genre_mapping:
        genre = mood_genre_mapping[mood.lower()]
        return get_movies_by_genre(genre)
    else:
        return "Sorry, I'm not sure which genre to recommend for that mood."
    
def get_top_rated_movies():
    # Filter movies with ratings from 10 to 6.5
    top_rated_movies = df[(df['vote_average'] >= 6.5) & (df['vote_average'] <= 10)].sort_values(by='vote_average', ascending=False)['MovieDetails']

    if top_rated_movies.empty:
        return "Sorry, no top-rated movies found."

    # Join movie details with a newline character to separate movies on different lines
    movie_list = top_rated_movies.str.cat(sep='\n\n')
    return movie_list


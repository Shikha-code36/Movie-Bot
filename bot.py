from flask import Flask, render_template, request
from movies import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form.get('user_input').strip().lower()
    selected_option = request.form.get('selected_option')

    if user_input == 'exit':
        response = "Goodbye!"
    elif selected_option == '1':  # Movie
        movie_name = user_input
        response = get_movie_details(movie_name)
    elif selected_option == '2':  # Genre
        genre = user_input
        response = get_movies_by_genre(genre)
    elif selected_option == '3': # Mood
        mood = user_input
        response = get_movies_by_mood(mood)
    else:
        user_input = "Top Rated Movies"
        response = get_top_rated_movies()

    return render_template('index.html', response=response, selected_option=selected_option)

if __name__ == '__main__':
    app.run(debug=True)

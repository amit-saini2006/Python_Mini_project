"""
 Challenge:  Personal Movie Tracker with JSON

Create a Python CLI tool that lets users maintain their own personal movie database, like a mini IMDb.

Your program should:
1. Store all movie data in a `movies.json` file.
2. Each movie should have:
   - Title
   - Genre
   - Rating (out of 10)
3. Allow the user to:
   - Add a movie
   - View all movies
   - Search movies by title or genre
   - Exit the app

Bonus:
- Prevent duplicate titles from being added
- Format output in a clean table
- Use JSON for reading/writing structured data
"""

import json
import os

FILENANE = "movies.json"

def load_movies():
    if not os.path.exists(FILENANE):
        return []
    with open(FILENANE, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def save_movies(movies):
    with open(FILENANE, 'w', encoding='utf-8') as f:
        json.dump(movies, f, indent=2)

def add_movies(movies):
    title = input("Enter the movie name: ").strip().lower()

    if any(movie['title'].lower() == title for movie in movies):
        print("Movie already exist")
        return
    genre = input("Genre: ").strip().lower()
    try:
        rating = float(input("Enter rating(0-10): "))
        if not (0 <= rating <= 10):
            raise ValueError
    except ValueError:
        print("Please enter a valid number")

    movies.append({'title': title, 'genre': genre, 'rating': rating})
    save_movies(movies)
    print("Movie is added to your list")

def search_movie(movies):
    term = input("Enter the title or genre: ").strip().lower()

    results = [
        movie for movie in movies 
        if term in movie['title'].lower() or term in movie['genre'].lower()
    ]

    if not results:
        print("No matching result found")
        return

    print(f"\n{len(results)} result's found")
    
    print('-' * 30)
    for movie in results:
        print(f"{movie['title']} -- {movie['genre']} -- {movie['rating']}")
    print('-' * 30)

def view_all_movies(movies):
    if not movies:
        print("No movies in DB")
        return
    
    print("-" * 30)
    for movie in movies:
        print(f"{movie['title']} -- {movie['genre']} -- {movie['rating']}")
    print("-" * 30)


def run_movie_db():
    movies = load_movies()

    while True:
        print("\n MyMovieDB")
        print("1. Add Movie")
        print("2. View all movie")
        print("3. Search Movie")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        match choice:
            case '1':
                add_movies(movies)
            case '2':
                view_all_movies(movies)
            case '3':
                search_movie(movies)
            case '4':
                print("Thank you for visiting! ")
                break
            case _:
                print("Invalid number")
                continue


run_movie_db()
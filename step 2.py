import random

def get_random_movie(genre):
    """
    Returns a list of recommended movies based on user's preferred genre.
    :param genre: The movie genre chosen by the user.
    :return: A list of recommended movies for the genre
    """
    movies = {
        "action": ["Mad Mac: Fury Road", "John Wick", "Monkey Man", "Gladiator"],
        "comedy": ["Step Brothers", "Superbad", "The Hangover", "Neighbors"],
        "horror": ["The Conjuring", "Get Out", "A Quiet Place", "Birdbox"],
        "sci-fi": ["Inception", "The Matrix", "Interstellar"]
    }
    if genre.lower() in movies:
        return random.choice(movies[genre.lower()])
    else:
        return "Sorry we don't have recommendations for that genre."

def main():
    print("Welcome to the Movie Recommendation System!")
    genre = input("Enter your favorite movie genre: ").strip()

    movie = get_random_movie(genre)
    print(f"Here's a movie recommendation for you: {movie}")

if __name__ == "__main__":
    main()
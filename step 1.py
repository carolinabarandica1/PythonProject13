def get_movie_recommendations(genre):
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
    return movies.get(genre.lower(), [])

def main():
    print("Welcome to the Movie Recommendation System!")
    genre = input("Enter your favorite movie genre: ").strip()

    recommendations = get_movie_recommendations(genre)

    if recommendations:
        print(f"Here are some {genre.capitalize()} movie recommendations: {', '.join(recommendations)}")
    else:
        print("Sorry, we don't have recommendations for that genre.")

if __name__ == "__main__":
    main()
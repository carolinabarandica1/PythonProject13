movies = {

    "Terminator": {"director": "James Cameron", "genre": "Action"},
    "Mad Max: Fury Road": {"director": "George Miller", "genre": "Action"},
    "The Matrix": {"director": "Lana & Lilly Wachowski", "genre": "Action"},
    "The Dark Knight": {"director": "Christopher Nolan", "genre": "Action"},
    "The Lord of the Rings": {"director": "Peter Jackson", "genre": "Action"},
    "Top Gun": {"director": "Tony Scott", "genre": "Action"},
    "Mission: Impossible": {"director": "Brian De Palma", "genre": "Action"},
    "The Avengers": {"director": "Joss Whedon", "genre": "Action"},

    "Superbad": {"director": "Greg Mottola", "genre": "Comedy"},
    "Step Brothers": {"director": "Adam McKay", "genre": "Comedy"},
    "Dumb and Dumber": {"director": "Peter Farrelly", "genre": "Comedy"},
    "Anchorman": {"director": "Adam McKay", "genre": "Comedy"},
    "The Hangover": {"director": "Todd Phillips", "genre": "Comedy"},
    "Tropic Thunder": {"director": "Ben Stiller", "genre": "Comedy"},
    "Zoolander": {"director": "Ben Stiller", "genre": "Comedy"},
    "Ferris Bueller's Day Off": {"director": "John Hughes", "genre": "Comedy"}
}


user_ratings = {}


def get_movie_info(movie_name):
    """Returns movie details if found."""
    return movies.get(movie_name.strip().title())


def rank_movie(movie_name):
    """Allows the user to rank a movie from 1 to 10."""
    while True:
        try:
            rating = int(input(f"Rank '{movie_name}' from 1 to 10: "))
            if 1 <= rating <= 10:
                user_ratings[movie_name] = rating
                print(f"You ranked '{movie_name}' a {rating}/10!\n")
                break
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a numeric value between 1 and 10.")


def get_movies_by_genre():
    """Displays movies of a specific genre."""
    genre = input("Enter a genre (e.g., Action, Comedy): ").strip().title()
    genre_movies = [movie for movie, details in movies.items() if details['genre'] == genre]

    if genre_movies:
        print(f"\nMovies in {genre} genre:")
        for movie in genre_movies:
            print(f"- {movie}")
    else:
        print("No movies found for that genre.")


def show_all_movies():
    """Displays all available movies."""
    print("\nAvailable Movies:")
    for movie in movies:
        print(f"- {movie}")


def display_rankings():
    """Displays the user's ranked movies."""
    if user_ratings:
        print("\nYour Movie Rankings:")
        for movie, rating in user_ratings.items():
            print(f"{movie}: {rating}/10")
    else:
        print("\nNo movies were ranked.")


def main():
    """Main function to run the movie ranking system."""
    print("\nWelcome to the Movie Information System!")

    while True:
        print("\nMenu Options:")
        print("1. Search for a movie")
        print("2. Rank a movie")
        print("3. Show movies by genre")
        print("4. Show all movies")
        print("5. View my rankings")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            movie_name = input("\nEnter a movie name: ").strip()
            movie_info = get_movie_info(movie_name)
            if movie_info:
                print(f"\nMovie: {movie_name.title()}")
                print(f"Director: {movie_info['director']}")
                print(f"Genre: {movie_info['genre']}\n")
            else:
                print("Sorry, we don't have information on that movie.\n")

        elif choice == "2":
            movie_name = input("\nEnter a movie name to rank: ").strip()
            if movie_name in movies:
                rank_movie(movie_name)
            else:
                print("Movie not found in the database.")

        elif choice == "3":
            get_movies_by_genre()

        elif choice == "4":
            show_all_movies()

        elif choice == "5":
            display_rankings()

        elif choice == "6":
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option (1-6).")


if __name__ == "__main__":
    main()
import pandas as pd

file_path = '/Users/carolinabarandica/Downloads/IMDB Top 250 Movies.csv'
df = pd.read_csv(file_path)

print("Actual Column Names in CSV:", df.columns.tolist())

df.columns = df.columns.str.strip().str.lower()

df.rename(columns={"name": "title", "directors": "director"}, inplace=True)

required_columns = {'title', 'director', 'genre'}
missing_columns = required_columns - set(df.columns)

if missing_columns:
    print(f"Error: The following columns are missing in the CSV file: {missing_columns}")
    print("Please check the CSV file and update the script accordingly.")
    exit()

print("\nColumns have been successfully mapped!")

user_ratings = {}


def get_movie_info(movie_name):
    """Returns details about a movie."""
    movie_name = movie_name.strip().lower()
    movie = df[df['title'].str.lower() == movie_name]

    if not movie.empty:
        movie_info = movie.iloc[0]  # Get the first match
        print(f"\nMovie: {movie_info['title']}")
        print(f"Director: {movie_info['director']}")
        print(f"Genres: {movie_info['genre']}\n")
    else:
        print("Sorry, we don't have information on that movie.\n")


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
    """Displays movies that have at least one of the requested genres."""
    genre_input = input("Enter a genre (e.g., Action, Comedy) or multiple genres separated by commas: ").strip()
    genre_list = [genre.strip().title() for genre in genre_input.split(",")]

    matching_movies = df[df['genre'].str.contains('|'.join(genre_list), case=False, na=False)]

    if not matching_movies.empty:
        print(f"\nMovies that match at least one of the genres ({', '.join(genre_list)}):")
        for _, row in matching_movies.iterrows():
            print(f"- {row['title']} ({row['genre']})")
    else:
        print("No movies found for the given genre(s).")


def show_all_movies():
    """Displays all available movies."""
    print("\nAvailable Movies:")
    for _, row in df.iterrows():
        print(f"- {row['title']} ({row['genre']})")


def display_rankings():
    """Displays the user's ranked movies."""
    if user_ratings:
        print("\nYour Movie Rankings:")
        for movie, rating in user_ratings.items():
            print(f"{movie}: {rating}/10")
    else:
        print("\nNo movies were ranked.")


def main():
    """Main function to run the movie system."""
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
            get_movie_info(movie_name)

        elif choice == "2":
            movie_name = input("\nEnter a movie name to rank: ").strip()
            if movie_name in df['title'].values:
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
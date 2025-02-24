import requests
from bs4 import BeautifulSoup
import random


def scrape_letterboxd_movies(genre):
    """
    Scrapes Letterboxd for movie recommendations based on genre and returns a random movie.

    Parameters:
    genre (str): The movie genre chosen by the user.

    Returns:
    str: A randomly selected movie title or an error message if scraping fails.
    """
    url = f"https://letterboxd.com/films/genre/{genre.lower()}/"
    headers = {"User-Agent": "Mozilla/5.0"}  # Mimic a real browser request

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return "Failed to retrieve data. Please check the genre or your internet connection."

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract movie titles from the page
    movies = [tag["alt"] for tag in soup.find_all("img", class_="film-poster")]

    if not movies:
        return "No movies found for this genre. Try a different one."

    return random.choice(movies)  # Return a random movie


def main():
    print("Welcome to the Movie Recommendation System!")
    genre = input("Enter your favorite movie genre (e.g., action, comedy, horror, sci-fi): ").strip()

    print("\nFetching a movie recommendation from Letterboxd...")
    movie = scrape_letterboxd_movies(genre)

    print(f"Here's a random {genre.capitalize()} movie recommendation for you: {movie}")


if __name__ == "__main__":
    main()
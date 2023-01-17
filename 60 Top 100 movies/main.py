import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="jsx-4245974604")
#print(all_movies)

movie_title = [movie.getText() for movie in all_movies]
print(movie_title[::-1])

with open("movies.text", mode="w") as file:
    for movie in movie_title:
        file.write(f"{movie}\n")
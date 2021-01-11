import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlZGVhMmY5YzRmZWI4NjE1Mzg1ZTc0MmNlNGM2NTczNCIsInN1YiI6IjVmZWVmNmNlMmRkYTg5MDA0MGYxZWZjMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.jDODTh6PlIeTYrDKXypWn4BOSW4Mj2khyuqrQzu-lgE"

def get_popular_movies():
    url = "https://api.themoviedb.org/3/movie/popular"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(url, headers=headers)
    return response.json()

def get_poster_url(poster_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_path}"

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]



import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlZGVhMmY5YzRmZWI4NjE1Mzg1ZTc0MmNlNGM2NTczNCIsInN1YiI6IjVmZWVmNmNlMmRkYTg5MDA0MGYxZWZjMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.jDODTh6PlIeTYrDKXypWn4BOSW4Mj2khyuqrQzu-lgE"

def get_popular_movies():
    url = "https://api.themoviedb.org/3/movie/popular"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(url, headers=headers)
    return response.json()

def get_movies_list(list_type):
    url = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_poster_url(poster_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_path}"

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_single_movie(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(url, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(url, headers=headers)
    return response.json()

def get_movie_images(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(url, headers=headers)
    return response.json()

def get_lists_type():
    endpoint = f"https://api.themoviedb.org/3/list"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()

import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")

url = "https://api.themoviedb.org/3/movie/popular"

params = {
    "api_key": API_KEY,
    "language": "fr-FR",
    "page": 1
}

response = requests.get(url, params=params)

print(response.json())
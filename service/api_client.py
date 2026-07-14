import requests

import os
import requests
from dotenv import load_dotenv
from questionnaire import Questionnaire


load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = os.getenv("TMDB_BASE_URL")


def discover_movies(page):

    url = f"{BASE_URL}/discover/movie"

    params = {
        "api_key": API_KEY,
        "language": "fr-FR",
        "sort_by": "popularity.desc",
        "page": page
    }

    response = requests.get(url, params=params)

    response.raise_for_status()

    return response.json()


def get_movie_details(movie_id):

    url = f"{BASE_URL}/movie/{movie_id}"

    params = {
        "api_key": API_KEY,
        "language": "fr-FR"
    }

    response = requests.get(url, params=params)

    response.raise_for_status()

    return response.json()
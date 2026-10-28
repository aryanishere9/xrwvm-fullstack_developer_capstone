import os
from urllib.parse import quote

import requests
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    """Send a GET request to the Node/Express backend."""
    request_url = backend_url.rstrip('/') + endpoint
    print(f"GET from {request_url} with params {kwargs}")
    try:
        response = requests.get(request_url, params=kwargs, timeout=15)
        return response.json()
    except Exception as err:
        print(f"Network exception occurred: {err}")
        return None


def analyze_review_sentiments(text):
    """Ask the sentiment microservice whether a review is +ve/-ve/neutral."""
    request_url = sentiment_analyzer_url.rstrip('/') + "/analyze/" + quote(
        text)
    try:
        response = requests.get(request_url, timeout=15)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return {"sentiment": "neutral"}


def post_review(data_dict):
    """Send a new review to the Node/Express backend."""
    request_url = backend_url.rstrip('/') + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict, timeout=15)
        print(response.json())
        return response.json()
    except Exception as err:
        print(f"Network exception occurred: {err}")
        return None

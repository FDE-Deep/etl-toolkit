import json
import os

import requests
from dotenv import load_dotenv

from config.index import TIMEOUT

load_dotenv()


def getHeaders():
    headers = {}
    if os.getenv("AUTHORIZATION_TOKEN"):
        headers["Authorization"] = f"token {os.getenv("AUTHORIZATION_TOKEN")}"
    return headers


def getRequest(url, headers):
    response = requests.get(url, headers=headers, timeout=TIMEOUT)
    response.raise_for_status()
    return response.json()


def save_to_json(data, filepath):
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

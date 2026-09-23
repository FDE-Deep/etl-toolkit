import json
import os

import requests
from dotenv import load_dotenv

from config import TIMEOUT
from constants import RETRYABLE_STATUS_CODE
from exceptions import RetryableError

load_dotenv()


def get_headers():
    headers = {}
    if os.getenv("AUTHORIZATION_TOKEN"):
        headers["Authorization"] = f"token {os.getenv("AUTHORIZATION_TOKEN")}"
    return headers


def get_json(url, headers):
    response = requests.get(url, headers=headers, timeout=TIMEOUT)
    if response.status_code in RETRYABLE_STATUS_CODE:
        raise RetryableError("Transient Error : Retrying")
    response.raise_for_status()
    return response.json()


def save_to_json(data, filepath):
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

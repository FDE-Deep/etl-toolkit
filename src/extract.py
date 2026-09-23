from pathlib import Path

import requests

from config import GITHUB_BASE_URL
from decorators import retry
from utils import get_headers, get_request, save_to_json
from exceptions import RetryableError


@retry(
    attempts=3,
    exceptions=(
        RetryableError,
        requests.exceptions.ConnectTimeout,
        requests.exceptions.Timeout,
    ),
)
def get_json(user):
    url = f"{GITHUB_BASE_URL}/users/{user}/repos"
    headers = get_headers()
    data = get_request(url, headers)
    return data


def save_raw_data(data, user):
    filepath = Path(f"raw/repos/{user}.json")
    filepath.parent.mkdir(parents=True, exist_ok=True)
    save_to_json(data, filepath)

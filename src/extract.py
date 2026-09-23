from pathlib import Path

from config import GITHUB_BASE_URL
from constants import RETRYABLE_EXCEPTIONS
from decorators import retry
from utils import get_headers, get_json, save_to_json


@retry(
    attempts=3,
    exceptions=RETRYABLE_EXCEPTIONS,
)
def fetch_user(user):
    url = f"{GITHUB_BASE_URL}/users/{user}/repos"
    headers = get_headers()
    data = get_json(url, headers)
    return data


def save_raw_data(data, user):
    filepath = Path(f"raw/repos/{user}.json")
    filepath.parent.mkdir(parents=True, exist_ok=True)
    save_to_json(data, filepath)

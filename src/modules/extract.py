from pathlib import Path

import requests

from config.index import GITHUB_BASE_URL
from decorators.index import retry
from util.index import getHeaders, getRequest, save_to_json


@retry(attempts=3, exceptions=(requests.HTTPError, requests.Timeout))
def fetchRepos(user):
    url = f"{GITHUB_BASE_URL}/users/{user}/repos"
    headers = getHeaders()
    data = getRequest(url, headers)
    return data


def saveReposForUser(data, user):
    for repo in data:
        filepath = Path(f"raw/repos/{user}/{repo['name']}.json")
        filepath.parent.mkdir(parents=True, exist_ok=True)
        save_to_json(repo, filepath)

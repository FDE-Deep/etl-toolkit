import requests

from exceptions import RetryableError
from extract import fetch_user, save_raw_data


def main():
    try:
        user = "torvalds"
        data = fetch_user(user)
        save_raw_data(data, user)
    except (requests.exceptions.RequestException, RetryableError) as e:
        print(e)


if __name__ == "__main__":
    main()

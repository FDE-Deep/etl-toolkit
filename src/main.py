from constants import RETRYABLE_EXCEPTIONS
from extract import fetch_user, save_raw_data


def main():
    try:
        user = "torvalds"
        data = fetch_user(user)
        save_raw_data(data, user)
    except RETRYABLE_EXCEPTIONS as e:
        print(e)


if __name__ == "__main__":
    main()

import requests

from extract import get_json, save_raw_data


def main():
    user = "torvalds"
    data = get_json(user)
    save_raw_data(data, user)


if __name__ == "__main__":
    main()

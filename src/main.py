from modules.extract import fetchRepos, saveReposForUser


def main():
    try:
        user = "torvalds"
        data = fetchRepos(user)
        saveReposForUser(data, user)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

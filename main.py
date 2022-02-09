from core.reading import reader_factory
from core.modules.loaded_data import data
from core.modules.account import account_managment
import config


def main():
    reader_factory.JsonReader.load_songs(config.settings["songs_path"])
    reader_factory.JsonReader.load_users(config.settings["users_path"])
    account_managment.login("Ron", "1222222")
    account_managment.create_playlist("NO")
    tracks = []
    count = 0
    for k, v in data.Data.tracks.items():
        tracks.append(v)
        count += 1
        if count == 5:
            break

    account_managment.add_to_playlist("NO", tracks)
    account_managment.create_playlist("ABC")

    # data.test()


if __name__ == "__main__":
    main()

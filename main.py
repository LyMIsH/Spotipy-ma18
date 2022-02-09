from core.reading import reader_factory
from core.modules.loaded_data import data
import config


def main():
    reader_factory.JsonReader.load_songs(config.settings["songs_path"])
    reader_factory.JsonReader.load_users(config.settings["users_path"])
    # data.test()


if __name__ == "__main__":
    main()

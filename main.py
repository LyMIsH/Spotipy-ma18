import threading
from core.reading import reader_factory
import config
from core.uifunctionality import restfunctions, menu


def main():
    menu.start()


if __name__ == "__main__":
    reader_factory.JsonReader.load_songs(config.settings["songs_path"])
    reader_factory.JsonReader.load_users(config.settings["users_path"])
    threading.Thread(target=restfunctions.start).start()
    main()

import threading
from core.datahandling.loader import load_songs
from core.uifunctionality import restfunctions, menu


def main():
    menu.start()


if __name__ == "__main__":
    load_songs()
    threading.Thread(target=restfunctions.start).start()
    main()

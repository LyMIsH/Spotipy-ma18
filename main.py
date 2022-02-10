import threading
from core.datahandling.loader import load_songs
import config
from core.uifunctionality import restfunctions, menu
from core.account import account_managment


def main():
    # account_managment.signup("Ran", "111")
    menu.start()


if __name__ == "__main__":
    load_songs()
    threading.Thread(target=restfunctions.start).start()
    main()

from core.exceptions import exceptions
from core.datahandling.data import Data
from core.logging import logger
from core.datahandling import search


class AccountsData:
    logged_users = dict()


def is_artist(username):
    for artist in list(Data.artists.values()):
        if artist.name == username:
            return True

    return False


def login(username, password):
    if username in Data.users.keys():
        AccountsData.logged_users[username] = Data.users[username]
        if is_artist(username):
            Data.users[username].is_premium = True

        logger.info(f"User {username} logged in")
    else:
        raise exceptions.UsernameDoesNotExist(f"Cannot find user '{username}'")

    return Data.users[username]

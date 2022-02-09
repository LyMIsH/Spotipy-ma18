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
        logger.info(f"User {username} logged in")
        if Data.users[username].type == "Premium" or is_artist(username):
            search.premium = True
            logger.warning(f"Set user - {username} search type to premium")
    else:
        raise exceptions.UsernameDoesNotExist(f"Cannot find user '{username}'")

    return Data.users[username]

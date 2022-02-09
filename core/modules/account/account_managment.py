from core.exceptions import exceptions
from ..loaded_data.data import Data
from core.logging import logger

class AccountsData:
    logged_users = dict()


def add_to_playlist(playlist):
    if __name__ not in AccountsData.logged_users.keys():
        raise exceptions.UserNotLoggedInException(f"No user currently logged from '{__name__}'")


def login(username, password):
    if username in Data.users.keys():
        AccountsData.logged_users[__name__] = Data.users[username]
        logger.info(f"User {username} logged in")
    else:
        logger.error(f"Cannot find user '{username}'")
        raise exceptions.UsernameDoesNotExist(f"Cannot find user '{username}'")

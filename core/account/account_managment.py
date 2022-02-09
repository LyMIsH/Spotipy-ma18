from core.exceptions import exceptions
from core.datahandling.data import Data
from core.logging import logger


class AccountsData:
    logged_users = dict()


def login(username, password):
    if username in Data.users.keys():
        AccountsData.logged_users[username] = Data.users[username]
        logger.info(f"User {username} logged in")
    else:
        logger.error(f"Cannot find user '{username}'")
        raise exceptions.UsernameDoesNotExist(f"Cannot find user '{username}'")

    return Data.users[username]

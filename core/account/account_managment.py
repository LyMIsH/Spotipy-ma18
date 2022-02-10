from core.exceptions import exceptions
from core.datahandling.data import Data
from core.account.user import User
from core.logging import logger
from core.datahandling.data import load_user_data, save_user_data, Data


def is_artist(username):
    for artist in list(Data.artists.values()):
        if artist.name == username:
            return True

    return False


def login(username, password):
    user = load_user_data(username)
    if password != user.password:
        raise exceptions.IncorrectCredentialsError("Username or password incorrect")
    if is_artist(username):
        Data.users[username].is_premium = True
        logger.info(f"User {username} logged in")

    return user


# def signup(username, password):
#     save_user_credentials(User(username, password, False))

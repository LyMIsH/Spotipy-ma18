from core.exceptions import exceptions
from core.account.user import User
from core.logging import logger
from core.datahandling.data import load_user_data, save_user_data, Data, does_user_exists


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
        user.is_premium = True
        logger.info(f"User {username} logged in")

    return user


def signup(username, password):
    if does_user_exists(username):
        msg = f"User '{username}' already exists"
        logger.exception(msg)
        raise exceptions.SignupError(msg)

    save_user_data(User(username, password, False))
    logger.info(f"New user signup - {username}")

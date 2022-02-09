from core.exceptions import exceptions
from ..data_handling.data import Data
from core.logging import logger
from core.modules.base.playlist import Playlist


class AccountsData:
    logged_users = dict()


def add_to_playlist(playlist_name, tracks):
    user = AccountsData.logged_users[__name__]
    if __name__ not in AccountsData.logged_users.keys():
        raise exceptions.UserNotLoggedInException(f"No user currently logged from '{__name__}'")

    if playlist_name not in user.playlists.keys():
        raise exceptions.PlaylistDoesNotExists(f'{playlist_name}')
    else:
        user.playlists[playlist_name].add_tracks(tracks)
    logger.info(f"Added track {[track.name for track in tracks]} to {playlist_name}")


def create_playlist(playlist_name):
    user = AccountsData.logged_users[__name__]
    if __name__ not in AccountsData.logged_users.keys():
        raise exceptions.UserNotLoggedInException(f"No user currently logged from '{__name__}'")
    if playlist_name in user.playlists.keys():
        raise exceptions.PlaylistAlreadyExists(f"{playlist_name}")

    playlist = Playlist(playlist_name)
    user.add_playlist(playlist)
    logger.info(f"Added playlist {playlist_name}")


def login(username, password):
    if username in Data.users.keys():
        AccountsData.logged_users[__name__] = Data.users[username]
        logger.info(f"User {username} logged in")
    else:
        logger.error(f"Cannot find user '{username}'")
        raise exceptions.UsernameDoesNotExist(f"Cannot find user '{username}'")

from core.modules.base.album import Album
from core.modules.base.track import Track
import config
import os
from pathlib import Path
import pickle
from core.logging import logger
from core.exceptions import exceptions


class Data:
    artists = dict()
    tracks = dict()
    albums = dict()
    users = dict()


def add_track_data(album: Album, track: Track, artist_list: list):
    # Album adding
    if album.id() not in Data.albums.keys():
        Data.albums[album.id()] = album
    Data.albums[album.id()].add_song(track)

    # Track adding
    Data.tracks[track.id()] = track

    # Artists adding
    for artist in artist_list:
        if artist.id() not in Data.artists.keys():
            Data.artists[artist.id()] = artist
        Data.artists[artist.id()].add_album(album)


def load_user_data(username):
    user_data = Path(os.path.join(config.settings["users_data_path"], username))
    if user_data.exists():
        with open(os.path.join(config.settings["users_data_path"], username), "rb") as file:
            Data.users[username] = pickle.load(file)
            logger.info(f"Loaded user {username} from pickle")
            return Data.users[username]
    else:
        raise exceptions.UsernameDoesNotExist(f"User {username} not found")


def save_user_data(user):
    with open(os.path.join(config.settings["users_data_path"], user.username), "wb") as file:
        pickle.dump(user, file)
        logger.info(f"Wrote user {user.username} to pickle")

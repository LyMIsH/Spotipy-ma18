from core.modules.base.album import Album
from core.modules.base.track import Track
import config
import os
from pathlib import Path
import pickle
from core.logging import logger



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


def add_user_data(user):
    user_data = Path(os.path.join(config.settings["users_data_path"], user.username))
    if user_data.exists():
        with open(os.path.join(config.settings["users_data_path"], user.username), "rb") as file:
            Data.users[user.username] = pickle.load(file)
            logger.info(f"Loaded user {user.username} from pickle")
    else:
        Data.users[user.username] = user
        logger.info(f"Loaded user {user.username}")


def save_user_data(user):
    with open(os.path.join(config.settings["users_data_path"], user.username), "wb") as file:
        pickle.dump(user, file)
        logger.info(f"Wrote user {user.username} to pickle")

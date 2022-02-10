from core.modules.base.album import Album
from core.modules.base.artist import Artist
from core.modules.base.track import Track
from core.datahandling import data
from core.account.user import User
from ..logging import logger


def parse_track_json(track):
    artists = list()

    for artist in track.artists:
        artists.append(Artist(artist.id, artist.name))

    album = Album(track.album.id, track.album.name)
    track = Track(track.id, track.name, track.popularity)
    data.add_track_data(album, track, artists)
    logger.debug(f"Loaded track {track.name}")


def parse_users_json(users):
    for user in users:
        data.add_user_data(User(user.username, user.password, user.premium))
        logger.debug(f"Loaded user {user.username}")



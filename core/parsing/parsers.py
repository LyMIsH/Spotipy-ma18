from core.modules.base.album import Album
from core.modules.base.artist import Artist
from core.modules.base.track import Track
from core.datahandling import data
from ..logging import logger


def parse_track_json(track):
    artists = list()

    for artist in track.artists:
        if hasattr(artist, 'genre'):
            artists.append(Artist(artist.id, artist.name, artist.genre))
        else:
            artists.append(Artist(artist.id, artist.name))

    album = Album(track.album.id, track.album.name)
    track = Track(track.id, track.name, track.popularity)
    data.add_track_data(album, track, artists)
    logger.debug(f"Loaded track {track.name}")

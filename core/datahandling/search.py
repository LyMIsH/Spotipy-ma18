from .data import Data
from core.exceptions import exceptions


def get_artists():
    return list(Data.artists.values())


def get_albums(artist_id):
    if artist_id not in Data.artists.keys():
        raise exceptions.IDNotFound(f"No artist match for {artist_id}")
    artist = Data.artists[artist_id]
    return [album.name for album in artist.albums.values()]


def get_top_artist_tracks(artist_id):
    if artist_id not in Data.artists.keys():
        raise exceptions.IDNotFound(f"No artist match for {artist_id}")
    artist = Data.artists[artist_id]
    albums = list(artist.albums.values())
    tracks = []
    for album in albums:
        tracks.extend(list(album.tracks.values()))
    tracks.sort(key=lambda track: track.popularity, reverse=True)

    return tracks


def get_album_tracks(album_id):
    if album_id not in Data.albums.keys():
        raise exceptions.IDNotFound(f"No album match for {album_id}")
    return list(Data.albums[album_id].tracks.values())

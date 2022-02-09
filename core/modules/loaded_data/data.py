from core.modules.artist import Artist
from core.modules.album import Album
from core.modules.track import Track


class Data:
    artists = dict()
    tracks = dict()
    albums = dict()


def add_artists(artist_list: list):
    for artist in artist_list:
        if artist.__id not in Data.artists.keys():
            Data.artists[artist.__id] = Artist(artist.__id, artist.name)
        else:
            Data.artists[artist.__id].add_album(artist.)


def add_data(album: Album, track: Track, artist_list: list):
    # Album adding
    if album.__id not in Data.albums.keys():
        Data.albums[album.__id] = album

    Data.albums[album.__id].add_song(track.id)

    # Track adding
    Data.tracks[track.__id] = track

    # Artists adding
    for artist in artist_list:
        if artist.__id not in Data.artists.keys():
            Data.artists[artist.__id] = artist
        else:
            Data.artists[artist.__id].add_album(artist.)


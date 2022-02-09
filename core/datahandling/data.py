from core.modules.base.album import Album
from core.modules.base.track import Track


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
    Data.users[user.username] = user

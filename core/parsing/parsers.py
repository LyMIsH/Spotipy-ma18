from core.modules.album import Album
from core.modules.artist import Artist
from core.modules.track import Track


def parse_track_json(track):
    artists = list()
    album = Album(track.album.id, track.album.name)

    for artist in track.artists:
        artist_object = Artist(artist.id, artist.name)
        artist_object.add_album(album)
        artists.append(artist_object)

    track = Track(track.id, track.name, track.popularity)
    album.add_song(track)
    return track, artists, album

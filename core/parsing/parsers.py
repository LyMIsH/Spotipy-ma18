from core.modules.album import Album
from core.modules.artist import Artist
from core.modules.track import Track
from core.modules.loaded_data import data


def parse_track_json(track):
    artists = list()

    for artist in track.artists:
        artists.append(Artist(artist.id, artist.name))

    album = Album(track.album.id, track.album.name)
    track = Track(track.id, track.name, track.popularity)
    data.add_data(album, track, artists)




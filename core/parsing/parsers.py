from core.modules.album import Album
from core.modules.artist import Artist
from core.modules.track import Track
from core.modules.loaded_data import data


def parse_track_json(track):
    artists = data.artists
    albums = data.albums
    tracks = data.tracks

    album = Album(track.album.id, track.album.name)

    for artist in track.artists:
        artist_object = Artist(artist.id, artist.name)
        artist_object.add_album(album)
        artists.append(artist_object)

    track = Track(track.id, track.name, track.popularity)
    album.add_song(track)
    data.artists.extend(artists)
    data.albums.append(album)
    data.tracks.append(track)
    print(data.tracks, data.albums, data.artists)




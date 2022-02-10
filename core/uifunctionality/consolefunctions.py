from core.account import account_managment
from core.datahandling import data, search


def login_console():
    username = input("username: ")
    password = input("password: ")

    return account_managment.login(username, password)


def signup_console():
    username = input("username: ")
    password = input("password: ")

    return account_managment.signup(username, password)


def create_playlist_console(user):
    name = input("Name: ")
    user.create_playlist(name)
    _ = 0


def get_top_tracks_console(user):
    artist_id = input("Enter artist ID: ")
    # Adding check before exception because console menu cannot handle exceptions
    if artist_id not in data.Data.artists.keys():
        print(f"ID {artist_id} not found")
        return

    print(search.get_top_artist_tracks(artist_id, premium=user.is_premium))


def get_artist_albums_console(user):
    artist_id = input("Enter artist ID: ")
    # Adding check before exception because console menu cannot handle exceptions
    if artist_id not in data.Data.artists.keys():
        print(f"ID {artist_id} not found")
        return

    print(search.get_albums(artist_id, premium=user.is_premium))


def get_album_tracks_console(user):
    album_id = input("Enter album ID: ")
    # Adding check before exception because console menu cannot handle exceptions
    if album_id not in data.Data.albums.keys():
        print(f"ID {album_id} not found")
        return

    print(search.get_album_tracks(album_id, premium=user.is_premium))


def add_track_console(user):
    playlist_name = input("Playlist name: ")
    track_id = input("Enter track id, 0 to stop: ")
    tracks = []

    while track_id != '0':
        if track_id not in data.Data.tracks.keys():
            print(f"Track not found ID: {track_id}")
        else:
            tracks.append(data.Data.tracks[track_id])
        track_id = input("Enter track id, 0 to stop: ")

    if len(tracks) != 0:
        user.add_to_playlist(playlist_name, tracks)

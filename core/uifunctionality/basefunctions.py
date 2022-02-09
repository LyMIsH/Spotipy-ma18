from core.account import account_managment
from core.datahandling import data


def login_console():
    username = input("username: ")
    password = input("password: ")

    return account_managment.login(username, password)


def create_playlist_console(user):
    name = input("Name: ")
    user.create_playlist(name)
    _ = 0


def add_track_console(user):
    playlist_name = input("Playlist name: ")
    track_id = input("Enter track id, 0 to stop: ")
    tracks = []

    while track_id != '0':
        tracks.append(data.Data.tracks[track_id])
        track_id = input("Enter track id, 0 to stop: ")

    user.add_to_playlist(playlist_name, tracks)

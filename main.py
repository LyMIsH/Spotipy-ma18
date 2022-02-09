from core.reading import reader_factory
from core.datahandling import data
from core.account import account_managment
import config
from core.datahandling import search
from consolemenu import *
from consolemenu.items import *
from core.uifunctionality import basefunctions


def main():
    login_menu = ConsoleMenu("Spotipy", "Login menu")
    main_menu = ConsoleMenu("Spotipy", "Main menu")
    login_option = FunctionItem("Login", basefunctions.login_console, should_exit=True)
    login_menu.append_item(login_option)
    login_menu.show()
    user = login_option.return_value
    create_playlist_option = FunctionItem("Create playlist", basefunctions.create_playlist_console, [user])
    add_track_option = FunctionItem("Add track to playlist", basefunctions.add_track_console, [user])
    main_menu.append_item(create_playlist_option)
    main_menu.append_item(add_track_option)
    main_menu.show()

    tracks = []
    count = 0
    for k, v in data.Data.tracks.items():
        tracks.append(v)
        count += 1
        if count == 18:
            break

    user.add_to_playlist("NO", tracks)
    user.create_playlist("ABC")
    user.create_playlist("sdasdasd")
    user.create_playlist("dasda")
    user.create_playlist("asdasda")
    user.add_to_playlist("ABC", tracks)

    artists = search.get_artists()
    albums = search.get_albums(artists[1].id())
    top_tracks = search.get_top_artist_tracks(artists[1].id())
    album_tracks = search.get_album_tracks("2usyeZYdUHKlNHKDKgAYSo")

    _ = 0
   # data.test()


if __name__ == "__main__":
    reader_factory.JsonReader.load_songs(config.settings["songs_path"])
    reader_factory.JsonReader.load_users(config.settings["users_path"])
    main()

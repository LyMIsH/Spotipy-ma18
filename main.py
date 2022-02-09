from core.reading import reader_factory
from core.datahandling import data
from core.account import account_managment
import config
from core.datahandling import search
from consolemenu import *
from consolemenu.items import *
from core.uifunctionality import uifunctions


def main():
    login_menu = ConsoleMenu("Spotipy", "Login menu")
    main_menu = ConsoleMenu("Spotipy", "Main menu")
    login_option = FunctionItem("Login", uifunctions.login_console, should_exit=True)
    login_menu.append_item(login_option)
    login_menu.show()
    user = login_option.return_value
    create_playlist_option = FunctionItem("Create playlist", uifunctions.create_playlist_console, [user])
    add_track_option = FunctionItem("Add track to playlist", uifunctions.add_track_console, [user])
    get_artists_option = FunctionItem("Get artists", print, search.get_artists())
    get_albums_option = FunctionItem("Get album by artist ID", uifunctions.get_artist_albums_console)
    get_album_tracks_option = FunctionItem("Get album tracks by ID", uifunctions.get_album_tracks_console)
    get_top_tracks_option = FunctionItem("Get top 10 tracks by author ID", uifunctions.get_top_tracks_console)
    main_menu.append_item(create_playlist_option)
    main_menu.append_item(add_track_option)
    main_menu.append_item(get_artists_option)
    main_menu.append_item(get_albums_option)
    main_menu.append_item(get_album_tracks_option)
    main_menu.append_item(get_top_tracks_option)
    main_menu.show()


if __name__ == "__main__":
    reader_factory.JsonReader.load_songs(config.settings["songs_path"])
    reader_factory.JsonReader.load_users(config.settings["users_path"])
    main()

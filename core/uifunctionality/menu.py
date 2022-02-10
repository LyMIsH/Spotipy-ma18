from consolemenu import *
from consolemenu.items import *
from core.uifunctionality import consolefunctions
from core.datahandling import search


def start():
    login_menu = ConsoleMenu("Spotipy", "Login menu")
    main_menu = ConsoleMenu("Spotipy", "Main menu")
    login_option = FunctionItem("Login", consolefunctions.login_console, should_exit=True)
    signup_option = FunctionItem("Sign up", consolefunctions.signup_console)
    login_menu.append_item(login_option)
    login_menu.append_item(signup_option)
    login_menu.show()
    user = login_option.return_value
    create_playlist_option = FunctionItem("Create playlist", consolefunctions.create_playlist_console, [user])
    add_track_option = FunctionItem("Add track to playlist", consolefunctions.add_track_console, [user])
    get_artists_option = FunctionItem("Get artists", print, search.get_artists(premium=user.is_premium))
    get_albums_option = FunctionItem("Get album by artist ID", consolefunctions.get_artist_albums_console, [user])
    get_album_tracks_option = FunctionItem("Get album tracks by ID", consolefunctions.get_album_tracks_console, [user])
    get_top_tracks_option = FunctionItem("Get top 10 tracks by artist ID", consolefunctions.get_top_tracks_console,
                                         [user])
    get_top_genre_tracks_option = FunctionItem("Get top 10 tracks by genre", consolefunctions.get_top_genre_tracks_console,
                                         [user])
    main_menu.append_item(create_playlist_option)
    main_menu.append_item(add_track_option)
    main_menu.append_item(get_artists_option)
    main_menu.append_item(get_albums_option)
    main_menu.append_item(get_album_tracks_option)
    main_menu.append_item(get_top_tracks_option)
    main_menu.append_item(get_top_genre_tracks_option)
    main_menu.show()
from core.exceptions import exceptions
from core.logging import logger
from core.modules.base.playlist import Playlist
from core.datahandling.data import save_user_data


class User:
    def __init__(self, username, password, premium):
        self.username = username
        self.password = password
        self.is_premium = premium
        self.playlists = dict()

    def add_playlist(self, playlist):
        self.playlists[playlist.name] = playlist
        save_user_data(self)

    def add_to_playlist(self, playlist_name, tracks):
        if playlist_name not in self.playlists.keys():
            raise exceptions.PlaylistDoesNotExists(f'{playlist_name}')
        if len(self.playlists[playlist_name].tracks) + len(tracks) > 20 and not self.is_premium:
            raise exceptions.FreeUserException(
                f"User {self.username} is free and cannot have more than 20 tracks in playlist")
        else:
            self.playlists[playlist_name].add_tracks(tracks)
            save_user_data(self)
        logger.info(f"Added tracks {[track.name for track in tracks]} to {playlist_name}")

    def create_playlist(self, playlist_name):
        if playlist_name in self.playlists.keys():
            raise exceptions.PlaylistAlreadyExists(f"{playlist_name}")
        if len(self.playlists) == 5 and not self.is_premium:
            raise exceptions.FreeUserException(f"User {self.username} is free and cannot have more than 5 playlists")

        playlist = Playlist(playlist_name)
        self.add_playlist(playlist)
        logger.info(f"Added playlist {playlist_name}")
class User:
    def __init__(self, username, password, account_type):
        self.username = username
        self.password = password
        self.type = account_type
        self.playlists = dict()

    def add_playlist(self, playlist):
        self.playlists[playlist.name] = playlist

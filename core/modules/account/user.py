class User:
    def __init__(self, username, password, account_type):
        self.username = username
        self.password = password
        self.type = account_type
        self.playlists = set()

    def add_playlist(self, name, tracks):
        pass

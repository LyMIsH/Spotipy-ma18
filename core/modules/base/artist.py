import json


class Artist:
    def __init__(self, id, name, genre=None):
        self.__id = id
        self.name = name
        self.albums = dict()
        self.genre = genre

    def add_album(self, album):
        self.albums[album.id()] = album

    def id(self):
        return self.__id

    def __repr__(self):
        return json.dumps(self, default=lambda o: list(o) if isinstance(o, set) else o.__dict__,
                          sort_keys=True, indent=4)

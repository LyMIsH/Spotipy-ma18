import json


class Artist:
    def __init__(self, id, name):
        self.__id = id
        self.name = name
        self.albums = dict()

    def add_album(self, album):
        self.albums[album.id()] = album

    def id(self):
        return self.__id

    def __repr__(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

class Artist:
    def __init__(self, id, name):
        self.__id = id
        self.name = name
        self.albums = dict()

    def add_album(self, album):
        self.albums[album.id()] = album

    def id(self):
        return self.__id

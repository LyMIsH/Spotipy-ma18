class Artist:
    def __init__(self, id, name):
        self.__id = id
        self.name = name
        self.__albums = dict()

    def add_album(self, album):
        self.__albums[album.id()] = album

    def id(self):
        return self.__id

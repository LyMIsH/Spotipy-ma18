class Artist:
    def __init__(self, id, name):
        self.__id = id
        self.name = name
        self.__albums = list()

    def add_album(self, album):
        self.__albums.append(album)

class Artist:
    def __init__(self, id, name):
        self.__id = id
        self.name = name
        self.__albums = set()

    def add_album(self, album_id):
        self.__albums.add(album_id)

    def id(self):
        return self.__id

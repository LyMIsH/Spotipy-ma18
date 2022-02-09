class Album:
    def __init__(self, id, name):
        self.__id = id
        self.name = name
        self.__tracks = dict()

    def add_song(self, track):
        self.__tracks[track.id()] = track

    def id(self):
        return self.__id

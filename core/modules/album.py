class Album:
    def __init__(self, id, name):
        self.__id = id
        self.name = name
        self.__tracks = set()

    def add_song(self, track_id):
        self.__tracks.add(track_id)

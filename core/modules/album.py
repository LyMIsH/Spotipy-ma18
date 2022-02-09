class Album:
    def __init__(self, id, name):
        self.__id = id
        self.name = name
        self.__tracks = list()
    
    def add_song(self, track):
        self.__tracks.append(track)

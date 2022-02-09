import json


class Album:
    def __init__(self, id, name):
        self.__id = id
        self.name = name
        self.tracks = dict()

    def add_song(self, track):
        self.tracks[track.id()] = track

    def id(self):
        return self.__id

    def __repr__(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

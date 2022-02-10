import json


class Track:
    def __init__(self, id, name, popularity, genres=None):
        if genres is None:
            genres = set()
        self.__id = id
        self.name = name
        self.popularity = popularity
        self.genres = genres

    def id(self):
        return self.__id

    def __repr__(self):
        return json.dumps(self, default=lambda o: list(o) if isinstance(o, set) else o.__dict__,
                          sort_keys=True, indent=4)

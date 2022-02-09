import json


class Track:
    def __init__(self, id, name, popularity):
        self.__id = id
        self.name = name
        self.popularity = popularity

    def id(self):
        return self.__id

    def __repr__(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

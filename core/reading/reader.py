import abc


class Reader(abc.ABC):
    @classmethod
    def read(cls, path):
        pass

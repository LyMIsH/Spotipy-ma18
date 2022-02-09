from .reader import Reader
from core.exceptions import exceptions


def get_reader(name):
    try:
        return globals()[name]()
    except KeyError as e:
        raise exceptions.ReaderDoesNotExistException("Reader '" + name + "' Does not exist")


class JsonReader(Reader):
    def read(self, path):
        print("Reading from ", path)

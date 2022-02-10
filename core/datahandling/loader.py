from . import data
from core.reading.reader_factory import JsonReader
import config


def load_songs():
    JsonReader.load_songs(config.settings["songs_path"])

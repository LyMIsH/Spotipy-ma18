from .reader import Reader
from core.parsing import parsers
import os
import glob
import json
from types import SimpleNamespace
from core.logging import logger


class JsonReader(Reader):
    @staticmethod
    def load_songs(path):
        for filename in glob.glob(os.path.join(path, '*.json')):
            logger.info(f"Reading json from {filename}")
            with open(os.path.join(path, filename), 'r') as file:  # open in readonly mode
                # Parse JSON into an object with attributes corresponding to dict keys.
                json_object = json.load(file, object_hook=lambda d: SimpleNamespace(**d))
                parsers.parse_track_json(json_object.track)

    @staticmethod
    def load_users(path):
        with open(path, "r") as file:
            users = json.load(file, object_hook=lambda d: SimpleNamespace(**d))


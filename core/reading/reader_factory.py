from .reader import Reader
from core.exceptions import exceptions
from core.parsing import parsers
import os
import glob
import json
from types import SimpleNamespace
from core.modules import logger


class JsonReader(Reader):
    @staticmethod
    def load_songs(path):
        for filename in glob.glob(os.path.join(path, '*.json')):
            logger.info(f"Reading json from {filename}")
            with open(os.path.join(path, filename), 'r') as file:  # open in readonly mode
                data = file.readline()
                # Parse JSON into an object with attributes corresponding to dict keys.
                x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
                parsers.parse_track_json(x.track)

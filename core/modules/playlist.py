from .track import Track


class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = dict()

    def add_tracks(self, tracks):
        for track in tracks:
            self.tracks[track.id()] = track

from core.reading import reader_factory
from core.datahandling import data
from core.account import account_managment
import config
from core.datahandling import search


def main():
    reader_factory.JsonReader.load_songs(config.settings["songs_path"])
    reader_factory.JsonReader.load_users(config.settings["users_path"])
    user = account_managment.login("Rafa", "1222222")
    user.create_playlist("NO")
    tracks = []
    count = 0
    for k, v in data.Data.tracks.items():
        tracks.append(v)
        count += 1
        if count == 18:
            break

    user.add_to_playlist("NO", tracks)
    user.create_playlist("ABC")
    user.create_playlist("sdasdasd")
    user.create_playlist("dasda")
    user.create_playlist("asdasda")
    user.add_to_playlist("ABC", tracks)

    artists = search.get_artists()
    s = artists[1].id()
    albums = search.get_albums(artists[1].id())
    top_tracks = search.get_top_artist_tracks(artists[1].id())
    album_tracks = search.get_album_tracks("2usyeZYdUHKlNHKDKgAYSo")

    _ = 0
   # data.test()


if __name__ == "__main__":
    main()

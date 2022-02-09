from core.reading import reader_factory
from core.modules.loaded_data import data


def main():
    reader_factory.JsonReader.load_songs(r"E:\Natanya\GitProjects\songs")
    data.get_data()


if __name__ == "__main__":
    main()

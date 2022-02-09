from core.reading import reader_factory


def main():
    reader_factory.get_reader("JsonReader").load_songs(r"E:\Natanya\GitProjects\songs")


if __name__ == "__main__":
    main()

from core.reading import reader_factory


def main():
    reader_factory.get_reader("s").read("C:/s")


if __name__ == "__main__":
    main()

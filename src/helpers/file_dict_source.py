import pathlib


def get_words_from_file(filename):
    dict_path = pathlib.Path(filename)
    with dict_path.open('r') as dict_file:
        for line in dict_file:
            yield line.strip()

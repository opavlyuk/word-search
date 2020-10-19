import pathlib


def get_words_from_file(filename):
    """Dictionary file iterator.

        Args:
            filename (str): Path to file with newline separated words

        Yields:
            str: The next stripped line in dictionary file

    """
    dict_path = pathlib.Path(filename)
    with dict_path.open('r') as dict_file:
        for line in dict_file:
            yield line.strip()

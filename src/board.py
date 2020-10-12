import random
import string


def make_board(side_len):
    """Generate square matrix with random chars.

    Args:
          side_len (int): Length of the side of the matrix.

    Returns:
        :obj:`list` of :obj:`list` of :obj:`str`: Generated matrix.matrix

    Raises:
        AssertionError: If side_len <= 0.

    """
    assert side_len > 0, 'Board size should be > 0.'
    return [[random.choice(string.ascii_lowercase) for _ in range(side_len)] for _ in range(side_len)]

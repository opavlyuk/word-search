import random
import string


def make_board(size):
    assert size > 0, 'Board size should be > 0.'
    return [[random.choice(string.ascii_lowercase) for _ in range(size)] for _ in range(size)]

import random
import string


def make_board(size):
    assert size > 0
    return [random.sample(string.ascii_lowercase, size) for i in range(size)]

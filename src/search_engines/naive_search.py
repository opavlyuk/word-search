import functools
from multiprocessing import Pool


def _forwards(i, j):
    return i, j + 1


def _backwards(i, j):
    new_j = j - 1
    if new_j >= 0:
        return i, new_j
    raise IndexError


def _upwards(i, j):
    new_i = i - 1
    if new_i >= 0:
        return new_i, j
    raise IndexError


def _downwards(i, j):
    return i + 1, j


def _forward_upwards(i, j):
    new_i = i - 1
    if new_i >= 0:
        return new_i, j + 1
    raise IndexError


def _forward_downwards(i, j):
    return i + 1, j + 1


def _back_upwards(i, j):
    new_i = i - 1
    new_j = j - 1
    if new_i >= 0 and new_j >= 0:
        return new_i, new_j
    raise IndexError


def _back_downwards(i, j):
    new_j = j - 1
    if new_j >= 0:
        return i + 1, new_j
    raise IndexError


directions = (_forwards, _backwards, _upwards, _downwards,
              _forward_upwards, _forward_downwards, _back_upwards, _back_downwards)


def track_word(n, word, i, j, board, direction, found_word=None):
    if found_word is None:
        found_word = ''
    if word[n] == board[i][j]:
        found_word += word[n]
        if n == len(word) - 1:
            return found_word
        i, j = direction(i, j)
        return track_word(n + 1, word, i, j, board, direction, found_word)
    else:
        raise StopIteration


def _iterate_board(board, word):
    for i, row in enumerate(board):
        for j, char in enumerate(row):
            for direction in directions:
                try:
                    word_found = track_word(0, word, i, j, board, direction)
                except (IndexError, StopIteration):
                    continue
                else:
                    return word_found


def naive_search(words, board, *args):
    with Pool() as p_pool:
        results = p_pool.map(functools.partial(_iterate_board, board), words)
    return {word for word in results if word}

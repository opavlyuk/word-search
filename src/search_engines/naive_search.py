from multiprocessing import Pool


def fws(i, j):
    return i, j + 1


def bws(i, j):
    new_j = j - 1
    if new_j > 0:
        return i, new_j
    raise IndexError


def upws(i, j):
    new_i = i - 1
    if new_i > 0:
        return new_i, j
    raise IndexError


def dws(i, j):
    return i + 1, j


def fuws(i, j):
    new_i = i - 1
    if new_i > 0:
        return new_i, j + 1
    raise IndexError


def fdws(i, j):
    return i + 1, j + 1


def buws(i, j):
    new_i = i - 1
    new_j = j - 1
    if new_i > 0 and new_j > 0:
        return new_i, new_j
    raise IndexError


def bdws(i, j):
    new_j = j - 1
    if new_j > 0:
        return i + 1, new_j
    raise IndexError


directions = (fws, bws, upws, dws, fuws, fdws, buws, bdws)


def track_word(n, word, i, j, board, direction, found_word=''):
    if word[n] == board[i][j]:
        found_word += word[n]
        if n == len(word) - 1:
            return found_word
        i, j = direction(i, j)
        return track_word(n + 1, word, i, j, board, direction, found_word)
    else:
        raise StopIteration


def iterate_board(board, word):
    for i, row in enumerate(board):
        for j, char in enumerate(row):
            for direction in directions:
                try:
                    word_found = track_word(0, word, i, j, board, direction)
                except (IndexError, StopIteration):
                    continue
                else:
                    return word_found


def naive_search(words, board):
    import functools
    with Pool() as p_pool:
        results = p_pool.map(functools.partial(iterate_board, board), words)

    # results = []
    # for word in words:
    #     word_found = iterate_board(board, word)
    #     if word_found:
    #         results.append(word_found)
    return [word for word in results if word]

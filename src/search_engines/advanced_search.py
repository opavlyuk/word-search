def _traverse_e(board, i, j, l):
    seq = ''
    for j in range(j, j + l):
        seq += board[i][j]
    return seq


def _traverse_se(board, i, j, l):
    seq = ''
    for i, j in zip(range(i, i + l), range(j, j + l)):
        seq += board[i][j]
    return seq


def _traverse_s(board, i, j, l):
    seq = ''
    for i in range(i, i + l):
        seq += board[i][j]
    return seq


def _traverse_sw(board, i, j, l):
    seq = ''
    while l - 1 >= i and j >= 0:
        seq += board[i][j]
        i, j = i + 1, j - 1
    return seq


def _choose_directions(i, j, min_len, board_size):
    directions = []
    if board_size - i >= min_len:
        directions.append(_traverse_s)
    if board_size - j >= min_len:
        directions.append(_traverse_e)
    if board_size - i >= min_len and board_size - j >= min_len:
        directions.append(_traverse_se)
    if board_size - i >= min_len and min_len <= j + 1:
        directions.append(_traverse_sw)
    return directions


def _pre_generate_char_seqs(board, min_len, max_len):
    board_size = len(board)
    seqs = set()
    for i, row in enumerate(board):
        for j, _ in enumerate(row):
            directions = _choose_directions(i, j, min_len, board_size)
            for get_direction in directions:
                for len_val in range(min_len, max_len + 1):
                    try:
                        seq = get_direction(board, i, j, len_val)
                        seqs.add(seq)
                        seqs.add(seq[::-1])
                    except IndexError:
                        continue
    return seqs


def advanced_search(words, board, min_len, max_len):
    """Search for words in board.

    Perform search along all diagonals, forwards, upwards, downwards or backwards

    Args:
        words (set): Set of words to search for.
        board (:obj:`list` of :obj:`list` of :obj:`str`): 2D iterable with chars.
        min_len (int): Length of the shortest word in input words.
        max_len (int): Length of the longest word in input words.

    Returns:
        set: Set with words found.

    """
    seqs = _pre_generate_char_seqs(board, min_len, max_len)
    return seqs & words

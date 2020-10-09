def _get_forwards(board, i, j, l):
    seq = ''
    for j in range(j, j + l):
        seq += board[i][j]
    return seq


def _get_forward_downwards(board, i, j, l):
    seq = ''
    for i, j in zip(range(i, i + l), range(j, j + l)):
        seq += board[i][j]
    return seq


def _get_downwards(board, i, j, l):
    seq = ''
    for i in range(i, i + l):
        seq += board[i][j]
    return seq


def _get_back_downwards(board, i, j, l):
    seq = ''
    # start_j = j
    while l - 1 >= i and j >= 0:  # and start_j - j <= l:
        seq += board[i][j]
        i, j = i + 1, j - 1
    return seq


def _choose_directions(i, j, min_len, board_size):
    directions = []
    if board_size - i >= min_len:
        directions.append(_get_downwards)
    if board_size - j >= min_len:
        directions.append(_get_forwards)
    if board_size - i >= min_len and board_size - j >= min_len:
        directions.append(_get_forward_downwards)
    if board_size - i >= min_len and min_len <= j + 1:
        directions.append(_get_back_downwards)
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
    words_found = []
    seqs = _pre_generate_char_seqs(board, min_len, max_len)
    for word in words:
        if word in seqs:
            words_found.append(word)
    return words_found

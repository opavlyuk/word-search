from src.board import make_board
from src.helpers.cli import parse_cl_args
from src.preprocess.words import preprocess_words
from src.search_engines.advanced_search import advanced_search as search


def main():
    args = parse_cl_args()
    board = make_board(args.board_size)
    words, min_len, max_len = preprocess_words(args)
    found_words = search(words, board, min_len, max_len)
    if found_words:
        print('Words found:', ', '.join(found_words))
    else:
        print('No words found.')


if __name__ == '__main__':
    main()

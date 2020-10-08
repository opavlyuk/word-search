import argparse

from src.board import make_board
from src.helpers import get_words_from_file
from src.search_engines.naive_search import naive_search as search

BOARD_SIZE = 15


class ArgumentError(Exception):
    pass


def _validate_args(args):
    if args.board_size < 0:
        raise ArgumentError('Board size should be > 0')


def _parse_cl_args():
    parser = argparse.ArgumentParser(description='Find words in two-dimensional array of random letters.')
    parser.add_argument('--board_size', type=int, default=BOARD_SIZE, help='Board side size')
    words_group = parser.add_mutually_exclusive_group(required=True)
    words_group.add_argument('--dictionary_file', type=str, help='File with words, separated by newline.'
                                                                 'Excludes `--words` argument if provided.')
    words_group.add_argument('--words', nargs='+', type=str, help='Words to search for, comma-separated.')
    args = parser.parse_args()
    return args


def main():
    args = _parse_cl_args()
    board = make_board(args.board_size)
    words = args.words or get_words_from_file(args.dictionary_file)
    found_words = search(words, board)
    if found_words:
        print('Words found:', ', '.join(found_words))
    else:
        print('No words found.')


if __name__ == '__main__':
    main()

import argparse

from src.board import make_board

BOARD_SIZE = 15


class ArgumentError(Exception):
    pass


def _validate_args(args):
    if args.board_size < 0:
        raise ValueError('Board size should be > 0')
    if args.dictionary_file and args.words:
        raise ArgumentError('Please provide only one argument with words to search for'
                            '(`--dictionary_file or --words`).')


def _parse_cl_args():
    parser = argparse.ArgumentParser(description='Find words in two-dimensional array of random letters.')
    parser.add_argument('--board_size', type=int, default=BOARD_SIZE, help='Board side size')
    parser.add_argument('--dictionary_file', type=str, help='File with words, separated by newline.'
                                                            'Excludes `--words` argument if provided.')
    parser.add_argument('--words', nargs='+', help='Words to search for, comma-separated.')
    args = parser.parse_args()
    _validate_args(args)
    return args


def main():
    args = _parse_cl_args()
    board = make_board(args.board_size)
    print(board)


if __name__ == '__main__':
    main()

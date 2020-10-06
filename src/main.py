import argparse

from src.board import make_board

BOARD_SIZE = 15


def _validate_args(args):
    if args.board_size < 0:
        raise ValueError('Board size should be > 0')


def _parse_cl_args():
    parser = argparse.ArgumentParser(description='Find words in two-dimensional array of random letters.')
    parser.add_argument('--board_size', type=int, default=BOARD_SIZE, help='Board side size')
    args = parser.parse_args()
    _validate_args(args)
    return args


def main():
    args = _parse_cl_args()
    board = make_board(args.board_size)
    print(board)


if __name__ == '__main__':
    main()

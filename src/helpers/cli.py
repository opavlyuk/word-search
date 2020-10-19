import argparse


class ArgumentError(Exception):
    pass


def _validate_args(args):
    if args.board_size < 0:
        raise ArgumentError('Board size should be > 0')


def parse_cl_args():
    parser = argparse.ArgumentParser(description='Find words in two-dimensional array of random letters.')
    parser.add_argument('--board_size', type=int, default=15, help='Board side size')
    words_group = parser.add_mutually_exclusive_group(required=True)
    words_group.add_argument('--dictionary_file', type=str, help='File with words, separated by newline.'
                                                                 'Excludes `--words` argument if provided.')
    words_group.add_argument('--words', nargs='+', type=str, help='Words to search for, comma-separated.')
    args = parser.parse_args()
    return args

from src.board import make_board
from src.helpers.cli import parse_cl_args
from src.preprocess.words import preprocess_words
from src.search_engines.advanced_search import advanced_search as search


def search_words(args):
    board = make_board(args.board_size)
    words, min_len, max_len = preprocess_words(args)
    return search(words, board, min_len, max_len)


def main():
    args = parse_cl_args()
    found_words = search_words(args)
    if found_words:
        print('Words found:', ', '.join(found_words))
    else:
        print('No words found.')


if __name__ == '__main__':
    main()

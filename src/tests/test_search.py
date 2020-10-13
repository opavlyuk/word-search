import itertools
import unittest

# from src.search_engines.naive_search import naive_search as search
from src.search_engines.advanced_search import advanced_search as search


class BaseTestSuite(unittest.TestCase):
    board = [
        ['a', 'b', 'c', 'd', 'e'],
        ['f', 'g', 'h', 'i', 'j'],
        ['k', 'l', 'm', 'n', 'o'],
        ['p', 'q', 'r', 's', 't'],
        ['u', 'v', 'w', 'x', 'y'],
    ]
    MIN_WORD_LEN = 1
    MAX_WORD_LEN = len(board)


class TestSuiteSearch(BaseTestSuite):
    def get_rows(self, board=None):
        if board is None:
            board = self.board
        return (row for row in board)

    def get_columns(self, board=None):
        if board is None:
            board = self.board
        return zip(*board)

    def get_ew_diagonals(self):
        b = [None] * (len(self.board) - 1)
        board = [b[:i] + r + b[i:] for i, r in enumerate(self.get_rows(self.board))]
        return ([c for c in r if c is not None] for r in self.get_columns(board))

    def get_we_diagonals(self):
        b = [None] * (len(self.board) - 1)
        board = [b[i:] + r + b[:i] for i, r in enumerate(self.get_rows(self.board))]
        return ([c for c in r if c is not None] for r in self.get_columns(board))

    @staticmethod
    def get_all_combinations(seq):
        return {''.join(seq[i:j]) for i, j in itertools.combinations(range(len(seq) + 1), r=2)}

    def test_existing_combinations(self):
        spaces = zip(
            ('rows', 'columns', 'ew_diagonals', 'we_diagonals'),
            (self.get_rows(), self.get_columns(), self.get_ew_diagonals(), self.get_we_diagonals()),
        )
        for name, space in spaces:
            for i, unit in enumerate(space):
                expected = self.get_all_combinations(unit)
                with self.subTest(space=name, unit_num=i):
                    self.assertEqual(
                        expected,
                        search(expected, self.board, self.MIN_WORD_LEN, self.MAX_WORD_LEN)
                    )

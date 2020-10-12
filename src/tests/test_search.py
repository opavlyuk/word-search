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
        return [''.join(seq[i:j]) for i, j in itertools.combinations(range(len(seq) + 1), r=2)]

    def test_horizontal(self):
        for i, row in enumerate(self.get_rows()):
            expected = self.get_all_combinations(row)
            with self.subTest(row_num=i):
                self.assertEqual(
                    expected,
                    search(expected, self.board, self.MIN_WORD_LEN, self.MAX_WORD_LEN)
                )

    def test_vertical(self):
        for i, col in enumerate(self.get_columns()):
            expected = self.get_all_combinations(col)
            with self.subTest(col=i):
                self.assertEqual(
                    expected,
                    search(expected, self.board, self.MIN_WORD_LEN, self.MAX_WORD_LEN)
                )

    def test_ew_diagonals(self):
        for i, diagonal in enumerate(self.get_ew_diagonals()):
            expected = self.get_all_combinations(diagonal)
            with self.subTest(diag=i):
                self.assertEqual(
                    expected,
                    search(expected, self.board, self.MIN_WORD_LEN, self.MAX_WORD_LEN)
                )

    def test_we_diagonals(self):
        for i, diagonal in enumerate(self.get_we_diagonals()):
            expected = self.get_all_combinations(diagonal)
            with self.subTest(diag=i):
                self.assertEqual(
                    expected,
                    search(expected, self.board, self.MIN_WORD_LEN, self.MAX_WORD_LEN)
                )

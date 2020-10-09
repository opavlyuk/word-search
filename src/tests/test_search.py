import unittest
import itertools

from src.search_engines.advanced_search import advanced_search as search

board = [
    ['a', 'b', 'c', 'd', 'e'],
    ['f', 'g', 'h', 'i', 'j'],
    ['k', 'l', 'm', 'n', 'o'],
    ['p', 'q', 'r', 's', 't'],
    ['u', 'v', 'w', 'x', 'y'],
]
MIN_LEN = 1
MAX_LEN = len(board)


class TestSuiteSearchForwards(unittest.TestCase):
    def test_first_line(self):
        expected_words = []
        expected_words.extend([])
        self.assertEqual(expected_words, search(expected_words, board, MIN_LEN, MAX_LEN))

    def test_last_line(self):
        forwards = ['u', 'uv', 'uvw', '', 'abcde', 'bcde', 'cde', 'de', 'e', 'bcd', 'bc', 'cd', 'b', 'c', 'd', ]
        backwards = [word[::-1] for word in forwards]
        expected_words = forwards + backwards
        self.assertEqual(expected_words, search(expected_words, board, MIN_LEN, MAX_LEN))

    def test_first_row(self):
        forwards = ['a', 'af', 'afk', 'afkp', 'afkpu', 'fkpu', 'kpu', 'pu', 'u', 'bcd', 'bc', 'cd', 'b', 'c', 'd', ]
        backwards = [word[::-1] for word in forwards]
        expected_words = forwards + backwards
        self.assertEqual(expected_words, search(expected_words, board, MIN_LEN, MAX_LEN))

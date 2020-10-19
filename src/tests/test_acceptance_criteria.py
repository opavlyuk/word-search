import timeit
import unittest
import pathlib

from src.main import search_words


class TestSuiteAcceptanceCriteria(unittest.TestCase):
    class ArgsMock:  # Quick but ugly mock
        board_size = 15
        words = None
        dictionary_file = pathlib.Path(__file__).parent.parent.parent / 'data/words.txt'

    def test_time(self):
        expected = 0.5
        exec_num = 100
        t = timeit.timeit(lambda: search_words(self.ArgsMock), number=exec_num)
        self.assertLessEqual(t / exec_num, expected)

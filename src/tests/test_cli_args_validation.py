import unittest

from src.board import make_board
from src.main import BOARD_SIZE


class TestMakeBoardPositive(unittest.TestCase):
    board = make_board(BOARD_SIZE)

    def assertIsIterable(self, obj, msg=None):
        if msg is None:
            msg = 'Object is not iterable.'
        try:
            (i for i in obj)
        except TypeError:
            raise AssertionError(msg)

    def _get_board_rows(self):
        for i, row in enumerate(self.board):
            yield i, row

    def _get_board_elements(self):
        for row_id, row in enumerate(self.board):
            for el_id, el in enumerate(row):
                yield el, el_id, row_id

    def test_board_is_iterable(self):
        self.assertIsIterable(self.board)

    def test_rows_are_iterable(self):
        for row_id, row in self._get_board_rows():
            self.assertIsIterable(row, f'Expected {row_id}th row to be iterable, actual got not.')

    def test_vertical_size(self):
        self.assertEqual(len(self.board), BOARD_SIZE)

    def test_horizontal_size(self):
        for row_id, row in self._get_board_rows():
            row_len = len(row)
            self.assertEqual(row_len, BOARD_SIZE, f'Row {row_id} expected length {BOARD_SIZE}, actual {row_len}.')

    def test_elements_type(self):
        elements = self._get_board_elements()
        for el, el_id, row_id in elements:
            self.assertIsInstance(el, str, f'Expected type `str`,'
                                           f' got {el_id}th element {el} of {type(el)} in row {row_id}')

    def test_elements_size(self):
        elements = self._get_board_elements()
        expected_size = 1
        for el, el_id, row_id in elements:
            el_len = len(el)
            self.assertEqual(expected_size, el_len,
                             f'Expected element of length {expected_size},'
                             f' got {el_id}th element {el} of length {el_len} in row {row_id}')


class TestMakeBoardNegative(unittest.TestCase):
    def test_zero(self):
        self.assertRaises(AssertionError, make_board, 0)

    def test_negative(self):
        self.assertRaises(AssertionError, make_board, -1)


if __name__ == '__main__':
    unittest.main()
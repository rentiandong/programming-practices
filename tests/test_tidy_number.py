import unittest
from tidy_number import tidy_number


class TestTidyNumbers(unittest.TestCase):

    def test_small_0(self):
        self.assertEqual('129', tidy_number('132'))

    def test_small_1(self):
        self.assertEqual('999', tidy_number('1000'))

    def test_small_2(self):
        self.assertEqual('7', tidy_number('7'))

    def test_large_0(self):
        self.assertEqual('99999999999999999', tidy_number('111111111111111110'))

    def test_large_1(self):
        self.assertEqual('119999999999999999', tidy_number('122222211635179876'))

import unittest
from google_tech_dev_guide.decompress import decompress


class TestMinWindow(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual('', decompress(''))

    def test_0_length_subsequence(self):
        self.assertEqual('', decompress('0[a]'))

    def test_simple_0(self):
        self.assertEqual('a', decompress('1[a]'))

    def test_simple_1(self):
        self.assertEqual('aaa', decompress('3[a]'))

    def test_simple_2(self):
        self.assertEqual('aabbcc', decompress('2[a]2[b]2[c]'))

    def test_simple_3(self):
        self.assertEqual('2222', decompress('4[2]'))

    def test_simple_4(self):
        self.assertEqual('cbacbapp2', decompress('2[cba]2[p]1[2]'))

    def test_simple_5(self):
        self.assertEqual('abc', decompress('abc'))

    def test_nested_0(self):
        self.assertEqual('dedeabababdedeababab', decompress('2[2[de]3[ab]]'))

    def test_nested_1(self):
        self.assertEqual('bcbcdebcbcde', decompress('2[2[bc]de]'))

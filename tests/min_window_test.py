import unittest
from min_window import min_window
from random import Random


class TestStringMethods(unittest.TestCase):

    def test_empty_source(self):
        self.assertEqual('', min_window('', 'a'))

    def test_empty_target(self):
        self.assertEqual('', min_window('abcde', ''))

    def test_both_emtpy(self):
        self.assertEqual('', min_window('', ''))

    def test_simple_0(self):
        self.assertEqual('BANC', min_window('ADOBECODEBANC', 'ABC'))

    def test_simple_1(self):
        self.assertEqual('abbc', min_window('aaabbbccccddddaaabbccdd', 'abc'))

    def test_hard_0(self):
        r = Random()
        r.seed(a=1)
        m = 1000000
        mid = int(m / 2)
        arr = [str(r.randint(0, 9)) for _ in range(0, m)]
        arr.insert(mid, 'A')
        s = ''.join(arr)
        expected = s[mid:s.find('9', mid) + 1]
        self.assertEqual(expected, min_window(''.join(arr), 'A9'))


if __name__ == '__main__':
    unittest.main()

import unittest
from bathroom_stalls import calc_space


class TestBathroomStalls(unittest.TestCase):

    def test_edge_0(self):
        self.assertEqual((0, 0), calc_space(1000, 1000))

    def test_small_0(self):
        self.assertEqual((1, 0), calc_space(4, 2))

    def test_small_1(self):
        self.assertEqual((1, 0), calc_space(5, 2))

    def test_small_2(self):
        self.assertEqual((1, 1), calc_space(6, 2))

    def test_medium_0(self):
        self.assertEqual(calc_space(1000, 1), (500, 499))

    #def test_large_0(self):
    #    calc_space(650701937524199729, 556692397629582053)


if __name__ == '__main__':
    unittest.main()

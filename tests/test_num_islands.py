import unittest
from src.num_islands import num_islands


class TestMinWindow(unittest.TestCase):

    def test_simple(self):
        topology = [
            ['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']
        ]
        self.assertEqual(1, num_islands(topology))

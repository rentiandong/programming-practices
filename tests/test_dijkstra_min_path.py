import unittest
from dijkstra_min_path import min_path


class TestEvaluateDivision(unittest.TestCase):

    def test_small_0(self):
        graph = [
            ('s', 'a', 1),
            ('s', 'b', 2),
            ('s', 'd', 4),
            ('a', 'd', 1),
            ('a', 'c', 3),
            ('d', 'c', 1),
            ('b', 'd', 2),
            ('b', 'e', 3),
            ('d', 'e', 2)
        ]
        costs = min_path('s', graph)
        self.assertEqual(4, costs['e'])

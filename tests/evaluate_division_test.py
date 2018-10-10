import unittest
from evaluate_division import evaluate_division


class TestEvaluateDivision(unittest.TestCase):

    def test_small_0(self):
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [["a", "c"], ["b", "c"], ["a", "e"], ["a", "a"], ["x", "x"]]
        self.assertEqual([6, 3, -1, 1, -1], evaluate_division(equations, values, queries))

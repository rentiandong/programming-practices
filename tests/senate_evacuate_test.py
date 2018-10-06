import unittest
from senate_evacuate import EvacPlan


# check if perfomring the current step on the party is valid
def verify_one_step(parties, step):
    for s in step:
        parties[s] -= 1
    total = sum([parties[i] for i in parties])
    for i in parties:
        if parties[i] < 0 or parties[i] > total / 2:
            return False
    return True


# check if performing all listed steps will be valid
def verify_all_steps(parties, steps):
    for step in steps:
        if not verify_one_step(parties, step):
            return False
    # check if everyone executed when done
    for i in parties:
        if parties[i] > 0:
            return False
    return True


class TestStringMethods(unittest.TestCase):

    def test_empty(self):
        self.assertEqual([], EvacPlan({}).plan)

    # edge case of {'A': 1, 'B': 1, 'C': 1}
    def test_edge_0(self):
        steps = EvacPlan({'A': 1, 'B': 1, 'C': 1}).plan
        self.assertTrue(verify_all_steps({'A': 1, 'B': 1, 'C': 1}, steps))

    def test_edge_1(self):
        steps = EvacPlan({'A': 1, 'B': 1}).plan
        self.assertTrue(verify_all_steps({'A': 1, 'B': 1}, steps))

    def test_small_0(self):
        steps = EvacPlan({'A': 1, 'B': 1, 'C': 1, 'D': 1}).plan
        self.assertTrue(verify_all_steps({'A': 1, 'B': 1, 'C': 1, 'D': 1}, steps))

    def test_small_1(self):
        steps = EvacPlan({'A': 1, 'B': 2, 'C': 2, 'D': 2}).plan
        self.assertTrue(verify_all_steps({'A': 1, 'B': 2, 'C': 2, 'D': 2}, steps))

    def test_large_0(self):
        steps = EvacPlan({'A': 1000, 'B': 1000, 'C': 1000}).plan
        self.assertTrue(verify_all_steps({'A': 1000, 'B': 1000, 'C': 1000}, steps))

    def test_large_1(self):
        steps = EvacPlan({'A': 40000, 'B': 20000, 'C': 10000, 'D': 10000}).plan
        self.assertTrue(verify_all_steps({'A': 40000, 'B': 20000, 'C': 10000, 'D': 10000}, steps))


if __name__ == '__main__':
    unittest.main()

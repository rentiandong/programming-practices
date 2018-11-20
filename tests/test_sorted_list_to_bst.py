import unittest
from sorted_list_to_bst import sorted_list_to_bst
from data_structures.linked_list import from_list


class TestSortedListToBST(unittest.TestCase):

    def test_small_0(self):
        sorted_list_to_bst(from_list([-10, -3, 0, 5, 9]))


if __name__ == '__main__':
    unittest.main()

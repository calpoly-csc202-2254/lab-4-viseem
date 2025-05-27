import unittest
from bst import frozenBinarySearchTree, insert, lookup

class SimpleBSTTests(unittest.TestCase):
    #test for numeric ordering
    def test_numeric_order(self):
        compare = lambda a, b: a < b
        bst = frozenBinarySearchTree(compare)
        bst = insert(bst, 42)
        self.assertEqual(lookup(bst, 42), True)

    #atest for alphabetic ordering
    def test_alphabetic_order(self):
        compare = lambda a, b: a < b
        bst = frozenBinarySearchTree(compare)
        bst = insert(bst, 'k')
        self.assertEqual(lookup(bst, 'k'), True)

    #test for Euclidean distance ordering
    def test_distance_order(self):
        compare = lambda p, q: (p[0]**2 + p[1]**2) < (q[0]**2 + q[1]**2)
        bst = frozenBinarySearchTree(compare)
        point = (3, 4)
        bst = insert(bst, point)
        self.assertEqual(lookup(bst, point), True)

if __name__ == '__main__':
    unittest.main()

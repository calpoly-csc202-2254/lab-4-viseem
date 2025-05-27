import unittest
from bst import frozenBinarySearchTree, insert, lookup

class SimpleBSTTests(unittest.TestCase):
    #test numeric ordering
    def test_numeric_order(self):
        cmp_fn = lambda a, b: a < b
        bst = frozenBinarySearchTree(cmp_fn)
        bst = insert(bst, 42)
        self.assertEquals(lookup(bst, 42), True)

    #test alphabetic ordering
    def test_alphabetic_order(self):
        cmp_fn = lambda a, b: a < b
        bst = frozenBinarySearchTree(cmp_fn)
        bst = insert(bst, 'k')
        self.assertEquals(lookup(bst, 'k'), True)

    #test Euclidean-distance ordering
    def test_distance_order(self):
        cmp_fn = lambda p, q: (p[0]**2 + p[1]**2) < (q[0]**2 + q[1]**2)
        bst = frozenBinarySearchTree(cmp_fn)
        pt = (3, 4)  # distance 5
        bst = insert(bst, pt)
        self.assertEquals(lookup(bst, pt), True)

if __name__ == '__main__':
    unittest.main()
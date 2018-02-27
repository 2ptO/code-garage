import unittest
import bst

class TestBinarySearchTree(unittest.TestCase):
    
    def test_emptyTree(self):
        emptyTree = bst.BinarySearchTree()
        self.assertEqual(emptyTree.getHeight(), 0)
        self.assertEqual(emptyTree.getValuesInOrder(), [])

    def test_insert(self):
        testTree = [15, 8, 20, 5, 10, 18, 25, 16]
        bstree = bst.BinarySearchTree()
        for value in testTree:
            bstree.insert(value)
        expectedResult = bstree.getValuesInOrder()
        self.assertEqual(sorted(testTree), expectedResult, "Returned values not inorder")
        self.assertEqual(bstree.getHeight(), 4, "Height didn't match with the test tree")


if __name__ == '__main__':
    unittest.main()
import unittest
import bst

class TestBinarySearchTree(unittest.TestCase):
    
    def test_emptyTree(self):
        emptyTree = bst.BinarySearchTree()
        self.assertEqual(emptyTree.get_height(), 0)
        self.assertEqual(emptyTree.get_values_in_order(), [])
    
    def test_singleNodeTree(self):
        test_tree = bst.BinarySearchTree()
        test_tree.insert(45)
        self.assertEqual([45], test_tree.get_values_in_order())

    def test_insert(self):
        testTree = [15, 8, 20, 5, 10, 18, 25, 16]
        bstree = bst.BinarySearchTree()
        for value in testTree:
            bstree.insert(value)
        expectedResult = bstree.get_values_in_order()
        self.assertEqual(sorted(testTree), expectedResult, "Returned values not inorder")
        self.assertEqual(bstree.get_height(), 4, "Height didn't match with the test tree")


if __name__ == '__main__':
    unittest.main()
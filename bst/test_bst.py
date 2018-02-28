import unittest
import bst

class TestBinarySearchTree(unittest.TestCase):
    
    def test_emptyTree(self):
        emptyTree = bst.BinarySearchTree()
        self.assertEqual(emptyTree.get_height(), 0)
        self.assertEqual(emptyTree.get_values_in_order(), [])
        with self.assertRaises(IndexError):
            emptyTree.get_min()
    
    def test_singleNodeTree(self):
        test_tree = bst.BinarySearchTree()
        test_tree.insert(45)
        self.assertEqual([45], test_tree.get_values_in_order())
        self.assertEqual(45, test_tree.get_min(), "Invalid min value in single node tree")
        self.assertEqual(45, test_tree.get_max(), "Invalid max value in single node tree")
    
    def test_min_max_values(self):
        test_tree = bst.BinarySearchTree()
        test_inputs = [34, 56, 5, 24, 10, -1]
        for i in test_inputs:
            test_tree.insert(i)
        self.assertEqual(test_tree.get_min(), min(test_inputs), "Invalid minimum value")
        self.assertEqual(test_tree.get_max(), max(test_inputs), "Invalid max value")

    def test_insert(self):
        test_inputs = [15, 8, 20, 5, 10, 18, 25, 16]
        test_tree = bst.BinarySearchTree()
        for value in test_inputs:
            test_tree.insert(value)
        expectedResult = test_tree.get_values_in_order()
        self.assertEqual(sorted(test_inputs), expectedResult, "Returned values not inorder")
        self.assertEqual(test_tree.get_height(), 4, "Height didn't match with the test tree")
        self.assertEqual(len(test_inputs), len(test_tree), "Invalid node count")


if __name__ == '__main__':
    unittest.main()
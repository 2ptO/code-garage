import unittest
import bst

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.test_tree = bst.BinarySearchTree()
    
    def tearDown(self):
        del self.test_tree
    def test_emptyTree(self):
        emptyTree = self.test_tree
        self.assertEqual(emptyTree.get_height(), 0)
        self.assertEqual(emptyTree.get_values_in_order(), [])
        with self.assertRaises(IndexError):
            emptyTree.get_min()

    def test_singleNodeTree(self):
        self.test_tree.insert(45)
        self.assertEqual([45], self.test_tree.get_values_in_order())
        self.assertEqual(45, self.test_tree.get_min(), "Invalid min value in single node tree")
        self.assertEqual(45, self.test_tree.get_max(), "Invalid max value in single node tree")
    
    def test_min_max_values(self):
        test_inputs = [34, 56, 5, 24, 10, -1]
        for i in test_inputs:
            self.test_tree.insert(i)
        self.assertEqual(self.test_tree.get_min(), min(test_inputs), "Invalid minimum value")
        self.assertEqual(self.test_tree.get_max(), max(test_inputs), "Invalid max value")

    def test_insert(self):
        test_inputs = [15, 8, 20, 5, 10, 18, 25, 16]
        for value in test_inputs:
            self.test_tree.insert(value)
        expectedResult = self.test_tree.get_values_in_order()
        self.assertEqual(sorted(test_inputs), expectedResult, "Returned values not inorder")
        self.assertEqual(self.test_tree.get_height(), 4, "Height didn't match with the test tree")
        self.assertEqual(len(test_inputs), len(self.test_tree), "Invalid node count")
    
    def test_delete_empty_tree(self):
        with self.assertRaises(KeyError):
            self.test_tree.delete(10)

    def test_delete_missing_value(self):
        self.test_tree.insert(100)
        with self.assertRaises(KeyError):
            self.test_tree.delete(10)

    def test_delete_root_only_tree(self):
        self.test_tree.insert(10)
        self.test_tree.delete(10)
        self.assertEqual(len(self.test_tree), 0, "Unexpected node found after deleting the root")
    
    def test_delete_leaf_node(self):
        input_values = [15, 10, 25]
        for i in input_values:
            self.test_tree.insert(i)
        self.test_tree.delete(10)
        self.assertEqual(self.test_tree.find(10), None, "Deleted node found after deletion")
    
    def test_delete_single_child_node(self):
        input_values = [5, 10, 25]
        for i in input_values:
            self.test_tree.insert(i)
        self.test_tree.delete(10)
        self.assertEqual(self.test_tree.find(10), None, "Deleted node found after deletion")
    
    def test_delete_two_child_node(self):
        input_values = [15, 10, 25, 20, 30]
        value_to_delete = 25
        for i in input_values:
            self.test_tree.insert(i)
        self.test_tree.delete(value_to_delete)
        self.assertEqual(self.test_tree.find(value_to_delete),
                         None,
                         "Deleted node found after deletion")
        input_values.remove(value_to_delete)
        self.assertEqual(sorted(input_values),
                         self.test_tree.get_values_in_order(), 
                         "Deleted node found after deletion")
    
    def test_delete_root_node(self):
        input_values = [15, 10, 25, 20, 30]
        value_to_delete = 15
        for i in input_values:
            self.test_tree.insert(i)
        self.test_tree.delete(value_to_delete)
        self.assertEqual(self.test_tree.find(value_to_delete),
                         None,
                         "Deleted node found after deletion")
        input_values.remove(value_to_delete)
        self.assertEqual(sorted(input_values),
                         self.test_tree.get_values_in_order(), 
                         "Deleted node found after deletion")


if __name__ == '__main__':
    unittest.main()
import unittest
from .q9 import BTNode, is_binary_search_tree

class TestQ9(unittest.TestCase):
    def test_bs_tree_valid(self):
        root = BTNode(50)
        root.left = BTNode(30, BTNode(20), BTNode(40))
        root.right = BTNode(80, BTNode(70), BTNode(90))
        self.assertTrue(is_binary_search_tree(root))

    def test_bs_tree_invalid_left_subtree(self):
        root = BTNode(50)
        root.left = BTNode(30, BTNode(20), BTNode(60))
        root.right = BTNode(80, BTNode(70), BTNode(90))
        self.assertFalse(is_binary_search_tree(root))

    def test_bs_tree_invalid_right_subtree(self):
        root = BTNode(50)
        root.left = BTNode(30, BTNode(20), BTNode(40))
        root.right = BTNode(80, BTNode(85), BTNode(90))
        self.assertFalse(is_binary_search_tree(root))
    
    def test_bs_tree_invalid_duplicate_values(self):
        root = BTNode(50)
        root.left = BTNode(30, BTNode(20), BTNode(40))
        root.right = BTNode(80, BTNode(85), BTNode(80))
        self.assertFalse(is_binary_search_tree(root))
    
    def test_bs_tree_single_node(self):
        root = BTNode(50)
        self.assertTrue(is_binary_search_tree(root))
import unittest
import q8

class TestQ8(unittest.TestCase):
    def test_balanced_tree(self):
        root = q8.Node(15)
        root.left = q8.Node(8, q8.Node(5), q8.Node(10))
        root.right = q8.Node(20, q8.Node(16), q8.Node(25))
        self.assertTrue(q8.is_super_balanced(root, use_recursion=True))
        self.assertTrue(q8.is_super_balanced(root, use_recursion=False))
    
    def test_unbalanced_tree_left_heavy(self):
        root = q8.Node(15)
        root.left = q8.Node(8, left=q8.Node(5))
        self.assertTrue(q8.is_super_balanced(root, use_recursion=True))
        self.assertTrue(q8.is_super_balanced(root, use_recursion=False))
        
    def test_unbalanced_tree_right_heavy(self):
        root = q8.Node(15)
        root.right = q8.Node(20, right=q8.Node(25))
        self.assertTrue(q8.is_super_balanced(root, use_recursion=True))
        self.assertTrue(q8.is_super_balanced(root, use_recursion=False))
    
    def test_empty_tree(self):
        root = None
        self.assertTrue(q8.is_super_balanced(root, use_recursion=True))
        self.assertTrue(q8.is_super_balanced(root, use_recursion=False))
    
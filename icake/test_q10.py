import unittest
import q10
from random import randint

class TestQ10(unittest.TestCase):
    def test_balanced_tree(self):
        # inputs = [15, 10, 8, 15, 20, 18, 25]
        inputs = [43, 11, 100, 27, 54, 87, 19, 80, 38, 74]
        root = q10.BTNode(inputs[0])
        for value in inputs[1:]:
            q10.insert(root, value)
        self.assertEqual(sorted(inputs)[-2], q10.find_second_max(root))

    def test_random_tree(self):
        inputs = [randint(1, 100) for x in range(10)]
        root = q10.BTNode(inputs[0])
        for value in inputs[1:]:
            q10.insert(root, value)
        self.assertEqual(sorted(inputs)[-2], q10.find_second_max(root),
                            "Second-max from {} didn't match".format(inputs))
    
    def test_invalid_tree(self):
        root = None
        with self.assertRaises(ValueError):
            q10.find_second_max(root)
        
        root = q10.BTNode(19)
        with self.assertRaises(ValueError):
            q10.find_second_max(root)
    
    def test_left_only_tree(self):
        inputs = [randint(1, 100) for x in range(10)]
        inputs.sort(reverse=True)
        root = q10.BTNode(inputs[0])
        for value in inputs[1:]:
            q10.insert(root, value)
        self.assertEqual(inputs[1], q10.find_second_max(root),
                            "Second-max from {} didn't match".format(inputs))
    
    def test_right_only_tree(self):
        inputs = [randint(1, 100) for x in range(10)]
        inputs.sort()
        root = q10.BTNode(inputs[0])
        for value in inputs[1:]:
            q10.insert(root, value)
        self.assertEqual(inputs[-2], q10.find_second_max(root),
                            "Second-max from {} didn't match".format(inputs))
        
        

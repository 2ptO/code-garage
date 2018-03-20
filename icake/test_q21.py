import unittest
import q21

class TestQ21(unittest.TestCase):
    def test_list_with_unique_nums(self):
        numbers = [1, 2, 4, 5, 6, 2, 1, 4, 5]
        self.assertEqual(q21.find_unique_number(numbers), 6)
    
    def test_list_without_unique_nums(self):
        numbers = [1, 2, 4, 5, 2, 1, 4, 5]
        self.assertEqual(q21.find_unique_number(numbers), 0)
import unittest
import random
import q35

class TestQ35(unittest.TestCase):
    def test_shuffle_items_in_place(self):
        items = [random.randint(0, 100) for _ in range(10)]
        dup_items = items[::]
        q35.shuffle(items)
        for item in dup_items:
            self.assertIn(item, items)
    
    def test_shuffle_empty_list(self):
        self.assertListEqual([], q35.shuffle([]))

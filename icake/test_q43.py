import unittest
import heapq
import random
import q43

class TestQ43(unittest.TestCase):
    def test_merge_of_empty_lists(self):
        self.assertListEqual(q43.merge_sorted_lists([], []), [])

    def test_merge_of_one_empty_list(self):
        left = [1, 3, 5, 6]
        right = []
        self.assertEqual(q43.merge_sorted_lists(left, right), left)
    
    def test_merge_of_two_equal_lists(self):
        left = [3, 4, 6, 10, 11, 15]
        right = [1, 5, 8, 12, 14, 19]
        merged_lists = list(heapq.merge(left, right))
        self.assertEqual(q43.merge_sorted_lists(left, right), merged_lists)

    def test_merge_of_two_lists_with_negative_nums(self):
        left = [-3, 4, 6, 10, 11, 15]
        right = [-1, 5, 8, 12, 14, 19]
        merged_lists = list(heapq.merge(left, right))
        self.assertEqual(q43.merge_sorted_lists(left, right), merged_lists)
    
    def test_merge_of_unequal_lists(self):
        left = [-3, 4, 6, 10, 11, 15]
        right = [-1, 5]
        merged_lists = list(heapq.merge(left, right))
        self.assertEqual(q43.merge_sorted_lists(left, right), merged_lists)
    
    def test_merge_of_random_numbers(self):
        left = [random.randint(0, 50000) for _ in range(10000)]
        right = [random.randint(0, 50000) for _ in range(10000)]

        left.sort()
        right.sort()
        
        heapq_merged_lists = list(heapq.merge(left, right))
        q43_merged_lists = q43.merge_sorted_lists(left, right)
        self.assertEqual(q43_merged_lists, heapq_merged_lists)
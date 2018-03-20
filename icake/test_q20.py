import unittest
import q20
from random import randint

class TestQ20(unittest.TestCase):

    def setUp(self):
        self.max_stack = q20.MaxStack()
    
    def tearDown(self):
        del self.max_stack

    def test_get_max_from_stack(self):
        numbers = [10, 9, 4, 15, 15, 20, 2]
        for num in numbers:
            self.max_stack.push(num)
        self.assertEqual(max(numbers), self.max_stack.get_max())
        stacked_numbers = [self.max_stack.pop() for _ in range(len(numbers))]
        stacked_numbers.reverse()
        self.assertEqual(numbers, stacked_numbers)
    
    def test_get_max_random_numbers(self):
        numbers = [randint(1, 100) for _ in range(100)]
        for num in numbers:
            self.max_stack.push(num)
        self.assertEqual(max(numbers), self.max_stack.get_max())
        stacked_numbers = [self.max_stack.pop() for _ in range(len(numbers))]
        stacked_numbers.reverse()
        self.assertEqual(numbers, stacked_numbers)
    
    def test_get_max_in_between_push_and_pop(self):
        numbers = [randint(1, 100) for _ in range(100)]
        for stop_point in range(0, len(numbers), 10):
            temp_numbers = numbers[stop_point:stop_point+10]
            # push 5 items from stop point
            for i in range(5):
                self.max_stack.push(temp_numbers[i])
            # Verify max
            self.assertEqual(self.max_stack.get_max(), max(temp_numbers[:5]))
            # Pop 3 items
            for _ in range(3):
                self.max_stack.pop()
            
            # push the remaining items
            for i in range(5, 10):
                self.max_stack.push(temp_numbers[i])
            
            # Verify max from the 7 items in the stack
            self.assertEqual(self.max_stack.get_max(), max(temp_numbers[:2] + temp_numbers[5:]))

            # Drain the stack
            for _ in range(7):
                self.max_stack.pop()
            
class TestQ20Optimized(TestQ20):
    """
    Test optimized version of MaxStack that runs in O(1) space
    """
    def setUp(self):
        self.max_stack = q20.MaxStackOptimized()
    
    def tearDown(self):
        del self.max_stack
 
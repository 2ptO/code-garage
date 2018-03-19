import unittest
import q20
from random import randint

class TestQ20(unittest.TestCase):
    def test_get_max_from_stack(self):
        max_stack = q20.MaxStack()
        numbers = [10, 9, 4, 15, 14, 20, 2]
        for num in numbers:
            max_stack.push(num)
        self.assertEqual(max(numbers), max_stack.get_max())
        stacked_numbers = [max_stack.pop() for _ in range(len(numbers))]
        stacked_numbers.reverse()
        self.assertEqual(numbers, stacked_numbers)
    
    def test_get_max_random_numbers(self):
        max_stack = q20.MaxStack()
        numbers = [randint(1, 100) for _ in range(100)]
        for num in numbers:
            max_stack.push(num)
        self.assertEqual(max(numbers), max_stack.get_max())
        stacked_numbers = [max_stack.pop() for _ in range(len(numbers))]
        stacked_numbers.reverse()
        self.assertEqual(numbers, stacked_numbers)
    
    def test_get_max_in_between_push_and_pop(self):
        max_stack = q20.MaxStack()
        numbers = [randint(1, 100) for _ in range(100)]
        for stop_point in range(0, len(numbers), 10):
            temp_numbers = numbers[stop_point:stop_point+10]
            # push 5 items from stop point
            for i in range(5):
                max_stack.push(temp_numbers[i])
            # Verify max
            self.assertEqual(max_stack.get_max(), max(temp_numbers[:5]))
            # Pop 3 items
            for _ in range(3):
                max_stack.pop()
            
            # push the remaining items
            for i in range(5, 10):
                max_stack.push(temp_numbers[i])
            
            # Verify max from the 7 items in the stack
            self.assertEqual(max_stack.get_max(), max(temp_numbers[:2] + temp_numbers[5:]))

            # Drain the stack
            for _ in range(7):
                max_stack.pop()
            


    

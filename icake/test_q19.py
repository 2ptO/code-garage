import unittest
import q19

class TestQ19(unittest.TestCase):
    def test_enqueue_and_dequeue_success(self):
        input_numbers = [1, 2, 3, 4, 5]
        queue_using_stack = q19.QueueUsingStack()
        for num in input_numbers:
            queue_using_stack.enqueue(num)
        output_numbers = [queue_using_stack.dequeue() for x in range(len(input_numbers))]
        self.assertEqual(output_numbers, input_numbers)
    
    def test_queue_full_error(self):
        queue_using_stack = q19.QueueUsingStack()
        with self.assertRaises(OverflowError):
            for i in range(q19.DEFAULT_STACK_SIZE + 1):
                queue_using_stack.enqueue(i)
    
    def test_queue_empty_error(self):
        queue_using_stack = q19.QueueUsingStack()
        with self.assertRaises(IndexError):
            queue_using_stack.dequeue()


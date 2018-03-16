import unittest
import q15

class TestQ15(unittest.TestCase):
    def test_fib_numbers(self):
        fib_nums = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

        for n, nth_fib_num in enumerate(fib_nums):
            self.assertEqual(q15.fib(n), nth_fib_num)
    
    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            q15.fib(-10)

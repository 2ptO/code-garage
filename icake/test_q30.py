import unittest
import q30

class TestQ30(unittest.TestCase):
    def test_valid_palindrome(self):
        self.assertTrue(q30.is_palindrome("civic"))
        self.assertTrue(q30.is_palindrome("ivicc"))
        self.assertTrue(q30.is_palindrome(""))
        self.assertTrue(q30.is_palindrome("racecar"))
    
    def test_invalid_palindrom(self):
        self.assertFalse(q30.is_palindrome("civicsviiv"))
        self.assertFalse(q30.is_palindrome("ivilc"))

if __name__ == "__main__":
    unittest.main()

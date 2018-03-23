import unittest
import q26

class TestQ26(unittest.TestCase):
    def test_reverse_empty_string(self):
        with self.assertRaises(ValueError):
            q26.reverse_text("")

        with self.assertRaises(ValueError):
            q26.reverse_text(None)    
    def test_reverse_single_char(self):
        test_text = 'a'
        self.assertEqual(test_text, q26.reverse_text(test_text))
    
    def test_reverse_string(self):
        test_text = " lorem ipsum"
        reversed_text = test_text[::-1] # step -1 from the end, shortcut to reverse a list
        self.assertEqual(reversed_text, q26.reverse_text(test_text))